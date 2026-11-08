# Bibliothèque de passages de cours — Captage, version 1 (8 novembre 2026)

Objet : des passages d'expertise tirés des cours de Rachid, que Rachid peut reprendre dans
ses posts LinkedIn sous la forme « J'en parle dans mon cours X ». 42 passages, classés
par potentiel (A d'abord, puis B). Le calendrier des 24 premiers est dans
`calendrier-24-passages.md`.

---

## 1. Sources trouvées

### Google Drive (lecture seule)

| Source | Où | Fichiers lus | Cours |
|---|---|---|---|
| Scripts mot pour mot DCF, sections 4 et 5 | dossier `03-Scripts` (production DCF) | `DCFS4-scripts.html` (5 capsules), `DCFS5-scripts.html` (5 capsules). Doublons texte : `DCFS4-SCRIPTS.txt`, `DCFS5-SCRIPTS.txt` | Comment évaluer une entreprise par la méthode DCF |
| Pages capsules DCF, section 1 | dossier `06-Livrables` | `dcf-s1-c1.html`, `dcf-s1-c2.html`, `dcf-s1-c3.html` : citation mentor + exercice, pas de script complet | DCF |
| Scripts de narration FMIA | dossier `FMIA-production`, sous-dossiers `1.1` et suivants | 5 fichiers `script.txt` (capsules 1.1, E1 « signature », E1 « trois âges », E1 « revue mensuelle », E1 « quatre verbes ») + 31 petits HTML d'écrans (`E1-…` à `E7-prompt-card.html`) | Cours finance du dirigeant avec l'IA (cas fil rouge Maison Lumen) |
| Ancien script valorisation | `script valo dcf 2111.docx` (2020) | 1 fichier, texte de manuel, peu exploitable | Ancienne version du cours valorisation |
| Script YouTube | `03-script/SCRIPT-v5.html` | « Les grandes écoles sont-elles toujours grandes ? » | Hors cours : non retenu |

En tout, une cinquantaine de fichiers HTML (`mimeType = 'text/html'`) sur le Drive. Seuls les 5 HTML
DCF et les scripts FMIA sont des scripts de cours. Le reste : pages web enregistrées
en 2019-2020, reçus, `index.html` de sites, écrans d'exercice.

### Descript (lecture seule) : transcriptions utilisées

Transcriptions automatiques, approximatives : les passages ci-dessous sont reformulés
à partir du fond, jamais cités tels quels. Timecodes = début du paragraphe dans le projet.

| Projet Descript | Cours (code) | Contenu |
|---|---|---|
| `valos1global` | valo — Évaluation d'entreprise, section 1 | L'évaluation est une prise de position ; les 10 compétences de l'évaluateur |
| `valo s2` | valo, section 2 | Le jeu d'acteurs ; le flux d'une mission de valorisation |
| `AFS3G` | AF / AFS — Analyse financière, section 3 | La collecte d'information (sources, recevabilité, quatre familles, liasse et états de synthèse) |
| `AFS4G` | AF / AFS, section 4 | Cinq réflexes de mise en œuvre |
| `BMCGLOBAL` | BMC, section 1 | Posture et méthode : intuition, lecture systémique, entreprise et porteur |
| `MLFS1` | MLF, section 1 | Responsabilités, accepter ou refuser une mission |
| `MLF S5 GLOBAL` | MLF, section 5 | Le closing d'une levée de dette bancaire, la facturation |
| `ldfs3` | LDF, section 3 | Définir le besoin avant le montant |
| `taxlaws2global` | taxlaws, section 2 | Lecture juridique du client en quatre dimensions |
| `advs5global` | advs — Advisory Accelerator, section 5 | Les missions de conseil et les modèles d'exercice |
| `METIERS1P1VF` | METIERS, section 1 | Qui peut devenir advisor |
| `Advisory Accelerator certificate: Cercle de Mentorat III` | Cercle de Mentorat | Séance en direct de 3 h environ : cas réels, mandat, honoraires |

Testé mais sans contenu de cours : dépôt local (`competences.html` contient une maquette
de cinq cours génériques ; `outputs/cours-analyse-financiere-ia.yaml` est un plan de cours
« Analyse financière à l'IA » sans script).

### Méthode

1. Recherche Drive : `mimeType = 'text/html'`, puis plein texte `mot-pour-mot`, puis titres
   `script` / `SCRIPTS`. Lecture intégrale des scripts de cours trouvés.
2. Liste complète des 230 projets Descript ; export des transcriptions des projets
   « global » (une section entière) pour couvrir un maximum de cours en peu d'exports.
3. Sélection selon quatre critères : important pour un décideur, surprenant ou à
   contre-courant, concret (chiffre, cas, règle), réellement présent dans le cours.
4. Reformulation fidèle au fond ; chiffres repris seulement s'ils sont dans la source.

### Ce qui manque

- **Les HTML de la plupart des cours ne sont pas sur le Drive connecté** : rien pour advs,
  valo, AF, MLF, BMC, LDF, METIERS, taxlaws, Cercle de Mentorat. Soit ils sont dans un autre
  compte ou un Drive partagé, soit en local sur l'ordinateur de Rachid. À demander.
- **Intitulés commerciaux exacts** : seuls « Comment évaluer une entreprise par la méthode
  DCF » et « Advisory Accelerator » sont écrits en toutes lettres dans les sources. Les autres
  noms ci-dessous sont des noms de travail tirés du contenu (marqués « à confirmer »).
  Rachid doit valider la phrase de citation avant publication.
- **Sections non exploitées** (transcriptions disponibles, pas encore lues) : ADVS1, advs3
  (intro, P1 à P4), advs4, BMCS2 à BMCS4, MLF S2 à S4, LDF S1, S2, S4 à S6, METIERS S1P4,
  « Cerle de Mentorat Posture », valos1 p1 à p5 (déjà couvert par le global), AFS3/AFS4
  parties, DCFS2. Elles donneront les 60 passages restants pour atteindre 100.
- **Anciens scripts Word 2020-2022** (`Script Ch3`, `Script cH4 formalités administratives`,
  `CHAPITRE 6_script`, `CH7_SCRIPT_VDEF`, `CH8_IS_SCRIPT`, `script CFPC.xlsx`) : ancien
  certificat CFPC, non lus.
- **Cercle de Mentorat III** : transcription très bruitée (séance en direct, accents,
  conversions dirhams/euros). Les montants du passage n° 3 sont à faire confirmer par Rachid.

### Noms de cours utilisés dans la bibliothèque

| Code | Nom utilisé (à confirmer sauf mention) |
|---|---|
| DCF | Comment évaluer une entreprise par la méthode DCF (nom présent dans le script) |
| FMIA | La finance du dirigeant avec l'IA (dossier « FMIA-production », cas Maison Lumen) |
| valo | Évaluation d'entreprise |
| AF / AFS | Analyse financière bancaire |
| BMC | Lire l'entreprise et son business model (analyse du client et du porteur) |
| MLF | Conduire une mission de levée de dette bancaire |
| LDF | Levée de fonds |
| taxlaws | Lecture juridique et fiscale du client |
| advs | Advisory Accelerator (nom présent dans la source) |
| METIERS | Les métiers du conseil (module de l'Advisory Accelerator) |
| Cercle | Cercle de Mentorat de l'Advisory Accelerator (nom présent dans la source) |

### Répartition des 42 passages

| Cours | Passages | Part |
|---|---|---|
| Analyse financière bancaire (AF) | 8 | 19 % |
| DCF | 7 | 17 % |
| Finance du dirigeant avec l'IA (FMIA) | 6 | 14 % |
| Évaluation d'entreprise (valo) | 5 | 12 % |
| Advisory Accelerator (advs 3, METIERS 1, Cercle 1) | 5 | 12 % |
| Levée de dette bancaire (MLF) | 4 | 10 % |
| Lecture juridique du client (taxlaws) | 3 | 7 % |
| BMC | 3 | 7 % |
| Levée de fonds (LDF) | 1 | 2 % |

Public principal : dirigeants et DAF 17 ; banque (DG, directeurs crédit et risques,
chargés d'affaires) 14 ; conseil et M&A 10 ; DRH formation 1 (et public secondaire de
7 autres fiches). Potentiel : 24 A, 18 B.

---

## 2. Les passages

Format de chaque fiche : source exacte, passage reconstitué, idée forte, public, potentiel,
angle et accroche, phrase de citation.

### Potentiel A

**N° 1 — Le compte de résultat avant le bilan**
- Source : AF, projet Descript `AFS4G`, 00:05:15 à 00:09:23.
- Passage : Presque tout le monde ouvre un dossier de crédit par le bilan. C'est l'inverse
  qu'il faut faire. Le bilan est une photo, figée à la date de clôture : il dit où en est
  l'entreprise, pas comment elle y est arrivée. Le compte de résultat est le film des douze
  mois : comment elle produit, construit sa marge, gagne de l'argent. Le compte de résultat
  répond à la question « cette entreprise mérite-t-elle d'être financée ? », le bilan à
  « peut-elle supporter ce financement ? ». Si la réponse à la première est non, le bilan ne
  sert à rien. En comité, on arrive avec une histoire, pas avec une image figée.
- Idée forte : le compte de résultat dit *si* on finance, le bilan dit *comment* ; le « si »
  passe avant le « comment ».
- Public : directeurs crédit et risques, DG de banque, analystes seniors.
- Potentiel : A. Règle simple, contraire à l'habitude de la majorité des analystes, facile
  à débattre en commentaires.
- Angle : « Vous lisez vos dossiers dans le mauvais ordre. »
- Accroche : « En 30 ans de banque, j'ai vu presque tous les analystes ouvrir un dossier par le bilan. C'est le mauvais ordre. »
- Citation : « J'en parle dans mon cours Analyse financière bancaire sur Xelanc. »

**N° 2 — Un point de taux, vingt pour cent de valeur**
- Source : DCF, `DCFS4-scripts.html`, capsule 2, § 4.2 « Le taux n'est pas un chiffre, c'est un jugement ».
- Passage : Le taux d'actualisation n'est pas un paramètre qu'on va chercher dans une table.
  C'est le prix du risque : la rentabilité exigée par ceux qui financent cette entreprise-là.
  Il se place au dénominateur : le risque fait monter le taux, le taux fait fondre la valeur.
  Un seul point de taux en plus, et c'est souvent vingt pour cent de la valeur qui
  s'évaporent, sans bruit. En négociation, l'acheteur défend un taux élevé, le vendeur un
  taux bas. Entre les deux, il n'y a pas un chiffre vrai et un chiffre faux, il y a un
  jugement sur le risque. Celui qui maîtrise ce jugement maîtrise la valeur.
- Idée forte : dans une valorisation, la bataille ne se joue pas sur les flux mais sur un
  seul chiffre, le taux.
- Public : dirigeants vendeurs ou acquéreurs, DAF, directeurs M&A et corporate finance.
- Potentiel : A. Chiffre frappant (1 point = 20 %), utile à tout dirigeant qui vend ou achète.
- Angle : ce que votre acquéreur ne vous dira pas sur le taux.
- Accroche : « Un point. Vingt pour cent de la valeur de votre entreprise. C'est ce que vaut un débat sur le taux d'actualisation. »
- Citation : « J'en parle dans mon cours Comment évaluer une entreprise par la méthode DCF sur Xelanc. »

**N° 3 — La commission de 200 000 euros et la porte**
- Source : Cercle de Mentorat, projet `Advisory Accelerator certificate: Cercle de Mentorat III`, 01:29:44 à 01:35:00.
- Passage : Un président de PME en difficulté reçoit Rachid et passe la réunion à se
  plaindre de ses banques qui l'asphyxient. Rachid lui répond calmement que ce n'est pas un
  problème, que cela se règle. Le lendemain, proposition : une levée d'environ 6 millions
  d'euros, avec une commission de succès de 3 %. Le dirigeant sort sa calculatrice : « Vous
  allez toucher autour de 200 000 euros pour trois ou quatre mois de travail ? » Rachid se
  lève et sort : le client était en train d'évaluer son travail à sa place. Il ne signe rien
  ce jour-là. Leçon : la rémunération se prépare dès la première réunion, en jaugeant ce que
  le client est prêt à payer pour régler son problème, et elle ne se brade pas.
- Idée forte : un conseiller qui accepte que le client fixe la valeur de son travail a déjà
  perdu la mission.
- Public : consultants, advisors indépendants, banquiers qui envisagent le conseil.
- Potentiel : A. Récit vécu, tension, chiffres ; le format qui marche le mieux pour Rachid.
- Angle : récit de mission, « le jour où je suis sorti de la réunion ».
- Accroche : « Il a sorti sa calculatrice, a fait le calcul de ma commission, et m'a regardé. Je me suis levé et je suis sorti. »
- Citation : « J'en parle dans le Cercle de Mentorat de l'Advisory Accelerator sur Xelanc. »
- À vérifier avec Rachid : montant de la levée (la transcription mélange dirhams et euros) et
  taux de commission exact.

**N° 4 — « Quel est le meilleur outil d'IA pour la finance ? » est la mauvaise question**
- Source : FMIA, Drive `FMIA-production`, capsule E1 « quatre verbes » (`script.txt` et `E1-quatre-verbes.html`).
- Passage : La question qu'on pose le plus souvent est « quel est le meilleur outil d'IA pour
  la finance ? ». C'est la mauvaise. La bonne est : que voulez-vous faire ? Lire, structurer,
  simuler ou rédiger. Lire : déposer un compte de résultat et demander trois chiffres, pas
  « résume ce document ». Structurer : 412 opérations bancaires en vrac classées en huit
  catégories, et l'on découvre que les fournisseurs pèsent 64 % des sorties. Simuler : +5 %
  de prix, −3 % de volume, 422 000 euros de marge brute en plus, à condition de ne pas
  confondre simulation et prévision. Rédiger : le courriel au banquier. Limite commune :
  l'IA ne décide pas, ne signe pas et ne garantit pas un chiffre qu'elle ne peut pas sourcer.
- Idée forte : on choisit un usage avant un outil ; l'outil vient après.
- Public : dirigeants de PME, DAF, DRH formation.
- Potentiel : A. Dans la ligne du post qui a marché (« l'IA ne rend pas productif par
  magie »), et concret.
- Angle : à contre-courant des classements d'outils IA.
- Accroche : « On me demande chaque semaine quel est le meilleur outil d'IA pour la finance. Je réponds toujours la même chose : mauvaise question. »
- Citation : « J'en parle dans mon cours La finance du dirigeant avec l'IA sur Xelanc. »

**N° 5 — Le client qui gagne de l'argent mais ne le garde pas**
- Source : taxlaws, projet `taxlaws2global`, 00:12:56 à 00:16:59.
- Passage : Quand on finance un client, on finance rarement une entreprise autonome. On
  finance une entité dans un groupe : holding au-dessus, filiales en dessous, sociétés sœurs
  à côté. Premier cas, le client autonome : il appartient au groupe sur le papier, mais rien
  ne circule. Deuxième cas, le client donneur de cash : il produit du cash, et ce cash remonte
  régulièrement à la holding en dividendes, frais de gestion ou prêts intragroupe. Le compte de
  résultat dit que l'entreprise gagne de l'argent, mais cet argent ne reste pas dans l'entité
  financée : le crédit local ne sera pas remboursé par le cash local. Troisième cas, le client
  receveur de cash : soutenu, donc protégé, mais dépendant, donc fragile.
- Idée forte : le cash produit n'est pas le cash disponible pour rembourser.
- Public : directeurs crédit et risques, chargés d'affaires grandes entreprises, DG de banque.
- Potentiel : A. Risque réel, souvent manqué, illustrable par trois profils.
- Angle : « Un bon résultat ne rembourse pas un crédit. »
- Accroche : « Le compte de résultat était bon. Le crédit n'a pas été remboursé. Le cash était parti à la holding. »
- Citation : « J'en parle dans mon cours Lecture juridique et fiscale du client sur Xelanc. »

**N° 6 — Deux experts sérieux, deux valeurs, aucune erreur**
- Source : valo, projet `valos1global`, 00:00:00 à 00:04:50.
- Passage : On imagine l'évaluation comme un exercice technique : Excel, ratios, multiples.
  C'est rassurant, mais faux. Une évaluation n'est pas un calcul, c'est une prise de position
  financière et stratégique. Il n'existe pas un chiffre juste caché quelque part : deux
  professionnels sérieux peuvent analyser la même entreprise et arriver à deux valorisations
  différentes, toutes deux défendables, sans que personne ait fait d'erreur. Ils n'ont pas fait
  la même lecture du marché, du management, du futur. La vraie question n'est pas « mon calcul
  est-il bon ? » mais « puis-je défendre cette valeur face à quelqu'un qui a de l'argent en jeu ? ».
- Idée forte : la valeur est une interprétation structurée, pas une vérité.
- Public : dirigeants actionnaires, DAF, investisseurs.
- Potentiel : A. Contredit une croyance très répandue chez les dirigeants qui vendent.
- Angle : « Votre entreprise n'a pas une valeur. »
- Accroche : « Deux banquiers d'affaires sérieux. La même entreprise. Deux valeurs différentes. Aucun ne s'est trompé. »
- Citation : « J'en parle dans mon cours Évaluation d'entreprise sur Xelanc. »

**N° 7 — Quarante documents demandés, c'est un analyste perdu**
- Source : AF, projet `AFS3G`, 00:01:25 à 00:03:24.
- Passage : On ne demande pas la même chose pour une facilité de caisse, un crédit
  d'investissement ou une restructuration. Pour la caisse, on regarde le cycle d'exploitation,
  les délais clients et fournisseurs, la saisonnalité, six mois de relevés. Pour
  l'investissement, le programme, les devis, le plan de financement, les projections sur la
  durée du crédit. Pour une restructuration, on ajoute la carte des créanciers et le hors bilan.
  Un analyste qui demande la même liste à tous ses clients n'est pas rigoureux, il est scolaire.
  Un analyste qui demande quarante documents n'est pas rigoureux non plus : il se protège
  derrière le volume. La qualité d'une demande d'information révèle déjà le niveau de l'analyste.
- Idée forte : une demande ciblée et proportionnée est le premier acte d'analyse.
- Public : directeurs crédit, directeurs d'agence entreprises, DRH formation des banques.
- Potentiel : A. Les dirigeants de PME vivent ces listes interminables ; les banquiers se reconnaissent.
- Angle : ce que la liste de pièces dit de votre banquier.
- Accroche : « Quand un analyste vous demande quarante documents, ce n'est pas de la rigueur. C'est de la peur. »
- Citation : « J'en parle dans mon cours Analyse financière bancaire sur Xelanc. »

**N° 8 — Les trois quarts de la valeur sont hors du business plan**
- Source : DCF, `DCFS5-scripts.html`, capsule 5, § 5.5 « Apprécier la valeur : le regard critique ».
- Passage : Sur le cas MÉRIDIA, 76 % de la valeur d'entreprise est dans la valeur terminale.
  Les trois quarts de ce que vaut l'entreprise ne sont pas dans les cinq années soigneusement
  modélisées, mais dans l'au-delà, condensés dans une seule formule. Ce n'est pas une anomalie :
  sur une entreprise en croissance, c'est presque toujours le cas. Mais il faut le savoir et le
  dire, car cela déplace le débat vers deux chiffres : le taux et la croissance perpétuelle.
  Et c'est pourquoi un analyste ne présente jamais un point, mais une fourchette (ici 130 à
  178 autour d'un central à 153), avec les hypothèses qui tiennent chaque borne.
- Idée forte : on présente une fourchette, jamais un chiffre unique.
- Public : DAF, dirigeants qui lèvent ou cèdent, comités d'investissement.
- Potentiel : A. Chiffre fort (76 %), contre-intuitif pour qui croit au business plan détaillé.
- Angle : « Votre business plan de cinq ans pèse un quart de la valeur. »
- Accroche : « Vous avez passé trois semaines sur votre business plan à cinq ans. Il pèse 24 % de la valeur de votre entreprise. »
- Citation : « J'en parle dans mon cours Comment évaluer une entreprise par la méthode DCF sur Xelanc. »

**N° 9 — L'accord de la banque n'est pas la fin de la mission**
- Source : MLF, projet `MLF S5 GLOBAL`, 00:00:13 à 00:03:26 et 00:08:20.
- Passage : La banque donne son accord de principe, tout le monde respire, le dirigeant
  commence à dépenser l'argent dans sa tête. C'est le moment de ralentir. Un accord n'est pas
  un décaissement : c'est une intention, souvent assortie de conditions suspensives, de
  garanties à formaliser, de covenants. Il faut relire l'accord comme un analyste crédit :
  si la durée a été raccourcie, le DSCR tient-il encore ? Si le différé est plus court, la
  première année devient-elle tendue ? On ne quitte pas la mission quand l'accord est donné,
  on la quitte quand l'argent est sur le compte et que tout est conforme.
- Idée forte : beaucoup de financements se perdent entre le « oui » et le décaissement.
- Public : dirigeants de PME, DAF, conseils en financement.
- Potentiel : A. Situation vécue par beaucoup de dirigeants, conseil directement applicable.
- Angle : « Le jour où la banque dit oui, le danger commence. »
- Accroche : « La banque a dit oui. Tout le monde a sabré le champagne. Trois semaines plus tard, le dossier était bloqué. »
- Citation : « J'en parle dans mon cours Conduire une mission de levée de dette bancaire sur Xelanc. »

**N° 10 — L'indépendance mal préparée est une précarité déguisée**
- Source : advs, projet `advs5global`, 00:12:33 à 00:16:36.
- Passage : Devenir consultant indépendant, c'est choisir ses missions, ses clients, son
  rythme, et garder la valeur que l'on crée. Mais tout repose sur vous : la prospection, la
  négociation, la livraison. Vous gagnez seul ou vous perdez seul. Le risque principal est le
  plafond : tout dépend de votre temps et de votre capacité. Sans offre claire, sans modèle
  ficelé, sans savoir sélectionner ses clients, cette liberté tant recherchée devient vite une
  précarité déguisée. Il faut être l'acteur, mais aussi avoir le système.
- Idée forte : on ne quitte pas la banque pour être libre, on la quitte avec un système.
- Public : cadres bancaires seniors tentés par le conseil, DAF en transition.
- Potentiel : A. Sujet très partagé chez les cadres de 40-55 ans, position nette.
- Angle : à contre-courant du discours « lancez-vous ».
- Accroche : « On vous vend l'indépendance comme une liberté. Sans système, c'est une précarité déguisée. »
- Citation : « J'en parle dans mon cours Advisory Accelerator sur Xelanc. »

**N° 11 — Qui signe ? Vous. Toujours.**
- Source : FMIA, Drive `FMIA-production`, capsule E1 « signature » (`script.txt`, `E1-signature.html`).
- Passage : Quand une décision a été préparée avec l'IA, qui signe ? Vous, toujours. Trois
  règles pour tout le cours : l'IA propose (analyses, scénarios, brouillons, souvent
  excellents) ; vous vérifiez la source de chaque chiffre qui compte ; vous décidez et vous
  signez. L'IA ne portera jamais la décision à votre place, ni devant votre conseil, ni devant
  votre banquier. Ce n'est pas de la méfiance envers la technologie : c'est la responsabilité
  du dirigeant, et elle ne se délègue pas.
- Idée forte : la responsabilité ne se délègue pas à un outil.
- Public : DG, dirigeants de PME, administrateurs, DRH.
- Potentiel : A. Message court et net sur l'IA, dans la ligne des posts qui marchent.
- Angle : « L'IA ne viendra pas au conseil d'administration à votre place. »
- Accroche : « Votre IA a préparé le dossier. Votre banquier vous pose une question sur un chiffre. Qui répond ? »
- Citation : « J'en parle dans mon cours La finance du dirigeant avec l'IA sur Xelanc. »

**N° 12 — Le dividende qui dépasse le résultat**
- Source : AF, projet `AFS3G`, 00:20:07 à 00:21:52.
- Passage : Dans la liasse fiscale, le résultat apparaît comme un résultat, point. Dans les
  états de synthèse, il est affecté : en réserve (il renforce les fonds propres), en report à
  nouveau (neutre en cash) ou en dividendes (il sort de l'entreprise). Une entreprise qui met
  tout en réserve augmente sa capacité d'endettement ; une entreprise qui distribue 80 %
  appauvrit sa structure, et souvent ce cash finance la vie personnelle du dirigeant. Plus
  sensible encore : un dividende supérieur au résultat de l'exercice, pris sur les réserves
  passées. Il faut se demander pourquoi les actionnaires se désengagent. Ce signal ne se lit
  dans aucun ratio : il se lit dans le croisement liasse, états de synthèse, procès-verbal d'assemblée.
- Idée forte : les vrais signaux de risque sont dans l'écart entre les documents, pas dans les ratios.
- Public : directeurs risques, analystes crédit seniors, auditeurs.
- Potentiel : A. Exemple précis, signal faible concret.
- Angle : le signal que vos ratios ne verront jamais.
- Accroche : « Ce signal de risque n'apparaît dans aucun ratio. Il est dans le procès-verbal d'assemblée générale. »
- Citation : « J'en parle dans mon cours Analyse financière bancaire sur Xelanc. »

**N° 13 — On peut faire dire presque n'importe quoi à un WACC**
- Source : DCF, `DCFS4-scripts.html`, capsule 3, § 4.3 « L'anatomie du coût du capital ».
- Passage : Le coût moyen pondéré du capital s'assemble brique par brique : taux sans risque,
  bêta, prime de risque, coût de la dette après impôt, pondérations aux valeurs de marché et
  non comptables. Chacune de ces briques est un choix, et chaque choix est contestable : quel
  taux sans risque, sur quelle maturité ? Quel bêta, sur quelle période, quels comparables ?
  Un demi-point de prime par-ci, un bêta arrondi par-là, et le taux bouge, et la valeur avec
  lui. Le professionnel ne se contente pas d'un WACC : il interroge chaque ingrédient, le
  documente et le défend.
- Idée forte : derrière un taux d'apparence technique se cachent cinq choix discutables.
- Public : DAF, administrateurs, investisseurs, directeurs financiers de groupe.
- Potentiel : A. Démystifie un chiffre que beaucoup de dirigeants acceptent sans le discuter.
- Angle : les cinq questions à poser à votre banquier d'affaires sur son taux.
- Accroche : « Un demi-point de prime de risque, un bêta arrondi. Personne ne le voit dans le rapport. Tout le monde le paie dans le prix. »
- Citation : « J'en parle dans mon cours Comment évaluer une entreprise par la méthode DCF sur Xelanc. »

**N° 14 — La valorisation fixe la fourchette, pas le prix**
- Source : valo, projet `valos1global`, 00:09:53 à 00:12:46.
- Passage : Sans valorisation, pas de lettre d'intention (elle contient un prix indicatif) et
  pas de structure de financement (les banques calent la dette sur la transaction). Le vendeur
  arrive avec un prix d'ancrage, souvent un multiple ambitieux et une vision optimiste. En face,
  l'acquéreur raisonne en capacité d'endettement, cash disponible et rendement cible. La
  valorisation ne fixe pas le prix final : elle construit la zone dans laquelle le prix sera
  négocié. Elle doit tenir en négociation, en audit d'acquisition et en comité d'investissement.
  Et avec un fonds, elle doit être compatible avec un scénario de sortie crédible.
- Idée forte : la valorisation est un outil de transaction, pas un exercice académique.
- Public : dirigeants vendeurs, actionnaires familiaux, DAF.
- Potentiel : A. Utile à tout dirigeant qui pense à céder.
- Angle : « Votre prix d'ancrage va vous coûter la vente. »
- Accroche : « Le vendeur arrive avec un prix. L'acheteur arrive avec un tableur de dette. Devinez qui gagne. »
- Citation : « J'en parle dans mon cours Évaluation d'entreprise sur Xelanc. »

**N° 15 — Dire non fait partie du métier**
- Source : MLF, projet `MLFS1`, 00:02:23 à 00:04:10.
- Passage : Après avoir clarifié le besoin, testé l'éligibilité, défini le périmètre et posé
  les responsabilités, il faut décider : accepter ou refuser la mission. Un advisor qui ne sait
  pas refuser ne sélectionne pas, et met sa crédibilité en jeu. Trois questions avant de dire
  oui : ce dossier est-il défendable en comité de crédit ? La structure peut-elle absorber la
  dette ? Serais-je à l'aise pour le défendre face à un analyste exigeant ? Si les réponses
  sont fragiles : on restructure, on attend ou on refuse. Refuser un dossier non finançable,
  ce n'est pas perdre un client, c'est gagner du respect, et parfois sauver une entreprise
  d'une mauvaise décision.
- Idée forte : votre nom vaut plus que des honoraires.
- Public : consultants en financement, chargés d'affaires, dirigeants qui choisissent un conseil.
- Potentiel : A. Position morale claire, trois questions réutilisables.
- Angle : « Les trois questions qui m'ont fait refuser des mandats. »
- Accroche : « Le meilleur service que j'ai rendu à certains dirigeants, c'est de refuser leur mandat. »
- Citation : « J'en parle dans mon cours Conduire une mission de levée de dette bancaire sur Xelanc. »

**N° 16 — L'IA gagne en autonomie, le dirigeant doit gagner en contrôle**
- Source : FMIA, Drive `FMIA-production`, capsule E1 « trois âges » (`script.txt`, `E1-trois-ages.html`).
- Passage : Une même question, « quel est notre produit le plus rentable ? », traitée de trois
  façons. Premier âge, la conversation : on colle un tableau dans un assistant, c'est rapide,
  mais c'est une copie figée, et les données sont parties dans un outil extérieur. Deuxième âge,
  l'assistant intégré au tableur : plus de copier-coller, le classement évolue avec les données.
  Troisième âge, l'agent connecté : chaque lundi, il va chercher les ventes et envoie les trois
  écarts principaux, en lecture seule. À chaque âge, l'IA gagne en autonomie, et vous devez
  gagner en contrôle : relire une réponse, puis vérifier un fichier, puis définir des accès et
  des règles. Ce n'est plus une question d'outil, c'est une question de direction.
- Idée forte : plus l'IA est autonome, plus la gouvernance devient le sujet du dirigeant.
- Public : DG, DSI et DAF, DRH formation.
- Potentiel : A. Grille simple en trois niveaux, utile pour situer son entreprise.
- Angle : « Votre entreprise est à quel âge de l'IA ? »
- Accroche : « Le problème de l'IA en entreprise n'est pas l'outil. C'est qui a le droit de lui ouvrir quels fichiers. »
- Citation : « J'en parle dans mon cours La finance du dirigeant avec l'IA sur Xelanc. »

**N° 17 — L'intuition est un piège pour le banquier**
- Source : BMC, projet `BMCGLOBAL`, 00:03:01 à 00:05:18 et 00:07:56 à 00:09:41.
- Passage : On ouvre un dossier, on regarde vite les chiffres, et on se fait un avis : « je le
  sens » ou « je ne le sens pas ». Le problème n'est pas l'intuition, c'est quand elle remplace
  l'analyse. Chacun a son expérience, ses biais, ses limites : l'intuition ne peut pas être un
  cadre commun, et deux analystes arrivent à deux conclusions. Vous avez sans doute validé un
  dossier qui s'est mal passé, ou refusé un dossier qui a réussi chez un confrère. L'information
  était là ; c'est le traitement qui a manqué. Une méthode convenue protège : elle force les
  bonnes questions, évite les angles morts et rend le jugement lisible par tous.
- Idée forte : l'expérience nourrit l'analyse, elle ne la remplace pas.
- Public : directeurs crédit, DG de banque, responsables formation bancaire.
- Potentiel : A. Tout banquier a un dossier « refusé ici, réussi ailleurs ».
- Angle : « Le dossier que vous avez refusé et que votre concurrent a financé. »
- Accroche : « Vous avez refusé ce dossier. Votre confrère l'a financé. Il marche très bien. Qu'est-ce qui a manqué ? »
- Citation : « J'en parle dans mon cours BMC (Lire l'entreprise et son business model) sur Xelanc. »

**N° 18 — 120 millions de chiffre d'affaires, ce n'est pas un chiffre**
- Source : AF, projet `AFS4G`, 00:09:23 à 00:14:11.
- Passage : L'analyse financière ne se fait pas dans les agrégats, elle se fait dans le détail.
  Un agrégat additionne plusieurs réalités et efface ce qui les distingue. Un chiffre
  d'affaires de 120 millions peut cacher une activité historique en baisse, un client dominant,
  une saisonnalité forte. Celui qui reste dans l'agrégat dit « 120 millions ». Celui qui descend
  dit « 120 millions, dont 90 récurrents en baisse et 30 sur un contrat non reconductible ». Ce
  n'est pas le même constat, ni la même décision de comité. La matière pour décomposer est déjà
  dans le dossier : état des soldes de gestion, tableau de financement, état des dettes par
  échéance, état des informations complémentaires.
- Idée forte : un agrégat n'est jamais une réponse, c'est une porte d'entrée.
- Public : analystes et directeurs crédit, DAF, contrôleurs de gestion.
- Potentiel : A. Exemple chiffré mémorisable.
- Angle : « La phrase qui change une décision de comité. »
- Accroche : « "Chiffre d'affaires : 120 millions." Cette phrase a fait accorder un crédit qui n'aurait jamais dû l'être. »
- Citation : « J'en parle dans mon cours Analyse financière bancaire sur Xelanc. »

**N° 19 — Dix-huit ans en banque d'affaires, puis la question du décalage**
- Source : advs, projet `advs5global`, 00:16:36 à 00:20:20.
- Passage : La plupart des grands advisors indépendants sont passés par les banques d'affaires
  ou les grands cabinets : c'est là qu'on apprend les standards, la rigueur, la pression des
  grandes décisions. Rachid y a passé près de 18 ans. Il a fini par voir le décalage entre les
  commissions qu'il générait pour ses employeurs, banques d'affaires et fonds, et ce qu'il en
  gardait. Il a monté sa propre boutique de fusions-acquisitions. Mais ce chemin de dix ou
  quinze ans n'est plus le seul : ce qui compte aujourd'hui, c'est le niveau de structuration et
  de maîtrise des missions. La vraie question n'est pas d'où vous venez, mais à quel standard
  vous voulez exercer.
- Idée forte : on ne demande plus d'où vous venez, mais à quel standard vous travaillez.
- Public : cadres bancaires seniors, directeurs financiers en fin de cycle salarié.
- Potentiel : A. Récit personnel, chiffre (18 ans), décision de carrière.
- Angle : récit, « pourquoi j'ai quitté la banque d'affaires ».
- Accroche : « Pendant 18 ans, j'ai généré des commissions pour d'autres. Un jour, j'ai fait le calcul. »
- Citation : « J'en parle dans mon cours Advisory Accelerator sur Xelanc. »

**N° 20 — Le piège à 70 % : l'erreur de période sur la valeur terminale**
- Source : DCF, `DCFS4-scripts.html`, capsule 5, § 4.5 « La valeur terminale ramenée au présent ».
- Passage : La valeur terminale pèse autour de 70 % de la valeur totale. Elle est calculée à la
  fin de l'horizon explicite, disons l'année cinq, et doit être actualisée sur cinq ans, pas sur
  six. Par confusion, beaucoup l'actualisent sur une période de trop ou de moins. Un seul cran
  d'écart sur un chiffre qui pèse 70 % de la valeur, et toute la valorisation dérape de
  plusieurs pour cent. Cette erreur ne se voit pas dans le rapport ; elle ne saute aux yeux que
  de celui qui sait où regarder. S'y ajoutent le double comptage de la croissance et une
  croissance perpétuelle supérieure à celle de l'économie, ce qui est impossible.
- Idée forte : l'erreur la plus chère d'une valorisation tient dans un exposant.
- Public : DAF, M&A, auditeurs, administrateurs.
- Potentiel : A pour un public technique ; message « vérifiez ce point avant de signer ».
- Angle : le point unique à contrôler dans un rapport d'évaluation.
- Accroche : « Dans un rapport de valorisation, je regarde d'abord un seul chiffre : l'exposant de la valeur terminale. »
- Citation : « J'en parle dans mon cours Comment évaluer une entreprise par la méthode DCF sur Xelanc. »

**N° 21 — Ce qui n'est pas écrit n'a pas eu lieu**
- Source : AF, projet `AFS3G`, 00:06:28 à 00:07:26.
- Passage : Toutes les sources ne se valent pas. Par fiabilité décroissante : comptes certifiés
  sans réserve, comptes avec observations ou réserves (à creuser), comptes non audités (à
  croiser avec TVA, déclarations sociales, relevés), information publique, puis déclaratif du
  client. Un engagement sur l'honneur n'est pas une preuve, c'est une intention. Une information
  orale n'existe pas dans un dossier bancaire : en cas de contentieux, personne ne se souviendra
  d'une conversation téléphonique. Un analyste sérieux documente même la hiérarchie de ses
  sources, parce qu'en cas de problème on ne lui demandera pas ce qu'il a compris, mais ce qu'il
  a vu et où.
- Idée forte : en banque, la traçabilité protège autant que l'analyse.
- Public : directeurs risques et conformité, chargés d'affaires, DRH formation.
- Potentiel : A. Règle de terrain, liée aux contentieux.
- Angle : « On ne vous demandera pas ce que vous avez compris. »
- Accroche : « Le jour du contentieux, on ne vous demandera pas ce que vous avez compris. On vous demandera ce que vous avez vu, et où. »
- Citation : « J'en parle dans mon cours Analyse financière bancaire sur Xelanc. »

**N° 22 — Facturer sans s'excuser**
- Source : MLF, projet `MLF S5 GLOBAL`, 00:11:01 à 00:13:59.
- Passage : Au moment d'encaisser la commission de succès, beaucoup d'advisors hésitent,
  impressionnés par le montant, alors qu'ils étaient si exigeants en le structurant. La
  rémunération n'est pas une faveur : c'est la conséquence d'une mission livrée, grâce à une
  expertise accumulée pendant des années, pas grâce à deux ou trois mois de travail. À un client
  qui trouvait la commission énorme, Rachid répondait : « Oui, parce que ce que vous me demandez
  est énorme. » Au décaissement, on tend la facture, sans excuse ni renégociation. Et la façon de
  clôturer prépare la suite : avec ses clients, il a fait le plus souvent cinq à six missions.
- Idée forte : un advisor parle de ses honoraires avec la même sérénité que du DSCR.
- Public : consultants, banquiers d'affaires, indépendants.
- Potentiel : A. Sujet tabou, réponse vécue.
- Angle : « La phrase que je réponds quand un client trouve ma commission énorme. »
- Accroche : « "C'est énorme, votre commission." "Oui. Ce que vous me demandez aussi est énorme." »
- Citation : « J'en parle dans mon cours Conduire une mission de levée de dette bancaire sur Xelanc. »

**N° 23 — Le dirigeant qui signe n'est pas celui qui décide**
- Source : taxlaws, projet `taxlaws2global`, 00:08:25 à 00:12:56.
- Passage : Lire le contrôle, c'est répondre à trois questions différentes : qui détient le
  capital, qui dirige officiellement, qui décide vraiment. Premier cas, le dirigeant majoritaire
  engagé : pouvoir de droit et de fait coïncident, profil le plus lisible. Deuxième cas, le
  capital éclaté sans pacte : le risque devient la lenteur, un client bloqué non par manque de
  moyens mais par incapacité à trancher. Troisième cas, le dirigeant de fait : le signataire
  officiel exécute, et un actionnaire en retrait, un membre de la famille, un associé silencieux
  prend les décisions. C'est le profil le plus risqué : l'interlocuteur visible n'est pas le décideur réel.
- Idée forte : en crédit, le premier risque est parfois de ne pas parler au bon interlocuteur.
- Public : chargés d'affaires, directeurs crédit, DG de banque, investisseurs.
- Potentiel : A. Situation très fréquente dans les PME familiales d'Afrique et du Maghreb.
- Angle : « Vous avez négocié avec la mauvaise personne. »
- Accroche : « Il signait tout. Il ne décidait de rien. Le vrai patron n'est jamais venu à la banque. »
- Citation : « J'en parle dans mon cours Lecture juridique et fiscale du client sur Xelanc. »

**N° 24 — « Je peux défendre un dossier, je ne peux pas inventer des chiffres »**
- Source : MLF, projet `MLFS1`, 00:00:00 à 00:02:23.
- Passage : Une mission échoue rarement à cause des chiffres ; elle échoue à cause des
  comportements, quand les rôles ne sont pas clairs. L'advisor ne remplace pas le dirigeant :
  les informations viennent du client, les décisions stratégiques lui appartiennent, la méthode
  et la structuration sont la responsabilité de l'advisor. Principe simple : je peux défendre
  un dossier, je ne peux pas inventer des chiffres. D'où l'exigence de transparence totale,
  historiques bancaires et incidents compris, non pour contrôler mais pour protéger le process :
  si une information inconnue sort en comité de crédit, on perd le dossier et sa crédibilité.
- Idée forte : une responsabilité floue fait une mission à risque.
- Public : dirigeants qui préparent une demande de financement, conseils.
- Potentiel : A. Message utile aux dirigeants comme aux banquiers.
- Angle : ce que votre conseil doit savoir avant votre banquier.
- Accroche : « Le pire moment d'un comité de crédit : quand la banque découvre un incident que votre conseil ignorait. »
- Citation : « J'en parle dans mon cours Conduire une mission de levée de dette bancaire sur Xelanc. »

### Potentiel B

**N° 25 — Ne commencez jamais une levée par un montant**
- Source : LDF, projet `ldfs3`, 00:00:00 à 00:02:56.
- Passage : Un montant sans besoin clair fait une demande fragile, et une demande fragile fait
  un dossier fragile. Les banques ne financent pas des projets, elles financent des besoins
  identifiés : investissement, exploitation, acquisition, refinancement, sans les mélanger.
  « Besoin de trésorerie » ne veut rien dire : quel poste, quelle contrainte, pourquoi maintenant ?
  Et tous les besoins ne sont pas acceptables : une banque finance volontiers un actif
  identifiable, se méfie du fonds de roulement structurel, et refuse de financer un déficit structurel.
- Idée forte : on vend un besoin à une banque, pas un montant.
- Public : dirigeants de PME, DAF.
- Potentiel : B. Utile et concret, moins surprenant pour un public bancaire.
- Angle : « La première phrase de votre demande de crédit. »
- Accroche : « "Nous avons besoin de 2 millions." C'est la pire façon d'ouvrir un rendez-vous avec votre banquier. »
- Citation : « J'en parle dans mon cours Levée de fonds sur Xelanc. »

**N° 26 — Les cinq questions qu'un dirigeant doit poser à ses chiffres chaque mois**
- Source : FMIA, Drive `FMIA-production`, capsule E1 « revue mensuelle » (`script.txt`, `E1-revue-mensuelle.html`).
- Passage : Si vous regardez chaque mois le chiffre d'affaires, vous voyez l'essentiel et ratez
  le reste. Cinq questions : où en suis-je ? Vais-je manquer de cash ? Dois-je investir ?
  Comment me financer ? Puis-je me fier aux chiffres ? Aucune ne commence par un outil. La
  dernière est la plus négligée, et c'est elle qui protège toutes les autres. À chaque question
  correspond un document : sans plan de trésorerie, pas de réponse sur le cash. L'IA ne remplace
  pas le document, elle le lit.
- Idée forte : la question « puis-je me fier aux chiffres ? » protège toutes les autres.
- Public : dirigeants de PME, DAF.
- Potentiel : B. Grille utile, moins polémique.
- Angle : la revue mensuelle en cinq questions.
- Accroche : « Chaque mois, vous regardez votre chiffre d'affaires. C'est la question la moins utile des cinq. »
- Citation : « J'en parle dans mon cours La finance du dirigeant avec l'IA sur Xelanc. »

**N° 27 — Le compte de résultat et l'impôt ne racontent pas la même histoire**
- Source : AF, projet `AFS3G`, 00:11:59 à 00:13:33.
- Passage : La liasse fiscale donne accès à la mécanique brute, avant les choix de
  présentation. C'est souvent dans l'écart entre résultat comptable et résultat fiscal qu'on
  comprend la vraie dynamique. Une entreprise au résultat comptable correct mais avec de fortes
  réintégrations fiscales a une base taxable bien plus élevée : le cash est là. Une entreprise
  qui accumule les déficits reportables traverse une mauvaise passe durable, ou optimise
  méthodiquement sa base fiscale. Savoir distinguer les deux, c'est le métier.
- Idée forte : l'écart comptable-fiscal est une source d'information, pas un détail.
- Public : analystes crédit seniors, auditeurs, DAF.
- Potentiel : B. Technique, pour un public spécialisé.
- Angle : lire l'entreprise par sa liasse fiscale.
- Accroche : « Le résultat comptable vous dit ce que l'entreprise veut montrer. La liasse fiscale, ce qu'elle déclare au fisc. Regardez l'écart. »
- Citation : « J'en parle dans mon cours Analyse financière bancaire sur Xelanc. »

**N° 28 — Les dix compétences de l'évaluateur, et la dernière**
- Source : valo, projet `valos1global`, 00:13:14 à 00:22:29.
- Passage : Les compétences de l'évaluateur apparaissent dans l'ordre de la mission : lecture
  sectorielle, vision stratégique, compréhension du business model, accès à l'information,
  analyse financière, maîtrise des méthodes, jugement, présentation, négociation. On ne parle
  des méthodes qu'en sixième position. La dixième traverse tout : tenir sous pression, face à
  des dirigeants, des fonds, des banques souvent pressés, puissants, parfois durs et rarement
  patients. Une bonne valorisation portée par quelqu'un qui tremble perd sa substance. Un mauvais
  évaluateur calcule ; un bon comprend ; un excellent défend une position jusqu'au bout.
- Idée forte : la méthode arrive en sixième position ; la tenue sous pression traverse tout.
- Public : DRH formation, directeurs corporate finance, jeunes associés.
- Potentiel : B. Liste utile pour recruter ou former, moins de tension narrative.
- Angle : ce qu'on ne teste jamais en entretien d'un évaluateur.
- Accroche : « Dans les dix compétences d'un évaluateur, la maîtrise des méthodes n'arrive qu'en sixième position. »
- Citation : « J'en parle dans mon cours Évaluation d'entreprise sur Xelanc. »

**N° 29 — L'acheteur raisonne en TRI : chaque million payé en plus coûte du rendement**
- Source : valo, projet `valo s2`, 00:01:47 à 00:04:25.
- Passage : Une valorisation est un jeu d'acteurs. L'actionnaire qui vend une entreprise construite
  en vingt ou trente ans ne vend pas une bicyclette : il vend une partie de sa vie, et attend un
  prix qui le reflète. L'acquéreur veut optimiser son prix d'entrée : chaque million payé en plus
  est du rendement en moins. Un fonds raisonne entrée et sortie : il sait qu'on ne gagne pas à la
  sortie si l'on n'a pas gagné à l'entrée. La banque regarde le cash qui remboursera la dette et
  la tension des covenants. Une valorisation qui ignore les intérêts en présence ne survit pas.
- Idée forte : chaque partie lit la même valeur avec son propre filtre.
- Public : dirigeants actionnaires familiaux, DAF, investisseurs.
- Potentiel : B. Bon éclairage pour un dirigeant vendeur, sans chiffre fort.
- Angle : « Votre acheteur ne regarde pas votre entreprise. Il regarde son TRI. »
- Accroche : « Vous vendez trente ans de votre vie. Votre acheteur, lui, calcule un rendement à cinq ans. »
- Citation : « J'en parle dans mon cours Évaluation d'entreprise sur Xelanc. »

**N° 30 — Votre nom est sur la fourchette**
- Source : valo, projet `valo s2`, 00:12:21 à 00:13:53.
- Passage : Si l'évaluateur se voit comme un technicien qui produit un fichier, il disparaît
  derrière son document, et sa valorisation ne vaut rien. S'il se voit comme celui qui tient le
  process, il porte la conviction et fait tenir le deal. Rachid a porté cette responsabilité dans
  plusieurs dizaines, voire centaines de missions : quand vous posez une fourchette de valeur sur
  une table de négociation, c'est votre nom qui est dessus, votre réputation et votre crédibilité
  pour les dix années suivantes. C'est aussi pour cela que cette responsabilité est bien rémunérée.
- Idée forte : la valeur engage la réputation de celui qui la porte.
- Public : banquiers d'affaires, consultants, DAF.
- Potentiel : B. Position forte mais plus attendue.
- Angle : « Le livrable qui finit dans un Drive. »
- Accroche : « Un rapport de valorisation n'est pas un livrable. C'est votre signature pour les dix prochaines années. »
- Citation : « J'en parle dans mon cours Évaluation d'entreprise sur Xelanc. »

**N° 31 — Une offre floue est toujours tirée vers le bas**
- Source : advs, projet `advs5global`, 00:00:53 à 00:02:04.
- Passage : Le conseil ne se vend pas sous forme de compétences vagues ; il se vend à travers des
  missions que le marché reconnaît et achète : missions de financement, de rapprochement, de
  stratégie et de transformation, d'accompagnement récurrent. Chacune correspond à un moment
  précis et important de la vie d'une entreprise. Tant qu'un consultant ne décrit pas ses missions
  avec précision, son offre reste floue, et une offre floue est toujours challengée, comparée,
  sous-estimée, négociée. Quand la mission est claire, le rapport change : on n'a plus à se justifier.
- Idée forte : on vend une mission identifiée, pas une compétence.
- Public : consultants, cadres en reconversion vers le conseil.
- Potentiel : B. Utile, moins de surprise.
- Angle : « Arrêtez de vendre votre expertise. »
- Accroche : « "Je fais du conseil en finance." Cette phrase vous fait perdre la moitié de vos honoraires. »
- Citation : « J'en parle dans mon cours Advisory Accelerator sur Xelanc. »

**N° 32 — Le conseil ne commence pas au début d'une carrière**
- Source : METIERS, projet `METIERS1P1VF`, 00:00:00 à 00:03:47.
- Passage : L'advisor dont on parle n'est pas un jeune diplômé : c'est un expert qui a
  accumulé dix ou quinze ans, voire plus, de situations vécues, de décisions imparfaites et
  d'enjeux réels. Le point clé n'est pas la durée : avec le temps, il voit vite, repère les
  signaux, distingue le critique du secondaire, tranche là où d'autres expliquent. Il ne
  simplifie pas, il a déjà vécu des situations semblables. Ce profil est rare, parce que
  beaucoup restent dans l'exécution, vendent leur temps, et peu transforment leur expertise en
  produit vendable.
- Idée forte : l'expertise devient conseil quand elle se transforme en jugement vendable.
- Public : cadres seniors (banque, direction financière), DRH.
- Potentiel : B. Message valorisant pour les seniors, plus attendu.
- Angle : « Après 45 ans, votre valeur n'est pas votre temps. »
- Accroche : « La plupart des experts seniors vendent encore leur temps. C'est la ressource la moins rare qu'ils aient. »
- Citation : « J'en parle dans mon cours Les métiers du conseil (Advisory Accelerator) sur Xelanc. »

**N° 33 — Compter deux fois le risque**
- Source : DCF, `DCFS4-scripts.html`, capsule 4, § 4.4 « Actualiser l'horizon explicite ».
- Passage : Certains chargent leur taux d'actualisation pour le risque et, en même temps,
  rabotent leurs flux par prudence. Le même risque est pénalisé deux fois, et la valeur
  s'effondre, non parce que l'entreprise est mauvaise, mais parce que le modèle se contredit.
  Même logique pour le réel et le nominal : des flux avec inflation se divisent par un taux avec
  inflation, jamais de croisement. Et la convention de milieu d'année, qui reconnaît que le cash
  rentre tout au long de l'année, augmente mécaniquement la valeur de plusieurs pour cent.
- Idée forte : l'excès de prudence est aussi une erreur de valorisation.
- Public : DAF, analystes, comités d'investissement, dirigeants acheteurs.
- Potentiel : B. Contre-intuitif (« la prudence peut fausser »), mais technique.
- Angle : « Trop de prudence détruit de la valeur, sur le papier. »
- Accroche : « Le modèle était prudent. Doublement prudent. C'est exactement ce qui le rendait faux. »
- Citation : « J'en parle dans mon cours Comment évaluer une entreprise par la méthode DCF sur Xelanc. »

**N° 34 — La valeur d'entreprise n'est pas ce que touche l'actionnaire**
- Source : DCF, `DCFS5-scripts.html`, capsule 4, § 5.4 « L'output : tout converge vers la valeur ».
- Passage : Sur le cas MÉRIDIA, la valeur d'entreprise ressort à 183 000. C'est là que beaucoup
  s'arrêtent, et se trompent. La valeur d'entreprise est celle de l'outil économique entier,
  qui appartient à la fois aux actionnaires et aux créanciers. L'actionnaire n'achète que les
  fonds propres. D'où le pont : on retire la dette financière (45 000), on ajoute la trésorerie
  (15 000), on ajuste les minoritaires et les engagements de retraite s'il y en a : 153 000 de
  fonds propres, soit 153 euros par action.
- Idée forte : entre la valeur affichée et le chèque du vendeur, il y a la dette nette.
- Public : dirigeants vendeurs, actionnaires familiaux.
- Potentiel : B. Pédagogique, utile pour éviter une déception en négociation.
- Angle : « On vous annonce 183. Vous toucherez 153. »
- Accroche : « Votre banquier d'affaires vous annonce une valeur. Ce n'est pas le montant que vous toucherez. »
- Citation : « J'en parle dans mon cours Comment évaluer une entreprise par la méthode DCF sur Xelanc. »

**N° 35 — Les chiffres ne sont que la traduction d'un business**
- Source : BMC, projet `BMCGLOBAL`, 00:05:43 à 00:07:46.
- Passage : Une pratique fréquente : analyser un dossier élément par élément. Le chiffre
  d'affaires, la marge, la structure financière, puis le porteur, puis le secteur. On a
  l'impression d'avancer, mais on collectionne. Une entreprise ne fonctionne pas par morceaux,
  c'est un système, et dans un système les éléments n'ont de sens que par leurs liens. Un chiffre
  d'affaires seul ne veut rien dire, une marge seule non plus, un endettement seul non plus. Ce
  qui explique l'ensemble, c'est le modèle, le secteur, les choix. Il faut lire les liens, pas les éléments.
- Idée forte : un dossier épais n'est pas un dossier compris.
- Public : analystes crédit, chargés d'affaires, formation bancaire.
- Potentiel : B. Juste, plus abstrait.
- Angle : « Votre dossier de crédit est une collection, pas une analyse. »
- Accroche : « Trente indicateurs dans la note de crédit. Pas une phrase pour dire comment ils tiennent ensemble. »
- Citation : « J'en parle dans mon cours BMC (Lire l'entreprise et son business model) sur Xelanc. »

**N° 36 — Analyser l'entreprise et le porteur, séparément puis ensemble**
- Source : BMC, projet `BMCGLOBAL`, 00:09:54 à 00:12:24.
- Passage : Une décision de financement analyse deux réalités : l'entreprise et son porteur.
  Pour l'entreprise : son écosystème sectoriel, son business model, ses relations avec les
  parties prenantes, y compris avec le fisc (son « modèle fiscal », qui pèse sur son cash et sa
  performance), ses chiffres et ses perspectives. Pour le porteur : sa capacité à avoir les
  bonnes idées avant ses concurrents, à les mettre en œuvre, à piloter, à faire grandir l'affaire.
  Deux méthodes différentes, à mener séparément, puis à relier sans les confondre.
- Idée forte : un bon projet porté par le mauvais dirigeant reste un mauvais dossier.
- Public : banquiers d'entreprise, investisseurs, capital-risque.
- Potentiel : B.
- Angle : « On finance une entreprise. On parie sur un dirigeant. »
- Accroche : « J'ai vu d'excellents projets échouer avec le mauvais dirigeant, et des projets moyens réussir avec le bon. »
- Citation : « J'en parle dans mon cours BMC (Lire l'entreprise et son business model) sur Xelanc. »

