# Scénario « Valeur » · emails de relance jusqu'au paiement

**Version** : 04/11/2026, brouillon · **Pour** : Rachid, puis l'agent Brevo · **Statut** : rien n'est envoyé sans le GO de Rachid.
**Principe** (décision de Rachid du 04/11) : on ne baisse pas le prix et on ne propose pas d'étalement. On montre la valeur de l'abonnement, un bénéfice par email, tous les deux jours, jusqu'au paiement. Au paiement, le contact sort du scénario.

Variables Brevo : `{{ contact.PRENOM }}`. Expéditeur : Rachid El Maataoui (texte simple, pas de modèle de campagne). Un seul bouton par email, vers la page d'abonnement avec UTM `utm_source=brevo&utm_medium=email&utm_campaign=valeur&utm_content=eN`.

**À vérifier avant envoi** (marqué ⚠ dans les textes) :
- le chiffre de 36 000 ressources doit être visible sur le site ;
- l'IA (xelia.xelanc.org) : nom exact, et peut-on poser une question sans abonnement ?
- la garantie de 5 jours (prévue dans le cahier des charges des landing pages) : existe-t-elle en vrai, et pour quelles formules ?
- l'email d'accès automatique après paiement doit être en place.

---

## Les bénéfices retenus, du plus fort au plus faible

| # | Bénéfice | Pourquoi il porte | Preuve |
|---|---|---|---|
| 1 | **Un tuteur IA qui répond à vos questions de finance, à toute heure, en français** | Personne ne l'a dans nos marchés. C'est concret et ça se montre en une capture | xelia.xelanc.org ⚠ |
| 2 | **Toute la bibliothèque du métier dans un seul abonnement** | La richesse : 36 000 ressources ⚠, modèles Excel, fiches métiers, glossaire, guides IA | Site |
| 3 | **Apprendre sur un vrai dossier, du début à la fin** | Le fil rouge Atlas : une demande de crédit menée de la liasse fiscale à la note de comité. Aucun concurrent ne le fait | Benchmark du 23/10 |
| 4 | **Utiliser l'IA sans se tromper devant un comité** | Un protocole de vérification en 3 contrôles, dans chaque capsule. La peur n°1 des banquiers : l'IA qui invente | Benchmark du 23/10 |
| 5 | **Vos normes : SYSCOHADA, CGNC, PCG** | Les autres plateformes sont en US GAAP ou IFRS génériques, et en anglais | Benchmark du 23/10 |
| 6 | **Un certificat vérifiable, à publier sur LinkedIn** | La reconnaissance professionnelle est ce que nos marchés achètent | Pages /certificats/ |
| 7 | **Des capsules de 3 à 5 minutes, sur téléphone** | Lève l'objection du temps. 97 % des achats se font sur téléphone | Historique Meta |
| 8 | **Le prix de tout ça : moins de 25 € par mois** | Ancrage : un séminaire de 2 jours sur l'IA en finance coûte 1 590 € HT chez Cegos | Benchmark du 23/10 |

---

## Phase 1 · La proposition de valeur (6 emails, un tous les deux jours)

### E1 · J0 · Le tuteur IA
**Objet** : {{ contact.PRENOM }}, posez votre question à notre IA
**Aperçu** : Elle répond en français, aux normes SYSCOHADA et CGNC.

Bonjour {{ contact.PRENOM }},

Une question de finance vous bloque ? Un ratio à interpréter, un retraitement, une garantie à évaluer ?

Avec votre abonnement XELANC, vous la posez à notre tuteur IA, à toute heure, depuis votre téléphone. Il répond en français, avec vos normes : SYSCOHADA, CGNC ou PCG.

Exemple, posé hier : *« Comment retraiter un crédit-bail dans l'analyse d'une PME en SYSCOHADA ? »*
[capture de la réponse ⚠]

C'est l'outil que nos abonnés ouvrent chaque jour, comme un collègue expert toujours disponible.

[Bouton] **Je m'abonne et je pose ma question**

Rachid El Maataoui
Financité Institute · XELANC

### E2 · J+2 · Toute la bibliothèque
**Objet** : 36 000 ressources de finance, dans un seul abonnement ⚠
**Aperçu** : Modèles Excel, fiches métiers, guides IA, dossiers réels.

Bonjour {{ contact.PRENOM }},

Ce que vous obtenez avec un abonnement XELANC, concrètement :

