# -*- coding: utf-8 -*-
"""Rend chaque illustration animee en MP4 1080x1920.

Chromium est pilote image par image : toutes les animations sont mises en pause
puis leur `currentTime` est force a la milliseconde voulue avant capture.
Le rendu est donc parfaitement deterministe (pas de dependance a la vitesse machine)."""
import json, os, subprocess, sys, shutil
from multiprocessing import Pool
sys.path.insert(0, os.path.dirname(__file__))
from base import page
from scenes import SCENES

CHROME = "/opt/pw-browsers/chromium-1194/chrome-linux/chrome"
ED     = "/home/user/xelanc/edit"
OUT    = f"{ED}/illus/mp4"
FPS    = 30
W, H   = 1080, 1920

PAUSE = "() => { const a = document.getAnimations(); a.forEach(x => x.pause()); return a.length; }"
SEEK  = "(t) => { document.getAnimations().forEach(a => { a.currentTime = t; }); }"


def rendre(nav, sid, duree):
    _, inner, css, gap = SCENES[sid]
    tmp = f"{ED}/build/frames/{sid}"
    shutil.rmtree(tmp, ignore_errors=True)
    os.makedirs(tmp, exist_ok=True)

    pg = nav.new_page(viewport={"width": W, "height": H}, device_scale_factor=1)
    pg.set_content(page(inner, duree, css, gap), wait_until="load")
    pg.evaluate("() => document.fonts.ready")
    n_anim = pg.evaluate(PAUSE)

    n = round(duree * FPS)
    for f in range(n):
        pg.evaluate(SEEK, f / FPS * 1000)
        pg.screenshot(path=f"{tmp}/{f:04d}.png")
    pg.close()

    r = subprocess.run(
        ["ffmpeg", "-y", "-v", "error", "-framerate", str(FPS), "-i", f"{tmp}/%04d.png",
         "-frames:v", str(n), "-c:v", "libx264", "-preset", "medium", "-crf", "17",
         "-pix_fmt", "yuv420p", "-r", str(FPS), "-g", "60", "-an", f"{OUT}/{sid}.mp4"],
        capture_output=True, text=True)
    shutil.rmtree(tmp, ignore_errors=True)
    if r.returncode:
        return f"ECHEC {sid}: {r.stderr[-300:]}"
    if n_anim == 0:
        return f"ALERTE {sid}: aucune animation detectee"
    return None


def lot(taches):
    """Un processus = une instance Playwright (l'API sync n'est pas partageable
    entre threads)."""
    from playwright.sync_api import sync_playwright
    out = []
    with sync_playwright() as p:
        nav = p.chromium.launch(executable_path=CHROME)
        try:
            for sid, dur in taches:
                out.append(rendre(nav, sid, dur))
        finally:
            nav.close()
    return out


def main(ids=None):
    segs = json.load(open(f"{ED}/build/edl2.json"))
    todo = [(s["illus"], s["dur"]) for s in segs
            if s["kind"] == "il" and (ids is None or s["illus"] in ids)]
    os.makedirs(OUT, exist_ok=True)
    os.makedirs(f"{ED}/build/frames", exist_ok=True)
    n_proc = min(3, len(todo))
    lots = [todo[i::n_proc] for i in range(n_proc)]
    with Pool(n_proc) as pool:
        pbs = [x for sous in pool.map(lot, lots) for x in sous if x]
    for x in pbs: print(x)
    print(f"{len(todo)-len(pbs)}/{len(todo)} illustrations rendues")
    return 1 if pbs else 0


if __name__ == "__main__":
    sys.exit(main(set(sys.argv[1:]) or None))