**N° 37 — La forme juridique dit ce que la banque pourra faire si tout se passe mal**
- Source : taxlaws, projet `taxlaws2global`, 00:03:49 à 00:08:25.
- Passage : La forme juridique n'est pas une mention en haut du bilan, c'est la coque du client.
  Elle dit jusqu'où va la responsabilité des associés, quel niveau de transparence on aura
  (comptes publiés, commissaire aux comptes), quelle capacité à lever des fonds propres en cas de
  difficulté, et quelles garanties on pourra prendre. La SARL familiale : responsabilité limitée,
  mais caution personnelle du dirigeant. La grande SA : transparence élevée, engagement personnel
  faible. La filiale locale d'un groupe étranger : dirigeant salarié, décisions prises ailleurs,
  garanties locales inexistantes, un risque structurel spécifique.
- Idée forte : lire la forme, c'est savoir d'avance ses recours.
- Public : chargés d'affaires, directeurs juridiques de banque, directeurs crédit.
- Potentiel : B. Solide, plus technique.
- Angle : la filiale de groupe étranger, profil sous-estimé.
- Accroche : « Le dirigeant local est charmant. Il n'a aucun pouvoir, et aucune garantie à vous donner. »
- Citation : « J'en parle dans mon cours Lecture juridique et fiscale du client sur Xelanc. »

