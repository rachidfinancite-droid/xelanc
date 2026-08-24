# -*- coding: utf-8 -*-
"""Les 29 illustrations, une par idee du discours. Textes en francais,
charte navy / gris argente / blanc. 100 % local, zero credit."""
import math


def cases(n=30, allumees=(), t0=.35, pas=.075, eteintes=(), t1=.5, pas1=.05):
    """Grille de 30 jours : certaines cases s'allument, d'autres s'eteignent."""
    h = []
    for i in range(n):
        if i in allumees:
            h.append(f'<div class="case a allume" style="--d:{t0+i*pas:.2f}s">{i+1}</div>')
        elif i in eteintes:
            k = list(eteintes).index(i)
            h.append(f'<div class="case a eteint" style="--d:{t1+k*pas1:.2f}s"></div>')
        else:
            h.append('<div class="case"></div>')
    return '<div class="grille">' + ''.join(h) + '</div>'


def points(n, d0=.4, pas=.045, taille=28):
    return ''.join(f'<div class="pastille a pop" style="--d:{d0+i*pas:.2f}s;'
                   f'width:{taille}px;height:{taille}px"></div>' for i in range(n))


def lion(taille=520, d0=.3):
    """Tete de lion : criniere en touffes irregulieres, oreilles, museau."""
    pts = []
    N = 46
    for i in range(N):
        a = i / N * 2 * math.pi - math.pi / 2
        r = (84 + 15 * abs(math.sin(3.5 * a + .4)) + 7 * math.sin(9 * a + 1.1)
             + 4 * math.sin(17 * a))
        pts.append(f"{100 + r*1.07*math.cos(a):.1f},{97 + r*math.sin(a):.1f}")
    criniere = "M" + " L".join(pts) + " Z"
    return f'''<svg viewBox="0 0 200 200" width="{taille}" height="{taille}">
<path d="M70 44 l-6 -22 l24 11 z" fill="#7E8EA0" class="a pop" style="--d:{d0+.1:.2f}s"/>
<path d="M130 44 l6 -22 l-24 11 z" fill="#7E8EA0" class="a pop" style="--d:{d0+.14:.2f}s"/>
<path d="{criniere}" fill="#AEBBC9" class="a pop" style="--d:{d0:.2f}s"/>
<path d="M100 50 C126 50 141 68 141 94 C141 122 124 148 100 148
         C76 148 59 122 59 94 C59 68 74 50 100 50 Z"
  fill="#1E3350" class="a pop" style="--d:{d0+.35:.2f}s"/>
<path d="M72 84 Q83 74 95 84 Q83 92 72 84 Z" fill="#FFFFFF" class="a pop" style="--d:{d0+.55:.2f}s"/>
<path d="M105 84 Q117 74 128 84 Q117 92 105 84 Z" fill="#FFFFFF" class="a pop" style="--d:{d0+.6:.2f}s"/>
<circle cx="83" cy="83" r="4.4" fill="#0B1524" class="a fade" style="--d:{d0+.75:.2f}s"/>
<circle cx="117" cy="83" r="4.4" fill="#0B1524" class="a fade" style="--d:{d0+.77:.2f}s"/>
<path d="M92 68 L78 63 M108 68 L122 63" stroke="#FFFFFF" stroke-width="3.4"
  stroke-linecap="round" class="a fade" style="--d:{d0+.68:.2f}s" opacity=".75"/>
<ellipse cx="86" cy="115" rx="13" ry="10" fill="#27405F" class="a pop" style="--d:{d0+.85:.2f}s"/>
<ellipse cx="114" cy="115" rx="13" ry="10" fill="#27405F" class="a pop" style="--d:{d0+.88:.2f}s"/>
<path d="M100 100 l-9 7 q9 5 18 0 z" fill="#FFFFFF" class="a pop" style="--d:{d0+.95:.2f}s"/>
<path d="M100 108 v7 M100 115 Q89 125 80 116 M100 115 Q111 125 120 116"
  stroke="#FFFFFF" stroke-width="4.2" fill="none" stroke-linecap="round"
  class="a fade" style="--d:{d0+1.1:.2f}s"/>
<path d="M74 112 l-14 -4 M74 118 l-14 2 M126 112 l14 -4 M126 118 l14 2"
  stroke="#FFFFFF" stroke-width="2.6" stroke-linecap="round" opacity=".6"
  class="a fade" style="--d:{d0+1.2:.2f}s"/>
</svg>'''


