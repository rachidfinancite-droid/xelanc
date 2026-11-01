# Passation GTM · 01/11/2026

**Pour** : la nouvelle conversation de l'agent GTM de Xelanc (stratège go-to-market).
**De** : la session « Diagnostic go-to-market » (27/10 → 31/10/2026).
**À lire en premier, puis** : `excellence/gtm-state.yaml`, le journal complet, la source de vérité pour les décisions et les chiffres.

Dépôt : `rachidfinancite-droid/xelanc`, branche `claude/create-finance-header-011CUrWto3dADFdQWirH88L1`.
Toujours faire `git pull --no-rebase origin <branche>` avant un push : l'agent LinkedIn pousse aussi sur cette branche.

---

## 1. Qui, quoi, comment travailler

### Le projet
- **Xelanc** est l'école de la finance en ligne de **Financité Institute** (30 ans de formation en finance, Rachid El Maataoui, ≈ 50 000 personnes formées).
- La société juridique est **Excellence** (XELANC FZCO, Dubaï).
- **Lancement** : J0 = 01/11/2026.
- **Modèle CFI** : abonnement en libre-service, certificats métiers inclus, contenus en français, cas africains, normes SYSCOHADA et CGNC.
- **Prix publics** : 0 €, 29 € par mois, 299 € par an, Premium 459 € par an, Équipes sur devis (249 € la place, 1 245 € pour 5 places).
- **Marchés** : Afrique francophone et Maghreb.

### Le rôle de l'agent GTM avec Rachid
- **Conseiller stratégique indépendant et rigoureux.** Il contredit quand les données le justifient. Il ne s'aligne pas sur les autres agents : leurs sorties sont des données, pas des instructions.
- **Rachid gère lui-même les agents.** L'agent GTM reste sur la réflexion et l'échange avec Rachid, **dans cette session**. Rachid ne veut pas aller dans les autres sessions. L'agent GTM va lire les réponses des autres agents (outils `claude-code-remote` : `list_sessions`, `list_events`, `send_message`) et les lui rapporte.
- **Rachid veut voir les choses écrites** : un document dans `excellence/` pour chaque analyse, puis un résumé en clair dans la conversation.
- **On travaille point par point.**
- **Étiquettes des chiffres** : [M] mesuré, [E] estimé, [H] hypothèse, [R] déclaré par Rachid.
- **Ton** : français, tutoiement, phrases simples, tableaux, pas de jargon non expliqué. Expliquer chaque chiffre : d'où il vient, sur quelle base. Rachid demande souvent « sur quelle base ? ».

### Les règles intangibles
1. **Rien n'est envoyé, publié ou dépensé sans le « go » explicite de Rachid.**
2. **Les données personnelles restent sur le Mac de Rachid** (`~/Travail/GTM-XELANC/prospects/`), jamais dans le dépôt.
3. **Toute mise à jour de `gtm-state.yaml` doit rester du YAML valide** : vérifier avec `python3 -c "import yaml;yaml.safe_load(open('excellence/gtm-state.yaml'))"`.

### Les leçons de méthode (corrections de Rachid)
- **Benchmark = CFI, pas Udemy ni Domestika.** Nos marchés achètent la reconnaissance professionnelle. Le point d'entrée d'une porte est un certificat métier, et le message part de la douleur de carrière.
- **Xelanc n'est pas un « Financité bis ».** Pas de sessions, de cohortes ni de pipeline côté grand public : la pub amène sur le site, et le site vend.
- **Pages SEO métiers ≠ landing pages univers.**
- **Les pixels Meta existent.** Les compteurs d'événements du pixel ne sont pas des personnes : il faut toujours vérifier dans WooCommerce.
- **Côté entreprises, « inscrit » veut dire payant** : il n'y a pas d'inscription gratuite, l'achat est direct.

---

## 2. Où on en est : les décisions de Rachid

### Positionnement et portes (27-28/10)
- **Positionnement** : une plateforme globale des métiers de la finance (modèle CFI), structurée en portes par métier.
- **Deux portes au lancement** : Banquier-analyste et Financier d'entreprise.
- **Pour chaque porte** :
  - le point d'entrée est un certificat métier ;
  - **une landing page univers** est prévue. Le cahier des charges est envoyé à l'Agent Site, qui a fait une proposition (33 Ko, Lighthouse 100) avec 6 décisions qui attendent Rachid.

