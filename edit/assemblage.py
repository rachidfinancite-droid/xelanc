# -*- coding: utf-8 -*-
"""Concatenation des segments, incrustation des mots-cles, mux audio intact."""
import json, subprocess, os
from PIL import Image

ED  = "/home/user/xelanc/edit"
SRC = "/home/user/xelanc/media/source"
TOTAL = 182.70
Y_BAS = 1320                       # tiers inferieur : ne couvre jamais le visage
# les trois mots de la liste s'empilent et restent ensemble a l'ecran
LISTE = {"k08": (1090, 142.6), "k09": (1320, 142.6), "k10": (1550, 142.6)}
MONTEE, F_IN, F_OUT = 38, 0.32, 0.28


def sh(cmd, **kw):
    r = subprocess.run(cmd, capture_output=True, text=True, **kw)
    if r.returncode:
        raise SystemExit(f"ECHEC: {' '.join(map(str,cmd))[:200]}\n{r.stderr[-1500:]}")
    return r.stdout


def concat(segs):
    liste = f"{ED}/build/concat.txt"
    with open(liste, "w") as f:
        for i in range(len(segs)):
            f.write(f"file '{ED}/segments/seg_{i:03d}.mp4'\n")
    sh(["ffmpeg", "-y", "-v", "error", "-f", "concat", "-safe", "0",
        "-i", liste, "-c", "copy", f"{ED}/build/visuel.mp4"])


def incruster(mots):
    """Un PNG boucle par mot-cle ; les fondus alpha en temps absolu
    ouvrent et referment la fenetre d'apparition, `enable` evite tout calcul
    en dehors."""
    cmd = ["ffmpeg", "-y", "-v", "error", "-i", f"{ED}/build/visuel.mp4"]
    for m in mots:
        cmd += ["-loop", "1", "-t", str(TOTAL), "-i", f"{ED}/png/{m['id']}.png"]

    parties, prec = [], "0:v"
    for i, m in enumerate(mots, start=1):
        t0, t1 = m["start"], m["end"]
        parties.append(
            f"[{i}:v]format=rgba,"
            f"fade=t=in:st={t0:.3f}:d={F_IN}:alpha=1,"
            f"fade=t=out:st={t1-F_OUT:.3f}:d={F_OUT}:alpha=1[m{i}]")
        parties.append(
            f"[{prec}][m{i}]overlay=x='(W-w)/2'"
            f":y='{m['y']}+{MONTEE}*max(0\\,1-(t-{t0:.3f})/{F_IN})'"
            f":enable='between(t,{t0:.3f},{t1:.3f})'[v{i}]")
        prec = f"v{i}"

    cmd += ["-filter_complex", ";".join(parties), "-map", f"[{prec}]",
            "-c:v", "libx264", "-preset", "medium", "-crf", "18",
            "-pix_fmt", "yuv420p", "-r", "30", "-an",
            f"{ED}/build/visuel_mots.mp4"]
    sh(cmd)


def muxer():
    """Audio avatar recopie tel quel, sans reencodage ni coupe."""
    sh(["ffmpeg", "-y", "-v", "error",
        "-i", f"{ED}/build/visuel_mots.mp4", "-i", f"{SRC}/avatar_raw.mp4",
        "-map", "0:v:0", "-map", "1:a:0", "-c:v", "copy", "-c:a", "copy",
        "-movflags", "+faststart",
        "/home/user/xelanc/salaire-trauma-vertical.mp4"])


if __name__ == "__main__":
    segs = json.load(open(f"{ED}/build/edl.json"))
    mots = json.load(open(f"{ED}/build/mots.json"))
    for m in mots:
        y, fin = LISTE.get(m["id"], (Y_BAS, m["end"]))
        m["y"], m["end"] = y, fin
        h = Image.open(f"{ED}/png/{m['id']}.png").height
        assert y + h < 1900, f"{m['id']} deborde en bas"
    print("concatenation..."); concat(segs)
    print("incrustation des mots-cles..."); incruster(mots)
    print("mux audio..."); muxer()
    print("termine")
