# -*- coding: utf-8 -*-
import math
"""Les 29 illustrations, une par idee du discours. 100 % local, zero credit."""

AR = str.maketrans("0123456789", "\u0660\u0661\u0662\u0663\u0664\u0665\u0666\u0667\u0668\u0669")


def cases(n=30, allumees=(), t0=.35, pas=.075, eteintes=(), t1=.5, pas1=.05):
    """Grille de 30 jours ; certaines cases s'allument, d'autres s'eteignent."""
    h = []
    for i in range(n):
        if i in allumees:
            h.append(f'<div class="case a allume" style="--d:{t0+i*pas:.2f}s">{str(i+1).translate(AR)}</div>')
        elif i in eteintes:
            k = list(eteintes).index(i)
            h.append(f'<div class="case a eteint" style="--d:{t1+k*pas1:.2f}s"></div>')
        else:
            h.append('<div class="case"></div>')
    return '<div class="grille">' + ''.join(h) + '</div>'


def points(n, d0=.4, pas=.045, taille=26):
    return ''.join(f'<div class="pastille a pop" style="--d:{d0+i*pas:.2f}s;'
                   f'width:{taille}px;height:{taille}px"></div>' for i in range(n))


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


def barreaux(d0=.3, n=7, h=1920):
    b = ''.join(f'<div style="width:34px;height:{h}px;border-radius:8px;'
                f'background:linear-gradient(180deg,#8DA0B8,#4A5C74);'
                f'box-shadow:0 0 30px rgba(0,0,0,.5);transform-origin:top;'
                f'animation:tombe .68s cubic-bezier(.3,1.3,.5,1) {d0+i*.075:.2f}s both"></div>'
                for i in range(n))
    return f'<div style="position:absolute;inset:0;display:flex;justify-content:space-around;' \
           f'align-items:flex-start;padding-top:0">{b}</div>'

CSS_BARREAUX = """
@keyframes tombe{from{transform:scaleY(0)}to{transform:scaleY(1)}}
"""

CSS_COMPTEUR = """
@property --n{syntax:'<integer>';initial-value:0;inherits:false}
.cpt{counter-reset:n var(--n);animation:cpt 1.7s cubic-bezier(.15,.9,.25,1) .35s both}
.cpt::after{content:counter(n,arabic-indic)}
@keyframes cpt{to{--n:var(--fin)}}
"""

CSS_PORTE = """
.mur{position:relative;width:520px;height:760px;border-radius:14px;background:#243349;
  box-shadow:inset 0 0 90px rgba(0,0,0,.55);display:flex;align-items:center;justify-content:center;
  perspective:1400px}
.lueur{position:absolute;inset:38px;border-radius:8px;
  background:radial-gradient(60% 70% at 50% 55%,#F6E6C3,#B89554 60%,#7A5F2E 100%);
  animation:lueur 1.5s ease-out .55s both}
@keyframes lueur{from{opacity:0}to{opacity:1}}
.battant{position:absolute;inset:38px;border-radius:8px;background:#31445F;
  border:4px solid #46soleil;border:4px solid #46586F;transform-origin:left center;
  animation:ouvre 1.5s cubic-bezier(.3,.9,.25,1) .5s both;backface-visibility:hidden}
@keyframes ouvre{from{transform:rotateY(0)}to{transform:rotateY(-78deg)}}
.poignee{position:absolute;right:26px;top:50%;width:20px;height:20px;border-radius:50%;background:#B89554}
"""

CSS_FISSURE = """
.bloc{position:relative;width:880px;height:400px;border-radius:22px;background:#EFE7D8;
  display:flex;align-items:center;justify-content:center;overflow:hidden;
  animation:secousse .5s ease-in-out 1.15s both}
@keyframes secousse{0%,100%{transform:translateX(0)}20%{transform:translateX(-13px)}
  45%{transform:translateX(11px)}70%{transform:translateX(-6px)}}
.bloc .mot{direction:rtl;color:#1E2A3B;font-size:118px;font-weight:700}
.fente{position:absolute;left:50%;top:0;width:9px;height:100%;background:#1E2A3B;
  transform-origin:top;animation:fend .55s cubic-bezier(.4,0,.2,1) 1.25s both}
@keyframes fend{from{transform:scaleY(0)}to{transform:scaleY(1)}}
"""

