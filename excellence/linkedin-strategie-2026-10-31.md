# Point LinkedIn Ads : stratégie Excellence, 31 octobre 2026

Agent LinkedIn Ads, mode lecture seule. Aucune campagne créée, modifiée ni mise en pause.
Étiquettes : [M] mesuré, [E] estimé (source citée), [H] hypothèse. Dates en 2026.

## Verdict

LinkedIn ne sera pas ton canal de volume pour les particuliers. À 3-8 € le clic [E], il faut 50 à 270 € pour obtenir un compte gratuit [E/H], contre environ 5 $ sur Meta (pub valo2) [M 27/10]. Il peut en revanche ouvrir le payeur employeur : RAF, DAF, directeurs de formation, banques, avec des places Équipes à 249 € la place [M /equipes/ 31/10]. Une seule vente Équipes de 5 places (1 245 €) pèse plus que tout ce que le test peut rapporter en abonnements individuels.

Aujourd'hui, on ne peut pas dépenser un euro : pas d'Insight Tag détecté, pas de landing univers (404), pas de lettre de prise en charge, Adspirer inaccessible. Tout ça se règle en une semaine. Le premier euro part après la porte G2 du 09/11, pas avant.

## Décision n°1

**Quoi** : valider LinkedIn comme canal « porte employeur + précision » (RAF/DAF/finance d'entreprise d'abord, banque ensuite), en 3 phases, avec un plafond de 1 600 € jusqu'au 18/12. Pas de dépense avant les 4 prérequis bloquants (section 3).
**Budget** : plafond 1 600 € [H] (Phase 1 : 1 100 €, Phase 2 : 500 €). Ton idée initiale de 10-15 €/jour pendant 2-3 semaines (210-315 €) donne un signal de mesure, jamais un verdict : à 5 € le clic, c'est 40 à 60 clics au total.
**Avant quand** : vendredi 06/11, pour que l'Insight Tag et la landing soient prêts à la porte G2 du 09/11.
**Effet attendu** : une réponse claire au 08/12 sur « LinkedIn rapporte-t-il des places Équipes à un coût acceptable ? » [H].
**Critère de réussite** : au moins 1 demande de devis Équipes qualifiée et un coût par compte gratuit inférieur à 60 €, sur au moins 100 clics par porte (détail section 6).

## 1. État des lieux au 31/10

### Accès Adspirer / LinkedIn
- Adspirer : **non vérifiable**. Les outils Adspirer (`get_connections_status`, etc.) ne sont pas exposés dans cette session. Je ne peux donc ni confirmer la connexion ni lire un historique. Lien de connexion : https://adspirer.ai/connections.
- Repli Supermetrics : la source LinkedIn Ads (LIA) existe mais est `NOT_AUTHENTICATED`. Aucune donnée lue.
- Journal (`linkedin-ads-state.yaml`) : aucune campagne, aucun historique. Compte Campaign Manager et ID de compte inconnus. La page entreprise LinkedIn existe (lien `linkedin.com/company/108065517` sur le site).

