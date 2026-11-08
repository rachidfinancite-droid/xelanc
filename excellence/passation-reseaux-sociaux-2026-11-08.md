# Passation : stratégie réseaux sociaux et posts LinkedIn de Rachid (8 novembre 2026)

Ce document permet de reprendre, dans une nouvelle conversation, tout le travail de la conversation « Stratégie de croissance réseaux sociaux » (session cloud `session_01LXovPVQzkTfW1BySYLtdX7`).

Il est autonome : la nouvelle conversation n'a besoin que de lui et des fichiers qu'il cite.

---

## 0. Comment reprendre (à faire en premier)

1. **Récupérer les fichiers sur le Mac.** Tout est dans le dépôt GitHub `rachidfinancite-droid/xelanc`, branche **`claude/amazing-thompson-r7gb78`** :
   ```bash
   git clone https://github.com/rachidfinancite-droid/xelanc.git
   ```
   ```bash
   cd xelanc && git checkout claude/amazing-thompson-r7gb78
   ```
   Si le dépôt est déjà cloné sur le Mac :
   ```bash
   git fetch origin claude/amazing-thompson-r7gb78 && git checkout claude/amazing-thompson-r7gb78 && git pull
   ```
2. **Ouvrir une nouvelle conversation Claude Code dans ce dossier** et coller le message de reprise de la section 13.
3. **Lire dans cet ordre :**
   - ce fichier ;
   - `excellence/posts/bibliotheque-idees-rachid.md` (le cœur du travail en cours) ;
   - `excellence/strategie-contenu-rachid-adam-loubna-2026-11-08.md` ;
   - `excellence/diagnostic-reseaux-organiques-2026-11-08.md`.

---

## 1. Le point de départ

Rachid publie sur LinkedIn, Instagram et Facebook pour XELANC (école de finance en ligne de Financité Institute). La portée organique est quasi nulle, alors que des contenus proches font 600 à 800 likes sur d'autres pages. Il demandait une stratégie fondée sur les bonnes pratiques pour remplir les pages d'abonnés et d'activité.

Ce que la conversation a produit, dans l'ordre :
1. un diagnostic des vrais chiffres (Metricool) ;
2. une stratégie de contenu à trois voix (Rachid, Adam, Loubna) ;
3. l'analyse des posts « hors du commun » de Rachid ;
4. un agent Captage, qui a extrait 42 passages des cours de Rachid ;
5. une bibliothèque d'idées de posts, alimentée par les récits de Rachid (6 fiches) ;
6. trois propositions d'illustration, et un montage photo de Rachid en cours sur son Mac.

---

## 2. Accès et identifiants utiles

### Metricool (connecteur disponible dans Claude)
| Marque Metricool | brandId | Réseaux reliés |
|---|---|---|
| XELANC | `7453104` | Facebook (page `136002856268436`), Instagram `@xelanc_finance`, LinkedIn page `urn:li:organization:108065517`, TikTok `xelanc` |
| Financite Institute | `7452435` | LinkedIn page `urn:li:organization:5397256` |
| Page perso Rachid | `7462866` | LinkedIn `urn:li:person:wn057P8sxy`, YouTube `UCbiLMjr-LmYImHPQHRNGx6A` |
| Page perso Adam | `7462895` | LinkedIn `urn:li:person:8QFoolF0V1` |

- Fuseau des marques : `Africa/Casablanca`.
- **Limite importante** : Metricool ne remonte que **8 posts** du profil de Rachid (du 24/08/2025 au 16/10/2026). Ses meilleurs posts (4 000 à 5 000 vues) n'y figurent pas. Pour l'historique, il faut les statistiques natives de LinkedIn : l'export sur 365 jours, et l'archive complète « Obtenir une copie de vos données », qui donne `Shares.csv` (textes sans chiffres).
- Loubna n'est pas connectée à Metricool.

