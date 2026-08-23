# -*- coding: utf-8 -*-
"""Rendu des segments 9:16 : recadrage visage, zooms lents, B-roll, cartons."""
import json, subprocess, sys, os
from concurrent.futures import ThreadPoolExecutor

SRC  = "/home/user/xelanc/media/source"
SEG  = "/home/user/xelanc/edit/segments"
PNG  = "/home/user/xelanc/edit/png"
FPS  = 30
W, H = 1080, 1920
PRE  = "1620:2880"          # pre-agrandissement : zoom fluide, sans tremblement
RALENTI = 1.25              # B-roll 24 -> 30 fps : 1 image source = 1 image sortie

# fraction verticale du visage dans chaque cadrage -> point d'ancrage du zoom
ANCRE_Y = {"large": 0.278, "moyen": 0.301, "serre": 0.325,
           "mains_semis": 0.45, "graine_pres": 0.55, "sol_chaud": 0.50,
           "pousse_jeune": 0.55, "pousse": 0.58, "pousse_macro": 0.55,
           "pousse_large": 0.58, "lion_loin": 0.45, "lion_face": 0.42,
           "lion_yeux": 0.40, "lion_marche": 0.48}

ENC = ["-c:v", "libx264", "-preset", "medium", "-crf", "18",
       "-pix_fmt", "yuv420p", "-r", str(FPS), "-g", "60", "-an"]


def zoompan(sens, n, ay, amp=0.09):
    z = f"1+{amp}*on/{n}" if sens == "in" else f"1+{amp}-{amp}*on/{n}"
    return (f"zoompan=z='{z}':x='(iw-iw/zoom)*0.5':y='(ih-ih/zoom)*{ay}'"
            f":d=1:s={W}x{H}:fps={FPS}")


def commande(s, i):
    n   = round(s["dur"] * FPS)
    out = f"{SEG}/seg_{i:03d}.mp4"

    if s["kind"] == "av":
        cw, ch, cx, cy = s["crop"]
        vf = (f"fps={FPS},crop={cw}:{ch}:{cx}:{cy},scale={PRE}:flags=lanczos,"
              f"{zoompan(s['zoom'], n, ANCRE_Y[s['framing']])},"
              f"unsharp=5:5:0.55:5:5:0.0,vignette=PI/5.5")
        cmd = ["ffmpeg", "-y", "-v", "error", "-ss", str(s["start"]),
               "-i", f"{SRC}/avatar_raw.mp4", "-vf", vf, "-frames:v", str(n)]

    elif s["kind"] == "br":
        cw, ch, cx, cy = s["crop"]
        besoin = s["dur"] / RALENTI + 0.3
        vf = (f"setpts={RALENTI}*PTS,fps={FPS},crop={cw}:{ch}:{cx}:{cy},"
              f"scale={PRE}:flags=lanczos,"
              f"{zoompan(s['zoom'], n, ANCRE_Y[s['framing']], 0.07)},"
              f"unsharp=7:7:0.75:7:7:0.0,"
              f"eq=brightness=0.055:contrast=1.05:saturation=1.12:gamma=1.32,"
              f"colorbalance=rs=-0.02:bs=0.03,"             # ombres vers le navy
              f"vignette=PI/6.5")
        cmd = ["ffmpeg", "-y", "-v", "error", "-ss", str(s["src_in"]),
               "-t", f"{besoin:.3f}", "-i", f"{SRC}/{s['clip']}_raw.mp4",
               "-vf", vf, "-frames:v", str(n)]

    else:  # carton plein ecran
        f_in, f_out = 0.12, 0.14
        vf = (f"fps={FPS},scale={PRE}:flags=lanczos,"
              f"{zoompan('in', n, 0.5, 0.035)},"
              f"fade=t=in:st=0:d={f_in},"
              f"fade=t=out:st={s['dur']-f_out:.3f}:d={f_out}")
        cmd = ["ffmpeg", "-y", "-v", "error", "-loop", "1",
               "-i", f"{PNG}/{s['card']}.png", "-vf", vf, "-frames:v", str(n)]

    return cmd + ENC + [out], out, n


def rendre(arg):
    s, i = arg
    cmd, out, n = commande(s, i)
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode:
        return f"ECHEC seg_{i:03d}: {r.stderr[-400:]}"
    got = subprocess.run(["ffprobe", "-v", "error", "-count_frames",
                          "-select_streams", "v:0", "-show_entries",
                          "stream=nb_read_frames", "-of", "csv=p=0", out],
                         capture_output=True, text=True).stdout.strip()
    if int(got) != n:
        return f"ECART seg_{i:03d}: {got} images au lieu de {n}"
    return None


if __name__ == "__main__":
    segs = json.load(open("/home/user/xelanc/edit/build/edl.json"))
    os.makedirs(SEG, exist_ok=True)
    with ThreadPoolExecutor(max_workers=6) as ex:
        pbs = [r for r in ex.map(rendre, [(s, i) for i, s in enumerate(segs)]) if r]
    for p in pbs:
        print(p)
    print(f"{len(segs)-len(pbs)}/{len(segs)} segments rendus")
    sys.exit(1 if pbs else 0)