### Ce qu'un prospect voit sur le site, relevé du 31/10 [M]
| Élément | Constat |
|---|---|
| Accueil | « Maîtriser la nouvelle finance avec l'IA ». Compte gratuit sans carte. 29 €/mois, 299 €/an, 459 €/an. Aucun témoignage. Aucune mention de lancement. Chiffres : 50 000 formés, +100 cours, 6 parcours certifiants. Dix logos sans lien |
| /membership/ | Prix identiques. Certificats seulement dans l'annuel et le Premium (la correction du 27/10 est faite). Remboursement 5 jours si aucun certificat. Paiement : Mobile Money (Orange, MTN, Moov, Wave), carte, virement. Aucune mention de facture entreprise |
| /competences/ | Toujours incohérente : « 34 compétences » (titre), « 38 » (filtre), « 15 disponibles » pour 16 cartes datées. Doublon présent. **Aucune carte datée du 1er novembre** |
| /equipes/ | Existe. Accès équipes 249 €/place/an, engagement annuel, « à partir de 5 » dans la grille mais « dès 3 » dans le bandeau et la FAQ. Devis sous 48 h ouvrées. Facture avec bon de commande et virement. Cas chiffrés (Bank of Africa 700 directeurs d'agence, CIH 500). « Près de 10 000 » professionnels dans l'intro contre « 50 000 » dans les stats. Aucune lettre de prise en charge |
| /univers/banque/ et /univers/finance-entreprise/ | **404** (testés le 31/10). Les landing pages décidées le 28/10 n'existent pas encore |
| Tracking | Dans le code : GA4 (`G-1197EQWRNE`), pixel Meta (`fbevents.js`), capture des UTM (`utm_campaign`, `utm_content`, `utm_creative`). **Aucun LinkedIn Insight Tag détecté** (ni `snap.licdn.com`, ni `_linkedin_partner_id`). Le bandeau cookies ne mentionne que Meta |

Lecture : le prospect LinkedIn d'aujourd'hui arriverait sur l'accueil générique, sans preuve et sans lien employeur. Un DAF qui ouvre /equipes/ tombe sur un seuil de 3 ou de 5 places selon l'endroit où il regarde, et sur deux chiffres de lauréats contradictoires. Cela suffit à perdre la confiance d'un financier.

## 2. Cible, payeur et audience

### Qui paie
| Payeur | Prix | Poids pour LinkedIn |
|---|---|---|
| Particulier | 299 €/an (annuel), 459 € (Premium) | Marginal. Son pouvoir d'achat est le point faible mesuré (1 Premium en un mois, un blocage de paiement, [M 27/10]) |
| Employeur | 249 €/place, de 3 ou 5 places, soit 1 245 € minimum [M /equipes/] | **Le vrai intérêt de LinkedIn.** Facture et virement existent déjà côté Équipes. Manquent la lettre et le devis type |

Le message « faites payer l'abonnement par votre employeur » fonctionne dans deux sens : le salarié demande la prise en charge (lettre à fournir), ou le décideur (RAF, DAF, responsable formation) achète des places. LinkedIn sert surtout le second. Pas de formule « démissionnez » : les employeurs sont aussi nos clients et nos références.

### Taille d'audience atteignable [E/H]
Membres LinkedIn (estimations publicitaires, comptes inscrits et non actifs) : Maroc ≈ 7,0 M (déc. 2025), Côte d'Ivoire ≈ 1,6 M (janv. 2025), Sénégal ≈ 1,3 M (début 2025) [E, NapoleonCat et Osiris, sources en fin de document].

| Pays | Membres [E] | Fonction finance (≈ 4-6 % [H]) | Dont manager et plus (≈ 25-30 % [H]) |
|---|---|---|---|
| Maroc | ≈ 7,0 M | ≈ 280-420 k | ≈ 70-125 k |
| Côte d'Ivoire | ≈ 1,6 M | ≈ 65-95 k | ≈ 16-28 k |
| Sénégal | ≈ 1,3 M | ≈ 50-80 k | ≈ 13-24 k |
| **Total trois pays** | ≈ 9,9 M | ≈ 400-600 k | **≈ 100-175 k** |

Ces parts (4-6 % et 25-30 %) sont des hypothèses de ma part, non sourcées. Elles donnent un ordre de grandeur : assez large pour un test, mais le ciblage fin (RAF/DAF + PME + trois pays) sera bien plus étroit. Pour le remplacer par une mesure, je lance la prévision d'audience dans Campaign Manager dès que l'accès existe. C'est gratuit.

Recoupement avec l'étude de profondeur du 27/10 [E/H] : cible banque ≈ 47-86 k personnes et finance d'entreprise ≈ 56-158 k sur toute l'Afrique francophone et le Maghreb. LinkedIn n'en atteint qu'une partie : les cadres connectés, donc les plus solvables. C'est cohérent avec l'idée de précision.

## 3. Par quoi commencer : l'ordre, avec les prérequis bloquants

Rien ne dépense avant les 4 premiers.

| # | Étape | Qui | Avant | Preuve attendue |
|---|---|---|---|---|
| P1 | **Accès** : Campaign Manager (compte, rôle admin, lien avec la page entreprise), puis connexion Adspirer ou Supermetrics LinkedIn Ads | Rachid | 03/11 | `get_connections_status` vert, ID de compte |
| P2 | **Insight Tag** posé (via le gestionnaire de balises ou le thème), bandeau cookies mis à jour pour la catégorie LinkedIn. Conversions déclarées : inscription gratuite, clic « J'accède à tout l'univers », demande de devis Équipes, achat | Agent Site Xelanc | 06/11 | Tag détecté dans le code ; événement visible dans Campaign Manager |
| P3 | **Landing `/univers/finance-entreprise/`** en ligne (puis `/univers/banque/`), selon le cahier des charges du 28/10, sans lien panier forcé, avec UTM LinkedIn conservées jusqu'à l'inscription | Webmaster | 08/11 | URL en 200, ≤ 400 Ko, recette du cahier des charges §8 |
| P4 | **Voie employeur** : lettre de demande de prise en charge (modèle en PDF), devis type et facture pro forma, page `/equipes/` corrigée (3 ou 5 places, un seul chiffre de lauréats), formulaire testé de bout en bout, réponse humaine sous 48 h | GTM + Loubna | 08/11 | Lettre et devis fournis ; test du formulaire reçu |
| P5 | Preuve visible : 3 témoignages signés et la compétence datée du 01/11 corrigées (prérequis P8 et P9 de Launch) | Site + Loubna | 09/11 | Captures |
| P6 | Utiliser UTM LinkedIn normées : `utm_source=linkedin&utm_medium=paid_social&utm_campaign=xel-li-<porte>-<mois>&utm_content=<angle>` | Moi | 08/11 | Liens vérifiés |
| P7 | Vidéo de Rachid, 30-45 s, face caméra, sous-titrée | Rachid | 12/11 | Fichier |

Ordre d'exécution :

1. **Phase 0 (31/10 → 09/11), gratuite.** Prérequis P1 à P7. En parallèle, LinkedIn organique : le profil de Rachid (30 ans de haute finance, 50 000 formés) est l'actif n°1 de confiance, et la page Xelanc publie les témoignages. Aucun coût, et ça chauffe l'audience avant la pub.
2. **Phase 1 (10/11 → 07/12), test de précision, 1 100 €.** Deux campagnes de contenu sponsorisé, une par porte. Lecture intermédiaire le 24/11, verdict le 08/12.
3. **Phase 2 (07/12 → 18/12), Message Ad, 500 €.** Un seul envoi aux RAF/DAF de la porte gagnante, texte validé par Rachid avant envoi. Les budgets formation se débloquent souvent en janvier [H] : décembre prépare les devis.

## 4. Rôle de LinkedIn face aux autres canaux

| Canal | Rôle | Ordre |
|---|---|---|
| 50 000 anciens, 233 payeurs, 20 000 prospects (Brevo, WhatsApp) | Cash le moins cher : audience possédée, confiance héritée. **Passe avant tout** | 1 |
| Meta | Volume et inscriptions à bas coût (≈ 5 $ par inscription sur valo2 [M 27/10]) | 2 |
| Google Search / YouTube | Capter l'intention (certificat, métier) | 3 |
| **LinkedIn** | Précision (RAF/DAF/banque), payeur employeur, badge du certificat, autorité de Rachid | 4, test |

À ne pas confondre : LinkedIn n'est pas moins bon, il joue ailleurs. Une inscription LinkedIn coûte 10 à 50 fois plus qu'une inscription Meta [E/H], mais un décideur employeur vaut 5 places. Il faut le mesurer, pas le supposer.

Deux points de coordination (pas mon périmètre, je les signale) :
- **Tête Grise / FIA** : l'audience DAF/RAF correspond aussi au programme DAF Dirigeant Augmenté (dès 2 375 €, vente humaine par Loubna). Pour ce public, la meilleure offre n'est peut-être pas à 299 €. Une décision de portefeuille est à prendre avant d'envoyer le Message Ad.
- **Launch** : les segments Advisory A à D sont exclus jusqu'au 07/12 et les inscrits au bootcamp du 18 au 22/11 jusqu'au 22/11. Les listes d'exclusion doivent aussi s'appliquer à LinkedIn.

## 5. Structure de campagnes recommandée

Groupe de campagnes `XEL-LI-2026-11`, objectif « Visites du site » puis « Conversions » dès 15 conversions enregistrées [H].

| Campagne | Objectif | Audience | Format | Budget/j | Statut |
|---|---|---|---|---|---|
| C1 · Finance d'entreprise | Inscriptions et demandes de devis Équipes | Fonctions Finance/Comptabilité, séniorité manager et plus, intitulés RAF/DAF/contrôleur de gestion/FP&A, entreprises de 11 à 1 000 employés, Maroc + Côte d'Ivoire + Sénégal | Vidéo de Rachid (30-45 s) + visuel unique | 20 € | Proposée, non créée |
| C2 · Banque | Même | Banque et services financiers, fonctions crédit/risque/clientèle entreprise, séniorité senior et plus, mêmes pays | Même format, accroche carrière | 20 € | Proposée, non créée |
| C3 · Message Ad (Phase 2) | Demande de devis Équipes | RAF/DAF/responsables formation de la porte gagnante, ≈ 600-700 envois | Message Ad, texte à valider | 500 € au total | Après verdict de la Phase 1 |
| C4 · Reciblage | Inscriptions | Visiteurs de la landing + vidéo vue à 50 % + liste d'anciens, dès 300 membres reconnus | Image + témoignage | min. 10 $/j | À ouvrir seulement si l'audience atteint 300 |

Règles de structure :
- **Un seul test à la fois.** Phase 1 : la porte (audience et message ensemble, comme décidé en D4). Dans la porte gagnante, ensuite : un angle à la fois.
- **Angles à tester, dans cet ordre** : (1) prise en charge par l'employeur, (2) certificat et badge LinkedIn, (3) gain de temps. Jamais de promesse d'emploi ni de promotion.
- **Exclusions** : acheteurs existants, abonnés actuels, segments Advisory A-D, inscrits bootcamps. Zones : seulement les trois pays au départ.
- **Destination** : la landing de la porte, URL HTTPS avec UTM. **Interdit** : les liens `/commander/?add-to-cart=` (décision D7).
- **Liste d'anciens et de prospects (audiences par liste)** : avant tout envoi à LinkedIn, vérifier la conformité (loi 09-08 / CNDP, consentement). À faire valider.
- **Créas** : texte d'introduction ≤ 600 caractères, vérifié avant publication. Voix Xelanc, vouvoiement.
- **Pays** : France, Belgique, Suisse et Canada ne sont pas testés sur LinkedIn. Le coût par clic y est nettement plus haut [E] et le test francophone solvable prévu fin novembre reste sur Meta et Google.

## 6. Ce qu'on vise, et quand on s'arrête

### Repères de coût, tous [E] (aucun mesuré pour Xelanc)
| Repère | Valeur | Source et réserve |
|---|---|---|
| CPC moyen LinkedIn | ≈ 5,98 € (+11,8 % sur un an) | Dreamdata, mars 2026, relayé par The Ad Spend. Données de vendeur |
| CPM moyen | ≈ 34 € | Idem |
| CPC finance B2B | 5-12 $, jusqu'à 10-12 $ pour les profils seniors | Blogs d'agences, **non traçables** (The Ad Spend le dit) |
| CPL services financiers | 100-300 $ | Idem, directionnel |
| Afrique | ≈ 2 $ le clic | **Un seul blog**, pas de chiffre par pays. Je ne m'en sers pas pour budgéter |
| Message Ad | 0,25-1,00 $ par envoi, ouverture 40-55 %, clic 3-4 % | Blogs d'agences, aucun référentiel officiel |
| Minimums LinkedIn | 10 $/jour par campagne ; enchère minimale 2 $ | Documentation relayée par des tiers |

Aucune source ne donne un coût fiable pour le Maroc, la Côte d'Ivoire ou le Sénégal. **Mon hypothèse de travail : CPC de 3 à 8 €**, à remplacer par la mesure. Les estimations d'enchères de Campaign Manager par pays seront relevées dès l'accès (P1).

### Entonnoir [H], Phase 1 (1 100 €)
| Étape | Bas | Central | Haut | Ancrage |
|---|---|---|---|---|
| Clics | 140 | 220 | 370 | 1 100 € ÷ CPC de 8 / 5 / 3 € |
| Clic vers compte gratuit | 3 % | 4 % | 6 % | Meta valo2 : 4/156 = 2,6 % [M 27/10] |
| Comptes gratuits | ≈ 4 | ≈ 9 | ≈ 22 | |
| Coût par compte gratuit | ≈ 270 € | ≈ 125 € | ≈ 50 € | Contre ≈ 5 $ sur Meta [M] |
| Abonnés particuliers (2,5 % à 10 % des comptes) | 0 | 0-1 | 1-2 | Taux de la Tête Grise et de ton modèle humain |
| Demandes de devis Équipes | 0 | 1 | 3 | Hypothèse : 0,5-1 % des clics |
| Cash individuel probable | ≈ 0 € | ≈ 0-300 € | ≈ 300-900 € | |

Conclusion honnête : **la Phase 1 ne bouge pas le cash de novembre** (cible centrale de la Tête Grise : 85 k€ sur nov-janv, 158 nouveaux payants en novembre). Elle achète une réponse sur l'employeur. Un abonné individuel obtenu par LinkedIn coûterait 300 à 1 200 € [E/H], bien au-dessus du seuil de 120 € du plan d'activation. Ce seuil n'est atteignable que par l'employeur.

### Objectifs chiffrés si le canal est validé (scénario, [H])
- Coût par demande de devis Équipes qualifiée : ≤ 150 €.
- Coût par vente Équipes (5 places, 1 245 €) : ≤ 310 € (25 % de la première année).
- Part employeur des ventes issues de LinkedIn : ≥ 50 %.
- Échelle : 1 500 à 3 000 €/mois de pub (règle « pub ≤ 30 % de l'encaissé ») pour 2 ventes Équipes par mois, soit 2,5 à 5 k€/mois, environ 15-25 % de la ligne Xelanc (18 k€/mois visée en mars 2027). Ce n'est pas un moteur de l'objectif de 86 k€ à lui seul, c'est un amplificateur du B2B que la Tête Grise veut relancer.

### Critères d'arrêt et de passage à l'échelle
| Situation | Décision |
|---|---|
| Moins de 100 clics ou moins de 500 € dépensés par porte | **Pas de verdict.** On laisse tourner et on le dit |
| ≥ 100 clics par porte et clic → compte < 2 % | Stop de la porte, on corrige la landing avant de relancer |
| 600 € dépensés sans aucune demande de devis ni abonné | Pause de la campagne la moins bonne |
| 1 100 € dépensés (fin de Phase 1) sans devis ni abonné | Arrêt du canal payant, LinkedIn organique seulement |
| Coût par compte < 60 € **et** au moins 1 devis qualifié | Phase 2 (Message Ad) autorisée |
| Coût par demande de devis ≤ 150 € sur ≥ 3 demandes | Proposition de passage à 1 500 € le premier mois, avec ton « go » |
| Une campagne dépense plus de 25 % au-dessus du plan | Baisse de budget immédiate, signalée |

## 7. Risques et ce qu'il ne faut PAS faire

| Risque | Parade |
|---|---|
| Brûler le budget sur une page qui n'existe pas encore | Aucun euro avant P1 à P4 |
| Mesure aveugle (pas d'Insight Tag) | P2 avant le 06/11, test de l'événement |
| Cible trop large (RAF/DAF) donc clics de curieux, étudiants | Séniorité et intitulés, exclusion des « étudiants » et des fonctions hors cible |
| Seuil Équipes contradictoire (3 ou 5 places), chiffres de lauréats contradictoires | Corriger `/equipes/` avant la pub |
| Message qui braque les employeurs | Jamais « démissionnez » ; message « votre employeur peut financer » |
| Message Ad sans texte validé | Interdit sans ton accord écrit |
| Doublon avec les relances d'emails et le bootcamp | Listes d'exclusion alignées avec Launch |
| Liste de contacts envoyée à LinkedIn sans base légale | Validation CNDP / loi 09-08 d'abord |
| Verdict prématuré sur 40 clics | Règle des 100 clics et 500 € |
| Confondre cash du test et cash du canal : le test seul ne rapporte presque rien | Je le dis dans chaque rapport |
| Promesse d'emploi ou de promotion, faux témoignage, fausse rareté | Interdit (cahier des charges §5) |
| Vente humaine Équipes : ça contredit la décision D9 (« ni pipeline commercial ») | Décision à trancher (section 8) |

## 8. Décisions attendues de Rachid

1. **Valider le rôle de LinkedIn et le plafond de 1 600 €** (décision n°1), ou ajuster. Alternative : tester une seule porte à 25 €/jour pour 500 € (verdict plus lent, une seule réponse).
2. **Accès** : créer ou confirmer le compte Campaign Manager, me donner l'ID du compte, connecter Adspirer (https://adspirer.ai/connections) ou autoriser Supermetrics LinkedIn Ads. Sans cela, je ne lis rien.
3. **Qui paie** : ouvrir officiellement l'employeur pour LinkedIn (Équipes, 249 € la place). Le B2B est « en pause » depuis le 08/10 et D9 exclut le pipeline humain : acceptes-tu une réponse humaine sous 48 h pour les seules demandes de devis Équipes ?
4. **Seuil Équipes** : 3 ou 5 places ? Un seul chiffre sur tout le site.
5. **Vidéo** : Rachid la tourne-t-il, et pour le 12/11 ? Sinon, quelle alternative (carrousel, image) ?
6. **DAF Dirigeant (FIA)** : on réserve le Message Ad aux RAF/DAF pour Équipes, ou on teste aussi l'offre DAF Dirigeant ? À arbitrer avec la Tête Grise.
7. **Listes** : feu vert pour vérifier la conformité avant tout envoi de liste à LinkedIn.

## 9. Ce que je n'ai pas pu vérifier

- La connexion Adspirer et tout historique LinkedIn (outils absents de la session, source Supermetrics non authentifiée).
- Le code source complet des pages : j'ai lu le HTML public (balises GA4 et Meta, UTM), mais je ne peux pas garantir qu'un gestionnaire de balises ne charge pas l'Insight Tag sous condition de consentement. À confirmer avec l'agent Site.
- Les audiences réelles par pays et fonction (hypothèses de la section 2) et les coûts locaux (aucune source fiable pour le Maroc, la Côte d'Ivoire, le Sénégal).
- Le contenu payable du 01/11 et le test de paiement Mobile Money, hors de mon périmètre.

## Sources (repères [E])
- Dreamdata via The Ad Spend, LinkedIn Ads B2B 2026 : https://theadspend.com/blog/linkedin-ads-overall
- Benchmarks CPC/CPL (agences, directionnels) : https://www.clickminded.com/linkedin-ads-benchmarks/ ; https://www.factors.ai/blog/linkedin-ads-cost ; https://www.webtonic.io/blog/fintech-linkedin-ads-statistics
- Message Ads : https://zenabm.com/blog/linkedin-message-ads ; https://theadspend.com/blog/linkedin-message-ads
- Afrique (~2 $ le clic, blog unique) : https://b2linked.com/blog-page/how-much-does-a-linkedin-ad-click-really-cost
- Maroc (7,02 M, déc. 2025) : https://stats.napoleoncat.com/linkedin-users-in-morocco/2025/12/
- Côte d'Ivoire (1,617 M, janv. 2025) : https://napoleoncat.com/stats/linkedin-users-in-cote_divoire/2025/01
- Sénégal (≈ 1,3 M) : https://osiris.sn/senegal-les-utilisateurs-de-linkedin-depassent-1-millions-en-2025.html
- Site Xelanc relevé le 31/10 : https://xelanc.org/ ; /membership/ ; /competences/ ; /equipes/