### Higgsfield (génération d'images)
- **Compte de l'application** (connecteur MCP `higg`) : offre Plus, 107 crédits, mais en **période de grâce** (paiement probablement en attente). Il est **bloqué** par la limite quotidienne : « You've reached the daily generation limit for your grace period ».
- **API Higgsfield** (`api.higgsfield.ai`, console `console.higgsfield.ai`, docs `docs.higgsfield.ai`) : Rachid y a acheté des crédits.
  - En-tête : `Authorization: Key ID:SECRET`.
  - La clé est sur le Mac, dans le dossier `~/Travail` (déposée le 08/11) ; ancienne copie dans `~/.higgsfield-api`.
  - **Ne jamais coller la clé dans une conversation.**
- **Photos de référence de Rachid déjà en ligne** (URL publiques, vérifiées le 08/11) :
  - scène de salle de réunion (référence de décor) : `https://d2ol7oe51mr4n9.cloudfront.net/user_3Dt5F1b6h4WNQhDDRiklj2Hat8M/7bca82ff-2781-4829-b2a5-cab5a5ad4016.png`
  - Rachid, veste bleu marine, à une table de marbre : `https://d2ol7oe51mr4n9.cloudfront.net/user_3Dt5F1b6h4WNQhDDRiklj2Hat8M/9954c2b2-a4bf-4f88-ae54-213a7f70df44.png`
  - Rachid, chemise bleue, terrasse : `https://d2ol7oe51mr4n9.cloudfront.net/user_3Dt5F1b6h4WNQhDDRiklj2Hat8M/d440bd72-d5ff-488f-bc84-527e668f3558.png`
  - Rachid, portrait à lunettes, costume : `https://d2ol7oe51mr4n9.cloudfront.net/user_3Dt5F1b6h4WNQhDDRiklj2Hat8M/be212a1f-b062-4a81-9378-d6641bfd116b.png`
  - Rachid a aussi fourni 3 autres photos (jardin, chemise blanche ; selfie à lunettes de soleil ; souriant sous le grenadier), non mises en ligne.

### HeyGen
- La génération d'images demande un forfait payant (refus 402 « plan_upgrade_required »). Non utilisable aujourd'hui.

### Sessions Claude liées
| Session | Où | Rôle | État au 08/11, 16 h 15 |
|---|---|---|---|
| `session_01LXovPVQzkTfW1BySYLtdX7` | cloud | Cette conversation | à clôturer après passation |
| `session_01LXovPULGUUqCE1YVVAJCq6` « Montage Higgsfield Rachid conseiller » | MacBook Air, dossier Travail (`env_01FmKdm1ZZxaHwQDketxELAK`) | Génère le montage de Rachid avec la clé API du dossier Travail | **en attente** : le Mac doit la prendre en charge (Claude ouvert, Remote Control actif sur Travail) |
| `session_01LXovPWTkyCntsaM2Gptu2F` « Agent publicité Meta 2 » | Mac (bridge) | A reçu la même consigne de montage avant la session ci-dessus | déconnectée, message en file. **Doublon** : une fois le montage obtenu, l'ignorer ou lui dire d'abandonner |

Les deux sessions sur le Mac ont pour consigne d'envoyer leur résultat à `session_01LXovPVQzkTfW1BySYLtdX7`. Si cette session est fermée, **aller chercher les images directement dans `~/Travail/linkedin-rachid/visuels/`**.

---

## 3. Diagnostic (chiffres Metricool, août → 8 novembre 2026)

Fichier complet : `excellence/diagnostic-reseaux-organiques-2026-11-08.md`.

| Compte | Abonnés | Portée moyenne par post |
|---|---|---|
| Instagram XELANC | **8** (0 → 8 depuis le 15/10) | Reels ≈ 23 personnes ; carrousels ≈ **3** |
| Facebook XELANC | **33** (4 → 33 depuis le 22/10) | Posts : portée organique remontée à 0 (à vérifier dans Meta Business Suite) ; Reels de 213 à 27 636 vues |
| LinkedIn page XELANC | **56** (40 → 56 depuis le 01/10) | ≈ 55 impressions (de 11 à 260) |
| LinkedIn Financité Institute | 4 157 | ≈ 158 impressions |
| LinkedIn Rachid | 11 491 | ≈ 590 impressions dans Metricool ; aucun post entre le 16/10 et le 08/11 |
| LinkedIn Adam | n.d. | ≈ 470 impressions, ≈ 2 réactions |

