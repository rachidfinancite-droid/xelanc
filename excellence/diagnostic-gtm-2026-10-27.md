# 🧭 Diagnostic go-to-market Xelanc, 27 octobre 2026 (J-5)

Première mission de l'agent GTM. Étiquettes : [M] mesuré, [E] estimé, [H] hypothèse.
Sources : relevé du site du 27/10 [M], ainsi que `cash-state.yaml`, `launch-state.yaml`,
`plan-activation-100k.md`, les campagnes et le benchmark du 23/10. Les mesures des agents
datent du 08 au 19/10 et sont **à reconfirmer** pour tout point bloquant.

**Verdict.** Le produit tient face aux comparables. Il coûte environ 40 % de moins que CFI [M],
il est en français et il prend l'IA comme angle. Ce qui ne tient pas encore, c'est la mise
sur le marché. Trois défauts se cumulent. La promesse est générique et parle à tout le
monde. Le prospect ne voit aucune preuve et ne sait pas ce qui est disponible le 1er novembre.
Enfin, tout le volume passe par un seul tuyau, l'email Brevo, dont le dernier état connu
est rouge. À cinq jours de J0, on ne refait pas le site. On resserre le message de lancement
sur un seul client idéal, on ajoute la preuve en 72 h et on sécurise le débit d'envoi.

## Tableau des axes

| Axe | Feu | Constat clé | Preuve |
|---|---|---|---|
| 1. Client idéal et payeur | 🟠 | Le site vise six métiers, trois types d'institutions et les équipes « dès 3 personnes ». Le B2B est pourtant en pause et personne n'a tranché qui paie : la personne ou l'employeur. | Site 27/10 [M] ; décision B2B du 08/10 [M] ; `payeur: null` |
| 2. Proposition de valeur | 🟠 | « Maîtriser la nouvelle finance avec l'IA » ne dit ni pour qui, ni ce qu'on obtient. Les vrais différenciants du benchmark (dossier fil rouge, vérification de l'IA à chaque étape, PCG/CGNC/SYSCOHADA) n'apparaissent pas. Le certificat « n'est pas un diplôme d'État » et son autorité de certification est le fondateur seul. | Site [M] ; benchmark 23/10 [M] |
| 3. Offre et prix | 🟠 | L'échelle est claire et bien placée (29 €/mois, 299 €/an, 459 €/an). Trois défauts : la carte Mensuel promet les certificats que la FAQ réserve à l'annuel ; « 2 mois offerts » vaut en réalité 1,7 mois (49 €) ; aucune offre de lancement n'est visible, et l'offre fondateurs attend une décision depuis le 08/10. | /membership/ 27/10 [M] |
| 4. Preuve | 🔴 | Aucun témoignage, aucune vidéo de preuve. Les logos n'ont pas de texte alternatif et rien ne prouve un partenariat. Les chiffres ne sont pas sourcés : 50 000 formés, 6 certificats annoncés pour 5 cartes. Sur /competences/, trois totaux se contredisent (34, 38, 35), le doublon est toujours là et **aucune carte n'est datée du 01/11**. Les « 9 compétences du 1er novembre » du 17/10 ne sont plus visibles. | /competences/ 27/10 [M] |
| 5. Canaux | 🔴 | Environ 25 200 contacts possédés (213 + 5 000 + 20 000) passent tous par Brevo. Au plafond de 300 emails/jour, il faut **84 jours** pour un seul envoi à tous, alors que le lancement en dure 91. L'historique Meta montre 0 inscription Advisory sur 512 leads [M]. Le nouveau compte, le pixel et les UTM ne sont pas prouvés le jour prévu des tests. LinkedIn n'a ni rythme ni mesure. | `launch-state` P1, P5, P6 ; calcul [E] |
| 6. Entonnoir et mesure | 🔴 | Pas de GA4, pas de pixel, aucune UTM au dernier relevé. Sans eux, la porte G2 du 09/11 ne peut pas se juger et on ne saura pas quelle vague convertit. | P5 rouge (08/10) |
| 7. Capacité commerciale | 🟠 | Loubna seule porte les WhatsApp des anciens (dont environ 340 qui ont payé hors ligne), les qualifiés Advisory et les bootcamps, sur la même quinzaine. Le paiement hors ligne passe par Rachid. | Campagne relance du 19/10 [M] |
| 8. Objectif ↔ marché | 🟠 | Xelanc seul atteint environ 32 k€/mois au 12e mois en scénario central [E]. Les 100 k$ demandent le high ticket et le B2B. Le levier qui casse le plafond (licences équipes, sur le modèle de CFI) est affiché sur le site mais en pause dans la stratégie. | Tête Grise du 17/10 [E] |

## Les 3 ruptures (ce qui empêche de vendre)

1. **Le prospect ne sait pas ce qu'il achète le 1er novembre.** Aucune compétence n'est datée
   de J0, les compteurs se contredisent et les cartes Mensuel et FAQ se contredisent aussi.
   Une personne qui hésite à payer 299 € s'arrête sur la première incohérence.
2. **Rien ne prouve que ça marche.** On a 233 anciens payeurs [M] et une vingtaine d'inscrits
   Advisory, mais aucun témoignage public. C'est l'écart n°1 avec CFI, devant la profondeur
   du catalogue.
3. **Le débit d'envoi ne porte pas le plan.** Les vagues V2 et V3 représentent 25 000 contacts.
   Avec Brevo non crédité ou plafonné, la V3 (20 000 contacts, départ prévu le 05/11)
   n'atteint pas sa fin avant janvier. Les 140 abonnés du scénario central de cette base [E]
   glissent donc après le Black Friday.

## Décision n°1

**Quoi** : verrouiller un **positionnement de lancement unique** pour toutes les vagues de
novembre. Il tient en trois éléments :

- **Client idéal** : les banquiers entreprise et PME et les analystes crédit, au Maroc et en
  Afrique francophone (UEMOA, CEMAC, RDC). C'est là que se concentrent nos preuves (logos
  bancaires, bootcamp Chargé de clientèle, parcours Chargé d'affaires PME et Analyste
  risque), le paiement Mobile Money et les leads Meta les moins chers.