**N° 38 — Simulation n'est pas prévision**
- Source : FMIA, Drive `FMIA-production`, capsule E1 « quatre verbes » (passage « simuler »).
- Passage : Dans un tableur, on demande à l'IA l'effet d'une hausse de prix de 5 % avec une
  perte de volume de 3 %. Sur le cas Maison Lumen, la marge brute passe de 5 340 000 à
  5 762 000 euros : 422 000 euros de plus en changeant une seule hypothèse. Attention : c'est une
  simulation, pas une prévision. Si les clients réagissent plus fortement à la hausse, le gain
  fond très vite. L'IA calcule vite ; elle ne connaît pas la réaction de vos clients.
- Idée forte : l'IA chiffre une hypothèse ; elle ne la rend pas vraie.
- Public : dirigeants, directeurs commerciaux, DAF.
- Potentiel : B. Utile, bon support de démonstration.
- Angle : le danger des simulations trop rapides.
- Accroche : « 422 000 euros de marge en plus en dix secondes. C'est exactement pour ça qu'il faut se méfier. »
- Citation : « J'en parle dans mon cours La finance du dirigeant avec l'IA sur Xelanc. »

**N° 39 — L'IA pose les bonnes questions, elle ne connaît rien de votre entreprise**
- Source : FMIA, Drive `FMIA-production`, capsule 1.1 « quatre décisions » (`script.txt` du dossier 1.1, `E2-quatre-decisions.html`).
- Passage : Ouvrir un showroom à Lyon pour 1,2 million d'euros : décision commerciale ou
  financière ? En finance d'entreprise, un dirigeant ne prend que quatre grandes décisions :
  investir, se financer, distribuer ou réinvestir, gérer le cash. On peut avoir un excellent
  projet et le financer très mal. Posée à ChatGPT, la question retrouve les quatre décisions dans
  le bon ordre et demande les bons documents. Mais pas un seul chiffre : l'IA pose les bonnes
  questions, elle ne connaît encore rien de votre entreprise. Tout ce qu'elle dira de précis
  dépendra des documents que vous lui confierez.
