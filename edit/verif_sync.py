# -*- coding: utf-8 -*-
"""Comparaison avant / apres sur le meme passage, meme cadrage, meme audio.
AVANT  : l'image du visage au temps t (ce que Rachid a juge decale).
APRES  : l'image du visage au temps t - 120 ms, l'audio inchange.
"""
import subprocess, os
SRC = "/home/user/xelanc/media/source/avatar_raw.mp4"
B, DEB, DUREE, MARGE, AVANCE = "/home/user/xelanc/edit/build/sync", 51.0, 12.0, 0.6, 0.120
POLICE = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
CADRE = "fps=30,crop=608:1080:441:0,scale=1080:1920:flags=lanczos"


def sh(c):
    r = subprocess.run(c, capture_output=True, text=True)
    if r.returncode:
        raise SystemExit(f"ECHEC\n{r.stderr[-900:]}")


os.makedirs(B, exist_ok=True)
sh(["ffmpeg", "-y", "-v", "error", "-ss", str(DEB - MARGE), "-t", str(DUREE + 2 * MARGE),
    "-i", SRC, "-vn", "-ac", "2", "-ar", "48000", "-c:a", "pcm_s16le", f"{B}/son.wav"])

parts = []
for i, (av, lib) in enumerate([(0.0, "AVANT   image au temps t"),
                               (AVANCE, "APRES   image avancee de 120 ms")]):
    sh(["ffmpeg", "-y", "-v", "error", "-ss", f"{DEB - av:.4f}", "-t", str(DUREE),
        "-i", SRC, "-an", "-vf", CADRE, "-c:v", "libx264", "-crf", "20",
        "-pix_fmt", "yuv420p", f"{B}/i{i}.mp4"])
    txt = (f"drawtext=fontfile={POLICE}:text='{lib}':fontsize=50:fontcolor=#EFE7D8:"
           f"box=1:boxcolor=#1E2A3B@0.92:boxborderw=26:x=(w-text_w)/2:y=140")
    sh(["ffmpeg", "-y", "-v", "error", "-i", f"{B}/i{i}.mp4",
        "-ss", str(MARGE), "-i", f"{B}/son.wav", "-map", "0:v", "-map", "1:a",
        "-t", str(DUREE), "-vf", txt, "-c:v", "libx264", "-crf", "24",
        "-pix_fmt", "yuv420p", "-c:a", "aac", "-b:a", "160k", f"{B}/p{i}.mp4"])
    parts.append(f"{B}/p{i}.mp4")

with open(f"{B}/l2.txt", "w") as f:
    for p in parts: f.write(f"file '{p}'\n")
sh(["ffmpeg", "-y", "-v", "error", "-f", "concat", "-safe", "0", "-i", f"{B}/l2.txt",
    "-c", "copy", "-movflags", "+faststart", "/home/user/xelanc/verif-synchro-avant-apres.mp4"])
print("ecrit")
