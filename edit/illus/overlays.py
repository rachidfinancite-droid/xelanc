# -*- coding: utf-8 -*-
"""Mots-cles incrustes sur les plans ou Rachid parle.

Chaque mot est place dans l'intersection entre le moment ou il est PRONONCE
(transcription Descript) et un plan avatar : le mot apparait sur son visage,
puis l'illustration qui suit le developpe."""
import json, os, shutil, subprocess, sys
sys.path.insert(0, os.path.dirname(__file__))
from base import page_ovl

CHROME = "/opt/pw-browsers/chromium-1194/chrome-linux/chrome"
ED, FPS = "/home/user/xelanc/edit", 30
MIN = 1.2          # duree minimale pour qu'une incrustation ait le temps d'exister

# (texte, debut prononce, fin prononcee) — releves sur le SRT
DITS = [
    ("Cinq jours",                6.54,  11.10),
    ("25 jours",                 13.26,  16.80),
    ("Prison de 30 jours",       26.42,  30.48),
    ("Traumatisme",              45.84,  50.42),
    ("J'ai fui",                 61.02,  66.86),
    ("Chaque heure",             89.24,  92.72),
    ("Tu dors, l'argent rentre", 99.58, 102.46),
    ("La porte",                115.68, 120.80),
    ("Des règles",              135.29, 138.00),
    ("Des pratiques",           138.00, 140.30),
    ("Des valeurs",             140.30, 142.02),
    ("J'ai payé cher",          142.05, 150.45),
    ("Le lion",                 166.02, 172.92),
    ("La prison ou le lion",    177.96, 179.52),
]


def placer():
    """Ne garde que les mots qui tombent sur un plan avatar assez longtemps."""
    segs = json.load(open(f"{ED}/build/edl2.json"))
    av = [s for s in segs if s["kind"] == "av"]
    out, pris = [], set()
    for i, (txt, d, f) in enumerate(DITS):
        best = None
        for s in av:
            a, b = max(d, s["start"]), min(f, s["end"])
            if b - a >= MIN and s["start"] not in pris:
                if best is None or (b - a) > best[1] - best[0]:
                    best = (a, b, s["start"])
        if best:
            a, b, cle = best
            pris.add(cle)
            out.append({"id": f"o{i:02d}", "txt": txt,
                        "start": round(a + .05, 2), "dur": round(min(b - a - .05, 3.4), 2)})
    return out


def rendre(ovls):
    from playwright.sync_api import sync_playwright
    base = f"{ED}/build/ovl"
    shutil.rmtree(base, ignore_errors=True)
    os.makedirs(base, exist_ok=True)
    with sync_playwright() as p:
        nav = p.chromium.launch(executable_path=CHROME)
        pg = nav.new_page(viewport={"width": 1080, "height": 1920}, device_scale_factor=1)
        for o in ovls:
            d = f"{base}/{o['id']}"; os.makedirs(d, exist_ok=True)
            pg.set_content(page_ovl(o["txt"], o["dur"]), wait_until="load")
            pg.evaluate("() => document.fonts.ready")
            pg.evaluate("() => document.getAnimations().forEach(a => a.pause())")
            n = round(o["dur"] * FPS)
            for k in range(n):
                pg.evaluate("(t) => document.getAnimations().forEach(a => { a.currentTime = t; })",
                            k / FPS * 1000)
                pg.screenshot(path=f"{d}/{k:04d}.png", omit_background=True)
            o["frames"] = n
        nav.close()
    return ovls


if __name__ == "__main__":
    o = rendre(placer())
    json.dump(o, open(f"{ED}/build/ovl.json", "w"), ensure_ascii=False, indent=1)
    for x in o:
        print(f"  {x['id']}  {x['txt']:22} {x['start']:6.1f}s  ({x['dur']}s, {x['frames']} images)")
    print(f"{len(o)} incrustations sur {len(DITS)} mots-cles "
          f"(les autres sont portes par une illustration)")
