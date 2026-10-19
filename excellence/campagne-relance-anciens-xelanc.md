# Relance des anciens acheteurs — lancement Xelanc

Conception : Tête Grise, 2026-10-19. Statut : **à valider**, rien n'est envoyé.
Étiquettes : [M] mesuré, [E] estimé, [H] hypothèse.

## 1. Qui (mis à jour le 19/10 d'après l'agent Site Xelanc [M])

- Consolidation Thinkific + Stripe : **233 payeurs, 56 431 $** encaissés au total.
- Base Afrique subsaharienne : 529 personnes, dont 472 payeurs (≈ 134 en ligne, ≈ 340 hors ligne, Western Union / virement).
- Règle de Rachid : « inscrit = a payé ».
- **Éligibles à l'offre 179 € : 213** (décision Rachid 19/10 : 299 − 120 = 179 € pour 1 an ; exclus : DAF, programmes, gros tickets — 257 exclus).
- Fichiers (Mac, non publiés) : `~/Travail/Export-FTA-2026-10-19/` (xlsx, page HTML, CSV au format Brevo).
- Exclus aussi : toute personne déjà abonnée à Xelanc.

**Conséquence canal** : une grande partie des payeurs a payé hors ligne. Pour eux, **WhatsApp passe avant l'email**,
et il faut une voie de paiement hors ligne (Loubna prend la demande, Rachid valide le paiement).

## 2. Le principe

1. **Un vrai service d'abord** : le cours acheté est accessible sur Xelanc. L'email l'annonce, sans argument commercial.
2. En se connectant, l'ancien client découvre le catalogue, les certificats et le tuteur IA.
3. **Quatre jours plus tard, l'offre ancien client** : l'abonnement annuel à **179 € au lieu de 299 €**,
   soit 299 − 120 : *« ce que vous avez payé compte comme acompte »*.
4. **Échéance réelle : vendredi 13 novembre à minuit**, fin de la période réservée aux anciens clients.

**Calage sur le plan de lancement** (`launch-state.yaml`, vague V1) : départ le **lundi 2 novembre**,
sous réserve du feu vert de la porte G0 du 29/10 (Brevo, paiement testé, cours accessibles).

**Condition non négociable** : avant l'envoi, chaque acheteur doit réellement retrouver son cours.
Si un ancien cours n'existe pas encore sur Xelanc, on lui ouvre l'équivalent le plus proche et on le dit
honnêtement (« votre cours a été refait ; vous accédez à sa nouvelle version »).

## 3. Calendrier

