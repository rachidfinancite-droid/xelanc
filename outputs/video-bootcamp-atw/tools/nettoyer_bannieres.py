"""Efface le titre incrusté des bannières de la plateforme (c6, c7, c8) par inpainting,
pour obtenir la même photo sans texte. Sortie : assets/bannieres/clean/<id>.jpg (1920 de large)."""
import cv2, numpy as np, os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = {'c6': 'c6.png', 'c7': 'c7.jpg', 'c8': 'c8.jpg'}
XMAX = {'c6': 0.49, 'c7': 0.66, 'c8': 0.53}  # limite droite du titre incrusté, par bannière

for cid, f in SRC.items():
    im = cv2.imread(os.path.join(ROOT, 'assets', 'bannieres', f))
    h, w = im.shape[:2]
    hsv = cv2.cvtColor(im, cv2.COLOR_BGR2HSV)
    # Lettres : traits fins et clairs, détectés par chapeau haut-de-forme (top-hat) sur la luminance,
    # ce qui ignore les grandes surfaces claires (fenêtre, mur) et ne garde que l'écriture.
    v = hsv[..., 2]
    k = cv2.getStructuringElement(cv2.MORPH_RECT, (max(9, w // 40), max(9, w // 40)))
    tophat = cv2.morphologyEx(v, cv2.MORPH_TOPHAT, k)
    mask = np.zeros((h, w), np.uint8)
    x1, y1, y2 = int(w * XMAX[cid]), int(h * 0.25), int(h * 0.80)
    mask[y1:y2, :x1] = (tophat[y1:y2, :x1] > 45).astype(np.uint8) * 255
    mask = cv2.dilate(mask, np.ones((3, 3), np.uint8), iterations=2)
    out = cv2.inpaint(im, mask, 7, cv2.INPAINT_NS)
    out = cv2.resize(out, (1920, int(h * 1920 / w)), interpolation=cv2.INTER_LANCZOS4)
    d = os.path.join(ROOT, 'assets', 'bannieres', 'clean')
    os.makedirs(d, exist_ok=True)
    cv2.imwrite(os.path.join(d, cid + '.jpg'), out, [cv2.IMWRITE_JPEG_QUALITY, 90])
    print(cid, 'ok', int(mask.mean() / 2.55), '% masqué')
