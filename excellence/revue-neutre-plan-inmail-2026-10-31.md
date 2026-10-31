# Revue neutre du plan InMail (Message Ads LinkedIn) de Xelanc · 31/10/2026

Revue indépendante et sceptique, menée par recherche web (WebSearch, Firecrawl) à partir du seul brief `brief-revue-neutre-perplexity-2026-10-31.md`. Aucun autre document du projet n'a été lu.

Échelle de confiance : **élevée** (source primaire LinkedIn, ou plusieurs sources indépendantes concordantes) · **moyenne** (une source sérieuse, ou des sources secondaires qui concordent) · **faible** (blog d'agence ou de vendeur, sans méthode, ou une seule source).

Conversions : 1 € = 655,957 FCFA ; 1 $ ≈ 0,92 € (ordre de grandeur).

---

## Synthèse en 6 lignes

1. Le chiffre de **7-10 % d'achat par envoi n'est documenté nulle part**. Il est même mécaniquement impossible : les taux de **clic** observés par envoi sont de 0,3 à 3 %, et on ne peut pas acheter plus qu'on ne clique.
2. L'estimation dite « prudente » de l'équipe (0,5-1 % à froid) est elle aussi **trop optimiste**. Je retiens **0,02-0,2 % à froid** (centre ≈ 0,05-0,1 %) et **0,2-1,5 % sur une liste chaude** (jusqu'à ≈ 3 % au mieux, par les canaux propres du fondateur).
3. Au coût de 0,35-0,90 € par envoi, le **point mort est à ≈ 0,12-0,30 % d'achat par envoi**. À froid, le plan a donc toutes les chances de **perdre de l'argent**.
4. La mécanique « 50 envois par jour, puis 50 % de l'encaissé réinjecté » **ne peut pas monter en charge** sous ≈ 0,3-0,6 % d'achat par envoi. Au rythme réaliste, on reste à quelques centaines d'envois par mois, pas 100 000.
5. **100 000 envois en 30 jours** se heurtent au plafond de fréquence (≈ 1 message par membre tous les 45 jours), à la délivrance limitée aux membres actifs, et à des audiences finance probablement bien plus petites que prévu.
6. **Les audiences LinkedIn globales sont confirmées, voire dépassées** (≈ 18 M de membres sur 7 des pays seulement). En revanche, je n'ai trouvé aucune donnée publique sur la fonction finance.

---

## Q1. Taux réels observés des Message Ads / Sponsored Messaging

### 1.1 Statut du produit (préalable)

| Constat | Source | Confiance |
|---|---|---|
| LinkedIn a annoncé en 2023 l'arrêt des Message Ads : plus de nouvelles campagnes à partir du 19/06/2023, fin de diffusion au 31/07/2023, bascule vers les Conversation Ads. | storykit.io, vixendigital.com, carnegiehighered.com, doc API Microsoft 2023 | élevée (sur l'annonce) |
| Le changelog officiel de l'API LinkedIn traite pourtant encore des **Message Ads** en 2024-2026 : ciblage UE rouvert en octobre 2024 pour les Message Ads et les Conversation Ads ; bouton « Not Interested » ajouté automatiquement aux Message Ads en juin 2026 ; `creativeSelection = OPTIMIZED` par défaut en juillet 2026 pour les `SPONSORED_INMAILS` (Message Ads et Conversation Ads). Le format existe donc bien en 2026. | learn.microsoft.com, Recent Marketing API Changes (vue li-lms-2026-08) | moyenne-élevée |
| **Nouveau en juin 2026 : un bouton « Not Interested » s'affiche sur chaque Message Ad.** On peut s'attendre à une baisse de la délivrance future auprès des membres qui cliquent dessus. | idem ; aide LinkedIn 71201 (« Not Interested » réduit la fréquence) | moyenne |

**À vérifier dans Campaign Manager** : que le format « Message Ad » (un seul CTA) est bien proposé pour vos comptes et vos pays. À défaut, le format sera une Conversation Ad, avec au moins deux boutons.

### 1.2 Ouverture, clic, conversion

| Indicateur | Chiffre | Nature de la source | Source | Confiance |
|---|---|---|---|---|
| Ouverture moyenne | ≈ 50 % (chiffre LinkedIn) | **LinkedIn** | cité par Search Engine Land, 10/10/2024 | moyenne (chiffre auto-déclaré) |
| Ouverture | 56,7 % sur un client de services financiers | praticien, 1 client | Search Engine Land, 10/10/2024 | faible |
| Ouverture | ≈ 30 % ; clic ≈ 3 % ; 0,50-1,00 $ par envoi (ABM) | vendeur ABM | zenabm.com, 03/2026 | faible |
| Ouverture | 47-48 % ; clic 1,7-3,2 % **sur les ouvertures** ; **≈ 0,28 % de clic par envoi** (48 % × 1,7 %) | compilations d'agences | résultats agrégés : nav43.com, b2linked.com, theb2bhouse.com, speedworksocial | faible |
| Ouverture 25-45 % ; CTR 2-5 % | deck d'un vendeur | slideshare | faible |
| Ouverture 35-65 % (Conversation Ads, Afrique francophone) ; taux de remplissage de formulaire 8-22 % | agence, 28 comptes SN/CI/CM, 95 M FCFA dépensés de janvier à mai 2026 | kolonell.com, 02/06/2026 | faible-moyenne (seule donnée régionale trouvée) |
| Cas éducation : ESSCA, ouverture 66 %, CTR 3,5 % ; Duke, ouverture 68 % | **LinkedIn (études de cas)** | business.linkedin.com | faible (cas sélectionnés par LinkedIn) |
| Cas éducation : OBS (école en ligne), CTR 1,96 % ; « conversion en inscription 4 % » (lead → inscription, tous formats confondus, pas par envoi) | **LinkedIn (étude de cas)** | business.linkedin.com, obs-case-study-ES-2023 | faible |
| Remplissage du Lead Gen Form ≈ 13 % (LinkedIn), 10-15 % (tiers) | LinkedIn et tiers | yougov.com, click-vision.com | moyenne |
| Coût par lead des Conversation Ads avec formulaire : 362 $ (51 annonceurs B2B, 2025) ; 98 $ selon une autre agence | benchmark indépendant / agence | metadata.io (rapport 2026), singlegrain.com | moyenne / faible |
| Coût par envoi « composite » ≈ 0,81 $, CPL ≈ 118 $ | compilation | résultats agrégés (2026) | faible |

**Lecture.**
- Le repère retenu par l'équipe (≈ 45 % d'ouverture, ≈ 3 % de clics) est **cohérent avec la fourchette publiée**, à une condition : bien distinguer clic **par ouverture** et clic **par envoi**. Si les 3 % sont rapportés aux ouvertures, cela fait ≈ 1,3-1,5 % de clics par envoi.
- Plusieurs sources le reconnaissent : il n'existe aucun jeu de données public et indépendant sur les Message Ads.
- **Je n'ai trouvé aucune donnée publique d'achat par envoi** pour une formation à 200-500 €. Les cas éducation publiés mesurent des leads, pas des ventes.