def barreaux(d0=.3, n=7, h=1920):
    b = ''.join(f'<div style="width:32px;height:{h}px;border-radius:3px;'
                f'background:linear-gradient(180deg,#9FB0C4,#3A5473);'
                f'box-shadow:0 0 30px rgba(0,0,0,.5);transform-origin:top;'
                f'animation:tombe .68s cubic-bezier(.3,1.3,.5,1) {d0+i*.075:.2f}s both"></div>'
                for i in range(n))
    return (f'<div style="position:absolute;inset:0;display:flex;justify-content:space-around;'
            f'align-items:flex-start">{b}</div>')

CSS_BARREAUX = "@keyframes tombe{from{transform:scaleY(0)}to{transform:scaleY(1)}}"

CSS_COMPTEUR = """
@property --n{syntax:'<integer>';initial-value:0;inherits:false}
.cpt{counter-reset:n var(--n);animation:cpt 1.7s cubic-bezier(.15,.9,.25,1) .35s both}
@keyframes cpt{to{--n:var(--fin)}}
"""

CSS_PORTE = """
.mur{position:relative;width:500px;height:740px;border-radius:3px;background:#1B2C45;
  box-shadow:inset 0 0 90px rgba(0,0,0,.55);perspective:1400px}
.lueur{position:absolute;inset:34px;border-radius:2px;
  background:linear-gradient(160deg,#FFFFFF,#DDE5EE 42%,#8B9CB0 100%);
  animation:lueur 1.5s ease-out .55s both}
@keyframes lueur{from{opacity:0}to{opacity:1}}
.battant{position:absolute;inset:34px;border-radius:2px;background:#27405F;
  border:3px solid #3A5473;transform-origin:left center;
  animation:ouvre 1.5s cubic-bezier(.3,.9,.25,1) .5s both;backface-visibility:hidden}
@keyframes ouvre{from{transform:rotateY(0)}to{transform:rotateY(-78deg)}}
.poignee{position:absolute;right:22px;top:50%;width:18px;height:18px;border-radius:50%;
  background:#AEBBC9}
"""

CSS_FISSURE = """
.bloc{position:relative;width:880px;height:340px;border-radius:4px;background:#DDE5EE;
  display:flex;align-items:center;justify-content:center;overflow:hidden;
  animation:secousse .5s ease-in-out 1.15s both}
@keyframes secousse{0%,100%{transform:translateX(0)}20%{transform:translateX(-13px)}
  45%{transform:translateX(11px)}70%{transform:translateX(-6px)}}
.bloc .mot{color:#0B1524;font-size:96px;font-weight:900;letter-spacing:-.03em}
.fente{position:absolute;left:50%;top:0;width:9px;height:100%;background:#0B1524;
  transform-origin:top;animation:fend .55s cubic-bezier(.4,0,.2,1) 1.25s both}
@keyframes fend{from{transform:scaleY(0)}to{transform:scaleY(1)}}
"""

CSS_ROUTE = ".route{filter:drop-shadow(0 0 26px rgba(174,187,201,.35))}"
CSS_TRACE = "@keyframes tr1{to{stroke-dashoffset:0}}"


def S(i, inner, css="", gap=48):
    return (i, inner, css, gap)