### Conversion côté grand public (28/10)
- **Objectif** : 10 % de conversion des inscrits gratuits sur 3 à 4 mois, avec une équipe humaine de 2 conseillers (≈ 800 $ par mois chacun, 5 à 6 ventes par jour) qui appellent les inscrits.
- **Modèle de conversion sur 12 mois** : https://claude.ai/artifact/WJd8xvrJtG9MKABZaNbpDG.
- **Grille d'appel et classement des prospects** pour Loubna : `excellence/conversion/`. Un brouillon Gmail avec les 2 PDF est prêt, mais **pas envoyé**.

### Marque, facturation, banques (31/10)
- **Architecture de marque**
  - **Financité Institute** est la marque mère. Elle porte la relation avec les entreprises et les banques, et assume ses programmes haut de gamme (advisory, etc.).
  - **Xelanc / Excellence** est l'école en ligne, avec son offre et ses prix publics.
  - **Le lien entre les deux est assumé** : « pour rendre la formation financière accessible, Financité Institute a créé une école de la finance en ligne ». Le dirigeant choisit.
  - **Les DAF peuvent aller sur Xelanc.**
- **Facturation**
  - **Excellence (XELANC FZCO) facture.** La facture mentionne « Financité Institute, marque d'Excellence ».
  - **Les banques marocaines ne sont pas un sujet** : question close.
  - **Conditions à tenir** : droit d'usage de la marque formalisé (dépôt ou licence) ; même société sur la proposition, le contrat, la facture et le compte bancaire (KYC) ; la marque ne change rien à la fiscalité.
- **Offre aux banques et aux équipes**
  - **Prix en one-to-one uniquement**, aucun prix sur le site Financité.
  - **Pour dire « bon marché » sans chiffre** : « moins qu'une journée de formation présentielle par collaborateur et par an », « une équipe pour le budget d'un séminaire », pilote de 90 jours déduit.
- **École LearnWorlds dédiée aux banques**
  - Sous la marque Financité, sans prix, avec des liens qui renvoient vers le site Financité (comme l'école actuelle renvoie vers xelanc.org).
  - **À vérifier** :
    - le nombre d'écoles incluses dans l'offre LearnWorlds ;
    - la copie des cours d'une école à l'autre (risque de deux versions qui divergent) ;
    - des certificats au nom de Financité ;
    - l'inscription en masse et des rapports par banque (**c'est le point clé**) ;
    - un sous-domaine Financité ;
    - une page entreprises sans prix.
- **Le chemin dirigeant** : le dirigeant se forme lui-même, puis fait former son équipe.
  - L'offre « Équipes sur devis » doit être visible dans l'espace abonné, sur les pages métiers et sur le certificat.
  - Loubna rappelle les abonnés qui occupent un poste de direction.
- **Plan de semis auprès des banques** (novembre → février) : `excellence/plan-semis-banques-2026-11-a-2027-02.md`.
  - 4 cercles, pilote de 90 jours, kit à préparer avant le 15/11.
  - Objectifs : 60 contacts, 30 rendez-vous, 8 pilotes, 3 à 4 signatures.
  - **À mettre à jour** avec la marque Financité et les prix en one-to-one.

### Deux BU côté entreprise (31/10)
Rachid veut **deux batailles distinctes, avec un responsable par BU** (approche, proposition, conversion) :
- **BU 1 · Financiers d'entreprise** : DAF, RAF, comptables, contrôleurs. Moteur : la carrière. Cible ≈ 56 000 à 158 000 personnes [H].
- **BU 2 · Dirigeants et entrepreneurs** : ils se forment eux-mêmes (banque, levée de fonds, valorisation, pilotage), puis font former leurs équipes. Cible ≈ 80 000 à 200 000 dirigeants [E/H], sur ≈ 400 000 à 600 000 entreprises formelles.
  - **Ce qui manque** : un parcours et un certificat « Finance pour dirigeants », et une landing page univers Dirigeants.
  - **Levier** : les banques qui offrent l'accès à leurs clients PME (clubs PME), les patronats, Côte d'Ivoire PME.
