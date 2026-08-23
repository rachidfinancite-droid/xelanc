# -*- coding: utf-8 -*-
"""Systeme graphique commun aux illustrations : charte, typo, primitives d'animation."""

NAVY, CREME, OR = "#1E2A3B", "#EFE7D8", "#B89554"

BASE_CSS = """
*{margin:0;padding:0;box-sizing:border-box}
html,body{width:1080px;height:1920px;overflow:hidden;background:#1E2A3B}
body{font-family:'Noto Naskh Arabic',serif;color:#EFE7D8;
     -webkit-font-smoothing:antialiased}

/* --- fond : degrade + vignette + grain, toujours en mouvement lent --- */
.scene{position:absolute;inset:0;display:flex;flex-direction:column;
  align-items:center;justify-content:center;gap:64px;padding:120px 76px;
  background:radial-gradient(120% 85% at 50% 38%,#2A3A50 0%,#1E2A3B 55%,#151F2C 100%);
  transform-origin:50% 45%;animation:derive var(--D) linear both}
@keyframes derive{from{transform:scale(1)}to{transform:scale(1.05)}}
.grain{position:absolute;inset:-50px;pointer-events:none;opacity:.16;
  background-image:url("data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='180' height='180'><filter id='n'><feTurbulence baseFrequency='.85' numOctaves='3'/></filter><rect width='180' height='180' filter='url(%23n)'/></svg>")}
.vign{position:absolute;inset:0;pointer-events:none;
  background:radial-gradient(75% 55% at 50% 45%,transparent 55%,rgba(8,12,18,.62) 100%)}

/* --- typographie --- */
.titre{direction:rtl;font-weight:700;font-size:152px;line-height:1.24;text-align:center;
  letter-spacing:-1px;text-shadow:0 6px 30px rgba(0,0,0,.45)}
.titre.sm{font-size:120px} .titre.xs{font-size:96px}
.sous{direction:rtl;font-size:66px;color:#EFE7D8;opacity:.72;text-align:center}
.or{color:#B89554}
.filet{width:250px;height:8px;border-radius:4px;background:#B89554}

/* --- primitives d'animation (--d = retard) --- */
.a{animation-duration:.72s;animation-fill-mode:both;
   animation-timing-function:cubic-bezier(.16,.84,.3,1);animation-delay:var(--d,0s)}
.up{animation-name:up}      @keyframes up{from{opacity:0;transform:translateY(58px)}to{opacity:1;transform:none}}
.down{animation-name:down}  @keyframes down{from{opacity:0;transform:translateY(-58px)}to{opacity:1;transform:none}}
.pop{animation-name:pop}    @keyframes pop{from{opacity:0;transform:scale(.82)}to{opacity:1;transform:none}}
.fade{animation-name:fade}  @keyframes fade{from{opacity:0}to{opacity:1}}
.rtl-in{animation-name:rin} @keyframes rin{from{opacity:0;transform:translateX(70px)}to{opacity:1;transform:none}}
.eteint{animation-name:et}  @keyframes et{from{opacity:1}to{opacity:.34}}
.allume{animation-name:al}  @keyframes al{
  from{background:#2C3B52;box-shadow:none;color:transparent}
  to{background:#B89554;box-shadow:0 0 46px rgba(184,149,84,.75);color:#1E2A3B}}
.barre{animation-name:ba;animation-duration:.5s} @keyframes ba{from{width:0}to{width:100%}}
.trace{animation-name:tr;animation-duration:1.5s;animation-timing-function:cubic-bezier(.5,0,.2,1)}
@keyframes tr{from{stroke-dashoffset:var(--L)}to{stroke-dashoffset:0}}
.pulse{animation:pl 1.5s ease-in-out infinite both}
@keyframes pl{0%,100%{opacity:.35;transform:scale(1)}50%{opacity:1;transform:scale(1.09)}}
.tourne{animation:tn 7s linear infinite both} @keyframes tn{to{transform:rotate(360deg)}}
.tourne-inv{animation:tni 7s linear infinite both} @keyframes tni{to{transform:rotate(-360deg)}}

/* --- composants --- */
.grille{display:grid;grid-template-columns:repeat(6,1fr);gap:20px;width:900px}
.case{aspect-ratio:1;border-radius:18px;background:#33455E;display:flex;
  align-items:center;justify-content:center;font-size:44px;font-weight:700;color:transparent}
.carte{direction:rtl;background:rgba(255,255,255,.055);border:2px solid rgba(184,149,84,.42);
  border-radius:30px;padding:42px 58px;font-size:80px;font-weight:700;text-align:center;
  min-width:440px;backdrop-filter:blur(2px)}
.rangee{display:flex;align-items:center;gap:26px;direction:rtl;width:100%;justify-content:center}
.pastille{width:30px;height:30px;border-radius:50%;background:#B89554;
  box-shadow:0 0 22px rgba(184,149,84,.6)}
.ligne-item{direction:rtl;display:flex;align-items:center;gap:36px;width:900px;
  font-size:94px;font-weight:700}
.num{flex:0 0 104px;height:104px;border-radius:50%;border:3px solid #B89554;color:#B89554;
  display:flex;align-items:center;justify-content:center;font-size:54px}
.raye{position:relative;display:inline-block}
.raye i{position:absolute;right:0;top:52%;height:9px;background:#B89554;border-radius:4px;display:block}
.tel{width:512px;height:1010px;border-radius:60px;border:7px solid #46586F;
  background:#101823;position:relative;overflow:hidden;box-shadow:0 30px 90px rgba(0,0,0,.55)}
.notif{direction:rtl;position:absolute;left:24px;right:24px;background:rgba(239,231,216,.94);
  color:#1E2A3B;border-radius:24px;padding:24px 32px;font-size:42px;font-weight:700;
  display:flex;justify-content:space-between;align-items:center}
.compteur{direction:ltr;font-size:210px;font-weight:700;color:#B89554;font-variant-numeric:tabular-nums}
"""