SCENES = dict(

I01=S("I01", f'''
<div class="filet a gliss" style="--d:.1s"></div>
<div class="titre a up" style="--d:.2s">Combien te faut-il <span class="arg">par mois</span> ?</div>
<div class="compteur cpt a fade" style="--d:.35s;--fin:100"></div>
<div class="sous a up" style="--d:1.5s">pour vivre à l&rsquo;aise</div>''',
CSS_COMPTEUR + ".cpt::after{content:counter(n) ' 000 DH'}"),

I02=S("I02", f'''
<div class="filet a gliss" style="--d:.1s"></div>
<div class="titre a up" style="--d:.2s">Cinq jours</div>
{cases(30, allumees=(0,1,2,3,4))}
<div class="sous a up" style="--d:1.15s">les seuls où tu vis vraiment</div>''', "", 44),

I03=S("I03", f'''
<div class="filet a gliss" style="--d:.1s"></div>
<div class="titre a up" style="--d:.2s">Les <span class="arg">25 autres</span></div>
{cases(30, allumees=(0,1,2,3,4), t0=.1, pas=.02, eteintes=tuple(range(5,30)), t1=.45, pas1=.045)}
<div class="sous a up" style="--d:1.75s">tu attends</div>''', "", 44),

I04=S("I04", '''
<div class="filet a gliss" style="--d:.1s"></div>
<div class="titre a up" style="--d:.2s">Tu <span class="arg">attends</span></div>
<div style="position:relative;width:880px;height:190px">
  <div style="position:absolute;top:92px;left:0;right:0;height:4px;background:#1E3350"></div>
  <div class="a barre" style="--d:.5s;position:absolute;top:92px;left:0;height:4px;
       background:#AEBBC9"></div>
  <div class="a pop" style="--d:.4s;position:absolute;top:14px;left:0;padding:12px 26px;
       background:#AEBBC9;color:#0B1524;border-radius:4px;font-size:32px;font-weight:900;
       letter-spacing:-.01em">JOUR 1</div>
  <div class="pulse" style="position:absolute;top:124px;left:300px;font-size:42px;
       color:#AEBBC9;letter-spacing:.1em">— — —  29 jours  — — —</div>
</div>
<div class="sous a up" style="--d:1.5s">l&rsquo;argent tombe une seule fois</div>'''),

I05=S("I05", f'''
{barreaux(.55, 7, 1920)}
<div class="filet a gliss" style="--d:.1s;position:relative;z-index:2"></div>
<div class="titre a up" style="--d:.2s;position:relative;z-index:2">C&rsquo;est une <span class="arg">prison</span></div>
<div class="titre a pop" style="--d:.42s;font-size:184px;position:relative;z-index:2">30 jours</div>
<div class="sous a up" style="--d:1.5s;position:relative;z-index:2">par mois. Tous les mois.</div>''',
CSS_BARREAUX),

I06=S("I06", '''
<div class="filet a gliss" style="--d:.1s"></div>
<div class="titre a up" style="--d:.2s">C&rsquo;est un <span class="arg">système</span></div>
<svg viewBox="0 0 300 200" width="620" height="414">
  <g class="tourne" style="transform-origin:95px 100px">
    <circle cx="95" cy="100" r="52" fill="none" stroke="#AEBBC9" stroke-width="11"
      stroke-dasharray="15 11"/><circle cx="95" cy="100" r="21" fill="none" stroke="#AEBBC9" stroke-width="7"/>
  </g>
  <g class="tourne-inv" style="transform-origin:196px 66px">
    <circle cx="196" cy="66" r="37" fill="none" stroke="#6E8299" stroke-width="10"
      stroke-dasharray="13 10"/><circle cx="196" cy="66" r="14" fill="none" stroke="#6E8299" stroke-width="6"/>
  </g>
  <g class="tourne" style="transform-origin:206px 149px">
    <circle cx="206" cy="149" r="28" fill="none" stroke="#DDE5EE" stroke-width="9"
      stroke-dasharray="11 9" opacity=".7"/>
  </g>
</svg>
<div class="sous a up" style="--d:1.2s">ce n&rsquo;est pas un hasard : il a été construit</div>'''),

I07=S("I07", '''
<div class="filet a gliss" style="--d:.1s"></div>
<div class="titre a up" style="--d:.2s">Et il y a ceux qui</div>
<div style="display:flex;flex-direction:column;gap:26px;width:100%">
  <div class="carte a gliss" style="--d:.45s">aiment ça</div>
  <div class="carte a gliss" style="--d:.75s;border-left-color:#6E8299">détestent ça</div>
  <div class="carte a gliss" style="--d:1.05s;border-left-color:#3A5473;opacity:.72">s&rsquo;y sont habitués</div>
</div>'''),

I08=S("I08", '''
<div class="filet a gliss" style="--d:.1s"></div>
<div class="titre a up" style="--d:.2s">Moi, je n&rsquo;aimais pas</div>
<div class="bloc"><span class="mot">TRAUMATISME</span><div class="fente"></div></div>
<div class="sous a up" style="--d:2.0s">et ça a laissé une trace</div>''', CSS_FISSURE),

I09=S("I09", '''
<div class="filet a gliss" style="--d:.1s"></div>
<div class="titre a up" style="--d:.2s">Je ne suis pas venu</div>
<div style="display:flex;flex-direction:column;gap:30px;width:100%">
  <div class="ligne-item a gliss" style="--d:.45s;font-size:50px">
     <span class="raye">pour devenir entrepreneur<i class="a barre" style="--d:.9s"></i></span></div>
  <div class="ligne-item a gliss" style="--d:.75s;font-size:50px">
     <span class="raye">pour réussir<i class="a barre" style="--d:1.2s"></i></span></div>
  <div class="ligne-item a gliss" style="--d:1.05s;font-size:50px">
     <span class="raye">pour choisir quoi que ce soit<i class="a barre" style="--d:1.5s"></i></span></div>
</div>'''),

I10=S("I10", '''
<div class="filet a gliss" style="--d:.1s"></div>
<div class="titre a up" style="--d:.2s">Je suis venu <span class="arg">en fuyant</span></div>
<div style="position:relative;width:880px;height:300px">
  <div style="position:absolute;right:0;top:0;width:170px;height:280px;border-radius:3px;
       background:#27405F;border:3px solid #3A5473"></div>
  <div style="position:absolute;left:0;right:200px;top:0;height:280px">
    <div style="position:absolute;top:70px;left:0;right:0;height:6px;background:#AEBBC9;
         border-radius:3px;transform-origin:right;animation:fuite 1.15s cubic-bezier(.3,.9,.25,1) .5s both"></div>
    <div style="position:absolute;top:136px;left:0;width:72%;height:6px;background:#AEBBC9;
         opacity:.55;border-radius:3px;transform-origin:right;animation:fuite 1.15s cubic-bezier(.3,.9,.25,1) .65s both"></div>
    <div style="position:absolute;top:198px;left:0;width:46%;height:6px;background:#AEBBC9;
         opacity:.3;border-radius:3px;transform-origin:right;animation:fuite 1.15s cubic-bezier(.3,.9,.25,1) .8s both"></div>
  </div>
</div>
<div class="sous a up" style="--d:1.6s">en fuyant le <span class="vif">salaire</span></div>''',
"@keyframes fuite{from{transform:scaleX(0)}to{transform:scaleX(1)}}"),

I11=S("I11", '''
<div class="filet a gliss" style="--d:.1s"></div>
<div class="titre a up" style="--d:.2s">Je ne voulais plus <span class="arg">attendre</span></div>
<svg viewBox="0 0 120 120" width="520" height="520" class="centre">
  <circle cx="60" cy="60" r="52" fill="#1B2C45" stroke="#3A5473" stroke-width="7"/>
  <g stroke="#6E8299" stroke-width="3" stroke-linecap="round">
    <line x1="60" y1="12" x2="60" y2="20"/><line x1="60" y1="100" x2="60" y2="108"/>
    <line x1="12" y1="60" x2="20" y2="60"/><line x1="100" y1="60" x2="108" y2="60"/>
  </g>
  <line x1="60" y1="60" x2="60" y2="26" stroke="#FFFFFF" stroke-width="6" stroke-linecap="round"
    style="transform-origin:60px 60px;animation:aig 2.4s linear .2s both"/>
  <line x1="60" y1="60" x2="88" y2="60" stroke="#AEBBC9" stroke-width="5" stroke-linecap="round"
    style="transform-origin:60px 60px;animation:aig2 2.4s linear .2s both"/>
  <circle cx="60" cy="60" r="5" fill="#AEBBC9"/>
  <path d="M24 24 L96 96 M96 24 L24 96" stroke="#DDE5EE" stroke-width="11" stroke-linecap="round"
    pathLength="1" stroke-dasharray="1" style="stroke-dashoffset:1;
    animation:croix .7s cubic-bezier(.4,0,.2,1) 1.5s both"/>
</svg>''',
"""@keyframes aig{to{transform:rotate(720deg)}}@keyframes aig2{to{transform:rotate(180deg)}}
@keyframes croix{to{stroke-dashoffset:0}}"""),

I12=S("I12", '''
<div class="filet a gliss" style="--d:.1s"></div>
<div class="titre a up" style="--d:.2s">Le salaire tous les <span class="arg">30 jours</span></div>
<div style="position:relative;width:560px;height:560px;display:flex;align-items:center;
     justify-content:center" class="centre">
  <svg viewBox="0 0 200 200" width="560" height="560"
       style="position:absolute;transform:rotate(-90deg)">
    <circle cx="100" cy="100" r="80" fill="none" stroke="#1E3350" stroke-width="18"
      stroke-dasharray="7.4 9.35"/>
    <circle cx="100" cy="100" r="80" fill="none" stroke="#AEBBC9" stroke-width="18"
      pathLength="1" stroke-dasharray="1" style="stroke-dashoffset:1;
      animation:cycle 2.2s cubic-bezier(.5,0,.5,1) .4s both"/>
  </svg>
  <div class="titre sm a pop" style="--d:1.7s;position:relative;text-align:center">30<br>jours</div>
  <div class="a pop" style="--d:.35s;position:absolute;top:-14px;left:50%;
    transform:translateX(-50%);width:88px;height:88px;border-radius:50%;background:#AEBBC9;
    color:#0B1524;display:flex;align-items:center;justify-content:center;font-size:44px;
    font-weight:900;box-shadow:0 0 48px rgba(174,187,201,.6)">1</div>
</div>
<div class="sous a up" style="--d:2.1s">un tour, et tu attends encore</div>''',
"@keyframes cycle{to{stroke-dashoffset:0}}"),

I13=S("I13", '''
<div class="filet a gliss" style="--d:.1s"></div>
<div class="titre a up" style="--d:.2s">J&rsquo;ai cherché <span class="arg">une autre voie</span></div>
<svg viewBox="0 0 300 233" width="880" height="683" class="route">
  <path d="M150 226 L150 150" stroke="#FFFFFF" stroke-width="13" fill="none" stroke-linecap="round"
    pathLength="1" stroke-dasharray="1" style="stroke-dashoffset:1;animation:tr1 .8s ease-out .3s both"/>
  <path d="M150 150 C150 100 78 96 40 44" stroke="#3A5473" stroke-width="11" fill="none"
    stroke-linecap="round" pathLength="1" stroke-dasharray="1"
    style="stroke-dashoffset:1;animation:tr1 .9s ease-out 1.0s both"/>
  <path d="M150 150 C150 100 224 96 262 30" stroke="#AEBBC9" stroke-width="15" fill="none"
    stroke-linecap="round" pathLength="1" stroke-dasharray="1"
    style="stroke-dashoffset:1;animation:tr1 1.0s cubic-bezier(.3,.9,.3,1) 1.1s both"/>
  <circle cx="262" cy="30" r="17" fill="#DDE5EE" class="a pop" style="--d:2.0s"/>
  <circle cx="40" cy="44" r="11" fill="#3A5473" class="a pop" style="--d:1.85s"/>
</svg>
<div class="sous a up" style="--d:2.1s">une autre façon de gagner sa vie</div>''', CSS_TRACE),

I14=S("I14", f'''
<div class="filet a gliss" style="--d:.1s"></div>
<div class="titre a up" style="--d:.2s">Encaisser</div>
<div style="display:flex;flex-direction:column;gap:40px;width:100%">
  <div>
    <div class="sous" style="margin-bottom:14px;opacity:.5">chaque mois</div>
    <div class="rangee">{points(1, .35, 0, 36)}</div>
  </div>
  <div style="height:2px;width:100%;background:#1E3350"></div>
  <div>
    <div class="sous a gliss" style="--d:.7s;margin-bottom:14px">chaque <span class="vif">semaine</span></div>
    <div class="rangee">{points(4, .9, .13, 36)}</div>
  </div>
</div>''', "", 40),

I15=S("I15", f'''
<div class="filet a gliss" style="--d:.1s"></div>
<div class="titre a up" style="--d:.2s">Ou chaque <span class="arg">heure</span></div>
<div style="display:flex;flex-direction:column;gap:34px;width:100%">
  <div>
    <div class="sous" style="margin-bottom:12px;opacity:.5">chaque jour</div>
    <div class="rangee" style="flex-wrap:wrap;gap:14px">{points(30, .3, .018, 22)}</div>
  </div>
  <div>
    <div class="sous a gliss" style="--d:.85s;margin-bottom:12px">chaque <span class="vif">heure</span></div>
    <div class="rangee" style="flex-wrap:wrap;gap:9px">{points(72, 1.0, .009, 16)}</div>
  </div>
</div>''', "", 36),

I16=S("I16", '''
<div class="sous a gliss" style="--d:.1s">Des années plus tard</div>
<div class="rangee" style="gap:30px">
  <div class="pastille a pop" style="--d:.35s;width:32px;height:32px"></div>
  <div class="pastille a pop" style="--d:.6s;width:32px;height:32px"></div>
  <div class="pastille a pop" style="--d:.85s;width:32px;height:32px"></div>
  <div class="pastille a pop" style="--d:1.1s;width:52px;height:52px"></div>
</div>
<div class="titre a up" style="--d:1.35s">Je suis arrivé à un <span class="arg">résultat</span></div>
<div style="position:relative;height:10px;width:100%">
  <div class="a barre" style="--d:1.75s;position:absolute;left:0;height:5px;background:#AEBBC9"></div>
</div>
<div class="sous a up" style="--d:2.0s">que je n&rsquo;attendais pas</div>'''),

I17=S("I17", '''
<div class="filet a gliss" style="--d:.1s"></div>
<div class="titre a up" style="--d:.2s">Tu <span class="arg">dors</span></div>
<div class="tel centre">
  <div style="position:absolute;inset:0;background:#0D1826;
       animation:ecran 1.0s ease-out .75s both"></div>
  <div style="position:absolute;top:44px;right:40px;width:52px;height:52px;border-radius:50%;
       box-shadow:inset -16px 5px 0 0 #DDE5EE;opacity:.35"></div>
  <div class="notif" style="top:330px;animation:glisse .75s cubic-bezier(.2,.9,.3,1) 1.35s both">
    <span>+ 450 DH</span><span style="color:#5A6E86">03:14</span></div>
</div>
<div class="sous a up" style="--d:2.3s">et l&rsquo;argent rentre</div>''',
"""@keyframes ecran{from{background:#0D1826}to{background:linear-gradient(180deg,#22344E,#131F2E)}}
@keyframes glisse{from{opacity:0;transform:translateY(46px) scale(.94)}to{opacity:1;transform:none}}""",
36),

I18=S("I18", '''
<div class="filet a gliss" style="--d:.1s"></div>
<div class="titre a up" style="--d:.2s">Tu te réveilles, et tu vois</div>
<div class="tel centre" style="background:#16243A">
  <div class="notif" style="top:84px;animation:glisse .6s cubic-bezier(.2,.9,.3,1) .45s both">
    <span>+ 450 DH</span><span style="color:#5A6E86">03:14</span></div>
  <div class="notif" style="top:240px;animation:glisse .6s cubic-bezier(.2,.9,.3,1) .8s both">
    <span>+ 1 200 DH</span><span style="color:#5A6E86">04:40</span></div>
  <div class="notif" style="top:396px;animation:glisse .6s cubic-bezier(.2,.9,.3,1) 1.15s both">
    <span>+ 320 DH</span><span style="color:#5A6E86">06:02</span></div>
  <div class="notif" style="top:552px;animation:glisse .6s cubic-bezier(.2,.9,.3,1) 1.5s both">
    <span>+ 980 DH</span><span style="color:#5A6E86">07:25</span></div>
  <div style="position:absolute;left:22px;right:22px;bottom:40px;text-align:center;
       font-size:46px;font-weight:900;color:#FFFFFF;letter-spacing:-.02em;
       animation:glisse .7s cubic-bezier(.2,.9,.3,1) 1.95s both">
       Total <span class="cpt" style="--fin:2950"></span></div>
</div>
<div class="sous a up" style="--d:2.5s">pendant que tu dormais</div>''',
CSS_COMPTEUR + ".cpt::after{content:counter(n) ' DH'}"
"@keyframes glisse{from{opacity:0;transform:translateY(40px) scale(.95)}to{opacity:1;transform:none}}",
36),

I19=S("I19", '''
<div class="filet a gliss" style="--d:.1s"></div>
<div class="titre a up" style="--d:.2s">Entreprendre n&rsquo;est pas</div>
<div style="display:flex;flex-direction:column;gap:30px;width:100%">
  <div class="ligne-item a gliss" style="--d:.45s">
     <span class="raye">une mode<i class="a barre" style="--d:.95s"></i></span></div>
  <div class="ligne-item a gliss" style="--d:.75s">
     <span class="raye">ni un rêve<i class="a barre" style="--d:1.25s"></i></span></div>
</div>
<div class="sous a up" style="--d:1.8s">c&rsquo;était une <span class="vif">nécessité</span></div>'''),

I20=S("I20", '''
<div class="filet a gliss" style="--d:.1s"></div>
<div class="titre a up" style="--d:.2s">C&rsquo;était la <span class="arg">porte</span></div>
<div class="mur centre"><div class="lueur"></div><div class="battant"><div class="poignee"></div></div></div>
<div class="sous a up" style="--d:2.0s">celle qui fait sortir de la prison</div>''', CSS_PORTE, 40),

I21=S("I21", '''
<div class="filet a gliss" style="--d:.1s"></div>
<div class="titre a up" style="--d:.2s">Pour sortir, il a fallu</div>
<div style="display:flex;flex-direction:column;gap:34px;width:100%">
  <div class="ligne-item a gliss" style="--d:.45s"><span class="num">01</span>bouger</div>
  <div class="ligne-item a gliss" style="--d:.8s"><span class="num">02</span>travailler</div>
  <div class="ligne-item a gliss" style="--d:1.15s"><span class="num">03</span>me battre</div>
</div>'''),

I22=S("I22", '''
<div class="filet a gliss" style="--d:.1s"></div>
<div class="titre a up" style="--d:.2s">Et ce <span class="arg">chemin</span></div>
<svg viewBox="0 0 330 310" width="700" height="657" class="route centre">
  <path d="M60 296 C60 236 268 250 268 190 C268 132 60 146 60 88 C60 46 168 34 268 22"
    stroke="#AEBBC9" stroke-width="11" fill="none" stroke-linecap="round"
    pathLength="1" stroke-dasharray="1" style="stroke-dashoffset:1;
    animation:tr1 2.4s cubic-bezier(.4,0,.25,1) .35s both"/>
</svg>
<div class="sous a up" style="--d:2.6s">a des choses qu&rsquo;on n&rsquo;apprend nulle part</div>''',
CSS_TRACE + CSS_ROUTE, 36),

I23=S("I23", '''
<div class="filet a gliss" style="--d:.1s"></div>
<div class="titre a up" style="--d:.2s">Il a</div>
<div style="display:flex;flex-direction:column;gap:28px;width:100%">
  <div class="ligne-item a gliss" style="--d:.45s"><span class="num">01</span><span class="arg">des règles</span></div>
  <div class="ligne-item a gliss" style="--d:.9s"><span class="num">02</span><span class="arg">des pratiques</span></div>
  <div class="ligne-item a gliss" style="--d:1.35s"><span class="num">03</span><span class="arg">des valeurs</span></div>
  <div class="ligne-item a gliss" style="--d:1.8s"><span class="num">04</span><span class="arg">des codes</span></div>
</div>
<div class="sous a up" style="--d:2.5s">personne ne me les a enseignés</div>''', "", 36),

I24=S("I24", '''
<div class="filet a gliss" style="--d:.1s"></div>
<div class="titre a up" style="--d:.2s">Je les ai appris <span class="arg">sur le terrain</span></div>
<div class="compteur cpt" style="--fin:100"></div>
<div class="sous a up" style="--d:2.2s">et je les ai payés <span class="vif">très cher</span></div>''',
CSS_COMPTEUR + ".cpt::after{content:counter(n) ' %'}"),

I25=S("I25", '''
<div class="filet a gliss" style="--d:.1s"></div>
<div class="titre a up" style="--d:.2s">Je te résume <span class="arg">le chemin</span></div>
<svg viewBox="0 0 330 280" width="700" height="594" class="route centre">
  <path d="M60 266 C60 210 268 224 268 168 C268 112 60 126 60 70 C60 32 168 24 268 16"
    stroke="#2C4059" stroke-width="9" fill="none" stroke-linecap="round"/>
  <path d="M60 266 C60 210 268 224 268 168 C268 112 60 126 60 70 C60 32 168 24 268 16"
    stroke="#AEBBC9" stroke-width="9" fill="none" stroke-linecap="round"
    pathLength="1" stroke-dasharray="1" style="stroke-dashoffset:1;
    animation:tr1 2.6s cubic-bezier(.35,0,.3,1) .3s both"/>
  <circle cx="60" cy="266" r="12" fill="#AEBBC9" class="a pop" style="--d:.45s"/>
  <circle cx="268" cy="168" r="12" fill="#AEBBC9" class="a pop" style="--d:1.2s"/>
  <circle cx="60" cy="70" r="12" fill="#AEBBC9" class="a pop" style="--d:2.0s"/>
  <circle cx="268" cy="16" r="16" fill="#FFFFFF" class="a pop" style="--d:2.7s"/>
</svg>
<div class="sous a up" style="--d:2.9s">une étape après l&rsquo;autre</div>''',
CSS_TRACE + CSS_ROUTE, 36),

I26=S("I26", f'''
{barreaux(.35, 7, 1920)}
<div class="filet a gliss" style="--d:.1s;position:relative;z-index:2"></div>
<div class="titre a up" style="--d:.2s;position:relative;z-index:2">
  Es-tu dans une <span class="arg">prison</span> qui te plaît ?</div>
<div class="sous a up" style="--d:1.5s;position:relative;z-index:2">et où tu te sens bien ?</div>''',
CSS_BARREAUX),

I27=S("I27", f'''
<div class="filet a gliss" style="--d:.1s"></div>
<div class="titre a up" style="--d:.2s">Ou veux-tu devenir <span class="arg">un lion</span> ?</div>
{lion(520, .35).replace('<svg', '<svg class="centre"', 1)}''', "", 36),

I28=S("I28", f'''
<div class="filet a gliss" style="--d:.1s"></div>
<div class="titre a up" style="--d:.2s">Le lion va <span class="arg">chercher</span></div>
{lion(300, .5).replace('<svg', '<svg class="centre"', 1)}
<div style="position:relative;width:100%;height:110px">
  <div style="position:absolute;top:50px;left:0;right:0;height:6px;background:#AEBBC9;
       border-radius:3px;transform-origin:left;animation:fleche 1.0s cubic-bezier(.3,.9,.25,1) 1.5s both"></div>
  <div class="a pop" style="--d:2.4s;position:absolute;top:22px;right:0;width:62px;height:62px;
       border-radius:50%;background:#DDE5EE;color:#0B1524;display:flex;align-items:center;
       justify-content:center;font-size:30px;font-weight:900">DH</div>
</div>
<div class="sous a up" style="--d:2.6s">dans la gueule des autres lions</div>''',
"@keyframes fleche{from{transform:scaleX(0)}to{transform:scaleX(1)}}", 34),

I29=S("I29", f'''
<div class="filet a gliss" style="--d:.1s"></div>
<div class="titre a up" style="--d:.2s;font-size:92px">La prison <span class="arg">ou</span> le lion ?</div>
<div style="display:flex;width:100%;gap:0;align-items:stretch;height:1080px;position:relative">
  <div style="flex:1;position:relative;overflow:hidden;background:#101E30">
    {barreaux(.35, 4, 1080)}
    <div style="position:absolute;inset:auto 0 0 0;height:340px;
         background:linear-gradient(transparent,#08111D 62%)"></div>
    <div class="titre sm a up" style="--d:1.0s;position:absolute;left:32px;bottom:34px;
         z-index:2;font-size:74px">La prison</div>
  </div>
  <div style="width:5px;background:#AEBBC9;transform-origin:top;
       animation:sep .7s cubic-bezier(.3,1.2,.5,1) .2s both"></div>
  <div style="flex:1;position:relative;overflow:hidden;background:#1B2C45;
       display:flex;align-items:center;justify-content:center">
    {lion(330, .6)}
    <div style="position:absolute;inset:auto 0 0 0;height:340px;
         background:linear-gradient(transparent,#111F33 62%)"></div>
    <div class="titre sm a up" style="--d:1.6s;position:absolute;left:32px;bottom:34px;
         z-index:2;font-size:74px">Le lion</div>
  </div>
</div>
<div class="sous a up" style="--d:2.4s">Écris-le en commentaire</div>''',
CSS_BARREAUX + "@keyframes sep{from{transform:scaleY(0)}to{transform:scaleY(1)}}", 34),
)