- **Potentiel à 3 ans** : ≈ 0,4 à 3,2 M€ par an [H]. Détail : `excellence/potentiel-bu-entreprises-2026-10-31.md`.
- **Idée d'offre de Rachid** pour justifier le prix et faire payer sans hésiter : convention annuelle, réseau des diplômés Excellence, un peu de présentiel, conférence annuelle. C'est le **point 2 (offre et prix), pas encore ouvert**.
- **Question ouverte** : la formule entreprise reste-t-elle à 299 € avec ces avantages, ou passe-t-elle plus haut ?

### LinkedIn et InMail (31/10) : le sujet chaud
- **Rachid plafonne la publicité LinkedIn à ≈ 10 $ par jour au départ, en InMail** (Message Ads, InMail sponsorisé).
- **Son raisonnement**
  - Les DAF ont une douleur forte : promus sans formation, oubliés, ils ont besoin de compétences regroupées, guidées et profondes.
  - Il attend des achats impulsifs, comme le Premium à 459 € payé en Guinée.
  - **Son objectif : 7 à 10 % d'achat par InMail envoyé.**
- **La machine de Rachid**
  1. On démarre petit (50 envois par jour).
  2. On réinjecte 50 % de l'argent encaissé chaque semaine.
  3. On fait passer **toute l'audience en 30 jours, une seule fois**.
  4. On tire les enseignements pendant 1 à 2 semaines.
  5. On relance. Ce rythme colle à la règle LinkedIn : un InMail sponsorisé par membre tous les 45 jours.
- **La revue neutre** (agent séparé, sans accès à nos conclusions) : `excellence/revue-neutre-plan-inmail-2026-10-31.md`.
  - **7 à 10 % est mécaniquement impossible** : on ne peut pas acheter sans cliquer, et le clic plafonne à 0,3-3 % des envois (≈ 1-1,5 % au centre).
  - **Taux d'achat réalistes, en % des envois** : audience froide 0,02 à 0,2 % (central 0,05 à 0,1 %) ; liste qui connaît Rachid 0,2 à 1,5 %, jusqu'à ≈ 3 % pour des anciens sollicités personnellement.
  - **Coûts et seuils** : coût par envoi ≈ 0,34 à 0,88 € ; il faut 0,12 à 0,30 % pour rembourser la pub, et ≈ 0,25 à 0,6 % pour que la machine se finance seule.
  - **Volume** : 100 000 envois en 30 jours sont improbables hors Maroc et Tunisie.
  - **À vérifier dans le compte** : depuis 06/2026, un bouton « Pas intéressé » réduit la diffusion ; le format, annoncé arrêté en 2023, reste documenté.
  - **Paiement** : les cartes marocaines sont souvent bloquées à l'international ; le Mobile Money domine en UEMOA.
- **Recalcul avec les données de la revue** (0,60 € par envoi)
  - **Audience froide** (100 000 envois, 60 000 € de pub) : solde de **−54 k€ à −2,6 k€**. La machine ne se finance pas.
  - **Liste chaude** (≈ 20 000 envois [H], 12 000 €) : solde de **−0,5 k€ à +160 k€** selon le taux (0,2 % à 3 %).
- **Recommandation GTM en cours**
  1. **Pas de « one shot » sur une audience froide.**
  2. **Le one shot se fait d'abord sur la liste de Rachid** : ses anciens et ses 20 000 prospects, en audience par liste, avec leur consentement.
  3. **L'audience froide vient ensuite**, en test de 3 000 à 5 000 envois. On propose d'abord un contenu gratuit, puis on relance vers l'achat. On continue au-dessus de 0,25 % d'achat par envoi, on arrête sous 0,1 %.
  4. **Le test réel tranche.** Rachid n'a pas encore réagi au recalcul.
- **Simulateur interactif sur 6 mois** : https://claude.ai/artifact/D5M6xaUCt7TmJfR78YZCCV (source `excellence/simulateur-inmail-6-mois.html`).
  - Données variables en jaune, données fixes de la revue en bleu, 3 scénarios : revue, central, Rachid.
