"""Assemble planches-artifact.html : remplace LOGO_* et BLOCS dans planches-artifact.src.html.
Les bannières des cours sont lues dans assets/bannieres/<id>.(jpg|png) si elles existent."""
import base64, os, html

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
A = lambda *p: os.path.join(ROOT, *p)

def data_uri(path):
    mime = 'image/png' if path.endswith('.png') else 'image/jpeg'
    return f'data:{mime};base64,' + base64.b64encode(open(path, 'rb').read()).decode()

def banner(cid):
    for ext in ('jpg', 'png', 'jpeg'):
        p = A('assets', 'bannieres', f'{cid}.{ext}')
        if os.path.exists(p):
            return data_uri(p)
    return None

# Doctrine de chaque cours : proposition à valider par Rachid (source entre parenthèses).
BLOCS = [
    dict(num='01', nom='Comprendre', sous="l'entreprise et son écosystème", periode='avril – juillet', cours=[
        dict(id='c1', titre="Pratique de la lecture 360° : écosystème sectoriel et business model",
             doctrine="Comprendre comment l'entreprise gagne sa vie dans son secteur, avant de regarder ses chiffres."),
        dict(id='c2', titre="Comment structurer et réussir son analyse financière",
             doctrine="Transformer un business model en décision bancaire, défendue en comité crédit."),
        dict(id='c3', titre="Aspects juridiques et fiscaux pour la relation de crédit",
             doctrine="Lire dans la structure juridique et fiscale les signaux que les chiffres cachent."),
    ]),
    dict(num='02', nom='Décider', sous="structurer et sécuriser l'engagement", periode='mai – juin', cours=[
        dict(id='c4', titre="Analyse financière pour la décision de crédit",
             doctrine="Détecter les défaillances que les bilans rentables cachent, et décider sur les vrais cashflows."),
        dict(id='c5', titre="Bonnes pratiques de financement de la croissance",
             doctrine="Structurer crédit moyen terme, leasing et investissement au rythme du projet du client."),
    ]),
    dict(num='03', nom='Piloter', sous="développer et accompagner la relation", periode='septembre – octobre', cours=[
        dict(id='c6', titre="Business plan : fondamentaux et prévisions financières (2 volets)",
             doctrine="Structurer le projet, poser les hypothèses, puis bâtir des prévisions cohérentes."),
        dict(id='c7', titre="Bonnes pratiques de prospection bancaire",
             doctrine="Cibler les entreprises à fort potentiel et construire une vraie raison de les contacter."),
        dict(id='c8', titre="Posture de banquier conseil",
             doctrine="Partir du besoin du client, jamais du produit, pour devenir le banquier que l'on garde."),
    ]),
]

def nb(s):  # espaces insécables avant : ; ? !
    return html.escape(s).replace(' :', '&nbsp;:').replace(' ;', '&nbsp;;').replace(' ?', '&nbsp;?').replace(' !', '&nbsp;!')

def bloc_page(i, b):
    n = len(b['cours'])
    w = 520 if n == 3 else 760
    cards = []
    for k, c in enumerate(b['cours']):
        img = banner(c['id'])
        ban = (f'<img src="{img}" alt="" style="width:100%;height:100%;object-fit:cover;display:block">' if img else
               '<div style="width:100%;height:100%;display:flex;align-items:center;justify-content:center;'
               'background:repeating-linear-gradient(135deg,#e3e4e6 0 14px,#d9dadd 14px 28px);'
               'font-size:22px;letter-spacing:.14em;color:#6f8198">BANNIÈRE DU COURS</div>')
        cards.append(f'''<div class="cr" style="width:{w}px">
  <div class="cb2">{ban}</div>
  <div class="cn">Cours {c['id'][1:]}</div>
  <div class="ct">{nb(c['titre'])}</div>
  <div class="cd">{nb(c['doctrine'])}</div>
</div>''')
    manquantes = [c['id'] for c in b['cours'] if not banner(c['id'])]
    etat = 'Bannières réelles de la plateforme.' if not manquantes else 'Bannières à fournir : cadre gris en attendant.'
    vo = {
        '01': "« Premier palier&nbsp;: apprendre à lire une entreprise. Son métier et son secteur, ses comptes, puis le droit et la fiscalité qui l'encadrent. »",
        '02': "« Deuxième palier&nbsp;: décider. Passer de l'analyse à un avis qui tient en comité, et financer la croissance au bon format. »",
        '03': "« Troisième palier&nbsp;: piloter. Lire un business plan, aller chercher le client au bon moment, et tenir la posture du conseiller. »",
    }[b['num']]
    return f'''
<section class="page">
  <div class="left"><div class="fw"><div class="fr bg">
    <div class="band"><div class="sur">Bloc {b['num']} · {b['periode']}</div><div class="ttl">{b['nom']}<span style="font-weight:400;font-style:italic;color:#6f8198">, {nb(b['sous'])}</span></div></div>
    <div style="position:absolute;left:110px;top:330px;display:flex;gap:40px">{''.join(cards)}</div>
  </div></div></div>
  <div class="right">
    <div class="n">0{6 + i + 1}</div><div class="tc">Bloc {b['num']} · {n} cours</div>
    <div class="role">{b['nom']}</div>
    <div class="lab">Voix off</div><div class="vo">{vo}</div>
    <div class="lab">À l'écran</div><div class="t">Les {n} cours arrivent un par un : la bannière, le titre, puis sa doctrine en une ligne. {etat}</div>
    <div class="lab">Doctrine des cours</div><div class="t">Proposition à valider, une ligne par cours.</div>
  </div>
  <div class="foot">Écran {6 + i + 1} / 9 · Synthèse DG, p. 9</div>
</section>'''

STYLE = '''<style>.cr{display:flex;flex-direction:column}.cb2{width:100%;aspect-ratio:16/9;border-radius:16px;overflow:hidden;box-shadow:0 8px 18px rgba(15,39,68,.18)}
.cn{font-size:22px;letter-spacing:.2em;text-transform:uppercase;color:#a8324a;margin-top:26px;font-weight:500}
.ct{font-family:var(--serif);font-size:40px;font-weight:600;line-height:1.1;color:#0f2744;margin-top:10px}
.cd{font-size:28px;line-height:1.35;color:#3f5168;margin-top:16px}</style>'''

s = open(A('planches-artifact.src.html')).read()
s = s.replace('LOGO_AA', data_uri(A('assets', 'logo-attijari-academy.png')))
s = s.replace('LOGO_FIN', data_uri(A('assets', 'logo-financite.png')))
s = s.replace('BLOCS', STYLE + ''.join(bloc_page(i, b) for i, b in enumerate(BLOCS)))
open(A('planches-artifact.html'), 'w').write(s)
print('ok', len(s) // 1024, 'Ko')
