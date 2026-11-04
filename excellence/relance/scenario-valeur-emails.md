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

## Les bénéfices retenus (révisés par Rachid le 04/11)

Deux idées portent tout le reste : **XELANC ne vend pas des cours, il mène à un métier**, et **la plateforme est un outil de travail augmenté par votre IA**.

| # | Bénéfice | Ce qu'on montre | Preuve |
|---|---|---|---|
| 1 | **6 parcours métiers certifiants dans un seul abonnement** | Chaque parcours : 5 compétences validées par quiz, examen final de 60 min, certificat vérifiable, 6 à 8 semaines. Vendus un par un 139 à 159 €, soit 884 € les six ; tous inclus dans l'annuel à 299 € | Pages /certificats/ et /membership/, relevées le 04/11 |
| 2 | **Votre IA, qui travaille avec vous** | On dialogue avec elle comme avec un collègue expert : question, dossier, calcul, note. Elle s'appuie sur les contenus de la plateforme ⚠ | xelia.xelanc.org ⚠ |
| 3 | **Un outil de travail pour chaque jour** | Calculateurs, modèles Excel, fiches, glossaire : on s'en sert au bureau dès le lendemain. 36 000 ressources ⚠ | /outils/, /ressources/ |
| 4 | **Apprendre en faisant le vrai travail** | Un dossier réel mené du début à la fin, et une méthode pour vérifier l'IA à chaque étape | Dossier Atlas, protocole en 3 contrôles |
| 5 | **La reconnaissance** | Un certificat vérifiable, avec son badge LinkedIn | /certificats/ |
| 6 | **Fait pour vous** | En français, aux normes SYSCOHADA, CGNC et PCG, avec des cas africains, en capsules de 3 à 5 minutes sur téléphone | Benchmark du 23/10 |
| 7 | **Tout dans un seul abonnement** | Moins de 25 € par mois, contre 1 590 € HT pour un séminaire de 2 jours | /membership/ |
| 8 | **Une plateforme qui grandit** | De nouveaux contenus chaque semaine (fait le pont avec la phase 3) | Calendrier des sorties ⚠ |

Chaque email ouvre par le plus grand bénéfice, le métier, puis montre un bénéfice précis.

---

## Phase 1 · La proposition de valeur (6 emails, un tous les deux jours)

### E1 · J0 · Six parcours métiers certifiants, un seul abonnement
**Surtitre** : La première plateforme francophone de parcours métiers certifiants
**Objet** : 6 parcours métiers certifiants, dans un seul abonnement
**Version HTML** : `html/e1-parcours-certifiants.html` (envoyée en test à Rachid le 04/11)
**Aperçu** : Séparément, ils valent 884 €. Avec l'annuel : 299 €.

Bonjour {{ contact.PRENOM }},

XELANC ne vous vend pas des cours. Il vous mène à un métier.

Chaque parcours suit l'ordre du métier : 5 compétences, chacune validée par un quiz, puis un examen final de 60 minutes et un certificat vérifiable. Comptez 6 à 8 semaines par parcours, à votre rythme.

