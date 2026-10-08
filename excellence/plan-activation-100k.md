# Plan d'activation cash — objectif 100 000 $/mois

Rédigé par la Tête Grise le 2026-10-08. Destiné à Rachid et aux agents du projet
(Publicité Meta, Site FIA, Site Xelanc, Orchestre Marketing). Chaque chiffre est
étiqueté : [M] mesuré, [E] estimé, [H] hypothèse.

## 1. La cible en euros

100 000 $ ≈ **86 000 € encaissés par mois** [E, taux ≈ 1,16]. Visée : **mars 2027**
(mois 5 après le lancement Xelanc).

| Ligne de cash | Mécanique | Cible mensuelle |
|---|---|---|
| High ticket FIA (Advisory ≈ 3 000 € [M agent site], DAF Dirigeant dès 2 375 € [M site], Business Leader [prix à confirmer]) | 14 ventes × ≈ 2 700 € | **38 k€** |
| Mandats B2B banques (8 mandats déjà réalisés [M site FIA]) | 1 mandat signé / mois × ≈ 25 k€ [H] | **25 k€** |
| Xelanc (cours 13,90 €, 29 €/mois, 299 €/an, 459 €/an) | récurrent + nouveaux abonnés | **18 k€** |
| Bootcamps présentiels FIA | ≈ 10 places × 500 € [H] | **5 k€** |
| **Total** | | **≈ 86 k€** |

Lecture : **Xelanc seul n'atteint pas 100 k$ avant 2028.** Le simulateur central
donne ≈ 22 k€ en janvier. Les 100 k$ viennent d'abord du high ticket et du B2B, que
Xelanc alimente en leads et en crédibilité.

## 2. Ce que disent les autres agents (synthèse au 08/10)