CSS_CHEMIN = """
.route{filter:drop-shadow(0 0 26px rgba(184,149,84,.45))}
"""


def S(id, inner, css=""):
    return (id, inner, css)


# --------------------------------------------------------------------------
SCENES = dict(

I01=S("I01", f'''
<div class="titre a down" style="--d:.15s">شحال خاصك <span class="or">فالشهر</span>؟</div>
<div class="filet a pop" style="--d:.45s"></div>
<div class="compteur cpt a fade" style="--d:.35s;--fin:100000"></div>
<div class="sous a up" style="--d:1.5s">باش تعيش مرتاح ماديا</div>''', CSS_COMPTEUR),

I02=S("I02", f'''
<div class="titre a down" style="--d:.1s"><span class="or">خمس أيام</span></div>
{cases(30, allumees=(0,1,2,3,4))}
<div class="sous a up" style="--d:1.15s">اللي كتعيش فيهم مرتاح</div>'''),

I03=S("I03", f'''
<div class="titre a down" style="--d:.1s"><span class="or">٢٥ يوم</span> الأخرى</div>
{cases(30, allumees=(0,1,2,3,4), t0=.1, pas=.02, eteintes=tuple(range(5,30)), t1=.45, pas1=.045)}
<div class="sous a up" style="--d:1.75s">تبقى <span class="or">تنتظر</span></div>'''),

I04=S("I04", '''
<div class="titre a down" style="--d:.1s">تبقى <span class="or">تنتظر</span></div>
<div style="position:relative;width:840px;height:200px">
  <div style="position:absolute;top:96px;left:0;right:0;height:5px;background:#2C3B52;border-radius:3px"></div>
  <div class="a barre" style="--d:.5s;position:absolute;top:96px;left:0;height:5px;
       background:#B89554;border-radius:3px"></div>
  <div class="a pop" style="--d:.4s;position:absolute;top:14px;left:0;width:150px;
       background:#B89554;color:#1E2A3B;border-radius:16px;padding:14px 0;text-align:center;
       font-size:34px;font-weight:700;direction:rtl">اليوم ١</div>
  <div class="pulse" style="position:absolute;top:132px;left:280px;right:0;text-align:center;
       direction:rtl;font-size:46px;color:#EFE7D8">···  تنتظر  ···</div>
</div>
<div class="sous a up" style="--d:1.5s">الفلوس كتجي مرة وحدة <span class="or">فالشهر</span></div>'''),

I05=S("I05", f'''
{barreaux(.55, 7, 1920)}
<div class="titre a pop" style="--d:.12s;position:relative;z-index:2">
  هذا <span class="or">حبس</span></div>
<div class="titre a pop" style="--d:.3s;font-size:168px;position:relative;z-index:2">
  <span class="or">٣٠ يوم</span></div>
<div class="sous a up" style="--d:1.5s;position:relative;z-index:2">فالشهر، كل شهر</div>''',
CSS_BARREAUX),

I06=S("I06", '''
<div class="titre a down" style="--d:.1s">هذا <span class="or">نظام</span></div>
<div style="position:relative;width:620px;height:420px">
  <svg viewBox="0 0 300 200" width="620" height="420">
    <g class="tourne" style="transform-origin:95px 100px">
      <circle cx="95" cy="100" r="52" fill="none" stroke="#B89554" stroke-width="11"
        stroke-dasharray="15 11"/><circle cx="95" cy="100" r="21" fill="none" stroke="#B89554" stroke-width="7"/>
    </g>
    <g class="tourne-inv" style="transform-origin:196px 66px">
      <circle cx="196" cy="66" r="37" fill="none" stroke="#8DA0B8" stroke-width="10"
        stroke-dasharray="13 10"/><circle cx="196" cy="66" r="14" fill="none" stroke="#8DA0B8" stroke-width="6"/>
    </g>
    <g class="tourne" style="transform-origin:206px 149px">
      <circle cx="206" cy="149" r="28" fill="none" stroke="#EFE7D8" stroke-width="9"
        stroke-dasharray="11 9" opacity=".75"/>
    </g>
  </svg>
</div>
<div class="sous a up" style="--d:1.2s">ماشي صدفة — <span class="or">تبنى</span></div>'''),

I07=S("I07", '''
<div class="titre a down" style="--d:.1s">وكاين اللي…</div>
<div style="display:flex;flex-direction:column;gap:30px">
  <div class="carte a rtl-in" style="--d:.45s">عاجبه</div>
  <div class="carte a rtl-in" style="--d:.75s;border-color:rgba(239,231,216,.3)">كاره</div>
  <div class="carte a rtl-in" style="--d:1.05s;border-color:rgba(239,231,216,.18);opacity:.75">ولف وارتاح ليه</div>
</div>'''),

I08=S("I08", '''
<div class="titre a down" style="--d:.1s">ما كانش <span class="or">عاجبني</span></div>
<div class="bloc"><span class="mot">traumatism</span><div class="fente"></div></div>
<div class="sous a up" style="--d:2.0s">وخلا فيا واحد الأثر</div>''', CSS_FISSURE),

I09=S("I09", '''
<div class="titre a down" style="--d:.1s">ما جيتش…</div>
<div style="display:flex;flex-direction:column;gap:34px;align-items:flex-end">
  <div class="ligne-item a rtl-in" style="--d:.4s;justify-content:flex-end">
     <span class="raye">باش نولي مقاول<i class="a barre" style="--d:.85s"></i></span></div>
  <div class="ligne-item a rtl-in" style="--d:.7s;justify-content:flex-end">
     <span class="raye">باش ننجح<i class="a barre" style="--d:1.15s"></i></span></div>
  <div class="ligne-item a rtl-in" style="--d:1.0s;justify-content:flex-end">
     <span class="raye">باش نختار شي حاجة<i class="a barre" style="--d:1.45s"></i></span></div>
</div>'''),

I10=S("I10", '''
<div class="titre a down" style="--d:.1s">أنا <span class="or">جيت هارب</span></div>
<div style="position:relative;width:860px;height:330px;display:flex;align-items:center">
  <div style="position:absolute;right:0;width:190px;height:300px;border-radius:12px;
       background:#31445F;border:4px solid #46586F"></div>
  <div style="position:absolute;right:210px;left:0;height:300px">
    <div style="position:absolute;top:80px;right:0;left:0;height:6px;background:#B89554;
         border-radius:3px;transform-origin:right;animation:fuite 1.15s cubic-bezier(.3,.9,.25,1) .5s both"></div>
    <div style="position:absolute;top:150px;right:0;width:70%;height:6px;background:#B89554;
         opacity:.55;border-radius:3px;transform-origin:right;animation:fuite 1.15s cubic-bezier(.3,.9,.25,1) .65s both"></div>
    <div style="position:absolute;top:212px;right:0;width:45%;height:6px;background:#B89554;
         opacity:.32;border-radius:3px;transform-origin:right;animation:fuite 1.15s cubic-bezier(.3,.9,.25,1) .8s both"></div>
  </div>
</div>
<div class="sous a up" style="--d:1.6s">هارب من <span class="or">الشهرية</span></div>''',
"@keyframes fuite{from{transform:scaleX(0)}to{transform:scaleX(1)}}"),

I11=S("I11", '''
<div class="titre a down" style="--d:.1s">ما بغيتش نبقى <span class="or">نتسنى</span></div>
<div style="position:relative;width:560px;height:560px">
  <svg viewBox="0 0 120 120" width="560" height="560">
    <circle cx="60" cy="60" r="52" fill="#22304A" stroke="#46586F" stroke-width="7"/>
    <g stroke="#8DA0B8" stroke-width="3" stroke-linecap="round">
      <line x1="60" y1="12" x2="60" y2="20"/><line x1="60" y1="100" x2="60" y2="108"/>
      <line x1="12" y1="60" x2="20" y2="60"/><line x1="100" y1="60" x2="108" y2="60"/>
    </g>
    <line x1="60" y1="60" x2="60" y2="26" stroke="#EFE7D8" stroke-width="6" stroke-linecap="round"
      style="transform-origin:60px 60px;animation:aig 2.4s linear .2s both"/>
    <line x1="60" y1="60" x2="88" y2="60" stroke="#B89554" stroke-width="5" stroke-linecap="round"
      style="transform-origin:60px 60px;animation:aig2 2.4s linear .2s both"/>
    <circle cx="60" cy="60" r="5" fill="#B89554"/>
    <path d="M24 24 L96 96 M96 24 L24 96" stroke="#B89554" stroke-width="11" stroke-linecap="round"
      pathLength="1" stroke-dasharray="1" style="--L:1;stroke-dashoffset:1;
      animation:croix .7s cubic-bezier(.4,0,.2,1) 1.5s both"/>
  </svg>
</div>''',
"""@keyframes aig{to{transform:rotate(720deg)}}@keyframes aig2{to{transform:rotate(180deg)}}
@keyframes croix{to{stroke-dashoffset:0}}"""),

I12=S("I12", '''
<div class="titre a down" style="--d:.1s"><span class="or">الشهرية</span> كل ٣٠ يوم</div>
<div style="position:relative;width:600px;height:600px;display:flex;
     align-items:center;justify-content:center">
  <svg viewBox="0 0 200 200" width="600" height="600"
       style="position:absolute;transform:rotate(-90deg)">
    <circle cx="100" cy="100" r="80" fill="none" stroke="#2C3B52" stroke-width="18"
      stroke-dasharray="7.4 9.35"/>
    <circle cx="100" cy="100" r="80" fill="none" stroke="#B89554" stroke-width="18"
      pathLength="1" stroke-dasharray="1" style="--L:1;stroke-dashoffset:1;
      animation:cycle 2.2s cubic-bezier(.5,0,.5,1) .4s both"/>
  </svg>
  <div class="titre sm a pop" style="--d:1.7s;position:relative">٣٠<br>يوم</div>
  <div class="a pop" style="--d:.35s;position:absolute;top:-18px;left:50%;
    transform:translateX(-50%);width:96px;height:96px;border-radius:50%;background:#B89554;
    color:#1E2A3B;display:flex;align-items:center;justify-content:center;font-size:52px;
    font-weight:700;box-shadow:0 0 52px rgba(184,149,84,.75)">١</div>
</div>
<div class="sous a up" style="--d:2.1s">دورة وحدة… وتعاود <span class="or">تنتظر</span></div>''',
"@keyframes cycle{to{stroke-dashoffset:0}}"),

I13=S("I13", '''
<div class="titre a down" style="--d:.1s">قلبت على <span class="or">طريقة أخرى</span></div>
<div style="position:relative;width:900px;height:700px">
  <svg viewBox="0 0 300 233" width="900" height="700" class="route">
    <path d="M150 226 L150 150" stroke="#EFE7D8" stroke-width="13" fill="none" stroke-linecap="round"
      pathLength="1" stroke-dasharray="1" style="--L:1;stroke-dashoffset:1;animation:tr1 .8s ease-out .3s both"/>
    <path d="M150 150 C150 100 78 96 40 44" stroke="#46586F" stroke-width="11" fill="none"
      stroke-linecap="round" pathLength="1" stroke-dasharray="1"
      style="--L:1;stroke-dashoffset:1;animation:tr1 .9s ease-out 1.0s both;opacity:.5"/>
    <path d="M150 150 C150 100 224 96 262 30" stroke="#B89554" stroke-width="15" fill="none"
      stroke-linecap="round" pathLength="1" stroke-dasharray="1"
      style="--L:1;stroke-dashoffset:1;animation:tr1 1.0s cubic-bezier(.3,.9,.3,1) 1.1s both"/>
    <circle cx="262" cy="30" r="17" fill="#B89554" class="a pop" style="--d:2.0s"/>
    <circle cx="40" cy="44" r="11" fill="#46586F" class="a pop" style="--d:1.85s" opacity=".5"/>
  </svg>
</div>
<div class="sous a up" style="--d:2.1s">une autre façon de <span class="or">gagner</span></div>''',
"@keyframes tr1{to{stroke-dashoffset:0}}"),

I14=S("I14", f'''
<div class="titre a down" style="--d:.1s">ندخل الفلوس…</div>
<div style="display:flex;flex-direction:column;gap:46px;width:820px">
  <div>
    <div class="sous" style="text-align:right;margin-bottom:16px;opacity:.55">كل شهر</div>
    <div class="rangee" style="justify-content:flex-end">{points(1, .35, 0, 34)}</div>
  </div>
  <div class="filet a barre" style="--d:.55s;width:100%;height:2px;background:#2C3B52"></div>
  <div>
    <div class="sous a rtl-in" style="--d:.7s;text-align:right;margin-bottom:16px">
      كل <span class="or">semaine</span></div>
    <div class="rangee" style="justify-content:flex-end">{points(4, .9, .13, 34)}</div>
  </div>
</div>'''),

I15=S("I15", f'''
<div class="titre a down" style="--d:.1s">ولا مرة <span class="or">كل ساعة</span></div>
<div style="display:flex;flex-direction:column;gap:38px;width:820px">
  <div>
    <div class="sous" style="text-align:right;margin-bottom:14px;opacity:.55">كل نهار</div>
    <div class="rangee" style="justify-content:flex-end;flex-wrap:wrap;gap:14px">{points(30, .3, .018, 22)}</div>
  </div>
  <div>
    <div class="sous a rtl-in" style="--d:.85s;text-align:right;margin-bottom:14px">
      كل <span class="or">ساعة</span></div>
    <div class="rangee" style="justify-content:flex-end;flex-wrap:wrap;gap:9px">{points(72, 1.0, .009, 16)}</div>
  </div>
</div>'''),

I16=S("I16", '''
<div class="sous a down" style="--d:.1s">Des années après…</div>
<div class="rangee" style="justify-content:center;gap:34px">
  <div class="pastille a pop" style="--d:.35s;width:34px;height:34px"></div>
  <div class="pastille a pop" style="--d:.6s;width:34px;height:34px"></div>
  <div class="pastille a pop" style="--d:.85s;width:34px;height:34px"></div>
  <div class="pastille a pop" style="--d:1.1s;width:52px;height:52px"></div>
</div>
<div class="titre a pop" style="--d:1.35s">وصلت لواحد <span class="or">النتيجة</span></div>
<div style="position:relative;height:12px;width:640px">
  <div class="a barre" style="--d:1.75s;position:absolute;left:0;height:9px;
       border-radius:5px;background:#B89554"></div>
</div>
<div class="titre sm a up" style="--d:2.0s">ما كنتش <span class="or">نتوقعها</span></div>'''),

I17=S("I17", '''
<div class="titre a down" style="--d:.1s">تكون <span class="or">ناعس</span>…</div>
<div class="tel">
  <div style="position:absolute;inset:0;background:linear-gradient(180deg,#0B111A,#16202E);
       animation:ecran 1.0s ease-out .75s both"></div>
  <div style="position:absolute;top:44px;right:40px;width:54px;height:54px;border-radius:50%;
       box-shadow:inset -17px 5px 0 0 #EFE7D8;opacity:.4"></div>
  <div class="notif" style="top:300px;animation:glisse .75s cubic-bezier(.2,.9,.3,1) 1.35s both">
    <span>+ ٤٥٠ درهم</span><span class="or">٠٣:١٤</span></div>
</div>
<div class="sous a up" style="--d:2.3s">و<span class="or">كتدخل الفلوس</span></div>''',
"""@keyframes ecran{from{background:#0B111A}to{background:linear-gradient(180deg,#233248,#16202E)}}
@keyframes glisse{from{opacity:0;transform:translateY(46px) scale(.94)}to{opacity:1;transform:none}}"""),

I18=S("I18", '''
<div class="titre a down" style="--d:.1s">كتفيق… <span class="or">وكتشوف</span></div>
<div class="tel" style="background:#1B2635">
  <div class="notif" style="top:96px;animation:glisse .6s cubic-bezier(.2,.9,.3,1) .45s both">
    <span>+ ٤٥٠</span><span class="or">٠٣:١٤</span></div>
  <div class="notif" style="top:242px;animation:glisse .6s cubic-bezier(.2,.9,.3,1) .8s both">
    <span>+ ١٢٠٠</span><span class="or">٠٤:٤٠</span></div>
  <div class="notif" style="top:388px;animation:glisse .6s cubic-bezier(.2,.9,.3,1) 1.15s both">
    <span>+ ٣٢٠</span><span class="or">٠٦:٠٢</span></div>
  <div class="notif" style="top:534px;animation:glisse .6s cubic-bezier(.2,.9,.3,1) 1.5s both">
    <span>+ ٩٨٠</span><span class="or">٠٧:٢٥</span></div>
  <div style="position:absolute;left:24px;right:24px;bottom:34px;text-align:center;
       direction:rtl;font-size:44px;font-weight:700;color:#B89554;
       animation:glisse .7s cubic-bezier(.2,.9,.3,1) 1.95s both">
       المجموع <span class="cpt" style="--fin:2950"></span></div>
</div>
<div class="sous a up" style="--d:2.5s">وأنت <span class="or">ناعس</span></div>''',
CSS_COMPTEUR + """
@keyframes glisse{from{opacity:0;transform:translateY(40px) scale(.95)}to{opacity:1;transform:none}}"""),

I19=S("I19", '''
<div class="titre a down" style="--d:.1s">المقاولة <span class="or">ماشي</span>…</div>
<div style="display:flex;flex-direction:column;gap:36px;align-items:center">
  <div class="ligne-item a pop" style="--d:.45s;justify-content:center;width:auto">
     <span class="raye">موضة<i class="a barre" style="--d:.95s"></i></span></div>
  <div class="ligne-item a pop" style="--d:.75s;justify-content:center;width:auto">
     <span class="raye">ولا حلم<i class="a barre" style="--d:1.25s"></i></span></div>
</div>
<div class="sous a up" style="--d:1.8s">كانت <span class="or">ضرورة</span></div>'''),

I20=S("I20", '''
<div class="titre a down" style="--d:.1s"><span class="or">الباب</span></div>
<div class="mur"><div class="lueur"></div><div class="battant"><div class="poignee"></div></div></div>
<div class="sous a up" style="--d:2.0s">ديال الخروج من الحبس</div>''', CSS_PORTE),

I21=S("I21", '''
<div class="titre a down" style="--d:.1s">باش نخرج خصني…</div>
<div style="display:flex;flex-direction:column;gap:34px;align-items:flex-end">
  <div class="ligne-item a rtl-in" style="--d:.45s"><span class="num">١</span>نتحرك</div>
  <div class="ligne-item a rtl-in" style="--d:.8s"><span class="num">٢</span>نخدم</div>
  <div class="ligne-item a rtl-in" style="--d:1.15s"><span class="num">٣</span>نتقرازل</div>
</div>'''),

I22=S("I22", '''
<div class="titre a down" style="--d:.1s">وهاد <span class="or">الطريق</span>…</div>
<div style="position:relative;width:660px;height:620px">
  <svg viewBox="0 0 330 310" width="660" height="620" class="route">
    <path d="M60 296 C60 236 268 250 268 190 C268 132 60 146 60 88 C60 46 168 34 268 22"
      stroke="#B89554" stroke-width="11" fill="none" stroke-linecap="round"
      pathLength="1" stroke-dasharray="1" style="--L:1;stroke-dashoffset:1;
      animation:route 2.4s cubic-bezier(.4,0,.25,1) .35s both"/>
  </svg>
</div>
<div class="sous a up" style="--d:2.6s">فيه حوايج ما كيقراوهاش</div>''',
"@keyframes route{to{stroke-dashoffset:0}}"),

I23=S("I23", '''
<div class="titre a down" style="--d:.1s">فيه…</div>
<div style="display:flex;flex-direction:column;gap:32px;align-items:flex-end">
  <div class="ligne-item a rtl-in" style="--d:.45s"><span class="num">١</span><span class="or">قواعد</span></div>
  <div class="ligne-item a rtl-in" style="--d:.9s"><span class="num">٢</span><span class="or">ممارسات</span></div>
  <div class="ligne-item a rtl-in" style="--d:1.35s"><span class="num">٣</span><span class="or">قيم</span></div>
  <div class="ligne-item a rtl-in" style="--d:1.8s"><span class="num">٤</span><span class="or">أعراف</span></div>
</div>
<div class="sous a up" style="--d:2.5s">ما قراهم ليا حتى واحد</div>'''),

I24=S("I24", '''
<div class="titre a down" style="--d:.1s">تعلمتهم <span class="or">فالطريق</span></div>
<div style="display:flex;align-items:baseline;gap:22px;direction:rtl">
  <div class="compteur cpt" style="--fin:100"></div>
  <div class="sous" style="font-size:58px">%</div>
</div>
<div class="sous a up" style="--d:2.2s">وخلصت عليهم <span class="or">الثمن غالي</span></div>
<div class="filet a pop" style="--d:2.5s"></div>''', CSS_COMPTEUR),

I25=S("I25", '''
<div class="titre a down" style="--d:.1s">نلخص عليك <span class="or">الطريق</span></div>
<div style="position:relative;width:660px;height:560px">
  <svg viewBox="0 0 330 280" width="660" height="560" class="route">
    <path d="M60 266 C60 210 268 224 268 168 C268 112 60 126 60 70 C60 32 168 24 268 16"
      stroke="#46586F" stroke-width="9" fill="none" stroke-linecap="round"/>
    <path d="M60 266 C60 210 268 224 268 168 C268 112 60 126 60 70 C60 32 168 24 268 16"
      stroke="#B89554" stroke-width="9" fill="none" stroke-linecap="round"
      pathLength="1" stroke-dasharray="1" style="--L:1;stroke-dashoffset:1;
      animation:route 2.6s cubic-bezier(.35,0,.3,1) .3s both"/>
    <circle cx="60" cy="266" r="12" fill="#B89554" class="a pop" style="--d:.45s"/>
    <circle cx="268" cy="168" r="12" fill="#B89554" class="a pop" style="--d:1.2s"/>
    <circle cx="60" cy="70" r="12" fill="#B89554" class="a pop" style="--d:2.0s"/>
    <circle cx="268" cy="16" r="16" fill="#EFE7D8" class="a pop" style="--d:2.7s"/>
  </svg>
</div>
<div class="sous a up" style="--d:2.9s">وحدة بوحدة</div>''',
"@keyframes route{to{stroke-dashoffset:0}}"),

I26=S("I26", f'''
{barreaux(.35, 7, 1920)}
<div class="titre a pop" style="--d:.15s;position:relative;z-index:2">واش نتا</div>
<div class="titre a pop" style="--d:.4s;font-size:150px;position:relative;z-index:2">
  ف<span class="or">حبس</span> تعجبك؟</div>
<div class="sous a up" style="--d:1.5s;position:relative;z-index:2">ومرتاح فيه؟</div>''',
CSS_BARREAUX),

I27=S("I27", f'''
<div class="titre a down" style="--d:.1s">ولا باغي <span class="or">تولي سبع</span>؟</div>
{lion(450, .35)}'''),

I28=S("I28", f'''
{lion(300, .2)}
<div class="titre sm a up" style="--d:1.1s">السبع كيمشي <span class="or">يجيب</span></div>
<div style="position:relative;width:760px;height:120px">
  <div style="position:absolute;top:56px;right:0;left:0;height:7px;background:#B89554;border-radius:4px;
       transform-origin:right;animation:fleche 1.0s cubic-bezier(.3,.9,.25,1) 1.5s both"></div>
  <div class="a pop" style="--d:2.4s;position:absolute;top:28px;left:0;width:66px;height:66px;
       border-radius:50%;background:#B89554;color:#1E2A3B;display:flex;align-items:center;
       justify-content:center;font-size:34px;font-weight:700">د</div>
</div>
<div class="sous a up" style="--d:2.6s">من فم السباع الآخرين</div>''',
"@keyframes fleche{from{transform:scaleX(0)}to{transform:scaleX(1)}}"),

I29=S("I29", f'''
<div style="display:flex;width:100%;gap:0;align-items:stretch;height:1020px;position:relative">
  <div style="flex:1;position:relative;display:flex;align-items:flex-end;justify-content:center;
       padding-bottom:36px;overflow:hidden;border-radius:22px;background:#16202E">
    {barreaux(.3, 4, 1020)}
    <div class="titre sm a up" style="--d:.9s;position:relative;z-index:2">الحبس</div>
  </div>
  <div style="width:7px;background:#B89554;border-radius:4px;
       transform-origin:top;animation:sep .7s cubic-bezier(.3,1.2,.5,1) .15s both"></div>
  <div style="flex:1;display:flex;flex-direction:column;align-items:center;justify-content:flex-end;
       gap:22px;padding-bottom:36px;border-radius:22px;background:#22304A">
    {lion(330, .55)}
    <div class="titre sm a up" style="--d:1.5s">السبع</div>
  </div>
</div>
<div class="titre a pop" style="--d:2.1s;font-size:190px"><span class="or">؟</span></div>
<div class="sous a up" style="--d:2.5s">اكتب لي فالتعليقات</div>''',
CSS_BARREAUX + "@keyframes sep{from{transform:scaleY(0)}to{transform:scaleY(1)}}"),
)
