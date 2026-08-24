# -*- coding: utf-8 -*-
"""Systeme graphique des illustrations.

Charte : bleu navy, gris argente, blanc. Typographie Inter.
Parti pris de mise en page : composition ALIGNEE A GAUCHE, pas de centrage
systematique — c'est le centrage generalise qui donnait au montage precedent
son air de diapositive generique."""
from fonts_inline import FACES

ENCRE      = "#0B1524"     # fond profond
NAVY       = "#132338"
NAVY_CLAIR = "#1E3350"     # surfaces
NAVY_HAUT  = "#27405F"     # surfaces claires
BORD       = "#3A5473"
ARGENT     = "#AEBBC9"     # accent
ARGENT_VIF = "#DDE5EE"
BLANC      = "#FFFFFF"

BASE_CSS = FACES + """
*{margin:0;padding:0;box-sizing:border-box}
html,body{width:1080px;height:1920px;overflow:hidden;background:#0B1524}
body{font-family:'Inter',sans-serif;color:#FFFFFF;-webkit-font-smoothing:antialiased;
     font-feature-settings:'tnum' 1}

.scene{position:absolute;inset:0;display:flex;align-items:center;padding:0 84px;
  background:radial-gradient(115% 80% at 26% 22%,#1B2E48 0%,#132338 52%,#0B1524 100%);
  transform-origin:34% 46%;animation:derive var(--D) linear both}
@keyframes derive{from{transform:scale(1)}to{transform:scale(1.045)}}
.contenu{display:flex;flex-direction:column;align-items:flex-start;gap:var(--gap,48px);
  width:100%}
.grain{position:absolute;inset:-50px;pointer-events:none;opacity:.12;
  background-image:url("data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='180' height='180'><filter id='n'><feTurbulence baseFrequency='.85' numOctaves='3'/></filter><rect width='180' height='180' filter='url(%23n)'/></svg>")}
.vign{position:absolute;inset:0;pointer-events:none;
  background:radial-gradient(78% 58% at 34% 44%,transparent 52%,rgba(4,8,15,.66) 100%)}

/* --- typographie --- */
.titre{font-weight:900;font-size:112px;line-height:1.04;letter-spacing:-.028em;
  text-transform:uppercase;text-align:left;text-shadow:0 6px 34px rgba(0,0,0,.4)}
.titre.sm{font-size:86px} .titre.xs{font-size:66px}
.sous{font-weight:400;font-size:46px;line-height:1.34;color:#AEBBC9;text-align:left;
  letter-spacing:-.005em}
.arg{color:#AEBBC9} .vif{color:#DDE5EE}
.filet{width:132px;height:3px;background:#AEBBC9}
.centre{align-self:center}

/* --- primitives d'animation (--d = retard) --- */
.a{animation-duration:.72s;animation-fill-mode:both;
   animation-timing-function:cubic-bezier(.16,.84,.3,1);animation-delay:var(--d,0s)}
.up{animation-name:up}     @keyframes up{from{opacity:0;transform:translateY(52px)}to{opacity:1;transform:none}}
.down{animation-name:down} @keyframes down{from{opacity:0;transform:translateY(-52px)}to{opacity:1;transform:none}}
.pop{animation-name:pop}   @keyframes pop{from{opacity:0;transform:scale(.84)}to{opacity:1;transform:none}}
.fade{animation-name:fade} @keyframes fade{from{opacity:0}to{opacity:1}}
.gliss{animation-name:gl}  @keyframes gl{from{opacity:0;transform:translateX(-64px)}to{opacity:1;transform:none}}
.eteint{animation-name:et} @keyframes et{from{opacity:1}to{opacity:.3}}
.allume{animation-name:al} @keyframes al{
  from{background:#1E3350;box-shadow:none;color:transparent;border-color:#1E3350}
  to{background:#AEBBC9;box-shadow:0 0 42px rgba(174,187,201,.5);color:#0B1524;border-color:#DDE5EE}}
.barre{animation-name:ba;animation-duration:.5s} @keyframes ba{from{width:0}to{width:100%}}
.pulse{animation:pl 1.5s ease-in-out infinite both}
@keyframes pl{0%,100%{opacity:.34;transform:scale(1)}50%{opacity:1;transform:scale(1.08)}}
.tourne{animation:tn 8s linear infinite both}     @keyframes tn{to{transform:rotate(360deg)}}
.tourne-inv{animation:tni 8s linear infinite both}@keyframes tni{to{transform:rotate(-360deg)}}

/* --- composants --- */
.grille{display:grid;grid-template-columns:repeat(6,1fr);gap:18px;width:840px}
.case{aspect-ratio:1;border-radius:4px;background:#1E3350;border:2px solid #1E3350;
  display:flex;align-items:center;justify-content:center;font-size:40px;font-weight:700;
  color:transparent}
.carte{background:rgba(255,255,255,.05);border-left:4px solid #AEBBC9;border-radius:4px;
  padding:30px 44px;font-size:60px;font-weight:700;min-width:520px;text-align:left}
.rangee{display:flex;align-items:center;gap:22px;width:100%}
.pastille{width:28px;height:28px;border-radius:50%;background:#AEBBC9;
  box-shadow:0 0 20px rgba(174,187,201,.45)}
.ligne-item{display:flex;align-items:center;gap:34px;width:100%;font-size:82px;
  font-weight:900;letter-spacing:-.02em;text-transform:uppercase}
.num{flex:0 0 84px;font-size:38px;font-weight:500;color:#AEBBC9;letter-spacing:.06em;
  border-top:2px solid #AEBBC9;padding-top:12px}
.raye{position:relative;display:inline-block}
.raye i{position:absolute;left:0;top:52%;height:8px;background:#AEBBC9;border-radius:4px;
  display:block}
.tel{width:496px;height:980px;border-radius:56px;border:6px solid #3A5473;
  background:#0D1826;position:relative;overflow:hidden;box-shadow:0 30px 90px rgba(0,0,0,.55)}
.notif{position:absolute;left:22px;right:22px;background:#DDE5EE;color:#0B1524;
  border-radius:10px;padding:22px 28px;font-size:38px;font-weight:700;
  display:flex;justify-content:space-between;align-items:center}
.compteur{font-size:164px;font-weight:900;color:#FFFFFF;letter-spacing:-.04em;
  white-space:nowrap}
"""