**Publicité Meta (compte FEF, 2023 → mai 2026) [M]**
- 2 624 $ dépensés, CPL moyen 0,60 $ (RDC, Guinée, Congo ≈ 0,55 $ ; Côte d'Ivoire 1,11 $).
- ≈ 540 $ gaspillés (20,6 %), dont Audience Network 359 $ pour 0 vente.
- Advisory mai 2026 : 381 leads → 100 bon profil → 27 en qualification → **0 inscrit**
  (nurturing arrêté). Sur 512 leads Meta Advisory : 0 inscrit ; les 20 inscrits
  viennent des canaux chauds.
- Pubs de cours : retour ≈ 1,3 au mieux. 97 % des achats sur téléphone.
- 0 pub sur 47 avec UTM. Synchro Meta → Brevo coupée depuis le 07/05.
- Plan Xelanc proposé, non lancé : nouveau compte en € + pixel, mesure ≈ 25/10,
  tests ≈ 27/10, Black Friday 27/11.

**Site FIA [M]** : page /advisory/ refaite sans prix (prix par e-mail),
formulaire → Brevo. **32 personnes qualifiées non rappelées.** Séquences e-mail
écrites mais rien chargé dans Brevo. Pages DAF et Business Leader non retravaillées.
Clé Brevo exposée en clair (snippet 13). Bootcamps : Advisory 22→31/10, Chargé de
clientèle entreprise 18→22/11, Casablanca.

**Site Xelanc [M]** : cours à **13,90 €**, 29 €/mois, 299 €/an. Paiement direct
opérationnel pour 5 cours seulement ; 5 cours bloqués (jeton Thinkific fiaacademy
en 401). **Aucun achat test réel.** Stripe + PawaPay (Mobile Money), Wio Pay en
attente. **Brevo sans crédits : les e-mails ne partent pas.** Pas de pixel ni GA4.
8 compétences au 01/11 puis 2/semaine.

**Orchestre Marketing [M/H]** : offre anciens 199 € pour 2 ans ou 299 € à vie ;
fondateurs 299 € à vie, 500 places, Black Friday 27–30/11 ; règles pub ≤ 30 % de
l'encaissé, coupure si coût par vente > 120 €. **Thinkific : 73 acheteurs payants
mesurés, pas 400.**

## 3. Les tuyaux à réparer d'abord (8 → 20 octobre)

Sans ces six points, aucune des campagnes chiffrées ne peut encaisser.

| # | Chantier | Agent | Pourquoi c'est du cash |
|---|---|---|---|
| 1 | **Brevo** : recharger les crédits, authentifier le domaine xelanc.org, rebrancher Meta → Brevo, sortir du plafond 300 e-mails/jour | Site Xelanc + Site FIA | Toutes les campagnes (73/400, 5 000, 20 000, lancement) passent par l'e-mail |
| 2 | **Sécurité** : régénérer la clé Brevo exposée et le jeton Meta affiché, désactiver le snippet 13 | Site FIA + Meta | Un compte bloqué = zéro envoi pendant des semaines |
| 3 | **Paiement** : un achat test réel sur chaque formule (cours, mensuel, annuel, premium) en carte et Mobile Money ; débloquer les 5 cours | Site Xelanc | Chaque bug de paiement est une vente perdue au pire moment |
| 4 | **Mesure** : pixel + API Conversions + GA4 sur xelanc.org, UTM sur toutes les pubs et tous les e-mails | Meta + Site Xelanc | Sans mesure, impossible de couper ce qui brûle du cash |
| 5 | **Meta** : exclure Audience Network, couper les optimisations « vues de page » | Meta | ≈ 20 % du budget récupéré immédiatement |
| 6 | **Prix alignés partout** : 13,90 € (site) vs 14 $ (discours), 459 € absent de certaines pages, ancien « 299 $ / 599 $ » | Site Xelanc + Orchestre | Un prix incohérent fait abandonner au paiement |

## 4. Plan d'activation

### Phase 1 — Cash immédiat (8 → 31 octobre)
1. **Rappeler les 32 qualifiés Advisory cette semaine.** Si 25 % signent [H] :
   8 × 3 000 € ≈ **24 k€**. C'est la meilleure action cash du mois.
2. **Bootcamp Advisory 22→31/10** : vendre les places restantes aux qualifiés et
   aux leads chauds.
3. **20 000 prospects high ticket** : extraire les 1–2 % les plus engagés
   (skill hot-lead-detection) et les appeler pour du high ticket. Le reste part
   vers Xelanc en novembre.
4. **Anciens acheteurs (73 mesurés, ou 400 ?)** : séquence « votre cours vous attend »
   + offre ancien client, envoi ≈ 20/10.

### Phase 2 — Lancement Xelanc (1 → 30 novembre)
1. **01/11 : ouverture douce** aux bases chaudes (anciens, 5 000 participants,
   20 000 prospects par lots). Pas de pub tant que les tuyaux ne sont pas validés.
2. **27/10 → mi-novembre** : tests Meta sur le nouveau compte (cours/certificat en
   accroche, jamais l'abonnement), Maroc / Côte d'Ivoire / Sénégal.
3. **18→22/11** : bootcamp Chargé de clientèle entreprise.
4. **27→30/11 : Black Friday fondateurs**, 500 places.

### Phase 3 — Montée en régime (décembre → mars)
1. **B2B** : relancer les 8 banques déjà clientes (nouvelles cohortes, licences
   Xelanc pour leurs équipes). Objectif 1 mandat signé par mois dès janvier.
2. **Pages DAF Dirigeant et Business Leader** refaites sur la méthode Advisory,
   avec séquences de nurturing actives.
3. **Meta en scale** selon les règles : pub ≤ 30 % de l'encaissé, palier de
   1 000 €, coupure si coût par vente > 120 € (Xelanc) ou > 600 € [H] (high ticket).
4. **Capacité commerciale** : 14 ventes high ticket/mois = environ 80 RDV pris,
   soit 4 appels qualifiés par jour ouvré. Il faut un closer dédié.

## 5. Tableau de bord hebdomadaire (chaque lundi)

| Indicateur | Source | Seuil d'alerte |
|---|---|---|
| Cash encaissé par ligne (HT, B2B, Xelanc, bootcamps) | Stripe, PawaPay, virements | < 50 % de la cible de la semaine |
| RDV high ticket pris / honorés / signés | CRM / Brevo | < 15 RDV pris par semaine |
| Leads qualifiés non rappelés sous 24 h | Brevo | > 0 |
| Abonnés Xelanc nouveaux / résiliés, part d'annuels | WooCommerce | part annuel < 40 % |
| Dépense pub / cash encaissé | Meta + paiements | > 30 % |
| Coût par vente (Xelanc / HT) | Meta + paiements | > 120 € / > 600 € |
| Délivrabilité e-mail (rebonds, plaintes) | Brevo | plaintes > 0,3 % |

## 6. Décisions attendues de Rachid

1. **Base anciens acheteurs : 73 (Thinkific) ou 400 ?** Toute la campagne en dépend.
2. **Offre fondateurs :** remplacer « 299 € à vie » par « 299 €/an, prix bloqué à vie ».
   Même cash immédiat, mais les renouvellements restent acquis à partir de 2028.
3. **Date de lancement :** ouverture douce le 01/11 aux bases chaudes, grand lancement
   au Black Friday.
4. **Budget pub mensuel**, nouveau compte Meta en €, et les trois feux verts en
   attente (Audience Network, règle SAFE FRAMWORK, pause d'urgence).
5. **Qui appelle les leads high ticket** et quel numéro WhatsApp réel.
6. **B2B** : l'Orchestre l'a exclu de la campagne Xelanc. D'accord pour Xelanc grand
   public, mais il faut une piste B2B FIA séparée pour atteindre 100 k$.
7. **Prix des formules DAF Dirigeant, Business Leader, Advisory** (Pro, Premium,
   Exécutif) et modalités d'échelonnement, pour chiffrer le cash réel par vente.