### 1.3 Ordre de grandeur reconstitué (estimation de l'auteur)

Envoi → ouverture 35-55 % → clic 2-5 % des ouvertures (≈ 0,7-2,7 % des envois) → achat direct à 299 € sans essai, trafic froid : 1-5 % des clics. Ce dernier taux s'appuie sur les références « page de vente » : 0,1-0,8 % du trafic social payant froid, ≈ 2,5 % de la page de destination au paiement pour un cours à 297 $ (webtonic.io, novapixeldev.com, learnybox.com ; confiance faible).

**Résultat : ≈ 0,01-0,15 % d'achat par envoi à froid.** Confiance moyenne sur l'ordre de grandeur, faible sur la valeur exacte.

---

## Q2. Un taux d'achat de 7 à 10 % par envoi est-il documenté ?

- **Non. Je n'ai trouvé aucune source**, ni LinkedIn ni tierce, qui rapporte 7-10 % d'achat par envoi. Confiance élevée sur l'absence, car des recherches ciblées n'ont rien donné.
- **Argument mécanique.** Toutes les sources placent le clic **par envoi** entre ≈ 0,3 % et ≈ 3 %, et entre 8 et 10 % seulement chez les meilleurs, et encore **par ouverture**. L'achat se fait sur le site, donc après un clic. **Le taux d'achat par envoi ne peut pas dépasser le taux de clic par envoi.** Atteindre 7-10 % exigerait que 100 % des cliqueurs achètent, sur un clic lui-même 3 à 10 fois supérieur aux meilleurs chiffres observés.
- **Dans quelles conditions approche-t-on de tels taux ?** Uniquement hors publicité payante : relance personnelle « un à un » de clients existants, renouvellement d'abonnement d'anciens élèves, ou vente à des personnes qui ont déjà demandé l'offre (liste d'attente, participants à un webinaire avec date limite). Repère : les e-mails de **campagne** e-commerce donnent ≈ **0,16 % de commandes par destinataire**, et les e-mails **automatisés déclenchés par un comportement** ≈ 2,1 % (4,3 % pour le top 10 %), selon le benchmark Klaviyo 2026 cité par eightx.co et branvas.com (confiance moyenne). Même sur des listes « chaudes » et à petit prix, 7-10 % est hors norme.
- L'estimation « prudente » de l'équipe (0,5-1 % à froid) suppose que 20 à 70 % des cliqueurs achètent un abonnement de 299 € sans essai. **Elle est aussi contredite** par les ordres de grandeur ci-dessus.

