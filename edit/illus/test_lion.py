# -*- coding: utf-8 -*-
import sys, os, math
sys.path.insert(0, os.path.dirname(__file__))
from apercu import apercu

def lion(taille=560, d0=.3):
    """Tete de lion stylisee : criniere en touffes irregulieres, oreilles,
    face en ecusson, museau feline. Apparait partie par partie."""
    pts = []
    N = 46
    for i in range(N):
        a = i / N * 2 * math.pi - math.pi / 2
        # touffes : bosses irregulieres, jamais un rayon constant
        r = 84 + 15 * abs(math.sin(3.5 * a + .4)) + 7 * math.sin(9 * a + 1.1) \
              + 4 * math.sin(17 * a)
        pts.append(f"{100 + r*1.07*math.cos(a):.1f},{97 + r*math.sin(a):.1f}")
    criniere = "M" + " L".join(pts) + " Z"
    return f'''<svg viewBox="0 0 200 200" width="{taille}" height="{taille}">
<path d="M70 44 l-6 -22 l24 11 z" fill="#9A7B41" class="a pop" style="--d:{d0+.1:.2f}s"/>
<path d="M130 44 l6 -22 l-24 11 z" fill="#9A7B41" class="a pop" style="--d:{d0+.14:.2f}s"/>
<path d="{criniere}" fill="#B89554" class="a pop" style="--d:{d0:.2f}s"/>
<path d="M100 50 C126 50 141 68 141 94 C141 122 124 148 100 148
         C76 148 59 122 59 94 C59 68 74 50 100 50 Z"
  fill="#26344A" class="a pop" style="--d:{d0+.35:.2f}s"/>
<path d="M72 84 Q83 74 95 84 Q83 92 72 84 Z" fill="#F2E4C6" class="a pop" style="--d:{d0+.55:.2f}s"/>
<path d="M105 84 Q117 74 128 84 Q117 92 105 84 Z" fill="#F2E4C6" class="a pop" style="--d:{d0+.6:.2f}s"/>
<circle cx="83" cy="83" r="4.4" fill="#1E2A3B" class="a fade" style="--d:{d0+.75:.2f}s"/>
<circle cx="117" cy="83" r="4.4" fill="#1E2A3B" class="a fade" style="--d:{d0+.77:.2f}s"/>
<path d="M92 68 L78 63 M108 68 L122 63" stroke="#F2E4C6" stroke-width="3.4"
  stroke-linecap="round" class="a fade" style="--d:{d0+.68:.2f}s" opacity=".8"/>
<ellipse cx="86" cy="115" rx="13" ry="10" fill="#31435E" class="a pop" style="--d:{d0+.85:.2f}s"/>
<ellipse cx="114" cy="115" rx="13" ry="10" fill="#31435E" class="a pop" style="--d:{d0+.88:.2f}s"/>
<path d="M100 100 l-9 7 q9 5 18 0 z" fill="#F2E4C6" class="a pop" style="--d:{d0+.95:.2f}s"/>
<path d="M100 108 v7 M100 115 Q89 125 80 116 M100 115 Q111 125 120 116"
  stroke="#F2E4C6" stroke-width="4.2" fill="none" stroke-linecap="round"
  class="a fade" style="--d:{d0+1.1:.2f}s"/>
<path d="M74 112 l-14 -4 M74 118 l-14 2 M126 112 l14 -4 M126 118 l14 2"
  stroke="#F2E4C6" stroke-width="2.6" stroke-linecap="round" opacity=".65"
  class="a fade" style="--d:{d0+1.2:.2f}s"/>
</svg>'''

if __name__ == "__main__":
    apercu(f'<div class="titre">ولا باغي <span class="or">تولي سبع</span>؟</div>{lion()}',
           2.2, "/home/user/xelanc/edit/build/qc/lion_v2.png")
    print("ok")
