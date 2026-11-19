"""Assemble planches-artifact.html : remplace LOGO_* et BLOCS dans planches-artifact.src.html.
Chaque bloc : grand titre, objectif, un écran par cours (bannière, descriptif, objectif), études de cas, résultats.
Sources : synthèse DG (16/10/2026), descriptions Thinkific des cours, « Évaluation globale du programme »
et « Des acquis à la compétence » (rapports à l'Académie du 22/10/2026)."""
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

def nb(s):  # espaces insécables avant : ; ? ! %
    return (html.escape(s).replace(' :', '&nbsp;:').replace(' ;', '&nbsp;;').replace(' ?', '&nbsp;?')
            .replace(' !', '&nbsp;!').replace(' %', '&nbsp;%'))

BLOCS = [
  dict(num='01', nom='Comprendre', sous="l'entreprise et son écosystème", periode='Avril – juillet 2026',
       objectif="On ne conseille, ne finance et n'engage correctement que ce que l'on comprend réellement.",
       obj_src='Synthèse DG, p. 3',
       cours=[
    dict(id='c1', num='1.1', titre="Pratique de la lecture 360° : écosystème sectoriel et business model",
         desc="Lire le secteur et le business model avant les chiffres, pour décider sur l'économie réelle de l'entreprise.",
         objectif="Comprendre comment l'entreprise gagne sa vie dans son secteur."),
    dict(id='c2', num='1.2', titre="Comment structurer et réussir son analyse financière",
         desc="Transformer un business model en décision bancaire : qualifier un dossier, comprendre le risque réel, structurer son analyse et défendre sa position en comité crédit.",
         objectif="Une analyse structurée, défendable en comité."),
    dict(id='c3', num='1.3', titre="Aspects juridiques et fiscaux pour la relation de crédit",
         desc="Détecter les signaux que les chiffres cachent, lire la structure et le comportement, calibrer décision, garanties, pricing et suivi.",
         objectif="Traduire le juridique et le fiscal en risque bancaire."),
  ],
       cas=[dict(nom="La Table de l'Atlas", type='Cas de synthèse du bloc 1', comp=3,
                 quoi="Trois lectures apprises séparément, croisées sur un même dossier : le secteur, les chiffres, le cadre juridique et fiscal.",
                 moy='76,5', cert='90')],
       res=[('Lecture 360° et business model', 'Module 1.1', 73, 76), ('Analyse financière orientée risque', 'Module 1.2', 81, 83),
            ('Lecture juridique et fiscale', 'Module 1.3', 84, 97), ("La Table de l'Atlas", 'Cas de synthèse', 76.5, 90)],
       lecture="La certification passe de 76 % au premier module à 97 % au troisième. Les sept apprenants en consolidation au départ sont tous certifiés au module 1.3."),
  dict(num='02', nom='Décider', sous="structurer et sécuriser l'engagement", periode='Mai – juin 2026',
       objectif="L'analyse devient décision : un avis argumenté, défendable en comité.",
       obj_src='Synthèse DG, p. 3',
       cours=[
    dict(id='c4', num='2.1', titre="Analyse financière pour la décision de crédit",
         desc="Détecter les défaillances que les bilans rentables cachent, construire un DCR juste sur les bons cashflows et la bonne annuité, lire les équilibres au-delà du ratio.",
         objectif="Trancher une demande de crédit sur les vrais cashflows."),
    dict(id='c5', num='2.2', titre="Bonnes pratiques de financement de la croissance",
         desc="Crédit moyen terme, leasing, investissement : choisir et structurer le financement adapté au projet de croissance du client.",
         objectif="Le bon financement, au rythme du projet."),
  ],
       cas=[dict(nom='ACHAPOST', type='Cas de synthèse du bloc 2', comp=4,
                 quoi="Un dossier de restructuration où il faut trancher, puis monter le financement et ses garanties. Le livrable : une note de comité.",
                 moy='68,5', cert='88')],
       res=[('Analyse financière de crédit', 'Quiz de certification', 98, 100), ('ACHAPOST', 'Cas de synthèse', 68.5, 88)],
       lecture="Le passage de l'analyse à la décision est le palier le plus exigeant du parcours. Il est franchi par 88 % de la promotion dès le premier cas."),
  dict(num='03', nom='Piloter', sous="développer et accompagner la relation", periode='Septembre – octobre 2026',
       objectif="Le GRE et le CCE deviennent des partenaires de référence, dans la durée.",
       obj_src='Synthèse DG, p. 3',
       cours=[
    dict(id='c6', num='3.1', titre="Business plan : fondamentaux et prévisions financières",
         desc="Deux volets : structurer le projet et ses hypothèses, puis construire des prévisions cohérentes (chiffre d'affaires, marges, BFR, bilan et trésorerie prévisionnels).",
         objectif="Challenger le business plan du client."),
    dict(id='c7', num='3.2', titre="Bonnes pratiques de prospection bancaire",
         desc="Cibler les entreprises à fort potentiel, construire une vraie raison de les contacter et adopter la posture de conseil qui ouvre les portes.",
         objectif="Passer de la prospection au hasard à l'entrée en relation."),
    dict(id='c8', num='3.3', titre="Posture de banquier conseil",
         desc="Partir du besoin du client, jamais du produit : diagnostiquer, recommander à partir des écarts, couvrir tous les besoins et piloter la relation dans la durée.",
         objectif="Devenir le banquier que l'on garde."),
  ],
       cas=[dict(nom='TERRALIS', type='Cas de synthèse · business plan', comp=5,
                 quoi="Un business plan à cinq ans à challenger : arbitrer entre les options de croissance du client.",
                 moy='78', cert='100'),
            dict(nom='AZURA Peintures', type='Évaluation globale du bloc 3', comp=6,
                 quoi="Du découvert demandé au dossier conseil complet : le cas le plus proche d'un vrai comité.",
                 moy='81', cert='100')],
       res=[('TERRALIS', 'Cas de synthèse', 78, 100), ('Traitement des objections', 'Module 3.2', 90, 87), ('AZURA Peintures', 'Cas de synthèse', 81, 100)],
       lecture="Le cas le plus complet, AZURA, obtient la meilleure moyenne : 81/100, et les 28 apprenants évalués sont certifiés."),
]