def page(inner, duree, css=""):
    return f"""<!doctype html><html lang="ar"><head><meta charset="utf-8">
<style>{BASE_CSS}{css}
:root{{--D:{duree}s}}</style></head><body>
<div class="scene">{inner}<div class="grain"></div><div class="vign"></div></div>
</body></html>"""


# --- incrustations : plaque de mot-cle sur fond transparent -----------------
CSS_OVL = """
html,body{background:transparent!important}
.ovl{position:absolute;left:0;right:0;bottom:330px;display:flex;justify-content:center;
  animation:ovl-sortie var(--t-out) cubic-bezier(.4,0,.7,.2) var(--sortie) both}
@keyframes ovl-sortie{from{opacity:1;transform:none}to{opacity:0;transform:translateY(34px)}}
.plaque{position:relative;direction:rtl;background:rgba(30,42,59,.94);
  border-radius:26px;padding:30px 52px 38px;box-shadow:0 18px 54px rgba(0,0,0,.5);
  animation:plaque var(--t-in) cubic-bezier(.16,.9,.3,1) both}
@keyframes plaque{from{opacity:0;transform:translateY(30px) scale(.94)}to{opacity:1;transform:none}}
.plaque span{display:inline-block;font-size:96px;font-weight:700;color:#EFE7D8;
  white-space:nowrap;
  animation:volet var(--t-volet) cubic-bezier(.3,.9,.2,1) var(--t-volet-d) both}
/* le texte se devoile de la droite vers la gauche : sens de lecture de l'arabe */
@keyframes volet{from{clip-path:inset(0 0 0 100%)}to{clip-path:inset(0 0 0 0)}}
.plaque i{position:absolute;right:52px;bottom:22px;height:8px;border-radius:4px;
  background:#B89554;animation:filet-in var(--t-volet) cubic-bezier(.2,.9,.3,1) var(--t-filet) both}
@keyframes filet-in{from{width:0}to{width:calc(100% - 104px)}}
"""


def page_ovl(texte, duree):
    """Incrustation animee : la plaque monte, le texte se devoile en RTL,
    le filet or se trace, puis tout ressort par le bas.

    Les durees sont proportionnelles a la duree du plan : meme sur une
    incrustation courte, le mot reste lisible un temps utile."""
    t_in    = min(0.42, duree * 0.26)
    t_volet = min(0.52, duree * 0.30)
    t_out   = min(0.34, duree * 0.22)
    d_volet = t_in * 0.35
    return f"""<!doctype html><html lang="ar"><head><meta charset="utf-8">
<style>{BASE_CSS}{CSS_OVL}
:root{{--D:{duree}s;--t-in:{t_in:.3f}s;--t-volet:{t_volet:.3f}s;
--t-volet-d:{d_volet:.3f}s;--t-filet:{d_volet + t_volet * 0.45:.3f}s;
--t-out:{t_out:.3f}s;--sortie:{max(0.05, duree - t_out):.3f}s}}</style></head>
<body><div class="ovl"><div class="plaque"><span>{texte}</span><i></i></div></div></body></html>"""