- Idée forte : la qualité de la réponse dépend des documents fournis, pas de l'outil.
- Public : dirigeants de PME, DAF.
- Potentiel : B.
- Angle : « Un bon projet mal financé reste un mauvais projet. »
- Accroche : « Un showroom à 1,2 million d'euros. Décision commerciale ou financière ? Votre réponse va probablement changer. »
- Citation : « J'en parle dans mon cours La finance du dirigeant avec l'IA sur Xelanc. »

**N° 40 — La lecture se pense avant d'ouvrir le dossier**
- Source : AF, projet `AFS4G`, 00:01:06 à 00:04:46.
- Passage : Quand on débute, on lit les documents dans l'ordre où ils arrivent : le bilan est
  en premier, on commence par le bilan. C'est laisser le dossier conduire l'analyse. Or cette
  documentation n'a jamais été faite pour la banque : elle a été faite pour le fisc, les
  actionnaires, le tribunal de commerce. La banque a une seule question : peut-on financer cette
  entreprise, à quel risque ? Trois réflexes : entrer par le contexte, jamais par les chiffres ;
  aller du général au détail et du passé au projeté ; marquer des pauses pour synthétiser, car
  accumuler n'est pas analyser.
- Idée forte : une analyse suit l'ordre de la pensée de l'analyste, pas celui du dossier.
- Public : analystes crédit, formation bancaire, DRH.
- Potentiel : B.
- Angle : « Les comptes de vos clients n'ont pas été écrits pour vous. »
- Accroche : « Les comptes que vous analysez ont été écrits pour le fisc et les actionnaires. Pas pour votre banque. »
- Citation : « J'en parle dans mon cours Analyse financière bancaire sur Xelanc. »