- **Promesse** : « Montez un dossier de crédit complet avec l'IA, vérifié à chaque étape,
  aux normes CGNC et SYSCOHADA, et obtenez un certificat vérifiable sur LinkedIn. »
- **Offre héros** : l'annuel à 299 €. Le mensuel sert de repli et le cours à 13,90 € de
  porte d'entrée en publicité.

Concrètement, le titre de l'accueil, l'objet des emails V2 et V3 et l'accroche des tests Meta
reprennent cette phrase. Les cinq autres parcours restent au catalogue sans porter le message.

**Qui** : Rachid valide. L'Orchestre réécrit les accroches, l'agent Site Xelanc change le
titre et le sous-titre de l'accueil.
**Avant quand** : mercredi 28/10, pour passer la porte G0 du 29/10.
**Effet attendu** : sur les mêmes listes, le taux d'inscription des emails passe de
moins de 15 % à 20–25 % [H]. Le coût par compte des tests Meta reste sous 1,5 € (seuil G3).
**Critère de réussite** : au 09/11, l'accroche ciblée bat la promesse générique d'au moins
30 % en clic → compte, sur au moins 1 000 envois (test A/B sur la V3).

## Correctifs classés (effet ÷ effort)

| # | Correctif | Effort | Effet | Pour qui |
|---|---|---|---|---|
| 1 | Dater sur /competences/ ce qui est réellement ouvert le 01/11, aligner les trois compteurs et supprimer le doublon | 2 h | Lève la rupture 1 | Site Xelanc |
| 2 | Carte Mensuel : retirer « certificats » ; remplacer « 2 mois offerts » par « 49 € d'économie » | 15 min | Supprime une incohérence au paiement et un risque de réclamation | Site Xelanc |
| 3 | Collecter 3 témoignages écrits avec photo et poste, plus 1 vidéo de 30 s, auprès d'anciens payeurs et d'inscrits Advisory | 48 h (Loubna) | Lève la rupture 2, prérequis P9 | Loubna |
| 4 | Brevo : passer à une offre sans plafond journalier avant le 02/11, ou à défaut garder V1 et V2 en email et faire de la V3 une vague « engagés d'abord » limitée à 3 000 contacts en novembre | 1 h et un budget | Lève la rupture 3 | Rachid et Site Xelanc |
| 5 | Montrer un vrai certificat et le badge LinkedIn au-dessus des prix, et nommer l'autorité de certification (Xelanc Groupe et Financité Institute, 30 ans) | 1 h | Soutient la part d'annuels (au moins 55 %) | Site Xelanc |
| 6 | Pixel, GA4 et UTM avant le premier euro de pub. Sans eux, les tests Meta du 27/10 sont reportés, pas lancés à l'aveugle | 0,5 j | Rend G2 et G3 jugeables | Meta et Site Xelanc |
| 7 | Garder le B2B « Équipes » en page, mais router toute demande vers une piste FIA tenue par Rachid (aucun prix affiché, réponse sous 48 h) | 30 min | Ne perd pas les demandes entrantes, en pause n'est pas fermé | Rachid |

