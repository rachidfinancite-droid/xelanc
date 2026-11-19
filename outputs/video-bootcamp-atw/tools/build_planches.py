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
    dict(id='c1', ecran_titre="Lecture 360° de l'entreprise : écosystème sectoriel et business model", num='1.1', titre="Pratique de la lecture 360° : écosystème sectoriel et business model",
         desc="Lire le secteur et le business model avant les chiffres, pour décider sur l'économie réelle de l'entreprise.",
         objectif="Comprendre comment l'entreprise gagne sa vie dans son secteur."),
    dict(id='c2', ecran_titre="Structurer et réussir son analyse financière", num='1.2', titre="Comment structurer et réussir son analyse financière",
         desc="Transformer un business model en décision bancaire : qualifier un dossier, comprendre le risque réel, structurer son analyse et défendre sa position en comité crédit.",
         objectif="Une analyse structurée, défendable en comité."),
    dict(id='c3', ecran_titre="Aspects juridiques et fiscaux de la relation de crédit", num='1.3', titre="Aspects juridiques et fiscaux pour la relation de crédit",
         desc="Détecter les signaux que les chiffres cachent, lire la structure et le comportement, calibrer décision, garanties, pricing et suivi.",
         objectif="Traduire le juridique et le fiscal en risque bancaire."),
  ],
       cas=[dict(nom="La Table de l'Atlas", quoi_court="Un dossier réel, trois lectures croisées : le secteur, les chiffres, le cadre juridique et fiscal.", type='Cas de synthèse du bloc 1', comp=3,
                 quoi="Trois lectures apprises séparément, croisées sur un même dossier : le secteur, les chiffres, le cadre juridique et fiscal.",
                 moy='76,5', cert='90')],
       res=[('Lecture 360° et business model', 'Module 1.1', 73, 76), ('Analyse financière orientée risque', 'Module 1.2', 81, 83),
            ('Lecture juridique et fiscale', 'Module 1.3', 84, 97), ("La Table de l'Atlas", 'Cas de synthèse', 76.5, 90)],
       lecture="La certification passe de 76 % au premier module à 97 % au troisième. Les sept apprenants en consolidation au départ sont tous certifiés au module 1.3."),
  dict(num='02', nom='Décider', sous="structurer et sécuriser l'engagement", periode='Mai – septembre 2026',
       objectif="L'analyse devient décision : un avis argumenté, défendable en comité.",
       obj_src='Synthèse DG, p. 3',
       cours=[
    dict(id='c4', ecran_titre="Analyse financière pour la décision de crédit", num='2.1', titre="Analyse financière pour la décision de crédit",
         desc="Détecter les défaillances que les bilans rentables cachent, construire un DCR juste sur les bons cashflows et la bonne annuité, lire les équilibres au-delà du ratio.",
         objectif="Trancher une demande de crédit sur les vrais cashflows."),
    dict(id='c5', ecran_titre="Bonnes pratiques de financement de la croissance", num='2.2', titre="Bonnes pratiques de financement de la croissance",
         desc="Crédit moyen terme, leasing, investissement : choisir et structurer le financement adapté au projet de croissance du client.",
         objectif="Le bon financement, au rythme du projet."),
    dict(id='c6', ecran_titre="Business plan : fondamentaux et prévisions financières", num='2.3', titre="Business plan : fondamentaux et prévisions financières",
         desc="Deux volets : structurer le projet et ses hypothèses, puis construire des prévisions cohérentes (chiffre d'affaires, marges, BFR, bilan et trésorerie prévisionnels).",
         objectif="Challenger le business plan du client."),
  ],
       cas=[dict(nom='ACHAPOST', quoi_court="Un dossier de restructuration : trancher, puis monter le financement et ses garanties.", type='Cas de synthèse du bloc 2', comp=4,
                 quoi="Un dossier de restructuration où il faut trancher, puis monter le financement et ses garanties. Le livrable : une note de comité.",
                 moy='68,5', cert='88')],
       res=[('Analyse financière de crédit', 'Quiz de certification', 98, 100), ('ACHAPOST', 'Cas de synthèse', 68.5, 88)],
       lecture="Le passage de l'analyse à la décision est le palier le plus exigeant du parcours. Il est franchi par 88 % de la promotion dès le premier cas."),
  dict(num='03', nom='Piloter', sous="développer et accompagner la relation", periode='Septembre – octobre 2026',
       objectif="Le GRE et le CCE deviennent des partenaires de référence, dans la durée.",
       obj_src='Synthèse DG, p. 3',
       cours=[
    dict(id='c7', ecran_titre="Bonnes pratiques de prospection bancaire", num='3.1', titre="Bonnes pratiques de prospection bancaire",
         desc="Cibler les entreprises à fort potentiel, construire une vraie raison de les contacter et adopter la posture de conseil qui ouvre les portes.",
         objectif="Passer de la prospection au hasard à l'entrée en relation."),
    dict(id='c8', ecran_titre="Posture de banquier conseil", num='3.2', titre="Posture de banquier conseil",
         desc="Partir du besoin du client, jamais du produit : diagnostiquer, recommander à partir des écarts, couvrir tous les besoins et piloter la relation dans la durée.",
         objectif="Devenir le banquier que l'on garde."),
  ],
       cas=[dict(nom='TERRALIS', quoi_court="Un business plan à cinq ans à challenger.", type='Cas de synthèse · business plan', comp=5,
                 quoi="Un business plan à cinq ans à challenger : arbitrer entre les options de croissance du client.",
                 moy='78', cert='100'),
            dict(nom='AZURA Peintures', quoi_court="Du découvert demandé au dossier conseil complet.", type='Évaluation globale du bloc 3', comp=6,
                 quoi="Du découvert demandé au dossier conseil complet : le cas le plus proche d'un vrai comité.",
                 moy='81', cert='100')],
       res=[('TERRALIS', 'Cas de synthèse', 78, 100), ('Traitement des objections', 'Module 3.2', 90, 87), ('AZURA Peintures', 'Cas de synthèse', 81, 100)],
       lecture="Le cas le plus complet, AZURA, obtient la meilleure moyenne : 81/100, et les 28 apprenants évalués sont certifiés."),
]

import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from blocs_cine import make

s = open(A('planches-artifact.src.html')).read()
s = s.replace('LOGO_AWB', data_uri(A('assets', 'logo-attijariwafa-bank.png')))
s = s.replace('LOGO_AA', data_uri(A('assets', 'logo-attijari-academy.png')))
s = s.replace('LOGO_FIN', data_uri(A('assets', 'logo-financite.png')))
s = s.replace(' / 9 ·', ' ·').replace(' / 9<', '<')
def clean_banner(cid):
    p = A('assets', 'bannieres', 'clean', cid + '.jpg')
    return data_uri(p) if os.path.exists(p) else banner(cid)

def case_img(name):
    p = A('assets', 'cas', name + '.jpg')
    return data_uri(p) if os.path.exists(p) else None

html_blocs, last = make(BLOCS, banner, nb, 6, clean_banner, case_img)
from origination import make as make_orig
html_orig, last = make_orig(last, nb, case_img)
html_blocs += html_orig
s = s.replace('\nBLOCS\n', '\n' + html_blocs + '\n')
from mise_en_ordre import reordonner, assombrir
s, last = reordonner(s)
s = assombrir(s)
open(A('planches-artifact.html'), 'w').write(s)
print('ok', len(s) // 1024, 'Ko', 'écrans:', last)