---

## Q3. Audiences LinkedIn et coût des envois dans ces pays

### 3.1 Membres LinkedIn (audience adressable publicitaire, NapoleonCat)

| Pays | Membres | Date | % population | Source | Confiance |
|---|---|---|---|---|---|
| Maroc | 7 881 000 | 09/2026 | 19,9 % | napoleoncat.com/stats/linkedin-users-in-morocco | moyenne-élevée |
| Tunisie | 3 082 000 | 09/2026 | 24,4 % | napoleoncat.com/stats/linkedin-users-in-tunisia | moyenne-élevée |
| Côte d'Ivoire | 2 081 000 | 09/2026 | 6,8 % | napoleoncat.com/stats/linkedin-users-in-cote-divoire | moyenne-élevée |
| Sénégal | 1 699 000 | 09/2026 | 8,5 % | napoleoncat.com/stats/linkedin-users-in-senegal | moyenne-élevée |
| Cameroun | 1 605 000 | 10/2025 | n. d. | stats.napoleoncat.com/linkedin-users-in-cameroon/2025/10 | moyenne |
| RDC | 1 209 000 | 09/2026 | 1,1 % | napoleoncat.com/stats/linkedin-users-in-dr-congo | moyenne-élevée |
| Congo-Brazzaville | 336 500 | 09/2026 | 5,1 % | napoleoncat.com/stats/linkedin-users-in-congo | moyenne-élevée |
| **Sous-total (7 pays)** | **≈ 17,9 M** | | | | |
| Bénin, Burkina, Mali, Togo, Guinée, Gabon | non recherchés en détail | | | | **donnée non trouvée** |

