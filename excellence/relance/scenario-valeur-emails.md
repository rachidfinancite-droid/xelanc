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

## Phase 2 · « Avez-vous les compétences de… ? » (à partir de J+12)

Un email par certificat, en commençant par la porte du prospect (Banquier-analyste ou Financier d'entreprise). Gabarit :

**Objet** : Avez-vous les compétences d'un [métier] ?
**Corps** : 3 ou 4 situations du métier (« vous devez présenter un dossier de crédit PME en comité… »), puis les ressources dédiées dans XELANC (cours, modèles, fiches), puis le certificat correspondant. Bouton : **Je vois les ressources du [métier]**.

Ordre proposé, porte bancaire : Chargé d'affaires entreprise, Analyste financier risque, Banquier conseil. Porte entreprise : Financier d'entreprise, Analyste financier corporate. Investment banker à la fin.
J'ai besoin de la liste réelle des ressources par certificat pour les rédiger.

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