## Briefs

**Pour** : Agent Site Xelanc · **Avant** : mer. 28/10, 18 h · **Pourquoi** : ruptures 1 et 2, porte G0
**À faire** : correctifs 1, 2 et 5 ; nouveau titre et sous-titre de l'accueil selon la décision n°1.
**Preuve attendue** : captures de /competences/ (compteurs = cartes), de /membership/ et de l'accueil.
**Ne pas faire** : changer un prix ou ajouter une promotion.

**Pour** : Loubna · **Avant** : jeu. 29/10 · **Pourquoi** : rupture 2, prérequis P9
**À faire** : 10 demandes WhatsApp de témoignage à des anciens payeurs satisfaits et aux
inscrits Advisory. Viser 3 témoignages écrits signés (nom, poste, banque, photo) et 1 vidéo
de 30 s au téléphone, avec accord écrit de publication.
**Preuve attendue** : les 3 textes et les accords.
**Ne pas faire** : solliciter les segments Advisory A–D en cours de campagne.

**Pour** : Orchestre Marketing · **Avant** : mer. 28/10 · **Pourquoi** : décision n°1
**À faire** : objets et premiers paragraphes des emails V2 et V3, et 3 accroches Meta (cours
Dossier de crédit à 13,90 €), toutes alignées sur la promesse ; une variante générique pour
le test A/B.
**Preuve attendue** : les textes en brouillon.
**Ne pas faire** : promettre une date de sortie non confirmée par le site.

## Décisions attendues de Rachid

1. **Valider le client idéal et la promesse de lancement** (décision n°1), ou en nommer un autre.
2. **Qui paie ?** Particulier seul pour novembre, ou employeur aussi, avec une facture au nom
   de la banque et un devis équipes ?
3. **Offre fondateurs** : « 299 € à vie » ou « 299 €/an, prix bloqué à vie ». La porte G4 du
   25/11 l'exige, et la liste d'attente du Black Friday se constitue dès la mi-novembre.
4. **Budget Brevo** pour lever le plafond de 300 emails/jour, et **budget de tests Meta**.
5. **Contenu réel de J0** : quelles compétences sont payables et complètes le 01/11 ?

## Pour Launch

- Ajouter à G0 deux critères : « compteurs /competences/ = cartes, au moins une compétence
  datée du 01/11 » et « débit d'envoi suffisant pour la V3 ou V3 redimensionnée ».
- Le prérequis P8 est toujours rouge au 27/10 [M], avec de nouveaux écarts (34, 38, 35).
- Un test A/B accroche ciblée contre générique sur le premier lot de la V3 (2 × 10 %).

## Pour la Tête Grise

- La prévision centrale de la base des 20 000 (140 abonnés, environ 35 k€) suppose un envoi
  complet en novembre. Avec un débit plafonné, il faut la décaler de 6 à 8 semaines ou la
  recaler sur 3 000 engagés.
- Hypothèse à ouvrir : un positionnement ciblé bancaire relève l'inscription de 15 % à
  20–25 % [H]. Mesure sur la V3 au 09/11.
- Le mix d'au moins 55 % d'annuels reste fragile tant qu'aucun certificat n'est montré et
  qu'aucune accréditation externe n'existe.
