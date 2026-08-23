# -*- coding: utf-8 -*-
"""Fabrique un fichier unique enchainant le meme passage parle avec plusieurs
decalages audio. Rachid regarde une fois et designe le bon : la perception
humaine reste le juge le plus fiable pour un calage labial."""
import subprocess, os

SRC = "/home/user/xelanc/media/source/avatar_raw.mp4"
B   = "/home/user/xelanc/edit/build/sync"
DEB, DUREE, MARGE = 51.0, 12.0, 0.6
# decalage positif = le SON arrive PLUS TARD que l'image
DECALAGES = [(-0.160, "SON PLUS TOT DE 160 ms"), (-0.080, "SON PLUS TOT DE 80 ms"),
             (0.000,  "TEL QUEL  (0 ms)"),
             (+0.080, "SON PLUS TARD DE 80 ms"), (+0.160, "SON PLUS TARD DE 160 ms")]
POLICE = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"


def sh(c):
    r = subprocess.run(c, capture_output=True, text=True)
    if r.returncode:
        raise SystemExit(f"ECHEC {' '.join(map(str,c))[:180]}\n{r.stderr[-900:]}")


os.makedirs(B, exist_ok=True)
# image de reference : meme cadrage 9:16 que le montage, sans zoom (on juge les levres)
sh(["ffmpeg", "-y", "-v", "error", "-ss", str(DEB), "-t", str(DUREE), "-i", SRC, "-an",
    "-vf", "fps=30,crop=608:1080:441:0,scale=1080:1920:flags=lanczos",
    "-c:v", "libx264", "-crf", "18", "-pix_fmt", "yuv420p", f"{B}/img.mp4"])
sh(["ffmpeg", "-y", "-v", "error", "-ss", str(DEB - MARGE), "-t", str(DUREE + 2 * MARGE),
    "-i", SRC, "-vn", "-ac", "2", "-ar", "48000", "-c:a", "pcm_s16le", f"{B}/son.wav"])

parts = []
for i, (d, lib) in enumerate(DECALAGES):
    o = f"{B}/v{i}.mp4"
    txt = (f"drawtext=fontfile={POLICE}:text='{lib}':fontsize=52:fontcolor=#EFE7D8:"
           f"box=1:boxcolor=#1E2A3B@0.92:boxborderw=26:x=(w-text_w)/2:y=140")
    sh(["ffmpeg", "-y", "-v", "error",
        "-i", f"{B}/img.mp4", "-ss", f"{MARGE - d:.3f}", "-i", f"{B}/son.wav",
        "-map", "0:v", "-map", "1:a", "-t", str(DUREE), "-vf", txt,
        "-c:v", "libx264", "-crf", "20", "-pix_fmt", "yuv420p",
        "-c:a", "aac", "-b:a", "160k", o])
    parts.append(o)

with open(f"{B}/liste.txt", "w") as f:
    for p in parts:
        f.write(f"file '{p}'\n")
sh(["ffmpeg", "-y", "-v", "error", "-f", "concat", "-safe", "0", "-i", f"{B}/liste.txt",
    "-c", "copy", "-movflags", "+faststart", "/home/user/xelanc/test-synchro-levres.mp4"])
print("ecrit : test-synchro-levres.mp4")
