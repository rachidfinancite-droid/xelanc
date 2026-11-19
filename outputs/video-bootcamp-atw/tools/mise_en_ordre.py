"""Mise en ordre finale des planches et passage de tous les écrans en fond sombre (navy, cyan, gris, blanc)."""
import re

SEP = '\n<section class="page'


def reordonner(html):
    """Remonte les écrans « En chiffres » et l'entrée dans le programme juste après l'écran 05, puis renumérote."""
    head, *secs = html.split(SEP)
    def n(sec):
        m = re.search(r'<div class="right">\s*<div class="n">(\d+)<', sec)
        return int(m.group(1)) if m else None
    def tc(sec):
        m = re.search(r'class="tc">([^<]*)<', sec)
        return m.group(1) if m else ''
    synth = [x for x in secs if tc(x).startswith('En chiffres') or tc(x).startswith('Entrée dans le programme')]
    reste = [x for x in secs if x not in synth]
    i = next(k for k, x in enumerate(reste) if n(x) == 5) + 1
    secs = reste[:i] + synth + reste[i:]
    k = 0
    out = []
    for sec in secs:
        if n(sec) is not None:
            k += 1
            sec = re.sub(r'(<div class="right">\s*<div class="n">)\d+<', lambda m: f'{m.group(1)}{k:02d}<', sec, count=1)
            sec = re.sub(r'Écran \d+', f'Écran {k}', sec, count=1)
        out.append(sec)
    return head + ''.join(SEP + x for x in out), k


# Couleurs des anciens écrans gris, remplacées dans les écrans seulement (pas dans les fiches de droite)
CARTE = [
    ('radial-gradient(ellipse at 28% 18%,#f7f7f6 0%,#ececeb 45%,#dedfe0 100%)',
     'radial-gradient(ellipse at 70% 30%,#173158 0%,#0b1a33 60%,#060f20 100%)'),
    ('#0f2744', '#ffffff'), ('#0b1f38', '#ffffff'), ('#3f5168', '#c9d6e6'), ('#6f8198', '#9db6d6'),
    ('#2f6d9e', '#5fd0ea'), ('#a8324a', '#5fd0ea'), ('#139fc4', '#5fd0ea'),
    ('rgba(15,39,68,', 'rgba(255,255,255,'),
]
SOMBRE = """<style>
/* Tous les écrans en sombre : navy, cyan, gris, blanc. */
.fr.bg:not(.clair),.fr .bg{background:radial-gradient(ellipse at 70% 30%,#173158 0%,#0b1a33 60%,#060f20 100%)}
.fr .sur{color:#9db6d6}.fr .ttl{color:#fff}.fr .src{color:#9db6d6}
.fr .disc{background:rgba(255,255,255,.07);box-shadow:none;border:1.5px solid rgba(95,208,234,.55)}
.fr .ico{stroke:#5fd0ea}
.fr .vc,.fr .vx,.fr .og-step,.fr .og-deal{background:rgba(255,255,255,.06)!important;box-shadow:none!important;border:1px solid rgba(255,255,255,.14)!important}
.fr .vtag-x{background:rgba(11,26,51,.85)!important;color:#fff!important;border:1px solid rgba(255,255,255,.5)}
</style>"""


def assombrir(html):
    def frame(m):
        x = m.group(0)
        if 'class="fr bg clair"' in x:
            return x
        for a, b in CARTE:
            x = x.replace(a, b)
        return x
    html = re.sub(r'<div class="fr[ "].*?<div class="right">', frame, html, flags=re.S)
    # styles des écrans (classes) : mêmes couleurs, sans toucher aux fiches
    def style(m):
        x = m.group(0)
        if '.page{' in x:   # feuille de mise en page des fiches : intacte
            return x
        for a, b in CARTE:
            x = x.replace(a, b)
        return x
    html = re.sub(r'<style>.*?</style>', style, html, flags=re.S)
    return html.replace('</style>', '</style>' + SOMBRE, 1) if False else html.replace('<!-- ============ COUVERTURE', SOMBRE + '\n<!-- ============ COUVERTURE', 1)