Six constats :
1. **Pas de noyau d'audience** : l'algorithme n'a personne sur qui tester les posts.
2. **Facebook achète des vues, pas une audience** : environ 194 000 vues du 22/10 au 06/11, mais environ 29 abonnés gagnés (très probablement la pub « valo2 »).
3. **Le même post partout, et presque toujours une vente** (gabarit identique « Vous êtes X ? Ce guide va… C'est gratuit, lien… »).
4. **Les Reels perdent les gens en 1 à 5 s** (visionnage moyen de 1,2 à 11,3 s).
5. **Deux publics mélangés** : tutoiement des jeunes diplômés, vouvoiement des DAF et banquiers.
6. **Les comptes qui ont une audience se taisent** (Rachid, Financité).

### Les posts « hors du commun » de Rachid (captures LinkedIn fournies par Rachid)
| Post | Âge | Impressions | Réactions | Ce qui le porte |
|---|---|---|---|---|
| « Le travail ne fatigue pas » + « La zone de confort porte très mal son nom » (carte citation RAEL) | 11 mois | 4 659 | 39, 1 commentaire, 3 republications | vérité universelle, phrases courtes, visuel fort |
| « Faire sortir les monstres qui dorment dans une équipe » (visuel Neil Armstrong) | 9 mois | 4 060 (48 % hors réseau, 2 522 membres touchés) | n.d. | leadership, image intrigante. **0 abonné gagné**, 15 visites de profil |
| « Très content pour notre client Grande Banque qui nous confie le reskilling de ses Chargés d'Affaires PME » | ≈ 1 an | 3 794 | 21 | annonce d'une mission réelle, photo réelle, 3 blocs de compétences |

Conclusion :
- les sujets universels font des vues, mais sans question finale, sans lien au métier et sans titre de profil clair, ces vues ne deviennent ni abonnés ni commentaires ;
- l'annonce d'une mission réelle fonctionne même quand elle parle d'une offre.

---

## 4. Stratégie décidée

Fichier : `excellence/strategie-contenu-rachid-adam-loubna-2026-11-08.md`.

- **Trois voix, trois publics** :
  - Rachid : l'autorité (DG, DRH, risques, DAF) ;
  - Adam : le guide carrière (jeunes diplômés, juniors) ;
  - Loubna : la voix du terrain (apprenants, managers, responsables formation ; 30 min par semaine, notes vocales rédigées par l'agent).
- **Rachid : 5 posts par semaine** (décision de Rachid), dont **2 qui citent Excellence/Xelanc** et 3 sans citation.
  - Les posts qui citent : le **récit vécu** est le format principal (une scène vraie, des chiffres, un retournement, la leçon, puis une seule ligne factuelle sur le cours, sans « allez voir »).
  - Rachid peut aussi décider qu'un post ne cite rien : c'est le cas de A1.
- Semaine type proposée :
  - lundi : prise de position hors du commun ;
  - mardi : expertise ou récit + cours ;
  - mercredi : récit vécu ;
  - jeudi : expertise ou récit + autre cours ;
  - vendredi : actualité ou question.
- Règles communes :
  - pas de lien dans le post (lien en premier commentaire) ;
  - première ligne forte ;
  - Adam et Loubna commentent dans les 30 minutes ;
  - 20 minutes d'engagement par jour ;
  - pas de groupes d'engagement ni d'achat de réactions.
- **Photo de Rachid** :
  - signature discrète (petite photo ronde et nom) sur la plupart des visuels ;
  - photo en grand seulement quand il est acteur du récit (environ 1 post sur 4 ou 5) ;
  - pas de retouche excessive ;
  - jamais de posture de « sauveur ».
- À faire côté profil :
  - titre qui dit pourquoi suivre Rachid et qui mentionne XELANC ;
  - page XELANC dans « Sélection ».
- À faire côté audience :
  - email « Suivez-nous » aux bases et relais WhatsApp ;
  - invitations de la page LinkedIn ;
  - bouton « Ajouter à mon profil » sur les certificats.
  - Aucun de ces points n'est encore fait.

---

## 5. LE STYLE DE RACHID : règles apprises (les plus importantes à respecter)

Rachid a rejeté plusieurs versions. Voici ce qu'il exige, tiré de ses retours :

1. **Partir de SES récits et de SES mots.** Il dicte une idée (souvent à la voix, donc avec des fautes de transcription) : on la met au propre sans changer le fond ni l'ordre. Le contenu générique est refusé (« ce contenu générique, c'est pas mon style »). Les passages trouvés dans les cours ont été jugés « pas du tout intéressants » comme base de posts.
2. **Forme de témoignage personnel, en « je ».**
3. **Rester « dans sa hauteur »** : jamais d'aveu de peur ou de fébrilité, ni de posture de héros ou de sauveur. La formation est « l'une de ses activités », pas « son métier ».
4. **Pas de détails techniques** inutiles (DCF, etc.) quand le message est de haut niveau.
5. **Court, percutant, « des gifles l'une après l'autre »**. Mais ce ne sont pas des listes sèches : c'est un **récit qui avance** (énigme, révélation, leçon). L'erreur commise : découper son histoire en listes de phrases courtes.
6. **Ne pas se mettre à dos les banquiers** : nuancer (« certains, pas tous »), montrer leur rôle, rester positif en conclusion.
7. **Ne pas vendre.** Pour citer un cours : une seule phrase factuelle, sans lien ni invitation.
8. Ponctuation signature : les suspensions « .. ».
9. **Signaler chaque phrase ajoutée** qui ne vient pas de lui, et ne jamais inventer de faits, de scènes ou de chiffres.
10. Il apprécie l'honnêteté directe (« tu me dis pas ce que j'ai envie d'entendre »).

Outil proposé, pas encore fait : construire un **guide de voix** à partir de 10 à 15 posts écrits par Rachid (outil installé `brand-voice:generate-guidelines`, puis `brand-voice:enforce-voice`). Il faut que Rachid fournisse ces posts en texte.

---

## 6. Bibliothèque d'idées de posts (le travail en cours)

Fichier : **`excellence/posts/bibliotheque-idees-rachid.md`**. Il contient pour chaque fiche :
- la matière brute de Rachid ;
- la douleur visée, le public, l'objectif ;
- les sources ;
- toutes les versions (la plus récente en premier) ;
- les points à confirmer.

Catégories : A (dirigeants et banquiers), B (la banque vue de l'intérieur, vide), C (coulisses du conseil), D (posture, leadership, carrière), E (finance et IA), F (stratégie, acquisitions et décisions).

| Fiche | Sujet | Statut | Cite Excellence | Reste à faire |
|---|---|---|---|---|
| **A1** | La peur des banquiers | **Deux versions en lice** : « consolidée » (≈ 200 mots, à partir de la dictée de Rachid) et **v10** (texte long apporté par Rachid, resserré à ≈ 230 mots avec questions finales aux dirigeants et aux banquiers) | **Non** (décision de Rachid) | Rachid choisit la version. Illustration : image du bureau vide (recommandée), carte texte, ou montage photo en cours |
| **C1** | La veille de la cession : 80 contre 45 (fonds d'investissement, actifs immobilisés, vente annulée après 15 min) | Brouillon v1 | Option : cours Évaluation d'entreprise | Devise des montants ; 2 phrases ajoutées à valider (« murs et machines », « clients, équipes, savoir-faire pris pour rien ») ; décider de la citation du cours (Rachid a dit qu'il renverrait au cours de valo) |
| **D1** | Entreprendre sans créer d'entreprise | Brouillon v1 | Non | Valider « une innovation qui va plus vite que soi » |
| **D2** | Les limites des dirigeants, le cas Porsche | Brouillon v1, faits sourcés | Non | Valider les ajouts (« preuve que tout se joue au sommet », « ni les ingénieurs ni les ouvriers », la chute) |
| **E1** | L'IA et le capital humain : la demande explose, les compétences manquent | v3, témoignage en hauteur | Non | Valider les ajouts ; Rachid a refusé les versions « j'ai eu peur » et « slogans » |
| **F1** | Manager, c'est prévoir : timing des acquisitions, Vivendi | Brouillon v1 | Option | Nom du « groupe UND » ; source de l'anecdote de l'AG (« Jean-Marie, j'étais ton professeur d'économie… ») ; titre et auteur du livre sur la « myopie des dirigeants » (introuvable sous ce titre) |

### Texte de A1, version « consolidée » (prête)
> On m'a souvent appelé pour accompagner des dirigeants face à leur banque.
> Levées de fonds, restructurations, négociations.
>
> Pendant longtemps, une chose m'a intrigué.
> Beaucoup de ces clients auraient pu le faire seuls.
> Ils avaient des équipes solides, des directeurs financiers compétents.
>
> J'ai fini par comprendre.
> Ce n'était pas la compétence qui leur manquait.
> C'était autre chose. Une chose que personne n'osait pointer.
>
> La peur du banquier.
> De son pouvoir.
> Ce pouvoir qu'il a quand on a besoin de lui.
> Quand on dépend de lui.
> Quand on lui cache quelque chose.
> Quand on ne sait pas comment il pense, ni comment il va réagir.
>
> Ces dirigeants n'avaient pas peur parce qu'ils étaient faibles.
> Ils avaient peur parce qu'ils ne comprenaient pas.
> Et on ne négocie jamais bien avec quelqu'un qu'on ne comprend pas.
>
> Pour être honnête, la peur ne vient pas du banquier.
> Elle vient de ce qu'on ne comprend pas de lui.
>
> Car le banquier, lui aussi, fait du business.
> Il veut accompagner ses clients.
> Il veut les meilleurs dossiers.
> Il ne veut ni contentieux, ni recouvrement.
>
> Quand ces conditions sont réunies, le banquier devient un allié.
> Parfois même.. un ange.
>
> Ce n'est pas sa faute si on le comprend mal.
> Mais certains banquiers, pas tous, gagneraient à casser cette image.

### Texte de A1, version v10 (texte de Rachid, resserré)
> J'ai rencontré des dirigeants qui négociaient des millions avec leurs clients..
> et perdaient leurs moyens face à leur banquier.
>
> Pas des incompétents.
> Des entrepreneurs expérimentés. Des entreprises bien gérées. Des directeurs financiers capables.
>
> Pendant des années, je les ai accompagnés dans leurs levées de fonds, leurs restructurations, leurs négociations bancaires.
> Et une question revenait : pourquoi avaient-ils besoin de moi ?
>
> J'ai fini par comprendre.
> Ce n'était pas un problème de compétence.
> C'était un problème de rapport au pouvoir.
>
> Quand on dépend de sa banque, on ne voit plus un partenaire.
> On voit celui qui peut dire non.
> Exiger des garanties.
> Remettre en cause un projet.
>
> Et quand on ne comprend pas comment il raisonne, ce qu'il cherche, ce qu'il redoute, la négociation est perdue d'avance.
>
> La peur commence souvent là où la compréhension s'arrête.
>
> Pourtant, le banquier aussi fait du business.
> Il a des objectifs, des risques à maîtriser, des décisions à défendre.
> Il préfère financer une entreprise qui réussit que gérer un dossier qui se dégrade.
>
> Comprendre son banquier ne garantit pas un oui.
> Mais on ne subit plus chaque non.
>
> Alors le banquier peut devenir un allié.
> À une condition : que certains sortent aussi de cette posture d'autorité qu'ils entretiennent, parfois sans le savoir.
>
> Dirigeants : avez-vous déjà eu peur de votre banquier ?
> Banquiers : savez-vous le pouvoir que vos clients vous prêtent ?

Le texte long original de Rachid (≈ 380 mots) n'est pas dans le dépôt ; seule la version resserrée l'est. Si Rachid veut repartir de l'original, il doit le recoller.

### Fonctionnement attendu de la bibliothèque
- Rachid dicte une idée.
- On crée une fiche dans la bonne catégorie, avec sa matière brute.
- On rédige selon les règles de la section 5.
- On tient à jour le **tableau de bord** en tête du fichier.

---

## 7. Agent Captage et passages de cours

- **Agent** : `.claude/agents/captage.md` (relançable pour aller jusqu'à environ 100 passages).
- **Bibliothèque** : `excellence/captage/bibliotheque-passages.md`, 42 passages (24 A, 18 B), avec la source exacte, le passage reconstitué, l'idée, le public et l'accroche.
- **Calendrier** : `excellence/captage/calendrier-24-passages.md`, 24 posts sur 12 semaines (mardi et jeudi, à partir du 9-13 novembre).
- **Sources trouvées** :
  - Google Drive : `DCFS4-scripts.html`, `DCFS5-scripts.html`, dossier `FMIA-production` (finance du dirigeant avec l'IA, cas Maison Lumen) ;
  - Descript : 12 transcriptions (valo, AFS, BMC, MLF, ldfs, taxlaws, advs, METIERS, Cercle de Mentorat).
- **Manquent** : les HTML des cours advs, valo, AF, MLF, BMC, LDF, METIERS, taxlaws et Cercle (Rachid dit que tout son contenu est passé par des HTML de narration ; à localiser sur le Mac).
- **Intitulés de cours confirmés** : seulement « Comment évaluer une entreprise par la méthode DCF », « Advisory Accelerator », « Cercle de Mentorat ». Les autres noms sont provisoires.
- **Retour de Rachid** : ces passages ne l'intéressent pas comme base de posts. Ils peuvent servir de matière d'appoint pour la ligne « j'en parle dans mon cours », mais **le format retenu est le récit vécu dicté par Rachid**.

---

## 8. Illustrations

Dossier : `excellence/posts/visuels/`.
| Fichier | Contenu | Statut |
|---|---|---|
| `image-pouvoir-a1.png` | Dirigeant de dos, petite chaise, face à un immense bureau et un fauteuil vide (générée par IA, sans visage) | **Recommandée pour A1** |
| `carte-a1.png` (+ `carte-a1.html`) | Carte texte : « La peur commence là où la compréhension s'arrête » + accroche + signature « RE » | Prête ; remplacer « RE » par la vraie photo de profil |
| `photo-a1.png` (+ `photo-a1.html`) | Maquette : zone pour une photo de Rachid + bandeau « Ce n'était pas un problème de compétence. C'était un rapport au pouvoir. » | Attend une photo |
| Montage Rachid conseiller | Rachid en retrait aux côtés d'un dirigeant, face à la banque | **En cours** sur le Mac (section 2), résultat attendu dans `~/Travail/linkedin-rachid/visuels/` |

Prompt du montage (à réutiliser si besoin) :
```
Photorealistic editorial photo in the style and setting of the first reference image: a long glossy dark wooden boardroom table in a bright room with tall windows, a classical painting on the wall, cold natural light, shallow depth of field. On the right side of the table, a company director in a dark suit faces the bank's team on the left side. Seated just beside the director, slightly behind his shoulder, is the advisor: the man shown in the other reference images (same face, salt-and-pepper beard, receding dark hair, rectangular glasses), wearing a navy blazer and open white shirt, calm and composed, leaning slightly towards the director as if quietly advising him. The director is the main subject; the advisor is clearly recognizable but secondary. Serious, discreet atmosphere of a bank negotiation. Natural skin texture, realistic hands, no text, no logos.
```
Conseils donnés à Rachid :
- une image générée doit être triée (mains, regard) ;
- elle reste une mise en scène, à ne pas présenter comme une photo de mission réelle ;
- pour les récits de missions réelles, une vraie photo est plus forte.

---

## 9. Autres fichiers produits

- `excellence/posts/rachid-lundis-semaines-1-2.md` : 2 posts du lundi (le financier promu puis laissé seul ; le chargé d'affaires coupable désigné). Rachid a rejeté la v1 générique. La v2 est restée **sans retour** : à considérer comme non validée.

---

## 10. Décisions de Rachid (à ne pas remettre en cause)

1. 5 posts par semaine, dont 2 qui citent Excellence.
2. Le récit vécu est le format des posts qui citent un cours.
3. A1 est publié **sans renvoi** à Xelanc ni au cours.
4. Rester en hauteur, nuancer sur les banquiers, conclusion positive.
5. Pas de photo de lui en grand sur A1 (posture de sauveur à éviter) ; présence discrète en général.

---

## 11. Questions ouvertes (à poser à Rachid)

1. **A1** : version « consolidée » ou v10 ? Quelle illustration (image du bureau vide, carte texte, montage) ?
2. **C1** : devise (dirhams ou euros) ? Citer le cours Évaluation d'entreprise (nom exact) ?
3. **F1** : « groupe UND » ? source de l'anecdote de l'AG ? titre et auteur du livre ?
4. **Noms exacts des cours** à citer (Levée de dette bancaire ? Évaluation d'entreprise ? Analyse financière à l'IA ?).
5. **Adam** : rôle réel (« Adam Fonda » apparaît aussi comme identité d'envoi des emails aux banques). Ses posts doivent être signés par une personne réelle.
6. **Loubna** : profil LinkedIn prêt ? connexion à Metricool ?
7. **10 à 15 posts écrits par Rachid** en texte, pour construire son guide de voix.
8. **Abonnement Higgsfield** de l'application à régulariser (période de grâce).
9. Emplacement des **HTML de narration des cours** sur le Mac (pour l'agent Captage).

---

## 12. Prochaines actions recommandées (dans l'ordre)

1. Récupérer le montage photo dans `~/Travail/linkedin-rachid/visuels/` (ou relancer la session « Montage Higgsfield Rachid conseiller »), vérifier la ressemblance, les mains et le cadrage. Fermer la consigne en double envoyée à « Agent publicité Meta 2 ».
2. Faire choisir à Rachid la version et l'illustration de A1, puis publier (lundi ou mardi, 8 h-9 h, heure de Casablanca).
3. Finaliser C1 (premier post qui cite un cours, avec le cours Évaluation d'entreprise).
4. Continuer la bibliothèque à partir des idées dictées par Rachid (catégorie B encore vide).
5. Construire le guide de voix dès que Rachid fournit ses posts.
6. Lancer les actions d'audience : email « Suivez-nous », invitations de la page, titre de profil, bouton certificats.
7. Mesurer chaque post 7 jours après :
   - impressions, part hors réseau ;
   - commentaires, visites de profil, abonnés gagnés ;
   - pour les posts qui citent un cours, visites de la page du cours dans GA4.

---

## 13. Message de reprise à coller dans la nouvelle conversation

```
Je reprends le travail sur ma stratégie LinkedIn et mes posts. Lis d'abord
excellence/passation-reseaux-sociaux-2026-11-08.md, puis
excellence/posts/bibliotheque-idees-rachid.md,
excellence/strategie-contenu-rachid-adam-loubna-2026-11-08.md et
excellence/diagnostic-reseaux-organiques-2026-11-08.md (branche claude/amazing-thompson-r7gb78).
Respecte strictement les règles de style de la section 5 de la passation.
Commence par vérifier si le montage photo est arrivé dans ~/Travail/linkedin-rachid/visuels/,
puis dis-moi où on en est sur A1 et les questions ouvertes de la section 11.
```