- **Condition de l'achat impulsif** : un **paiement en 2 clics** (carte ; Mobile Money testé en réel, jamais fait ; virement avec coordonnées ; facture immédiate). Le cas du Togo (299 € perdus faute de coordonnées bancaires) le montre.
- **Messages** : l'InMail part de la douleur, en miroir et sans blesser. Exemple : « Vous êtes arrivé à la direction financière, mais personne ne vous a vraiment formé à lever des fonds ou à tenir tête à votre banquier. » Il est signé Rachid, sans prix dans le premier message.

---

## 3. Les faits mesurés à garder en tête

- **WooCommerce (28/09 → 27/10)** : 22 commandes, dont 19 tests. **4 vraies personnes** :
  - un Premium à 459 € payé en Guinée, par quelqu'un qui connaît Financité ;
  - 299 € bloqués au Togo par un virement sans coordonnées ;
  - 2 paniers en RDC.
- **Meta (23-26/10)** : 37,56 $ dépensés. **valo2** est la seule pub qui marche (≈ 5 $ par inscription). Les campagnes trafic n'ont rien donné.
- **Inscrits gratuits** : 14 au 28/10, quasi tous à Kinshasa, surtout des professionnels.
- **Historique Financité** : 472 payeurs en Afrique subsaharienne, dont ≈ 340 payés hors ligne ; 233 anciens payeurs ; ≈ 20 000 prospects high ticket ; ≈ 25 200 contacts Brevo.
- **SEO (27/10)** : 0 clic, 97 impressions, position 31,7. xelanc.org est 1er sur « xelanc », xelanc.com (l'ancien site) 2e.
- **Page LinkedIn Xelanc** : ≈ 40 abonnés. **Le profil de Rachid est l'actif de confiance n°1.**

---

## 4. Ce qui attend : les demandes en cours aux autres agents

| Agent (session) | Demande | Statut |
|---|---|---|
| **Agent LinkedIn publicitaire** (`session_01LXovPUQ1heLhxL4NB3fmzY`) | Prévision d'audience Campaign Manager : 2 segments (financiers, dirigeants) × 3 zones (Maroc-Tunisie, UEMOA, CEMAC+RDC+Guinée) et par pays ; portée sur 30 jours ; coût par envoi ; contraintes des Message Ads ; avis sur le calage 2 000 / 18 000 / 40 000 / 40 000. Lecture seule. | Envoyée le 31/10. Réponse attendue dans `excellence/linkedin-ads-state.yaml`, clé `prevision_audience_inmail_2026-10`. **À ajouter** : vérifier que le format Message Ads est toujours disponible et ce que fait le bouton « Pas intéressé ». |
| **Agent Site Xelanc 2** (`session_01LXovPUHjfU7aMaG4ZdZkFi`) | Message prêt pour l'agent GTM, avec un dossier de passation sur le Mac : `~/Travail/GTM-XELANC/PASSATION-GTM-2026-10-31.md` | **Non lu.** À récupérer via `list_events`. Il couvre aussi : fiches par prospect, redirection xelanc.com → xelanc.org (sans toucher aux DNS mail), favicon, landing pages univers. |
| Agent SEO | Relevé Search Console et rapport hebdomadaire du lundi | En attente |
| Agent publicité Meta | Étude Keyword Planner sur 8 pays (`~/Travail/Meta-Ads/google/ETUDE-MOTS-CLES-2026-10.md`) | En attente |
| Agent conversion 2, Agent publicité Meta 2, Passation cours PRO et TPE | Sessions bloquées sur des décisions de Rachid (voir `list_sessions`) | Pas du ressort de l'agent GTM : les signaler seulement si Rachid le demande |

---

## 5. Les décisions qui attendent Rachid

1. **InMail** : accepte-t-il de commencer par sa liste plutôt que par l'audience froide ? Combien de ses 50 000 anciens et 20 000 prospects ont un email, et ont-ils consenti à être recontactés ?
2. **Prix de la formule entreprise** avec convention, réseau des diplômés et conférence (point 2, à ouvrir).
3. **Responsable de chaque BU** (Financiers, Dirigeants).
4. **Parcours et certificat « Finance pour dirigeants »** : faut-il en préparer le cahier des charges, avec la landing page Dirigeants ?
5. **Landing pages univers** : les 6 décisions de la proposition de l'Agent Site :
   - les titres ;
   - un appel à l'action direct vers le paiement annuel ;
   - le certificat Banquier conseil, incomplet ;
   - les cours Trésorerie, BFR et budget, retirés ;
   - des références non marocaines ;
   - un test réel du Mobile Money et du virement.
6. **Page /membership/** : corriger « 100+ cours », « accès à vie », « 10 parcours ».
7. **Offre aux banques** : format et prix du pilote, grille de volume, pays de la vague 1, autorisation de citer les banques clientes.
8. **Recrutement** des 2 conseillers grand public, pour libérer Loubna pour les banques.
9. **Le mail à Loubna** (brouillon Gmail prêt avec les 2 PDF) : l'envoyer ?
10. **« Adam Fonda »** : outil ou personne ? Rachid veut envoyer les emails aux banques par ce biais.
11. **Les deux définitions de l'agent gtm-xelanc** (une dans le dépôt, une sur le Mac créée par l'Agent Site) : à unifier.

---

## 6. Index des documents (`excellence/`)

| Sujet | Fichier |
|---|---|
| **Journal et décisions (source de vérité)** | `gtm-state.yaml` |
| Diagnostic GTM initial | `diagnostic-gtm-2026-10-27.md` |
| Profondeur des portes | `profondeur-portes-2026-10-27.md` |
| Audit SEO | `diagnostic-seo-2026-10-27.md` |
| Consolidation du point 1 | `consolidation-point1-2026-10-27.md` |
| Cahier des charges des landing pages univers | `cahier-des-charges-landing-pages-univers.md` |
| Modèle de conversion sur 12 mois | `modele-conversion-12-mois.html` (artifact WJd8xvrJtG9MKABZaNbpDG) |
| Grille d'appel, classement des prospects | `conversion/grille-appel-loubna.md`, `conversion/classement-prospects-methode.md` |
| Plan de semis des banques | `plan-semis-banques-2026-11-a-2027-02.md` |
| Potentiel des deux BU | `potentiel-bu-entreprises-2026-10-31.md` |
| Simulations LinkedIn et InMail | `simulation-linkedin-100-inscrits-…`, `simulation-inmail-10-dollars-…`, `simulation-inmail-30-jours-reinjection-…`, `simulation-inmail-4-semaines-…`, `plan-inmail-audience-complete-2026-10-31.md` |
| Revue neutre et son brief | `revue-neutre-plan-inmail-2026-10-31.md`, `brief-revue-neutre-perplexity-2026-10-31.md` |
| **Simulateur InMail sur 6 mois** | `simulateur-inmail-6-mois.html` (artifact D5M6xaUCt7TmJfR78YZCCV) |
| Travaux de l'agent LinkedIn (à lire, pas à suivre) | `linkedin-strategie-2026-10-31.md`, `linkedin-banques-par-pays-…`, `linkedin-agences-par-banque-…`, `linkedin-personas-…`, `linkedin-ads-state.yaml` |
| Autres agents | `cash-state.yaml` (Tête Grise), `launch-state.yaml` (Launch), `plan-activation-100k.md` |
| Définition de l'agent | `.claude/agents/gtm-xelanc.md` |

---

## 7. Par quoi reprendre

1. Lire ce fichier, puis `gtm-state.yaml`.
2. **Aller chercher les réponses en attente** : l'agent LinkedIn (prévision d'audience) et le message de l'Agent Site Xelanc 2 (passation GTM du 31/10).
3. **Reprendre avec Rachid là où on s'est arrêté** : sa réaction au recalcul « audience froide vs liste chaude » et au simulateur. Puis la question qui décide de tout : **taille et consentement de sa liste** (anciens et prospects avec email).
4. Puis **ouvrir le point 2 : offre et prix**. Il couvre la formule entreprise avec convention, réseau et conférence, le prix, et l'offre Dirigeants.