# Ajustement automatique : le francais est plus long que l'arabe, on reduit la
# typo jusqu'a ce que le contenu tienne dans le cadre.
AJUST = """
(() => {
  const sc = document.querySelector('.scene'), ct = document.querySelector('.contenu');
  if (!sc || !ct) return;
  const dispo = sc.clientHeight - 150;
  const el = [...ct.querySelectorAll('.titre,.sous,.ligne-item,.carte,.compteur')];
  const base = el.map(e => parseFloat(getComputedStyle(e).fontSize));
  let k = 1;
  while (ct.scrollHeight > dispo && k > 0.46) {
    k -= 0.035;
    el.forEach((e, i) => e.style.fontSize = (base[i] * k).toFixed(1) + 'px');
  }
})();
"""


def page(inner, duree, css="", gap=48):
    return f"""<!doctype html><html lang="fr"><head><meta charset="utf-8">
<style>{BASE_CSS}{css}
:root{{--D:{duree}s;--gap:{gap}px}}</style></head><body>
<div class="scene"><div class="contenu">{inner}</div>
<div class="grain"></div><div class="vign"></div></div>
<script>{AJUST}</script></body></html>"""


# --- incrustations : plaque de mot-cle sur fond transparent -----------------
CSS_OVL = """
html,body{background:transparent!important}
.ovl{position:absolute;left:84px;right:84px;bottom:320px;display:flex;
  animation:ovl-sortie var(--t-out) cubic-bezier(.4,0,.7,.2) var(--sortie) both}
@keyframes ovl-sortie{from{opacity:1;transform:none}to{opacity:0;transform:translateY(30px)}}
.plaque{position:relative;background:rgba(11,21,36,.93);border-left:5px solid #AEBBC9;
  border-radius:4px;padding:26px 44px 34px;box-shadow:0 18px 54px rgba(0,0,0,.55);
  animation:plaque var(--t-in) cubic-bezier(.16,.9,.3,1) both}
@keyframes plaque{from{opacity:0;transform:translateX(-38px)}to{opacity:1;transform:none}}
.plaque span{display:inline-block;font-size:76px;font-weight:900;color:#FFFFFF;
  letter-spacing:-.025em;text-transform:uppercase;white-space:nowrap;
  animation:volet var(--t-volet) cubic-bezier(.3,.9,.2,1) var(--t-volet-d) both}
/* devoilement de gauche a droite : sens de lecture du francais */
@keyframes volet{from{clip-path:inset(0 100% 0 0)}to{clip-path:inset(0 0 0 0)}}
.plaque i{position:absolute;left:44px;bottom:18px;height:5px;border-radius:3px;
  background:#AEBBC9;animation:filet-in var(--t-volet) cubic-bezier(.2,.9,.3,1) var(--t-filet) both}
@keyframes filet-in{from{width:0}to{width:calc(100% - 88px)}}
"""


def page_ovl(texte, duree):
    """Durees proportionnelles : meme une incrustation courte reste lisible."""
    t_in    = min(0.42, duree * 0.26)
    t_volet = min(0.52, duree * 0.30)
    t_out   = min(0.34, duree * 0.22)
    d_volet = t_in * 0.35
    return f"""<!doctype html><html lang="fr"><head><meta charset="utf-8">
<style>{BASE_CSS}{CSS_OVL}
:root{{--D:{duree}s;--t-in:{t_in:.3f}s;--t-volet:{t_volet:.3f}s;
--t-volet-d:{d_volet:.3f}s;--t-filet:{d_volet + t_volet * 0.45:.3f}s;
--t-out:{t_out:.3f}s;--sortie:{max(0.05, duree - t_out):.3f}s}}</style></head>
<body><div class="ovl"><div class="plaque"><span>{texte}</span><i></i></div></div>
<script>
(() => {{
  const o = document.querySelector('.ovl'), p = document.querySelector('.plaque'),
        s = p.querySelector('span');
  let f = parseFloat(getComputedStyle(s).fontSize);
  while (p.getBoundingClientRect().width > o.clientWidth && f > 34) {{
    f -= 2; s.style.fontSize = f + 'px';
  }}
}})();
</script></body></html>"""