- les cours de votre métier, en capsules courtes ;
- des modèles Excel prêts à l'emploi ;
- des fiches métiers et un glossaire de la finance ;
- des guides pour travailler avec l'IA ;
- des dossiers réels d'entreprises et de banques.

En tout, 36 000 ressources ⚠. Tout est inclus, pas de module à acheter en plus.

[Bouton] **Je découvre la bibliothèque**

Rachid

### E3 · J+4 · Le vrai dossier
**Objet** : Un vrai dossier de crédit, de la liasse à la note de comité
**Aperçu** : On n'apprend pas la finance par morceaux.

Bonjour {{ contact.PRENOM }},

Dans la plupart des formations, on voit un ratio ici, un tableau là. Puis, devant un vrai dossier, on ne sait pas par où commencer.

Chez XELANC, vous suivez un même dossier du début à la fin : Atlas, une PME qui demande un crédit. Vous partez de sa liasse fiscale, vous faites les retraitements, l'analyse, l'évaluation du risque, et vous rédigez la note pour le comité.

À la fin, vous avez fait le travail, pas seulement regardé quelqu'un le faire.

[Bouton] **Je commence le dossier Atlas**

Rachid

### E4 · J+6 · L'IA sans se tromper
**Objet** : L'IA invente parfois. Voici comment ne pas se faire piéger
**Aperçu** : 3 contrôles, dans chaque capsule.

Bonjour {{ contact.PRENOM }},

L'IA va vite. Mais elle se trompe parfois avec assurance, et devant un comité de crédit, une erreur coûte cher.

C'est pourquoi chaque capsule XELANC applique la même méthode : 3 contrôles pour vérifier ce que l'IA vous donne, avant de l'utiliser.

Vous gagnez la vitesse de l'IA, sans perdre la rigueur du métier. C'est ce que les banques attendent maintenant de leurs analystes.

[Bouton] **J'apprends à utiliser l'IA correctement**

Rachid

### E5 · J+8 · Le certificat
**Objet** : {{ contact.PRENOM }}, votre certificat sur LinkedIn
**Aperçu** : Vérifiable en ligne par n'importe quel recruteur.

Bonjour {{ contact.PRENOM }},

Ce que vous apprenez doit se voir.

Avec l'abonnement annuel, vous passez vos évaluations et vous obtenez un certificat XELANC, par Financité Institute :
- Analyste financier risque, Chargé d'affaires entreprise, Banquier conseil, Financier d'entreprise, Analyste financier corporate ou Investment banker ;
- vérifiable en ligne par un recruteur ou votre direction ;
- avec son badge, à publier sur votre profil LinkedIn.

