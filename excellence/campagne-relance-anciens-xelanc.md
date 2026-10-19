# Relance des anciens acheteurs — lancement Xelanc

Conception : Tête Grise, 2026-10-19. Statut : **à valider**, rien n'est envoyé.
Étiquettes : [M] mesuré, [E] estimé, [H] hypothèse.

## 1. Qui

- Personnes ayant acheté un cours chez Financité (≈ 120 € à l'époque).
- **Taille à trancher** : 73 acheteurs payants mesurés dans Thinkific [M agent Données] contre 400 annoncés [Rachid].
  La liste « payeurs » (Thinkific + Stripe Delaware + Stripe Dubaï) tranche la question.
- Exclus : toute personne déjà abonnée à Xelanc.

## 2. Le principe

1. **Un vrai service d'abord** : le cours acheté est accessible sur Xelanc. L'email l'annonce, sans argument commercial.
2. En se connectant, l'ancien client découvre le catalogue, les certificats et le tuteur IA.
3. **Quatre jours plus tard, l'offre ancien client** : l'abonnement annuel à **179 € au lieu de 299 €**,
   soit 299 − 120 : *« ce que vous avez payé compte comme acompte »*.
4. **Échéance réelle : le 1er novembre**, jour de l'ouverture publique de Xelanc.

**Condition non négociable** : avant l'envoi, chaque acheteur doit réellement retrouver son cours.
Si un ancien cours n'existe pas encore sur Xelanc, on lui ouvre l'équivalent le plus proche et on le dit
honnêtement (« votre cours a été refait ; vous accédez à sa nouvelle version »).

## 3. Calendrier

| Date | Canal | Message | But |
|---|---|---|---|
| **Mer. 21/10** | Email | E1 « Votre cours vous attend sur Xelanc » | Service, connexion |
| Ven. 23/10 | WhatsApp (ceux qui n'ont pas ouvert) | WA-A « Votre accès est prêt » | Connexion |
| **Dim. 25/10** | Email (non abonnés) | E2 Offre ancien client 179 € | Décision |
| Mer. 28/10 | Email + WhatsApp (ouvreurs non abonnés) | E3 Ce que contient l'annuel + témoignage | Lever les doutes |
| **Sam. 31/10** | Email | E4 Dernier jour | Échéance |
| Mar. 03/11 | Email (non abonnés) | E5 Repli : mensuel 29 €, sans engagement | Seconde porte |

5 emails et 2 WhatsApp en 13 jours, désinscription en un clic, aucun message après un « stop ».

**Ceux qui s'abonnent d'eux-mêmes au prix plein (avant le 25/10)** ne reçoivent pas l'offre :
ils passent gratuitement en Premium (459 €) la première année. Personne ne doit se sentir floué.

## 4. Les messages (vouvoiement, signés du Pr El Maataoui)

### E1 · Mer. 21/10 · « Votre cours vous attend sur Xelanc »
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
> Pr Rachid El Maataoui

### WA-A · Ven. 23/10 (non-ouvreurs) · modèle à valider par Meta
> Bonjour {{1}}, votre cours {{2}} est disponible sur votre nouvel espace Xelanc. Votre accès vous attend.
> Boutons : « Accéder à mon cours » (lien) · « Je n'ai pas reçu l'email »

### E2 · Dim. 25/10 · Offre ancien client
> Objet : {{prénom}}, ce que vous avez déjà payé compte pour vous
>
> Bonjour {{prénom}},
>
> Xelanc ouvre officiellement le 1er novembre. Avant cette date, nous réservons à nos anciens
> clients une offre qui ne sera pas proposée au public.
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
> L'offre reste valable jusqu'au **31 octobre à minuit**.
> {{lien_offre}}
>
> Pr Rachid El Maataoui

### E3 · Mer. 28/10 · Ce que contient l'annuel
> Objet : Ce que les certificats changent concrètement
>
> Contenu : un parcours certifiant expliqué en 5 lignes (exemple : Chargé d'affaires PME, 5 cours,
> 6 à 8 semaines, examen final, identifiant vérifiable, badge LinkedIn) + un témoignage d'ancien
> + rappel du prix ancien client 179 € jusqu'au 31/10.

### E4 · Sam. 31/10 · Dernier jour
> Objet : Dernier jour pour votre tarif ancien client
>
> Bonjour {{prénom}}, l'ouverture publique de Xelanc a lieu demain. Votre tarif de 179 € pour
> l'année s'arrête ce soir à minuit ; ensuite, l'abonnement annuel revient à 299 €.
> {{lien_offre}}

### E5 · Mar. 03/11 · Repli
> Objet : Une autre façon de commencer
>
> Bonjour {{prénom}}, si l'abonnement annuel ne vous convient pas maintenant, vous pouvez
> accéder à tous les cours pour 29 € par mois, sans engagement, et passer à l'annuel quand vous le souhaitez.

## 5. Prérequis (avant le 21/10)

| # | Prérequis | Qui |
|---|---|---|
| 1 | Liste des acheteurs avec le cours acheté (Thinkific + Stripe, depuis le Mac) | Session Mac |
| 2 | Correspondance ancien cours → cours Xelanc, et accès ouvert pour chaque acheteur | Agent Site Xelanc |
| 3 | Lien de connexion qui marche (test avec un compte réel) | Agent Site Xelanc |
| 4 | Coupon ou lien de paiement « annuel 179 € » valable jusqu'au 31/10 23 h 59, réservé à la liste | Agent Site Xelanc |
| 5 | Crédits Brevo, envoi depuis un domaine authentifié (xelanc.com ou xelanc.org) | Rachid |
| 6 | Modèle WhatsApp WA-A soumis à Meta | Rachid |
| 7 | Un témoignage d'ancien pour E3 | Loubna |

## 6. Ce qu'on peut en attendre [H]

Hypothèses : 85 % d'emails délivrés, 50 % d'ouverture, 1,8 % s'abonnent seuls à 299 €,
9 % des restants prennent l'offre à 179 €, frais de paiement 4 %.

| Base | Abonnés seuls (299 €) | Offre (179 €) | **Total** | **Cash** |
|---|---|---|---|---|
| 73 acheteurs | 1 | 5–6 | **≈ 7** | **≈ 1,3 k€** |
| 400 acheteurs | 6 | 30 | **≈ 36** | **≈ 7 k€** |

Seuil d'alerte : moins de 5 % de conversion à J+7 → revoir l'objet des emails et appeler les ouvreurs.