N = [6]
def nxt():
    N[0] += 1
    return N[0]

def page(left, n, tc, role, vo, ecran, src):
    return f'''
<section class="page">
  <div class="left"><div class="fw"><div class="fr bg">{left}</div></div></div>
  <div class="right">
    <div class="n">{n:02d}</div><div class="tc">{tc}</div>
    <div class="role">{role}</div>
    <div class="lab">Voix off</div><div class="vo">{vo}</div>
    <div class="lab">À l'écran</div><div class="t">{ecran}</div>
  </div>
  <div class="foot">Écran {n} · {src}</div>
</section>'''

def bloc_pages(b):
    out = []
    nc = len(b['cours'])
    # 1. Grand titre
    left = f'''<div style="position:absolute;left:110px;top:250px">
      <div class="sur" style="font-size:30px">Bloc {b['num']}</div>
      <div style="font-family:var(--serif);font-size:250px;font-weight:600;line-height:.95;color:#0f2744;margin-top:20px">{b['nom']}</div>
      <div style="font-family:var(--serif);font-style:italic;font-size:56px;color:#6f8198;margin-top:26px">{nb(b['sous'])}</div>
      <div style="width:140px;height:4px;background:#a8324a;margin-top:46px"></div>
      <div style="font-size:28px;letter-spacing:.18em;color:#6f8198;margin-top:26px;text-transform:uppercase">{b['periode']}</div></div>
'''
    out.append(page(left, nxt(), f"Bloc {b['num']} · titre", b['nom'], "Aucune. Transition musicale.",
                    "Le nom du bloc en très grand, sur un écran seul.", "Synthèse DG, p. 3"))
    # 2. Objectif
    noms = ''.join(f'<div class="ol"><span>{c["num"]}</span>{nb(c["titre"].split(" :")[0])}</div>' for c in b['cours'])
    left = f'''<div class="band"><div class="sur">Bloc {b['num']} · l'objectif</div></div>
      <div style="position:absolute;left:110px;top:200px;width:1700px;font-family:var(--serif);font-size:84px;font-weight:600;line-height:1.1;color:#0f2744">{nb(b['objectif'])}</div>
      <div style="position:absolute;left:110px;top:640px;width:1700px;display:flex;gap:60px">{noms}</div>
      <div style="position:absolute;left:110px;top:900px;font-size:24px;color:#6f8198">{nc} cours · {len(b['cas'])} cas de synthèse · {b['periode']}</div>'''
    out.append(page(left, nxt(), f"Bloc {b['num']} · objectif", "Ce que le bloc doit produire",
                    "« " + {'01': "D'abord, apprendre à lire une entreprise, avant de parler de financement.",
                            '02': "Ensuite, passer de l'analyse à la décision, et savoir la défendre.",
                            '03': "Enfin, faire vivre et grandir la relation."}[b['num']] + " »",
                    "L'objectif du bloc en grand, puis la liste de ses cours.", b['obj_src']))
    # 3. Un écran par cours
    for k, c in enumerate(b['cours']):
        img = banner(c['id'])
        left = f'''<div class="band"><div class="sur">Bloc {b['num']} · cours {k + 1} sur {nc}</div></div>
      <div style="position:absolute;left:110px;top:200px;width:980px;aspect-ratio:16/9;border-radius:22px;overflow:hidden;box-shadow:0 14px 30px rgba(15,39,68,.25)"><img src="{img}" alt="" style="width:100%;height:100%;object-fit:cover;display:block"></div>
      <div style="position:absolute;left:1150px;top:200px;width:660px">
        <div style="font-size:24px;letter-spacing:.2em;color:#a8324a;font-weight:500">COURS {c['num']}</div>
        <div style="font-family:var(--serif);font-size:50px;font-weight:600;line-height:1.08;color:#0f2744;margin-top:14px">{nb(c['titre'])}</div>
        <div style="font-size:27px;line-height:1.4;color:#3f5168;margin-top:26px">{nb(c['desc'])}</div>
      </div>
      <div style="position:absolute;left:110px;top:800px;width:1700px;border-top:3px solid #0f2744;padding-top:24px;display:flex;gap:30px;align-items:baseline">
        <div style="font-size:22px;letter-spacing:.2em;color:#6f8198;flex:none">OBJECTIF</div>
        <div style="font-family:var(--serif);font-size:46px;font-weight:600;color:#0f2744">{nb(c['objectif'])}</div></div>'''
        out.append(page(left, nxt(), f"Bloc {b['num']} · cours {c['num']}", c['titre'].split(' :')[0],
                        "À écrire au montage, sans reprendre le texte de l'écran.",
                        "Balayage latéral : la bannière entre par la droite, puis le titre, le descriptif et l'objectif.",
                        "Descriptif : plateforme banking.xelanc.com"))
    # 4. Études de cas
    w = 1700 if len(b['cas']) == 1 else 820
    cards = ''.join(f'''<div class="card2" style="width:{w}px">
        <div style="font-size:22px;letter-spacing:.2em;color:#a8324a;text-transform:uppercase">{nb(cs['type'])}</div>
        <div style="font-family:var(--serif);font-size:{86 if len(b['cas']) == 1 else 70}px;font-weight:600;color:#0f2744;line-height:1;margin-top:14px">{nb(cs['nom'])}</div>
        <div style="font-size:30px;line-height:1.4;color:#3f5168;margin-top:24px">{nb(cs['quoi'])}</div>
        <div style="display:flex;gap:56px;margin-top:34px">
          <div class="kv"><b>{cs['comp']}</b><span>compétences mobilisées</span></div>
          <div class="kv"><b>{cs['moy']}</b><span>moyenne sur 100</span></div>
          <div class="kv"><b>{cs['cert']}&nbsp;%</b><span>de certifiés</span></div></div></div>''' for cs in b['cas'])
    left = f'''<div class="band"><div class="sur">Bloc {b['num']} · la validation</div><div class="ttl">{'Le cas de synthèse' if len(b['cas']) == 1 else 'Deux cas de synthèse'}</div></div>
      <div style="position:absolute;left:110px;top:380px;display:flex;gap:60px">{cards}</div>'''
    out.append(page(left, nxt(), f"Bloc {b['num']} · études de cas", "Un dossier réel, sans mode d'emploi",
                    "« À la fin du bloc, un dossier réel et complet. Personne ne dit quel outil utiliser : il faut tout mobiliser et rendre un avis. »",
                    "La carte du cas, puis ses trois chiffres qui montent un par un.", "Rapports à l'Académie, 22/10/2026"))
    # 5. Résultats
    rows = ''.join(f'''<div class="rr"><div class="rl"><b>{nb(n)}</b><span>{nb(t)}</span></div>
        <div class="rb"><div style="width:{m}%;background:{'#a8324a' if 'synthèse' in t else '#0f2744'}"></div></div>
        <div class="rv">{str(m).replace('.', ',')}</div><div class="rc">{c}&nbsp;%</div></div>''' for n, t, m, c in b['res'])
    left = f'''<div class="band"><div class="sur">Bloc {b['num']} · les résultats</div><div class="ttl">Moyenne sur 100<br>et part de certifiés</div></div>
      <div style="position:absolute;left:110px;top:400px;width:1240px">
        <div style="display:grid;grid-template-columns:420px 1fr 150px 160px;font-size:20px;letter-spacing:.16em;color:#6f8198;margin-bottom:14px"><span>ÉPREUVE</span><span></span><span>MOYENNE</span><span>CERTIFIÉS</span></div>
        {rows}</div>
      <div style="position:absolute;right:110px;top:420px;width:380px;font-size:28px;line-height:1.4;color:#3f5168">{nb(b['lecture'])}</div>
      <div class="src" style="top:960px">Seuils : 70/100 pour les modules (80 % pour la prospection), 60/100 pour les cas de synthèse.</div>'''
    out.append(page(left, nxt(), f"Bloc {b['num']} · résultats", "Ce que la promotion a démontré",
                    "« Et les résultats suivent. »",
                    "Les barres poussent l'une après l'autre, la valeur et le taux de certifiés s'affichent au bout. En rouge, les cas de synthèse.",
                    "Évaluation globale du programme, 22/10/2026"))
    return ''.join(out)

