# -*- coding: utf-8 -*-
"""Mesure objective du decalage levres / audio.

On compare deux courbes echantillonnees a la cadence image de la source :
  * l'energie de MOUVEMENT dans un rectangle serre sur la bouche ;
  * la variation de l'ENVELOPPE RMS de l'audio.
Les zones de silence sont ecartees (elles n'apportent que du bruit).
Un pic de correlation a k images = audio en avance (k>0) ou en retard (k<0).

Le sens du decalage est verifie par un test de controle : on decale
artificiellement l'audio d'un nombre connu d'images et on verifie que le pic
se deplace exactement d'autant."""
import subprocess, sys
import numpy as np

SRC = "/home/user/xelanc/media/source/avatar_raw.mp4"
FPS = 25.0
BOUCHE = "180:110:641:329"      # rectangle serre sur la bouche (verifie a l'image)
LARG, HAUT, SR = 72, 44, 16000
MAX_K = 12                       # +/- 480 ms


def mouvement_bouche(f):
    brut = subprocess.run(
        ["ffmpeg", "-v", "error", "-i", f,
         "-vf", f"crop={BOUCHE},scale={LARG}:{HAUT},format=gray",
         "-f", "rawvideo", "-"], capture_output=True).stdout
    n = len(brut) // (LARG * HAUT)
    im = np.frombuffer(brut[:n * LARG * HAUT], np.uint8).astype(np.float32)
    return np.abs(np.diff(im.reshape(n, HAUT * LARG), axis=0)).mean(axis=1), n


def env_audio(f, n):
    brut = subprocess.run(
        ["ffmpeg", "-v", "error", "-i", f, "-map", "0:a", "-ac", "1",
         "-ar", str(SR), "-f", "s16le", "-"], capture_output=True).stdout
    x = np.frombuffer(brut, np.int16).astype(np.float32) / 32768.0
    p = SR / FPS
    env = np.array([np.sqrt(np.mean(x[int(i*p):int((i+1)*p)] ** 2) + 1e-12)
                    for i in range(n)])
    return env


def cr(v):
    v = v - v.mean()
    return v / (v.std() + 1e-9)


def correler(mv, au, masque):
    """mv[k+i] vs au[i] : un pic en k>0 signifie que la bouche bouge k images
    APRES le son, donc que l'audio est en avance."""
    res = []
    for k in range(-MAX_K, MAX_K + 1):
        if k >= 0:
            x, y, m = mv[k:], au[:len(au) - k or None], masque[:len(masque) - k or None]
        else:
            x, y, m = mv[:k], au[-k:], masque[-k:]
        n = min(len(x), len(y), len(m))
        x, y, m = x[:n], y[:n], m[:n].astype(bool)
        if m.sum() < 50:
            res.append((k, 0.0)); continue
        a, b = cr(x[m]), cr(y[m])
        res.append((k, float(np.dot(a, b) / len(a))))
    return res


def pic(res):
    k, r = max(res, key=lambda t: t[1])
    d = dict(res)
    if k - 1 in d and k + 1 in d:            # affinage parabolique sous-image
        y0, y1, y2 = d[k - 1], d[k], d[k + 1]
        den = y0 - 2 * y1 + y2
        if den != 0:
            k = k + 0.5 * (y0 - y2) / den
    return k, r


def analyser(f, decalage_test=0):
    mv, n = mouvement_bouche(f)
    env = env_audio(f, n)
    if decalage_test:                        # decale l'audio d'un nombre connu d'images
        env = np.roll(env, decalage_test)
    au = np.abs(np.diff(env))
    m = min(len(mv), len(au))
    mv, au, env = mv[:m], au[:m], env[:m]
    masque = env > np.percentile(env, 55)    # on ne garde que la parole
    res = correler(mv, au, masque)
    k, r = pic(res)
    return res, k, r, masque.sum(), m


if __name__ == "__main__":
    f = sys.argv[1] if len(sys.argv) > 1 else SRC
    res, k, r, nm, m = analyser(f)
    print(f"{f}\n  {m} images, dont {nm} retenues comme parole\n")
    print("  decalage          correlation")
    for kk, rr in res:
        print(f"   {kk:+3d} img {kk/FPS*1000:+7.0f} ms   {rr:+.4f}"
              f"{'   <<<' if kk == max(res, key=lambda t: t[1])[0] else ''}")
    print(f"\n  >>> MESURE : {k:+.2f} image = {k/FPS*1000:+.0f} ms   (r max = {r:.4f})")

    print("\n=== TEST DE CONTROLE (audio decale artificiellement de +5 images) ===")
    _, k2, r2, _, _ = analyser(f, decalage_test=5)
    # np.roll(env, +5) RETARDE l'audio de 5 images : le pic doit donc RECULER de 5
    print(f"  mesure attendue : {k-5:+.2f} img    mesure obtenue : {k2:+.2f} img")
    ok = abs((k2 - k) + 5) < 0.6
    print(f"  {'METHODE VALIDEE (signe et echelle corrects)' if ok else 'METHODE NON FIABLE'}")
