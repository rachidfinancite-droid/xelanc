# Phases, vagues et portes — lancement Xelanc

Base de départ rédigée le 2026-10-17 à partir de `excellence/plan-activation-100k.md`,
`excellence/cash-state.yaml` et de la page xelanc.org/competences/. Le mode Définir la
reprend et l'ajuste ; le plan en vigueur est `excellence/plan-lancement-xelanc.md`.
J0 = dimanche 01/11/2026. Heures : Casablanca.

## 1. Les phases

| Phase | Dates | But | Ce qui se passe |
|---|---|---|---|
| 0 · Préparation | 17/10 → 31/10 (J-15 → J-1) | Ouvrir sans fuite | Prérequis (tuyaux, qualité visible, listes d'exclusion), plan validé, tests Meta sur le nouveau compte en € à partir du 27/10, porte G0 le 29/10 |
| 1 · Ouverture douce | 01/11 → 15/11 (J0 → J+14) | Mesurer la vraie conversion sur les bases chaudes | Vagues 0 → 3 par lots, live de lancement de Rachid, 3 posts LinkedIn/semaine, sorties du 09/11 |
| 2 · Montée | 16/11 → 26/11 (J+15 → J+25) | Accélérer ce qui convertit | Lots restants des 20 000, pub en scale si G3 passée, sorties du 16/11 et du 23/11, liste d'attente Black Friday |
| 3 · Black Friday fondateurs | 27/11 → 30/11 (J+26 → J+29) | Pic d'encaissement | 500 places réelles, offre fondateurs (décision en attente), séquence de 4 jours, sorties du 30/11 |
| 4 · Consolidation | 01/12 → 31/01 (J+30 → J+91) | Transformer les inscrits en abonnés qui restent | Activation, passage mensuel → annuel (certificats), sorties de décembre (banque d'affaires), campagne de rentrée le 04/01, bilans J+30 et J+91 |

## 2. Les portes go/no-go

| Porte | Date | Décide | Critères (tous requis, sauf go partiel noté) |
|---|---|---|---|
| **G0 · Prêt à ouvrir** | jeu. 29/10 (J-3) | Ouverture du 01/11 et envoi aux bases | Achat test réussi sur chaque formule (cours, mensuel, annuel, premium), en carte **et** en Mobile Money · Brevo crédité, domaine xelanc.org authentifié (SPF, DKIM, DMARC) · pixel, GA4 et UTM actifs · les 9 compétences du 01/11 accessibles après paiement · compteurs de /competences/ cohérents avec les cartes · au moins 3 témoignages et 1 extrait vidéo public · listes d'exclusion chargées (Advisory, désinscrits). **Paiement ou Brevo rouge = aucun envoi aux bases** ; le reste peut passer en go partiel |
| **G1 · Lot suivant** | H+48 après le 1er lot de chaque base | Taille et rythme des lots suivants | Délivrabilité ≥ 95 % · rebonds < 3 % · plaintes < 0,1 % (double le lot) ou < 0,3 % (même taille) · ouverture ≥ 25 % (bases froides) ou ≥ 35 % (anciens acheteurs). Plaintes > 0,3 % = arrêt de la base |
| **G2 · Conversion** | lun. 09/11 (J+8) | Accélérer les vagues, élargir la pub au-delà des tests | Comptes → payants ≥ 0,8 % depuis J0 (repère pour 2,5 % à 90 jours) · activation ≥ 40 % · échecs de paiement < 10 % · au moins un paiement réel par formule |
| **G3 · Pub en scale** | lun. 16/11 (J+15) | Budget pub au-delà des tests | Coût par vente ≤ 120 € sur au moins 10 ventes attribuées · coût par compte gratuit ≤ 1,5 € [H] · dépense pub ≤ 30 % du cash encaissé |
| **G4 · Black Friday prêt** | mer. 25/11 (J+24) | Lancement de l'offre fondateurs | Offre décidée et écrite dans les CGV · compteur de places réel (500) · paiement testé sur l'offre · séquence chargée et relue · liste d'attente constituée |
| **G5 · Bilans** | mar. 01/12 (J+30) et dim. 31/01 (J+91) | Suite du lancement, puis passage en pilotage courant | Prévu vs réel sur le tableau de bord ; hypothèses recalées pour la Tête Grise |

## 3. Les vagues (de la plus chaude à la plus froide)

| Vague | Segment | Taille | Offre | Canal | Départ | Condition |
|---|---|---|---|---|---|---|
| 0 | Inscrits « premier cercle » du pré-lancement | à mesurer | Ouverture + prix fondateur s'il est décidé | Email de Rachid + WhatsApp si opt-in | dim. 01/11 (J0), 10 h | G0 |
| 1 | Anciens acheteurs (73 mesurés sur Thinkific, ou 400 ?) | 73–400 | Offre ancien client annuel 179–190 € (J+4), repli mensuel 29 € | Email, puis appel de Loubna aux ouvreurs | lun. 02/11 (J+1), 9 h | G0 |
| 2 | Apprenants formés pour les banques | ≈ 5 000 [H] | Accès libre + 1 cours offert, **sans promesse de cours transféré** | Email par lots de 500 | mar. 03/11 (J+2) | G1 sur le lot précédent |
| 3 | Prospects high ticket non convertis | ≈ 20 000 | Annuel 299 € mis en avant (downsell) | Email par lots, les plus engagés d'abord | jeu. 05/11 (J+4) | G1 ; les 1–2 % les plus engagés restent dans la piste d'appel high ticket |
| 4 | Trafic froid (Meta, LinkedIn, organique) | flux ≈ 3 000 comptes/mois [H] | Cours ou certificat en accroche, jamais l'abonnement | Pub Meta (Maroc, Côte d'Ivoire, Sénégal), posts de Rachid | tests dès le 27/10, scale après G3 | G3 |
| BF | Toutes les bases non converties + liste d'attente | — | Offre fondateurs, 500 places | Email, WhatsApp, pub sur liste | ven. 27/11 (J+26) | G4 |

## 4. Collisions à arbitrer

- **Campagne Advisory (FIA)** : segments A à D (≈ 600 personnes) sollicités jusqu'au 31/10,
  puis basculés vers la campagne Bootcamp Casablanca (début décembre). Exclus des vagues
  Xelanc jusqu'au 07/12, sauf demande de leur part.
- **Webinaire Advisory du mer. 21/10** : mobilise Rachid en phase 0 ; pas de live Xelanc
  la même semaine.
- **Bootcamp Chargé de clientèle entreprise (18 → 22/11)** : même public que le parcours
  « Chargé d'affaires entreprise ». Un contact inscrit au bootcamp sort des vagues Xelanc
  jusqu'au 22/11.
- **Piste high ticket des 20 000** : les plus engagés sont appelés pour DAF Dirigeant ou
  Business Leader, et ne reçoivent pas l'offre Xelanc tant que la piste est ouverte.

## 5. Sorties du catalogue (relevé xelanc.org/competences/ du 17/10 [M])

| Date | Sorties | Usage dans le lancement |
|---|---|---|
| 01/11 | 9 compétences : banquier conseil PME, chargé d'affaires PME, portefeuille PME, origination Corporate, marges/rentabilité/trésorerie, DCF × IA, capital-investissement, dossier de crédit, business plan × IA | Contenu de l'ouverture |
| lun. 09/11 | Trésorerie et BFR · Budget et pilotage de la performance | Email « nouveau » + post LinkedIn |
| lun. 16/11 | Modélisation financière avec Excel · Prévisions financières et modélisation | Accroche pub (Excel attire le trafic froid) |
| lun. 23/11 | Devenir chargé de clientèle pro | Pont vers le Black Friday |
| lun. 30/11 | Banquier augmenté conseil & IA · Décider d'un investissement et de son financement | Dernier jour du Black Friday |
| décembre | 5 compétences banque d'affaires + certificat Investment Banker | Nouveau segment (M&A, TS, PE) en phase 4 |

17 cartes n'ont pas de statut et les compteurs d'en-tête (« 16 disponibles ») contredisent
les cartes. **Un retard de sortie annoncée se signale aux inscrits avant la date**, avec
une nouvelle date ; jamais de silence.
