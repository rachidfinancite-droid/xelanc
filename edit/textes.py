# -*- coding: utf-8 -*-
"""Rendu des textes arabes — Noto Naskh Arabic via Pillow (direction=rtl, language=ar).
Aucun reshaper : Raqm/HarfBuzz fait la mise en forme contextuelle et le bidi."""
import json, os
from PIL import Image, ImageDraw, ImageFont, ImageFilter, features

assert features.check("raqm"), "Raqm requis pour direction=rtl"

W, H   = 1080, 1920
NAVY   = (0x1E, 0x2A, 0x3B)
CREME  = (0xEF, 0xE7, 0xD8)
OR     = (0xB8, 0x95, 0x54)
BOLD   = "/usr/share/fonts/truetype/noto/NotoNaskhArabic-Bold.ttf"
REG    = "/usr/share/fonts/truetype/noto/NotoNaskhArabic-Regular.ttf"
OUT    = "/home/user/xelanc/edit/png"
RTL    = dict(direction="rtl", language="ar")

# --- Mots-cles en surimpression, cales sur le SRT (debut, fin) -------------
MOTS = [
    ("k01", "خمس أيام",            7.20,  10.40),
    ("k02", "٢٥ يوم",             13.90,  17.20),
    ("k03", "حبس ٣٠ يوم",         26.90,  30.80),
    ("k04", "جيت هارب",           61.40,  65.00),
    ("k05", "كل ساعة",            90.60,  93.00),
    ("k06", "ناعس وكتدخل الفلوس", 99.90, 103.40),
    ("k07", "الباب",             117.40, 120.60),
    ("k08", "قواعد",             135.80, 138.00),
    ("k09", "ممارسات",           138.10, 140.30),
    ("k10", "قيم",               140.40, 142.60),
    ("k11", "خلصت الثمن غالي",   146.40, 150.20),
    ("k12", "السبع",             168.60, 172.00),
    ("k13", "الحبس ولا السبع",   177.90, 181.20),
]

# --- Cartons pleins ecran (echos litteraux du discours) -------------------
CARTONS = {
    "C1": "الحبس ديال ٣٠ يوم",
    "C2": "هادا نظام",
    "C3": "ما جيتش باش ننجح",
    "C4": "النتيجة ما كنتش نتوقعها",
    "C5": "المقاولة ماشي موضة",
    "C6": "تعلمتهم فالطريق",
    "C7": "الحبس ولا السبع؟",
}


def mesure(txt, font):
    im = Image.new("RGB", (10, 10))
    return ImageDraw.Draw(im).textbbox((0, 0), txt, font=font, **RTL)


def ajuster(txt, chemin, largeur_max, taille_dep, mini=40):
    """Plus grande taille de police tenant dans largeur_max."""
    t = taille_dep
    while t > mini:
        f = ImageFont.truetype(chemin, t)
        b = mesure(txt, f)
        if b[2] - b[0] <= largeur_max:
            return f, b
        t -= 2
    f = ImageFont.truetype(chemin, mini)
    return f, mesure(txt, f)


def mot_cle(nom, txt):
    """Plaque navy + texte creme + filet or. PNG transparent, rogne au contenu."""
    font, b = ajuster(txt, BOLD, 880, 96)
    tw, th = b[2] - b[0], b[3] - b[1]
    padx, pady, rayon = 46, 30, 28
    pw, ph = tw + 2 * padx, th + 2 * pady + 22        # +22 : filet or
    im = Image.new("RGBA", (pw + 40, ph + 40), (0, 0, 0, 0))
    d = ImageDraw.Draw(im)
    ox, oy = 20, 20
    # ombre portee
    omb = Image.new("RGBA", im.size, (0, 0, 0, 0))
    ImageDraw.Draw(omb).rounded_rectangle(
        [ox + 4, oy + 8, ox + pw + 4, oy + ph + 8], rayon, fill=(0, 0, 0, 120))
    im.alpha_composite(omb.filter(ImageFilter.GaussianBlur(10)))
    # plaque
    d.rounded_rectangle([ox, oy, ox + pw, oy + ph], rayon, fill=NAVY + (238,))
    # texte (ancrage a droite : naturel en RTL)
    d.text((ox + pw - padx, oy + pady - b[1]), txt, font=font,
           fill=CREME + (255,), anchor="ra", **RTL)
    # filet or sous le texte
    fy = oy + pady + th + 12
    d.rounded_rectangle([ox + padx, fy, ox + pw - padx, fy + 7], 4, fill=OR + (255,))
    im.crop(im.getbbox()).save(f"{OUT}/{nom}.png")
    return im.getbbox()


def carton(nom, txt):
    """Carton plein ecran 1080x1920, degrade navy + vignette + filets or."""
    im = Image.new("RGB", (W, H), NAVY)
    d = ImageDraw.Draw(im)
    # degrade vertical subtil
    for y in range(H):
        k = 1 - abs(y - H * 0.42) / (H * 0.9)
        f = 1 + 0.30 * max(0.0, k)
        d.line([(0, y), (W, y)], fill=tuple(min(255, int(c * f)) for c in NAVY))
    # vignette
    vg = Image.radial_gradient("L").resize((W, H)).point(lambda v: int(v * 0.62))
    im = Image.composite(Image.new("RGB", (W, H), (8, 12, 18)), im, vg)
    d = ImageDraw.Draw(im)
    # texte sur 2 lignes max
    mots = txt.split(" ")
    lignes = [txt]
    if len(mots) > 3:
        c = len(mots) // 2
        lignes = [" ".join(mots[:c]), " ".join(mots[c:])]
    font = min((ajuster(l, BOLD, 860, 150)[0] for l in lignes), key=lambda f: f.size)
    boites = [mesure(l, font) for l in lignes]
    hs = [b[3] - b[1] for b in boites]
    inter = int(font.size * 0.45)
    total = sum(hs) + inter * (len(lignes) - 1)
    y = (H - total) // 2
    lmax = max(b[2] - b[0] for b in boites)
    # filets or au-dessus / en dessous
    d.rounded_rectangle([(W - 190) // 2, y - 92, (W + 190) // 2, y - 85], 4, fill=OR)
    for l, b, hh in zip(lignes, boites, hs):
        d.text((W // 2, y - b[1]), l, font=font, fill=CREME, anchor="ma", **RTL)
        y += hh + inter
    y = y - inter + 78
    d.rounded_rectangle([(W - 190) // 2, y, (W + 190) // 2, y + 7], 4, fill=OR)
    im.save(f"{OUT}/{nom}.png")
    return lmax, font.size


if __name__ == "__main__":
    os.makedirs(OUT, exist_ok=True)
    for nom, txt, *_ in MOTS:
        bb = mot_cle(nom, txt)
        print(f"  {nom}  {txt:22}  {bb[2]-bb[0]:4}x{bb[3]-bb[1]:3} px")
    for nom, txt in CARTONS.items():
        lm, ts = carton(nom, txt)
        print(f"  {nom}  {txt:26}  police {ts}px  largeur {lm}px")
    json.dump([{"id": n, "txt": t, "start": a, "end": b} for n, t, a, b in MOTS],
              open("/home/user/xelanc/edit/build/mots.json", "w"),
              ensure_ascii=False, indent=1)
    print(f"\n{len(MOTS)} mots-cles + {len(CARTONS)} cartons -> {OUT}")