[visuel d'un vrai certificat ⚠]

Ce n'est pas un diplôme d'État. C'est la preuve, vérifiable, que vous savez faire.

[Bouton] **Je choisis mon certificat**

Rachid

### E6 · J+10 · Le prix de tout ça
**Objet** : Tout cela pour moins de 25 € par mois
**Aperçu** : Le prix d'un séminaire de 2 jours, c'est 1 590 €.

Bonjour {{ contact.PRENOM }},

Un séminaire de deux jours sur l'IA en finance coûte environ 1 590 € HT en France.

L'abonnement annuel XELANC, c'est 299 € pour l'année : moins de 25 € par mois. Pour ce prix, le tuteur IA, toute la bibliothèque, le dossier Atlas, la méthode de vérification et vos certificats. En capsules de 3 à 5 minutes, sur votre téléphone, à votre rythme.

Vous payez par Mobile Money ou par carte. Vos accès s'ouvrent tout de suite.

[Bouton] **Je m'abonne pour 299 €**

Si vous avez une question avant de vous décider, répondez simplement à cet email, ou écrivez à Loubna sur WhatsApp : [lien].

Rachid

---

## WhatsApp en appui (Loubna, un message par semaine au plus)

Hors de la fenêtre de 24 h, il faut un **modèle Meta validé**. Proposition de modèle (catégorie marketing) :

> Bonjour {{1}}, c'est Loubna, de XELANC (Financité Institute). Je vous ai envoyé par email une présentation de [{{2}}]. Si vous voulez, je vous montre en 2 minutes comment ça marche sur votre téléphone. Je vous envoie le lien ?

- `{{2}}` : « notre tuteur IA » (après E1), « le dossier Atlas » (après E3), « votre certificat » (après E5).
- Envoyer seulement si l'email n'a pas été ouvert, ou s'il a été cliqué sans paiement.

---

## Phase 2 · « Les N ressources pour maîtriser… » (à partir de J+12)

**Format** (décision de Rachid du 04/11) : un email par compétence. Il cite 10 à 15 ressources réelles de XELANC, avec leur lien, rangées en 5 blocs : comprendre (glossaire), calculer (outils), travailler (modèles Excel), avec l'IA (guides), se former et se certifier (cours et certificat). Le bouton mène à l'abonnement.

Tous les liens viennent du plan du site xelanc.org, relevé le 04/11. Les ressources du glossaire, des guides, des outils et des modèles sont publiques : le prospect les ouvre tout de suite, c'est la preuve par l'usage. Les cours et les certificats demandent l'abonnement.
⚠ Avant envoi : vérifier que chaque page de cours citée est bien un cours ouvert à l'abonnement, et ajouter les UTM (`utm_content=p2-1`, etc.) par l'option de suivi automatique de Brevo.

Ordre d'envoi : on commence par la porte du prospect. Porte bancaire : P2.1, P2.2, P2.3, puis P2.4, P2.5, P2.6. Porte entreprise : P2.4, P2.5, puis P2.1, P2.2, P2.3, P2.6.

### P2.1 · Analyse financière orientée risque
**Objet** : 15 ressources pour maîtriser l'analyse financière orientée risque
**Aperçu** : De la lecture des comptes à la notation d'une PME.

Bonjour {{ contact.PRENOM }},

Analyser un dossier de crédit, c'est répondre à une seule question : l'entreprise pourra-t-elle rembourser ? Voici les 15 ressources XELANC pour savoir y répondre.

**Comprendre**
1. [La capacité de remboursement](https://xelanc.org/ressources/glossaire/capacite-de-remboursement/)
2. [Le DSCR](https://xelanc.org/ressources/glossaire/dscr/)
3. [La capacité d'autofinancement (CAF)](https://xelanc.org/ressources/glossaire/capacite-d-autofinancement-caf/)
4. [Le ratio d'endettement (gearing)](https://xelanc.org/ressources/glossaire/ratio-d-endettement-gearing/)
5. [Les soldes intermédiaires de gestion en SYSCOHADA](https://xelanc.org/ressources/glossaire/soldes-intermediaires-de-gestion-syscohada/)
6. [Les covenants](https://xelanc.org/ressources/glossaire/covenants/)

**Calculer**
7. [Le calculateur de DSCR](https://xelanc.org/outils/calcul-dscr/)
8. [Le calculateur de capacité de remboursement](https://xelanc.org/outils/calcul-capacite-de-remboursement/)

**Travailler**
9. [Passer du bilan comptable au bilan financier (Excel)](https://xelanc.org/ressources/modeles-excel/passage-bilan-comptable-bilan-financier/)
10. [Les ratios financiers (Excel)](https://xelanc.org/ressources/modeles-excel/ratios-financiers-excel/)
11. [La notation crédit d'une PME (Excel)](https://xelanc.org/ressources/modeles-excel/notation-credit-pme-excel/)

**Avec l'IA**
12. [L'IA dans l'analyse de crédit](https://xelanc.org/ressources/guides/ia-analyse-de-credit/)
13. [Quelle IA pour analyser un bilan ?](https://xelanc.org/ressources/guides/quelle-ia-pour-analyser-un-bilan/)

**Se former et se certifier**
14. [Le cours d'analyse financière et de crédit](https://xelanc.org/analysefinancierecredit/)
15. [Le certificat Analyste financier risque](https://xelanc.org/certificats/analyste-financier-risque/)

Les 13 premières sont en accès libre : ouvrez-les maintenant. Le cours et le certificat sont inclus dans l'abonnement annuel.

[Bouton] **Je m'abonne et je passe le certificat**

Rachid

### P2.2 · Le crédit aux entreprises et aux PME
**Objet** : 15 ressources pour devenir chargé d'affaires entreprise
**Aperçu** : Prospecter, monter le crédit, prendre les bonnes garanties.

Bonjour {{ contact.PRENOM }},

Un bon chargé d'affaires trouve les clients, choisit le bon crédit et sécurise la banque. Voici les 15 ressources XELANC pour le faire.

**Comprendre**
1. [Le crédit de campagne](https://xelanc.org/ressources/glossaire/credit-de-campagne/)
2. [Le crédit spot](https://xelanc.org/ressources/glossaire/credit-spot/)
3. [L'escompte commercial](https://xelanc.org/ressources/glossaire/escompte-commercial/)
4. [L'affacturage](https://xelanc.org/ressources/glossaire/affacturage/)
5. [Les sûretés réelles et personnelles](https://xelanc.org/ressources/glossaire/suretes-reelles-et-personnelles/)
6. [La garantie à première demande](https://xelanc.org/ressources/glossaire/garantie-a-premiere-demande/)
7. [Le taux effectif global (TEG)](https://xelanc.org/ressources/glossaire/taux-effectif-global-teg/)

**Calculer**
8. [Mensualité et tableau d'amortissement](https://xelanc.org/outils/calcul-mensualite-tableau-amortissement/)

**Travailler**
9. [Crédit-bail ou emprunt ? (Excel)](https://xelanc.org/ressources/modeles-excel/credit-bail-ou-emprunt-excel/)
10. [Le plan de financement (Excel)](https://xelanc.org/ressources/modeles-excel/plan-de-financement-excel/)
11. [Le suivi des covenants et des garanties (Excel)](https://xelanc.org/ressources/modeles-excel/suivi-covenants-garanties-excel/)

**Se former et se certifier**
12. [La prospection bancaire](https://xelanc.org/prospection-bancaire/)
13. [Gérer un portefeuille PME](https://xelanc.org/portefeuille-pme/)
14. [L'origination auprès de la clientèle corporate](https://xelanc.org/origination-aupres-de-la-clientele-corporate/)
15. [Le certificat Chargé d'affaires entreprise](https://xelanc.org/certificats/charge-affaires-entreprise/)

[Bouton] **Je m'abonne et je passe le certificat**

Rachid

### P2.3 · Le conseil au client bancaire
**Objet** : 12 ressources pour devenir le banquier que les clients écoutent
**Aperçu** : Connaître le métier du client, puis le conseiller.

Bonjour {{ contact.PRENOM }},

Le client ne cherche pas un produit. Il cherche quelqu'un qui comprend son affaire. Voici les 12 ressources XELANC pour devenir ce banquier.

**Comprendre**
1. [Le besoin en fonds de roulement (BFR)](https://xelanc.org/ressources/glossaire/besoin-en-fonds-de-roulement-bfr/)
2. [La trésorerie nette](https://xelanc.org/ressources/glossaire/tresorerie-nette/)
3. [Le découvert bancaire](https://xelanc.org/ressources/glossaire/decouvert-bancaire/)
4. [Le crédit-bail](https://xelanc.org/ressources/glossaire/credit-bail/)

**Calculer**
5. [Le calculateur de BFR et de fonds de roulement](https://xelanc.org/outils/calcul-bfr-fonds-de-roulement/)
6. [Le calculateur de seuil de rentabilité](https://xelanc.org/outils/calcul-seuil-de-rentabilite-point-mort/)

**Travailler**
7. [Le scoring crédit d'une TPE (Excel)](https://xelanc.org/ressources/modeles-excel/scoring-credit-tpe-excel/)

**Avec l'IA**
8. [L'intelligence artificielle dans la banque en Afrique](https://xelanc.org/ressources/guides/intelligence-artificielle-banque-afrique/)

**Se former et se certifier**
9. [Connaître le métier du client à 360°](https://xelanc.org/connaitre-metier-client-360/)
10. [Le marché des TPE et des professionnels](https://xelanc.org/marche-tpe-professionnels/)
11. [Le parcours Banquier conseil](https://xelanc.org/banquier-conseil/)
12. [Le certificat Banquier conseil](https://xelanc.org/certificats/banquier-conseil/)

[Bouton] **Je m'abonne et je passe le certificat**

Rachid

### P2.4 · La finance d'entreprise : trésorerie, budget, pilotage
**Objet** : 15 ressources pour piloter les finances d'une entreprise
**Aperçu** : Trésorerie, BFR, budget, tableau de bord.

Bonjour {{ contact.PRENOM }},

Le directeur général vous demande où en est la trésorerie, et si le budget tient. Voici les 15 ressources XELANC pour répondre avec des chiffres.

**Comprendre**
1. [Le fonds de roulement](https://xelanc.org/ressources/glossaire/fonds-de-roulement/)
2. [Le tableau des flux de trésorerie OHADA](https://xelanc.org/ressources/glossaire/tableau-des-flux-de-tresorerie-ohada/)
3. [L'excédent brut d'exploitation (EBE)](https://xelanc.org/ressources/glossaire/excedent-brut-d-exploitation-ebe/)

**Calculer**
4. [Le calculateur de valeur ajoutée et d'EBE](https://xelanc.org/outils/calcul-valeur-ajoutee-ebe/)
5. [Le calculateur de CAF](https://xelanc.org/outils/calcul-caf-capacite-d-autofinancement/)

**Travailler**
6. [Le plan de trésorerie (Excel)](https://xelanc.org/ressources/modeles-excel/plan-de-tresorerie-excel/)
7. [Le suivi budgétaire (Excel)](https://xelanc.org/ressources/modeles-excel/suivi-budgetaire-excel/)
8. [Le tableau de bord financier (Excel)](https://xelanc.org/ressources/modeles-excel/tableau-de-bord-financier-excel/)
9. [La balance âgée clients (Excel)](https://xelanc.org/ressources/modeles-excel/balance-agee-clients-excel/)

**Avec l'IA**
10. [L'IA dans le contrôle de gestion](https://xelanc.org/ressources/guides/ia-controle-de-gestion/)
11. [Excel et l'IA en finance](https://xelanc.org/ressources/guides/excel-et-ia-finance/)
12. [Construire un business plan avec l'IA](https://xelanc.org/ressources/guides/business-plan-avec-l-ia/)

**Se former et se certifier**
13. [Les grandes décisions financières](https://xelanc.org/grandes-decisions-financieres/)
14. [Financer la croissance](https://xelanc.org/financementcroissance/)
15. [Le certificat Financier d'entreprise](https://xelanc.org/certificats/financier-entreprise/)

[Bouton] **Je m'abonne et je passe le certificat**

Rachid

### P2.5 · L'évaluation d'entreprise
**Objet** : 12 ressources pour savoir combien vaut une entreprise
**Aperçu** : DCF, multiples, coût du capital.

Bonjour {{ contact.PRENOM }},

Combien vaut cette entreprise ? C'est la question de tout investisseur, de tout acquéreur et de tout comité. Voici les 12 ressources XELANC pour y répondre.

**Comprendre**
1. [La méthode DCF](https://xelanc.org/ressources/glossaire/dcf/)
2. [Le coût moyen pondéré du capital (CMPC, WACC)](https://xelanc.org/ressources/glossaire/cmpc-wacc/)
3. [La méthode des multiples](https://xelanc.org/ressources/glossaire/methode-des-multiples/)
4. [L'EBITDA](https://xelanc.org/ressources/glossaire/ebitda/)
5. [La rentabilité des capitaux propres (ROE)](https://xelanc.org/ressources/glossaire/rentabilite-des-capitaux-propres-roe/)

**Travailler**
6. [Le modèle DCF (Excel)](https://xelanc.org/ressources/modeles-excel/modele-dcf-excel/)
7. [Le calcul de la VAN et du TRI (Excel)](https://xelanc.org/ressources/modeles-excel/calcul-van-tri-excel/)

**Avec l'IA**
8. [L'analyse financière avec l'IA](https://xelanc.org/ressources/guides/analyse-financiere-avec-l-ia/)

**Se former et se certifier**
9. [L'évaluation d'entreprise](https://xelanc.org/evaluation-entreprise/)
10. [Le DCF en pratique](https://xelanc.org/dcf/)
11. [Les multiples de transactions comparables](https://xelanc.org/multiples-transactions-comparables/)
12. [Le certificat Analyste financier corporate](https://xelanc.org/certificats/analyste-financier-corporate/)

[Bouton] **Je m'abonne et je passe le certificat**

Rachid

### P2.6 · La banque d'affaires
**Objet** : 10 ressources pour entrer dans la banque d'affaires
**Aperçu** : Fusions, LBO, levée de dette.

Bonjour {{ contact.PRENOM }},

La banque d'affaires paie bien, et elle exige beaucoup. Voici les 10 ressources XELANC pour vous y préparer.

**Comprendre**
1. [Le ratio de solvabilité](https://xelanc.org/ressources/glossaire/ratio-de-solvabilite/)
2. [La rentabilité des actifs (ROA)](https://xelanc.org/ressources/glossaire/rentabilite-des-actifs-roa/)

**Travailler**
3. [Le modèle DCF (Excel)](https://xelanc.org/ressources/modeles-excel/modele-dcf-excel/)

**Avec l'IA**
4. [Les agents IA en finance](https://xelanc.org/ressources/guides/agents-ia-finance/)
5. [Claude ou ChatGPT pour la finance ?](https://xelanc.org/ressources/guides/claude-ou-chatgpt-finance/)

**Se former et se certifier**
6. [Faire carrière en banque d'affaires](https://xelanc.org/faire-carriere-banques-affaires/)
7. [Les fusions et acquisitions](https://xelanc.org/fusions-acquisitions/)
8. [Les montages LBO](https://xelanc.org/montages-lbo/)
9. [La levée de dette bancaire](https://xelanc.org/levee-dette-bancaire/)
10. [Le certificat Investment banker](https://xelanc.org/certificats/investment-banker/)

[Bouton] **Je m'abonne et je passe le certificat**

Rachid

## Phase 3 · « Nouveau cours en ligne » (en continu)

Un email par cours réellement sorti, avec sa date. Jamais d'annonce d'un cours qui n'est pas en ligne.

---

## Scénario « Arrivés au paiement puis repartis » : 3 emails de confiance

Même parcours que ci-dessus. Les trois emails de confiance passent en premier (C1, C2, C3), puis E1 à E6.
**Source de la liste** : commandes WooCommerce réelles en attente ou annulées, avec un email saisi. Pas le pixel.
**Règle** : ne jamais écrire « vous avez commencé un paiement » ni parler du panier.

### C1 · J0 · Qui est derrière XELANC
**Objet** : Qui est derrière XELANC ?
**Aperçu** : 30 ans de formation des banquiers et financiers.

Bonjour {{ contact.PRENOM }},

Avant de vous engager, vous voulez savoir à qui vous avez affaire. C'est normal.

XELANC est la plateforme en ligne de Financité Institute, qui forme les banquiers et les financiers depuis 30 ans. Je suis le Pr Rachid El Maataoui, et je vous explique en une minute ce que vous trouverez sur la plateforme :

[vidéo face caméra, 30 à 60 s ⚠]

[Bouton] **Je découvre la plateforme**

Rachid

### C2 · J+2 · Le certificat, en vrai
**Objet** : Voici à quoi ressemble votre certificat
**Aperçu** : Vérifiable en ligne en un clic.

Bonjour {{ contact.PRENOM }},

Voici un vrai certificat XELANC, tel qu'il apparaît sur LinkedIn : [visuel ⚠]. N'importe quel recruteur peut le vérifier en ligne avec ce lien : [lien de vérification ⚠].

[Si un lauréat est d'accord, avec son accord écrit : son nom, son poste, sa banque, une phrase.]

[Bouton] **Je choisis mon certificat**

Rachid

### C3 · J+4 · Payer en toute sécurité
**Objet** : Mobile Money, carte : vos accès en quelques minutes
**Aperçu** : Et quelqu'un pour vous aider si besoin.

Bonjour {{ contact.PRENOM }},

Comment ça se passe concrètement :
1. Vous choisissez votre formule.
2. Vous payez par Mobile Money (Airtel, Orange, M-Pesa) ou par carte, en euros.
3. Vous recevez aussitôt un email avec votre lien d'accès direct.

[Garantie : si elle existe, l'écrire ici, avec ses conditions exactes ⚠]

Si quelque chose bloque, Loubna vous aide sur WhatsApp, pendant votre paiement si vous le souhaitez : [lien].

[Bouton] **Je choisis ma formule**

Rachid

---

## Règles pour l'agent Brevo

1. **Entrée** : liste A, promesse de payer (fiches de `/conversion`) ; liste B, commande WooCommerce réelle en attente ou annulée. Un contact appartient à une seule liste.
2. **Sortie immédiate** : paiement reçu, désinscription, réponse à un email (le contact passe à Loubna), demande de « moins d'emails ».
3. **Exclusions** : abonnés, inscrits Advisory, inscrits au bootcamp, contacts appelés dans les dernières 48 h.
4. **Rythme** : un email tous les deux jours, jamais le même jour qu'un WhatsApp.
5. **Arrêt de la liste** si les plaintes dépassent 0,3 % ou les rebonds 3 %.
6. **Suivi, chaque semaine, par scénario** : ouvertures, clics, réponses, paiements, désinscriptions.