| Date | Canal | Message | But |
|---|---|---|---|
| **Lun. 02/11** | Email | E1 « Votre cours vous attend sur Xelanc » | Service, connexion |
| Mer. 04/11 | WhatsApp (ceux qui n'ont pas ouvert) | WA-A « Votre accès est prêt » | Connexion |
| **Ven. 06/11** | Email (non abonnés) | E2 Offre ancien client 179 € | Décision |
| Lun. 09/11 | Email + WhatsApp (ouvreurs non abonnés) | E3 Ce que contient l'annuel + témoignage | Lever les doutes |
| **Ven. 13/11** | Email | E4 Dernier jour | Échéance |
| Lun. 16/11 | Email (non abonnés) | E5 Repli : mensuel 29 €, sans engagement | Seconde porte |

5 emails et 2 WhatsApp en 13 jours, désinscription en un clic, aucun message après un « stop ».

**Ceux qui s'abonnent d'eux-mêmes au prix plein (avant le 06/11)** ne reçoivent pas l'offre :
ils passent gratuitement en Premium (459 €) la première année. Personne ne doit se sentir floué.

## 4. Les messages (vouvoiement, signés « L'équipe Xelanc », captures de la plateforme)

Modèles HTML v2 : `excellence/emails/relance-anciens-e1.html` et `relance-anciens-e2.html` (images dans `excellence/emails/img/`).

### E1 · Lun. 02/11 · « Votre cours vous attend sur Xelanc »
> Objet : Votre cours {{cours}} est disponible sur votre nouvel espace
>
> Bonjour {{prénom}},
>
> Vous avez suivi avec nous le cours {{cours}}. Nous avons réuni nos formations sur une nouvelle
> plateforme, Xelanc, et votre cours y est désormais disponible.
>
> Votre accès : {{lien_connexion}}
> Votre identifiant : {{email}}
>
> Vous y retrouverez votre cours, et vous verrez aussi ce que nous avons construit depuis :
> plus de 100 cours, des parcours certifiants et un tuteur IA disponible à toute heure.
>
> Bonne reprise,
> L'équipe Xelanc

### WA-A · Mer. 04/11 (non-ouvreurs) · modèle à valider par Meta
> Bonjour {{1}}, votre cours {{2}} est disponible sur votre nouvel espace Xelanc. Votre accès vous attend.
> Boutons : « Accéder à mon cours » (lien) · « Je n'ai pas reçu l'email »

### E2 · Ven. 06/11 · Offre ancien client
> Objet : {{prénom}}, ce que vous avez déjà payé compte pour vous
>
> Bonjour {{prénom}},
>
> Xelanc vient d'ouvrir. Pendant une semaine, nous réservons à nos anciens clients
> une offre qui n'est pas proposée au public.
>
> L'abonnement annuel « Cours et certificats » coûte 299 €. Pour vous, il est à **179 €** :
> nous considérons les 120 € de votre premier achat comme un acompte.
>
> Ce que vous obtenez pendant un an :
> - tous les cours, et les nouveaux dès leur sortie ;
> - les 6 parcours certifiants et leurs certificats vérifiables ;
> - le tuteur IA, 5 questions par jour ;
> - les modèles Excel et les ressources de chaque cours.
>
> L'offre reste valable jusqu'au **vendredi 13 novembre à minuit**.
> {{lien_offre}}
>
> Vous préférez payer par Mobile Money, Western Union ou virement ? Répondez à cet email ou
> écrivez-nous sur WhatsApp : Loubna s'occupe de vous.
>
> L'équipe Xelanc

### E3 · Lun. 09/11 · Ce que contient l'annuel
> Objet : Ce que les certificats changent concrètement
>
> Contenu : un parcours certifiant expliqué en 5 lignes (exemple : Chargé d'affaires PME, 5 cours,
> 6 à 8 semaines, examen final, identifiant vérifiable, badge LinkedIn) + un témoignage d'ancien
> + rappel du prix ancien client 179 € jusqu'au 13/11.

### E4 · Ven. 13/11 · Dernier jour
> Objet : Dernier jour pour votre tarif ancien client
>
> Bonjour {{prénom}}, votre tarif ancien client de 179 € pour l'année s'arrête ce soir à minuit ;
> ensuite, l'abonnement annuel revient à 299 €.
> {{lien_offre}}

### E5 · Lun. 16/11 · Repli
> Objet : Une autre façon de commencer
>
> Bonjour {{prénom}}, si l'abonnement annuel ne vous convient pas maintenant, vous pouvez
> accéder à tous les cours pour 29 € par mois, sans engagement, et passer à l'annuel quand vous le souhaitez.

## 5. Prérequis (avant la porte G0 du 29/10)

| # | Prérequis | Qui |
|---|---|---|
| 1 | Liste des acheteurs avec le cours acheté (Thinkific + Stripe, depuis le Mac) | Session Mac |
| 2 | Correspondance ancien cours → cours Xelanc, et accès ouvert pour chaque acheteur | Agent Site Xelanc |
| 3 | Lien de connexion qui marche (test avec un compte réel) | Agent Site Xelanc |
| 4 | Coupon ou lien de paiement « annuel 179 € » valable jusqu'au 13/11 23 h 59, réservé à la liste | Agent Site Xelanc |
| 5 | Crédits Brevo, envoi depuis un domaine authentifié (xelanc.com ou xelanc.org) | Rachid |
| 6 | Modèle WhatsApp WA-A soumis à Meta | Rachid |
| 7 | Un témoignage d'ancien pour E3 | Loubna |

## 6. Ce qu'on peut en attendre [H]

Hypothèses : 85 % joignables, 1,8 % s'abonnent seuls à 299 €, 9 % des restants prennent l'offre à 179 €
(fourchette 5–15 %), frais de paiement 4 %.

| Scénario | Abonnés seuls (299 €) | Offre (179 €) | **Total** | **Cash** |
|---|---|---|---|---|
| Pessimiste (5 %) | 2 | 9 | **11** | **≈ 2,1 k€** |
| **Central (9 %)** | 3 | 16 | **19** | **≈ 3,6 k€** |
| Optimiste (15 %) | 4 | 27 | **31** | **≈ 5,8 k€** |

Seuil d'alerte : moins de 5 % de conversion à J+7 → Loubna appelle les ouvreurs et les cliqueurs.

## 7. Points bloquants relevés dans la session Site Xelanc (19/10)

- **Aucun achat de contrôle** ; **aucun paiement Mobile Money n'a abouti**. Critique pour une base africaine.
- **Pas de correspondance** entre les anciens cours Thinkific et les 15 cours LearnWorlds.
- 7 cours présentés sur xelanc.org n'existent pas dans LearnWorlds (à ouvrir ou à masquer).
- Les 4 modèles WhatsApp soumis (n° 24–27) ne couvrent pas cette campagne : WA-A reste à soumettre.
- Vérification d'entreprise Meta refusée : plafond 2 000 contacts/jour (suffisant pour 213).
- Préfixes de clés Stripe affichés en clair dans la session : clés à régénérer.
