# -*- coding: utf-8 -*-
"""Plans avatar du montage v2 : recadrage 9:16 centre visage, zoom lent alterne."""
import json, os, subprocess, sys
from concurrent.futures import ThreadPoolExecutor

SRC, SEG = "/home/user/xelanc/media/source", "/home/user/xelanc/edit/segments2"
FPS, W, H, PRE = 30, 1080, 1920, "1620:2880"
ANCRE_Y = {"large": 0.278, "moyen": 0.301, "serre": 0.325}

# Correction du calage labial. Les levres de l'avatar HeyGen bougent AVANT le
# son : au temps t de la timeline on va donc chercher l'image du visage au
# temps t - AVANCE dans la source. L'audio n'est jamais touche — il reste
# recopie bit a bit — et les illustrations gardent leur calage sur le SRT.
AVANCE = float(os.environ.get("AVANCE_LEVRES", "0.120"))
ENC = ["-c:v", "libx264", "-preset", "medium", "-crf", "18",
       "-pix_fmt", "yuv420p", "-r", str(FPS), "-g", "60", "-an"]


def commande(s, i):
    n = round(s["dur"] * FPS)
    cw, ch, cx, cy = s["crop"]
    ay = ANCRE_Y[s["framing"]]
    amp = 0.09
    z = f"1+{amp}*on/{n}" if s["zoom"] == "in" else f"1+{amp}-{amp}*on/{n}"
    vf = (f"fps={FPS},crop={cw}:{ch}:{cx}:{cy},scale={PRE}:flags=lanczos,"
          f"zoompan=z='{z}':x='(iw-iw/zoom)*0.5':y='(ih-ih/zoom)*{ay}'"
          f":d=1:s={W}x{H}:fps={FPS},"
          f"unsharp=5:5:0.55:5:5:0.0,vignette=PI/5.5")
    return (["ffmpeg", "-y", "-v", "error", "-ss", f"{max(0.0, s['start'] - AVANCE):.4f}",
             "-i", f"{SRC}/avatar_raw.mp4", "-vf", vf, "-frames:v", str(n)]
            + ENC + [f"{SEG}/seg_{i:03d}.mp4"]), n


def rendre(arg):
    s, i = arg
    cmd, n = commande(s, i)
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode:
        return f"ECHEC seg_{i:03d}: {r.stderr[-300:]}"
    got = subprocess.run(["ffprobe", "-v", "error", "-count_frames", "-select_streams", "v:0",
                          "-show_entries", "stream=nb_read_frames", "-of", "csv=p=0",
                          f"{SEG}/seg_{i:03d}.mp4"], capture_output=True, text=True).stdout.strip()
    return None if int(got) == n else f"ECART seg_{i:03d}: {got} != {n}"


if __name__ == "__main__":
    segs = json.load(open("/home/user/xelanc/edit/build/edl2.json"))
    os.makedirs(SEG, exist_ok=True)
    todo = [(s, i) for i, s in enumerate(segs) if s["kind"] == "av"]
    with ThreadPoolExecutor(max_workers=4) as ex:
        pbs = [r for r in ex.map(rendre, todo) if r]
    for p in pbs: print(p)
    print(f"{len(todo)-len(pbs)}/{len(todo)} plans avatar rendus")
    sys.exit(1 if pbs else 0)
