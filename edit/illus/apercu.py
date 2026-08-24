# -*- coding: utf-8 -*-
"""Rendu d'une seule image d'une illustration, pour iterer vite sur le dessin."""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from base import page
from playwright.sync_api import sync_playwright
CHROME = "/opt/pw-browsers/chromium-1194/chrome-linux/chrome"

def apercu(inner, t, sortie, duree=3.5, css="", w=1080, h=1920, gap=48):
    with sync_playwright() as p:
        nav = p.chromium.launch(executable_path=CHROME)
        pg = nav.new_page(viewport={"width": w, "height": h}, device_scale_factor=1)
        pg.set_content(page(inner, duree, css, gap), wait_until="load")
        pg.evaluate("() => document.fonts.ready")
        pg.evaluate("() => document.getAnimations().forEach(a => a.pause())")
        pg.evaluate("(t) => document.getAnimations().forEach(a => { a.currentTime = t; })", t * 1000)
        pg.screenshot(path=sortie)
        nav.close()