**N° 41 — La banque finance le futur ; l'historique ne sert qu'à le tester**
- Source : AF, projet `AFS4G`, 00:14:15 à 00:17:50.
- Passage : On passe l'essentiel du temps sur l'historique : trois ans de bilans, ratios,
  évolutions. On finit par croire que c'est cela, l'analyse. Mais l'historique n'est pas la
  décision : il prépare la décision. Il sert à trois choses : comprendre la mécanique de
  l'entreprise, identifier les tendances, calibrer la capacité réelle de remboursement. La
  décision se forge dans la confrontation du prévisionnel avec l'historique. Un bon prévisionnel
  n'est pas ambitieux, il est cohérent : une rupture avec le passé sans explication économique
  n'est pas recevable.
- Idée forte : un bon prévisionnel est cohérent, pas ambitieux.
- Public : directeurs crédit, dirigeants qui présentent un business plan.
- Potentiel : B.
- Angle : à double public (banquier et dirigeant).
- Accroche : « Votre business plan est ambitieux. C'est exactement ce qui inquiète votre banquier. »
- Citation : « J'en parle dans mon cours Analyse financière bancaire sur Xelanc. »

**N° 42 — Une entreprise vaut ce qu'elle va produire**
- Source : DCF, `dcf-s1-c1.html` et `dcf-s1-c2.html` (section 1, capsules 1 et 2, citations du mentor).
- Passage : Quand vous achetez une entreprise, vous n'achetez pas ce qu'elle possède : vous
  achetez ce qu'elle va produire, et la DCF ne regarde que cela. Le marché mesure un prix, le
  bilan une valeur comptable, les comparables un précédent ; la DCF est la seule à demander
  quelle richesse l'entreprise va créer demain. Toute la logique tient en une phrase : une
  entreprise vaut son cash futur, pour ses apporteurs de capitaux, ramené à aujourd'hui.