- NapoleonCat agrège des données du gestionnaire de publicités. Ce sont des **comptes adressables, pas des personnes actives**.
- Structure d'âge au Maroc : 18-24 ans 35,5 %, 25-34 ans 49,5 %, **35-54 ans seulement 14 %**. Les profils de DAF et de dirigeants (souvent 35 ans et plus) sont donc une **petite minorité**. Le schéma est similaire au Sénégal, en Tunisie et en RDC, où les 25-34 ans pèsent 46-49 %.
- **Utilisateurs actifs mensuels** selon kolonell.com (06/2026, données non sourcées, confiance faible) : Côte d'Ivoire 920 k, Sénégal 580 k, Cameroun 480 k, Mali 145 k, Gabon 180 k, Burkina 125 k, Bénin 95 k. Cela représente ≈ 30-45 % des comptes NapoleonCat, cohérent avec l'hypothèse de 20-30 % ou un peu au-dessus. Même source, **« audience séniorité » (toutes fonctions)** : Côte d'Ivoire 145 k, Sénégal 95 k, Cameroun 78 k, Gabon 32 k, Mali 24 k, Burkina 22 k, Bénin 18 k.
- **Part de la fonction finance/comptabilité et des dirigeants de PME : aucune donnée publique trouvée.** Seul le prévisionnel d'audience de Campaign Manager peut la donner, par fonction × séniorité × pays. Raisonnement (estimation de l'auteur, confiance faible) : si la finance représente 5 à 10 % de l'« audience séniorité », on obtient ≈ 7-15 k en Côte d'Ivoire, 5-10 k au Sénégal et 4-8 k au Cameroun. Le total de l'hypothèse 1 (120-240 k financiers confirmés) **n'est pas incompatible**, mais il repose sans doute surtout sur le Maroc et la Tunisie, et le nombre de membres **actifs et joignables par Message Ad sur 30 jours** sera bien plus faible.
- Hypothèse 2 (nombre d'entreprises formelles) : **non vérifiée** dans le cadre de cette revue, car elle ne fait pas partie des 6 questions.

### 3.2 Coût par envoi

| Chiffre | Zone | Source | Confiance |
|---|---|---|---|
| 220-580 FCFA par envoi (≈ 0,34-0,88 €) pour les Conversation Ads ; « InMails » 1 000-3 000 FCFA par message (≈ 1,5-4,6 €, formulation ambiguë) | SN/CI/CM | kolonell.com, 06/2026 | faible |
| CPM 12 000-38 000 FCFA selon le pays (Cameroun le moins cher, Gabon le plus cher) | Afrique francophone | kolonell.com | faible |
| 0,20-0,80 $ ; 0,26-0,50 $ ; 0,30-1,00 $ ; ≈ 0,80 $ en moyenne | mondial | compilations : webfx, zapier, hawksem, connectsafely… | faible |
| « Afrique et Amérique du Sud : CPC à partir de 2 $ » | régional | blog, sans méthode | faible |
| **Aucune donnée de coût par envoi trouvée pour le Maroc ou la Tunisie** | — | — | **donnée non trouvée** |

**Verdict sur l'hypothèse 3 (0,30-0,70 $ par envoi)** : elle est **plausible** et cohérente avec la seule source régionale, mais **non vérifiée**. Il faut planifier à **0,35-0,90 €** et prendre le prévisionnel de Campaign Manager comme vérité.

### 3.3 Frein au paiement (côté annonceur et côté acheteur)

- Maroc : les cartes bancaires locales sont souvent refusées pour payer LinkedIn Ads (contrôle des changes, blocages par BIN, plafonds de dotation à l'international). Source : spendfigo.com, un vendeur intéressé, confiance faible-moyenne. **Le même frein s'applique à vos acheteurs** s'ils paient 299 € par carte en devise.
- Côte d'Ivoire : inclusion financière 51-58 % (Findex 2025, cité par economie-ivoirienne.ci) et plus de 26 M de comptes de mobile money (ARTCI, fin 2024), confiance moyenne. **Le paiement par mobile money est indispensable** dans la zone UEMOA.

---

## Q4. Limites de délivrance

| Limite | Détail | Source | Confiance |
|---|---|---|---|
| **Fréquence** | « Un même membre ne reçoit la même Message Ad qu'une fois tous les 45 jours » (guide LinkedIn). Des tiers affirment que le plafond vaut **tous annonceurs confondus** (≈ 1 Sponsored Message tous les 45 jours par membre), ou par annonceur selon les sources. L'aide officielle reste vague : LinkedIn « limite la fréquence ». | guide LinkedIn « Getting Started Message Ads » (cité), linkedin.com/help/lms/answer/71201, zenabm.com, connectsafely.ai | élevée sur l'existence d'un plafond ; **moyenne-faible sur son périmètre exact** |
| **Délivrance** | Les messages ne partent **que lorsque le membre est actif** sur LinkedIn. Un message plus récent fait basculer le précédent dans « Archivés ». Un clic sur « Not Interested » réduit la diffusion. | aide LinkedIn 71201 | élevée |
| **Langue** | Le ciblage par langue suit la **langue du profil** : il faut une campagne par langue (FR, EN, AR). Beaucoup de cadres marocains et tunisiens ont un profil en anglais. | aide LinkedIn 71201 | élevée |
| **Pays** | Aucune restriction trouvée pour les 13 pays visés. Les restrictions documentées concernent l'UE, l'EEE et la Suisse (consentement), les mineurs, et les pays sous sanctions. Des Conversation Ads sont effectivement diffusées en SN/CI/CM (kolonell). | aide LinkedIn 71201, changelog API, kolonell.com | moyenne |
| **Budget minimum** | 10 $ par jour et par campagne ; enchère minimale de 2 $ en CPC/CPM ; **pas de plancher publié pour le coût par envoi** (l'enchère se fait par envoi). | webfx, zapier et autres (concordants) | moyenne-élevée |
| **Audience** | Au moins 300 membres par ciblage. LinkedIn **recommande ≈ 300 000** pour le Sponsored Messaging (50-300 k selon les sources). | linkedin.com/help/lms/answer/a423690 ; marketingprofs | élevée |
| **Gros volumes** | **Aucun quota quotidien publié.** En pratique, le volume de 30 jours est borné par : (nombre de membres de l'audience) × (part active pendant la période) × (part non saturée par d'autres annonceurs) × (taux de victoire aux enchères). | déduction | moyenne |

**Conséquence pour le plan** : avec un plafond d'un message tous les 45 jours, **100 000 envois en 30 jours exigent au moins 100 000 membres distincts, actifs et non saturés** dans l'audience ciblée. Sur la cible finance et dirigeants hors Maroc et Tunisie, c'est **très improbable**. On l'atteindra seulement en élargissant le ciblage (fonctions ou séniorités voisines, ou tout le Maroc et la Tunisie), ce qui dégradera la conversion.

---

## Q5. Risques principaux et ce que je ferais différemment

### 5.1 Risques chiffrés

1. **Économie unitaire négative à froid** (risque principal). Point mort = coût par envoi ÷ 299 €. À 0,35 €, il faut 0,12 % d'achat par envoi ; à 0,60 €, 0,20 % ; à 0,90 €, 0,30 %. Or mon estimation à froid est de 0,02-0,2 %.
   Exemple sur 100 000 envois à 0,60 € = **60 000 € dépensés** :
   - à 0,05 % : 50 ventes = 15 k€, soit **−45 k€** ;
   - à 0,1 % : 100 ventes = 30 k€, soit **−30 k€** ;
   - à 0,2 % : 200 ventes = 60 k€, soit l'équilibre.
   Par contraste, à 7 % : 7 000 ventes, soit 2,1 M€. **Cet écart de facteur 35 à 140 est le cœur du problème.**
2. **La réinjection ne décolle pas.** Le volume hebdomadaire suivant se calcule ainsi : V × taux × 299 € × 50 % ÷ coût par envoi. La croissance n'est positive que si le taux dépasse **2 × coût par envoi ÷ 299 ≈ 0,23-0,60 %**. Exemple : à 0,1 % et 0,60 € par envoi, la semaine 1 compte 350 envois (210 €) et rapporte 0,35 vente, soit ≈ 105 € encaissés. On réinjecte 52 €, soit ≈ 87 envois. **Le volume s'effondre.** Le plan n'atteint jamais 100 000 envois. Il atteint quelques centaines.
3. **Aucun signal statistique au démarrage.** À 50 envois par jour et 0,1 %, on attend 1,5 vente par mois. Zéro vente en 2 semaines ne prouve rien, et 2 ventes non plus. On ne peut pas piloter.
4. **Plafond de fréquence et audience** (Q4) : volume impossible à tenir sur la cible exacte, et on « brûle » chaque membre pour 45 jours avec un message de vente sèche. Le nouveau bouton « Not Interested » (juin 2026) peut aussi pénaliser la diffusion future.
5. **Proposition de vente directe sans essai à 299 €** dans un message non sollicité. Les praticiens déconseillent la vente directe sur trafic froid (novapixeldev, learnybox). Prix relatif : CFI est à **497 $ par an** en autoformation, 847 $ en « Full-Immersion », et 399-497 $ par licence en offre équipe (corporatefinanceinstitute.com). Pour un comptable de Douala ou d'Abidjan, 299 € pèse **bien plus** en pouvoir d'achat que 497 $ pour un analyste nord-américain.
6. **Friction de paiement** : cartes marocaines limitées à l'international, mobile money dominant en UEMOA. Sans CMI au Maroc ni Wave / Orange Money / MTN MoMo, une part des intentions d'achat sera perdue au moment du paiement.
7. **Mesure** : l'attribution du clic sur la Message Ad à l'achat sur le site exige l'Insight Tag et des UTM. Sinon, le chiffre d'achat par envoi sera inobservable.
8. **Profils linguistiques** : une campagne en français ne touche pas les profils en anglais au Maroc et en Tunisie.

### 5.2 Ce que je ferais à la place (concret)

1. **Test borné avant tout plan** : **3 000 à 5 000 envois** (≈ 1 500-4 500 €) répartis en 3 segments, par exemple (a) finance Maroc et Tunisie, (b) finance UEMOA et CEMAC, (c) dirigeants de PME, avec 2 messages par segment. Durée : 2-3 semaines.
2. **Changer l'appel à l'action** : pas d'achat direct. Proposer un **aimant à leads** à forte valeur (modèle Excel SYSCOHADA ou CGNC, webinaire avec le fondateur, cas africain), via un **Lead Gen Form** natif, puis relancer par e-mail et WhatsApp pendant 7-14 jours vers l'achat. Ajouter un essai de 7 jours ou une garantie « satisfait ou remboursé », et une offre fondateur limitée dans le temps.
3. **Critères d'arrêt ou de poursuite après le test** :
   - clic par envoi ≥ 1,5 % ;
   - coût par lead ≤ 15-25 € ;
   - lead → achat sous 30 jours ≥ 3-5 % ;
   - autrement dit, achat attribué par envoi ≥ 0,25 % (point mort à 0,60 € par envoi).
   Sous 0,1 % : arrêt des Message Ads froides.
4. **Commencer par le chaud** : mailing et WhatsApp personnels du fondateur vers les **anciens élèves de Financité** (30 ans de formation), puis audiences « matched » (liste d'e-mails importée) dans LinkedIn, puis reciblage des visiteurs du site. C'est là qu'on peut espérer 1-3 %.
5. **Vente aux entreprises** : une seule vente à un DAF pour 10 licences vaut 10 ventes individuelles. LinkedIn sert d'abord à ouvrir des conversations avec les décideurs (prise de rendez-vous), pas à vendre l'abonnement à l'unité.
6. **Budget de 30 jours plafonné** à 5-10 k€, et non indexé sur une réinjection qui, à ces taux, s'éteint d'elle-même. Mise à l'échelle seulement après validation des critères ci-dessus.
7. **Moyens de paiement locaux** opérationnels avant l'envoi, et **campagnes séparées par langue** (FR / EN).

---

## Q6. Concurrents et équivalents : chiffres publiés

| Acteur | Données | Source | Confiance |
|---|---|---|---|
| CFI (Corporate Finance Institute) | Autoformation 497 $ par an, Full-Immersion 847 $ par an, facturation annuelle uniquement ; équipes 399-497 $ par licence et par an ; « 1 M+ étudiants » ou « 3 M+ professionnels » (chiffres auto-déclarés et incohérents entre eux) ; **aucun chiffre de conversion ni de chiffre d'affaires publié** | corporatefinanceinstitute.com/subscription-pricing ; help.corporatefinanceinstitute.com | élevée (prix), faible (volumes) |
| Wall Street Prep | Premium ≈ 499 $ en achat unique, bundles à 799 $ et plus ; coaching 340-400 $ de l'heure ; **aucun chiffre de conversion publié** | onlinecourseing.com (affilié), benzinga.com | moyenne (prix) |
| Formation SYSCOHADA en Afrique | Pas de plateforme sur abonnement repérée. Offres ponctuelles : 20 000 FCFA (≈ 30 €) en ligne au Cameroun, 110 000-120 000 FCFA (≈ 170-185 €) au Togo, jusqu'à 500 000 FCFA (≈ 760 €) pour une certification au Tchad. Vente fréquente par Zoom ou WhatsApp. | ohada.com, emploitogo.info, cameroondesks.com, lesopportunites.com | moyenne |
| Écosystème EdTech UEMOA | 73 startups EdTech recensées, ≈ 80 % en Côte d'Ivoire et au Sénégal (étude Etudesk / Fondation Mastercard) ; aucun chiffre d'abonnés ni de conversion | cio-mag.com | moyenne |
| Maroc | Smartprof for Business se positionne en formation professionnelle en ligne ; le B2B est jugé le segment le plus ouvert à l'EdTech | lavieeco.com, teamfrance-export.fr | faible-moyenne |
| **Taux de conversion LinkedIn → achat de formation en Afrique** | **Aucune donnée publique trouvée** | — | — |

**Lecture.**
- Le créneau « abonnement façon CFI, en français, normes SYSCOHADA et CGNC » semble **peu occupé**. C'est un atout de positionnement.
- Mais le marché de référence vend souvent **moins cher et à la séance**. Le prix de 299 € par an est à **tester**, pas à présumer, surtout en zone UEMOA et CEMAC.

---

## Verdict final

| Hypothèse | Verdict |
|---|---|
| H1 · ≈ 16 M de membres LinkedIn dans les 13 pays | **Soutenue, probablement prudente** : ≈ 17,9 M sur 7 pays seulement (NapoleonCat). Les sous-audiences finance (120-240 k) et dirigeants (160-320 k) sont **invérifiables publiquement**, à contrôler dans Campaign Manager. Actifs mensuels : 20-30 % est plausible, une source régionale (faible) indique 30-45 %. |
| H2 · Nombre d'entreprises formelles | **Non testée** dans cette revue. |
| H3 · 0,30-0,70 $ par envoi | **Plausible** (une source régionale à ≈ 0,34-0,88 €). Non vérifiée pour le Maroc et la Tunisie. **Testable seulement en réel.** |
| H4a · Le fondateur vise 7-10 % d'achat par envoi | **Contredite** : aucune trace documentaire, et supérieure aux taux de **clic** observés. |
| H4b · L'équipe estime 0,5-1 % à froid | **Contredite (trop haute)** : la fourchette étayée est de 0,02-0,2 %. |
| H4c · 1-3 % sur une liste chaude | **Plausible seulement en haut de fourchette**, via les canaux propres du fondateur (e-mail ou WhatsApp vers les anciens élèves). Par Message Ad sur une audience importée, plutôt 0,2-1 %. **À tester.** |
| H5 · 100 000 envois en 30 jours avec réinjection de 50 % | **Contredite** : plafond de fréquence de 45 jours et délivrance aux seuls actifs (volume) ; réinjection qui s'éteint sous ≈ 0,25-0,6 % d'achat par envoi (économie). |
| H6 · ≈ 45 % d'ouverture, ≈ 3 % de clics | **Soutenue sur l'ouverture** (30-60 % publiés). Clics : les **3 % s'entendent par ouverture** dans la plupart des sources, soit ≈ 1-1,5 % par envoi. |

**Fourchette réaliste du taux d'achat par envoi (abonnement à 299 €, sans essai)**
- **(a) Audience froide, Message Ad avec CTA d'achat direct : 0,02-0,2 %, valeur centrale ≈ 0,05-0,1 %.** Soit 20 à 200 ventes pour 100 000 envois.
- **(b) Liste chaude qui connaît le fondateur : 0,2-1,5 %** par Message Ad ou e-mail de campagne. **Jusqu'à ≈ 3 %** pour des anciens élèves engagés, sollicités personnellement par le fondateur, avec offre limitée dans le temps et paiement local.

Ce qui reste **non testable sans essai réel** : le coût par envoi effectif par pays, la taille de l'audience finance active et joignable, le taux de clic sur vos messages, et la conversion clic → achat à 299 €. Le test de 3 000-5 000 envois décrit en Q5 suffit à trancher.

---

## Sources

**LinkedIn (sources primaires ou auto-déclarées)**
- Aide LinkedIn, Sponsored Messaging : https://www.linkedin.com/help/lms/answer/71201
- Aide LinkedIn, taille d'audience : https://www.linkedin.com/help/lms/answer/a423690
- Aide LinkedIn, Conversation ads : https://www.linkedin.com/help/lms/answer/104116
- Guide LinkedIn Message Ads (PDF) : https://business.linkedin.com/content/dam/me/business/en-us/marketing-solutions/resources/pdfs/Getting-Started-Guide-LinkedIn-Message-Ads-01.pdf
- Changelog de l'API Marketing LinkedIn (2024-2026) : https://learn.microsoft.com/en-us/linkedin/marketing/integrations/recent-changes?view=li-lms-2026-08
- Marketing API Changes 2023 : https://learn.microsoft.com/en-us/linkedin/marketing/integrations/archived-recent-changes/2023/marketing-api-changes?view=li-lms-2026-02
- Bonnes pratiques Sponsored Messaging : https://business.linkedin.com/marketing-solutions/cx/21/10/best-practices-m/sponsored-messaging-tips
- Étude de cas Duke : https://business.linkedin.com/marketing-solutions/blog/d/duke-university-sees-a-400-increase-in-conversions-using-linkedin-sponsored-inmail
- Étude de cas OBS : https://business.LinkedIn.com/content/dam/me/business/en-us/marketing-solutions/case-studies/pdfs/obs-case-study-ES-2023.pdf
- Étude de cas ESSCA : https://business.linkedin.com/content/dam/me/business/fr-fr/marketing-solutions/case-studies/pdfs/ESSCA_CS_VF.pdf

**Benchmarks tiers**
- Search Engine Land (10/10/2024) : https://searchengineland.com/linkedin-message-ads-447380
- ZenABM (03/2026) : https://zenabm.com/blog/linkedin-message-ads
- nav43 : https://nav43.com/blog/linkedin-conversation-ads-benchmarks-the-complete-2025-guide-to-costs-high-converting-flows/
- b2linked : https://b2linked.com/blog/linkedin-ad-benchmarks/ ; https://b2linked.com/blog-page/linkedin-ads-frequency-caps-how-often-can-someone-see-your-ads
- The B2B House : https://www.theb2bhouse.com/linkedin-ad-benchmarks/
- connectsafely : https://connectsafely.ai/articles/linkedin-sponsored-messages-guide-2026
- metadata.io benchmark : https://metadata.io/benchmark-report-2026/insights/forms-beat-pages
- Singlegrain : https://www.singlegrain.com/lead-generation/linkedin-conversation-ads-strategy/
- click-vision : https://click-vision.com/linkedin-lead-generation-statistics
- Statut des Message Ads en 2023 : https://storykit.io/blog/linkedin-message-ads ; https://www.vixendigital.com/linkedin/saying-goodbye-to-linkedin-message-ads/ ; https://www.carnegiehighered.com/changes-to-linkedin-sponsored-messaging/
- Coûts : https://www.webfx.com/blog/marketing/linkedin-advertising-cost/ ; https://zapier.com/blog/linkedin-advertising-costs/ ; https://hawksem.com/blog/linkedin-ads-cost/

**Afrique et Maghreb**
- NapoleonCat : https://napoleoncat.com/stats/linkedin-users-in-morocco/ ; https://napoleoncat.com/stats/linkedin-users-in-tunisia/ ; https://napoleoncat.com/stats/linkedin-users-in-cote-divoire/ ; https://napoleoncat.com/stats/linkedin-users-in-senegal/ ; https://stats.napoleoncat.com/linkedin-users-in-cameroon/2025/10/ ; https://napoleoncat.com/stats/linkedin-users-in-dr-congo/ ; https://napoleoncat.com/stats/linkedin-users-in-congo/
- Kolonell, LinkedIn Ads B2B en Afrique francophone (06/2026) : https://kolonell.com/en/blog/linkedin-ads-b2b-francophone-africa-strategy-2026
- Spendfigo, paiement LinkedIn Ads au Maroc : https://spendfigo.com/guides/linkedin-ads/morocco
- Inclusion financière en Côte d'Ivoire : https://economie-ivoirienne.ci/index.php/banques-et-finances/indicateurs-inclusion-financiere.html ; https://www.capmad.com/article/uemoa-la-cote-divoire-devient-premier-marche-du-mobile-money-devant-le-senegal
- Etudesk, EdTech en UEMOA : https://cio-mag.com/education-la-startup-ivoirienne-etudesk-propose-des-mesures-pour-faire-bouger-lecosysteme-edtech-dans-luemoa/
- Formations SYSCOHADA : https://www.ohada.com/actualite/8225/formation-en-ligne-sur-la-comptabilite-ohada-le-05-avril-2026.html ; https://www.emploitogo.info/formation-en-comptabilite-pratique-lieu-lome/ ; https://www.cameroondesks.com/2021/11/formation-en-ligne-en-comptabilite-generale.html ; https://www.lesopportunites.com/opportunite/afrique/formation/achat-transport/etablir-et-presenter-les-etats-financiers-selon-les-normes-syscohada-revise-ndjamena-tchad/
- EdTech au Maroc : https://www.lavieeco.com/affaires/les-10-start-up-qui-boostent-lunivers-de-leducation-1-3/ ; https://www.teamfrance-export.fr/fiche-marche/tech-et-services/education-et-edtech/MA

**Comparables et conversion e-learning / e-mail**
- Prix CFI : https://corporatefinanceinstitute.com/subscription-pricing/ ; https://help.corporatefinanceinstitute.com/article/1083-pricing-packaging
- Wall Street Prep : https://onlinecourseing.com/wall-street-prep-review/ ; https://benzinga.com/money/wall-street-prep-review
- Conversion des cours en ligne : https://www.webtonic.io/blog/education-coaching-landing-page-statistics ; https://novapixeldev.com/blog/why-course-ads-get-clicks-but-no-enrollments ; https://learnybox.com/blog/paid-ads-for-online-courses/
- Benchmarks e-mail Klaviyo : https://eightx.co/blog/average-ecommerce-email-revenue-share-by-vertical-2026 ; https://branvas.com/blogs/news/ecommerce-email-marketing-benchmarks ; https://www.inboxally.com/blog/klaviyo-email-benchmarks