STYLE = '''<style>.ol{font-size:28px;line-height:1.3;color:#3f5168;border-top:3px solid #0f2744;padding-top:16px;flex:1}.ol span{display:block;font-family:var(--serif);font-size:40px;font-weight:600;color:#a8324a}
.card2{background:#fff;border-radius:22px;box-shadow:0 10px 24px rgba(15,39,68,.14);padding:44px}.kv b{display:block;font-family:var(--serif);font-size:72px;font-weight:600;color:#0f2744;line-height:1}.kv span{display:block;font-size:22px;color:#6f8198;margin-top:8px}
.rr{display:grid;grid-template-columns:420px 1fr 150px 160px;align-items:center;gap:0;padding:18px 0;border-top:1px solid #cfd3d8}.rl b{display:block;font-family:var(--serif);font-size:32px;font-weight:600;color:#0f2744;line-height:1.1}.rl span{display:block;font-size:20px;color:#6f8198;margin-top:4px}
.rb{height:26px;background:#dfe1e4;border-radius:13px;overflow:hidden;margin-right:24px}.rb div{height:100%;border-radius:13px}.rv{font-family:var(--serif);font-size:44px;font-weight:600;color:#0f2744}.rc{font-size:30px;color:#3f5168;font-weight:500}</style>'''

s = open(A('planches-artifact.src.html')).read()
s = s.replace('LOGO_AA', data_uri(A('assets', 'logo-attijari-academy.png')))
s = s.replace('LOGO_FIN', data_uri(A('assets', 'logo-financite.png')))
s = s.replace(' / 9 ·', ' ·').replace(' / 9<', '<')
s = s.replace('BLOCS', STYLE + ''.join(bloc_pages(b) for b in BLOCS))
open(A('planches-artifact.html'), 'w').write(s)
print('ok', len(s) // 1024, 'Ko', 'écrans:', N[0])