- Idée forte : on achète un futur, pas un patrimoine.
- Public : dirigeants, investisseurs, DAF.
- Potentiel : B. Bonne porte d'entrée, idée connue des financiers.
- Angle : pédagogie pour dirigeants non financiers.
- Accroche : « Vous n'achetez pas ce qu'une entreprise possède. Vous achetez ce qu'elle va produire. »
- Citation : « J'en parle dans mon cours Comment évaluer une entreprise par la méthode DCF sur Xelanc. »

---

## 3. Pour aller vers 100 passages

Prochaines extractions, dans cet ordre (transcriptions déjà disponibles dans Descript) :
1. `ADVS1`, `advs3introdes`, `ADVS3P1des` à `ADVS3P4des`, `advs4p1`, `advs4p3` : récits de mission probables.
2. `Cerle de Mentorat Posture` et la suite du Cercle III (02:40 à la fin : cas de diagnostic d'une entreprise de génie civil, benchmark, multiples).
3. `BMCS2` à `BMCS4` (business model, modèle fiscal, porteur).
4. `MLFS2Global`, `MLF S3 GLOBAL`, `MLF S4 GLOBAL` (cadrage, contrat, négociation bancaire).
5. LDF sections 1, 2, 4 à 6.
6. `DCFS2C1F` (le cash) et les sections DCF 2 et 3 si leurs HTML sont retrouvés.
7. Les HTML manquants, dès que Rachid indique où ils sont.
