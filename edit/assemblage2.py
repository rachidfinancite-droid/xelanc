# -*- coding: utf-8 -*-
"""Assemblage v2 : concat plans avatar + illustrations, incrustation des
mots-cles animes, puis recopie de l'audio avatar sans reencodage ni coupe."""
import json, subprocess

ED, SRC, FPS = "/home/user/xelanc/edit", "/home/user/xelanc/media/source", 30
FINAL = "/home/user/xelanc/salaire-trauma-vertical.mp4"


def sh(cmd):
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode:
        raise SystemExit(f"ECHEC: {' '.join(map(str, cmd))[:220]}\n{r.stderr[-1800:]}")


def concat(segs):
    liste = f"{ED}/build/concat2.txt"
    with open(liste, "w") as f:
        for i, s in enumerate(segs):
            p = (f"{ED}/segments2/seg_{i:03d}.mp4" if s["kind"] == "av"
                 else f"{ED}/illus/mp4/{s['illus']}.mp4")
            f.write(f"file '{p}'\n")
    sh(["ffmpeg", "-y", "-v", "error", "-f", "concat", "-safe", "0",
        "-i", liste, "-c", "copy", f"{ED}/build/visuel2.mp4"])


def incruster(ovls):
    """Chaque mot-cle est une sequence PNG RGBA rendue dans Chromium ;
    tpad la decale a la seconde voulue, overlay la compose."""
    cmd = ["ffmpeg", "-y", "-v", "error", "-i", f"{ED}/build/visuel2.mp4"]
    for o in ovls:
        cmd += ["-framerate", str(FPS), "-i", f"{ED}/build/ovl/{o['id']}/%04d.png"]
    parties, prec = [], "0:v"
    for i, o in enumerate(ovls, start=1):
        parties.append(f"[{i}:v]format=rgba,"
                       f"tpad=start_duration={o['start']:.3f}:start_mode=add:color=#00000000[m{i}]")
        parties.append(f"[{prec}][m{i}]overlay=0:0:format=auto:eof_action=pass:"
                       f"repeatlast=0[v{i}]")
        prec = f"v{i}"
    cmd += ["-filter_complex", ";".join(parties), "-map", f"[{prec}]",
            "-c:v", "libx264", "-preset", "medium", "-crf", "18",
            "-pix_fmt", "yuv420p", "-r", str(FPS), "-an", f"{ED}/build/visuel2_mots.mp4"]
    sh(cmd)


def muxer():
    sh(["ffmpeg", "-y", "-v", "error",
        "-i", f"{ED}/build/visuel2_mots.mp4", "-i", f"{SRC}/avatar_raw.mp4",
        "-map", "0:v:0", "-map", "1:a:0", "-c:v", "copy", "-c:a", "copy",
        "-movflags", "+faststart", FINAL])


if __name__ == "__main__":
    segs = json.load(open(f"{ED}/build/edl2.json"))
    ovls = json.load(open(f"{ED}/build/ovl.json"))
    print("concatenation..."); concat(segs)
    print(f"incrustation de {len(ovls)} mots-cles..."); incruster(ovls)
    print("mux audio..."); muxer()
    print("termine ->", FINAL)