Voici les six parcours métiers certifiants :
- [**Analyste financier risque**](https://xelanc.org/certificats/analyste-financier-risque/) : transformer des comptes en décision de crédit, défendable en comité.
- [**Chargé d'affaires entreprise**](https://xelanc.org/certificats/charge-affaires-entreprise/) : prospecter, comprendre le client et financer sa croissance.
- [**Banquier conseil**](https://xelanc.org/certificats/banquier-conseil/) : conseiller le dirigeant et développer son portefeuille dans la durée.
- [**Financier d'entreprise**](https://xelanc.org/certificats/financier-entreprise/) : le bras droit financier du dirigeant, du diagnostic à la levée de dette.
- [**Analyste financier corporate**](https://xelanc.org/certificats/analyste-financier-corporate/) : expliquer la performance, construire les prévisions, éclairer les décisions.
- [**Investment banker**](https://xelanc.org/certificats/investment-banker/) : évaluation, fusions-acquisitions et LBO.

Achetés un par un, ces six parcours coûtent 884 €. Avec l'abonnement annuel, vous les avez tous, pour 299 € : vous commencez par le métier que vous visez, et vous continuez avec les autres.

[Bouton] **Je choisis mon parcours et je m'abonne**

Rachid El Maataoui
Financité Institute · XELANC

### E2 · J+2 · Votre IA
**Objet** : Dialoguez avec votre IA de finance
**Aperçu** : Comme un collègue expert, disponible à toute heure.

Bonjour {{ contact.PRENOM }},

Avec votre abonnement XELANC, vous n'êtes jamais seul devant un dossier. Vous dialoguez avec votre IA :
- vous lui posez une question de finance, elle vous répond en français, avec vos normes (SYSCOHADA, CGNC) ;
- vous lui soumettez un cas, elle vous guide pas à pas ;
- elle répond sur chaque leçon de la plateforme : 1 question par jour en mensuel, 5 en annuel, sans limite en Premium.

Exemple, posé cette semaine : *« Comment retraiter un crédit-bail dans l'analyse d'une PME en SYSCOHADA ? »*
[capture de la réponse ⚠]

La plateforme n'est pas une bibliothèque qu'on lit. C'est un outil qui travaille avec vous.

[Bouton] **Je m'abonne et je parle à mon IA**

Rachid

### E3 · J+4 · Un outil pour chaque jour de travail
**Objet** : Ce que vous ouvrirez demain matin au bureau
**Aperçu** : Calculateurs, modèles Excel, fiches : prêts à l'emploi.

Bonjour {{ contact.PRENOM }},

XELANC se sert au travail, pas seulement en formation. Quelques exemples, à ouvrir tout de suite :
- [Calculer un DSCR](https://xelanc.org/outils/calcul-dscr/)
- [Calculer un BFR et un fonds de roulement](https://xelanc.org/outils/calcul-bfr-fonds-de-roulement/)
- [Un plan de trésorerie (Excel)](https://xelanc.org/ressources/modeles-excel/plan-de-tresorerie-excel/)
- [La notation crédit d'une PME (Excel)](https://xelanc.org/ressources/modeles-excel/notation-credit-pme-excel/)
- [Le glossaire de la finance](https://xelanc.org/ressources/glossaire/)

Avec l'abonnement, vous avez toute la boîte à outils de votre métier : 36 000 ressources ⚠, et votre IA pour vous en servir.

[Bouton] **Je m'abonne et j'ouvre ma boîte à outils**

Rachid

### E4 · J+6 · Apprendre en faisant le vrai travail
**Objet** : Un vrai dossier, du début à la fin
**Aperçu** : Et une méthode pour ne jamais se faire piéger par l'IA.

Bonjour {{ contact.PRENOM }},

Devant un vrai dossier, beaucoup ne savent pas par où commencer. Chez XELANC, vous apprenez en faisant le travail du métier.

Vous suivez un même dossier du début à la fin : Atlas, une PME qui demande un crédit. De sa liasse fiscale aux retraitements, de l'analyse au risque, jusqu'à la note pour le comité.

À chaque étape, vous utilisez l'IA, et vous la vérifiez avec 3 contrôles. Vous gagnez sa vitesse sans perdre la rigueur du métier.

[Bouton] **Je m'abonne et je commence le dossier**

Rachid

### E5 · J+8 · La reconnaissance
**Objet** : {{ contact.PRENOM }}, votre métier sur LinkedIn
**Aperçu** : Un certificat vérifiable par n'importe quel recruteur.

Bonjour {{ contact.PRENOM }},

Ce que vous savez faire doit se voir.

Au bout de votre parcours, vous obtenez le certificat de votre métier, par Financité Institute :
- [Analyste financier risque](https://xelanc.org/certificats/analyste-financier-risque/), [Chargé d'affaires entreprise](https://xelanc.org/certificats/charge-affaires-entreprise/), [Banquier conseil](https://xelanc.org/certificats/banquier-conseil/), [Financier d'entreprise](https://xelanc.org/certificats/financier-entreprise/), [Analyste financier corporate](https://xelanc.org/certificats/analyste-financier-corporate/) ou [Investment banker](https://xelanc.org/certificats/investment-banker/) ;
- vérifiable en ligne par un recruteur ou votre direction ;
- avec son badge, à publier sur votre profil LinkedIn.

[visuel d'un vrai certificat ⚠]

Ce n'est pas un diplôme d'État. C'est la preuve, vérifiable, que vous savez faire le métier.

[Bouton] **Je m'abonne et je vise mon certificat**

Rachid

### E6 · J+10 · Tout, dans un seul abonnement
**Objet** : Votre métier, votre IA, vos outils : moins de 25 € par mois
**Aperçu** : Un séminaire de 2 jours coûte 1 590 €.

Bonjour {{ contact.PRENOM }},

Récapitulons ce que vous donne l'abonnement annuel XELANC :
- le parcours vers votre métier, et son certificat ;
- votre IA, pour dialoguer et travailler ;
- toute la boîte à outils : calculateurs, modèles Excel, fiches, glossaire ;
- de vrais dossiers, et une méthode pour vérifier l'IA ;
- en français, à vos normes, en capsules de 3 à 5 minutes sur téléphone ;
- et de nouveaux contenus chaque semaine.

Le tout pour 299 € par an, soit moins de 25 € par mois. Un séminaire de deux jours sur l'IA en finance coûte environ 1 590 € HT.

Vous payez par Mobile Money ou par carte. Vos accès s'ouvrent tout de suite.

[Bouton] **Je m'abonne pour 299 €**

Une question avant de vous décider ? Répondez à cet email, ou écrivez à Loubna sur WhatsApp : [lien].

Rachid

---

## WhatsApp en appui (Loubna, un message par semaine au plus)

Hors de la fenêtre de 24 h, il faut un **modèle Meta validé**. Proposition de modèle (catégorie marketing) :

> Bonjour {{1}}, c'est Loubna, de XELANC (Financité Institute). Je vous ai envoyé par email une présentation de [{{2}}]. Si vous voulez, je vous montre en 2 minutes comment ça marche sur votre téléphone. Je vous envoie le lien ?

- `{{2}}` : « les métiers que nous préparons » (après E1), « votre IA » (après E2), « le dossier Atlas » (après E4), « votre certificat » (après E5).
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
