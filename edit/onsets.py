# -*- coding: utf-8 -*-
"""Verification directe du calage levres/audio sur des attaques de parole.

On repere un instant ou la parole demarre apres un vrai silence (attaque
franche), puis on sort les images consecutives autour de cet instant.
Si les levres s'ouvrent AVANT l'attaque sonore, l'audio est en retard ;
si elles s'ouvrent APRES, l'audio est en avance."""
import subprocess
import numpy as np
from PIL import Image, ImageDraw

SRC = "/home/user/xelanc/media/source/avatar_raw.mp4"
SR, FPS = 16000, 25.0
QC = "/home/user/xelanc/edit/build/qc2"

brut = subprocess.run(["ffmpeg", "-v", "error", "-i", SRC, "-map", "0:a", "-ac", "1",
                       "-ar", str(SR), "-f", "s16le", "-"], capture_output=True).stdout
x = np.frombuffer(brut, np.int16).astype(np.float32) / 32768.0
pas = SR // 200                                   # enveloppe a 200 Hz (5 ms)
env = np.sqrt(np.array([np.mean(x[i:i+pas]**2) for i in range(0, len(x)-pas, pas)]) + 1e-12)
seuil = np.percentile(env, 75) * 0.45

def attaque(apres):
    """Premier instant ou l'energie franchit le seuil, apres un silence >= 0.6 s."""
    i = int(apres * 200)
    sil = 0
    while i < len(env) - 1:
        if env[i] < seuil * 0.5:
            sil += 1
        elif sil >= 120:                          # 0,6 s de silence
            return i / 200.0
        else:
            sil = 0
        i += 1
    return None

for cible in (31.0, 93.0, 121.0):
    t0 = attaque(cible)
    if t0 is None:
        print(f"pas d'attaque nette apres {cible}s"); continue
    print(f"attaque de parole a {t0:.3f}s")
    vign = []
    for k in range(-4, 5):                        # +/- 160 ms, pas de 40 ms
        t = t0 + k / FPS
        p = f"{QC}/on_{int(t0)}_{k}.png"
        subprocess.run(["ffmpeg", "-y", "-v", "error", "-ss", f"{t:.4f}", "-i", SRC,
                        "-frames:v", "1", "-vf", "crop=300:190:600:300,scale=190:-1", p],
                       check=True)
        e = env[int(t*200)] / (env.max() + 1e-9)
        vign.append((k, Image.open(p), e))
    w, h = vign[0][1].size
    sh = Image.new("RGB", (w*len(vign), h+46), (14, 18, 26))
    d = ImageDraw.Draw(sh)
    for i, (k, im, e) in enumerate(vign):
        sh.paste(im, (i*w, 0))
        col = (184,149,84) if k == 0 else (150,160,175)
        d.text((i*w+6, h+6), f"{k*40:+d}ms", fill=col)
        d.rectangle([i*w+6, h+30, i*w+6+int(e*(w-12)), h+38], fill=(184,149,84))
    sh.save(f"{QC}/attaque_{int(t0)}.png")
print("planches ecrites")
