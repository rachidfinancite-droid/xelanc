# Tableau de bord et règles d'ajustement — lancement Xelanc

Les cibles viennent de la prévision de la Tête Grise du 2026-10-17 (central = cible,
pessimiste = plancher). Quand la Tête Grise publie une nouvelle prévision, on reprend
ses chiffres ici.

## 1. L'entonnoir et ses indicateurs

| Maillon | Indicateur | Définition | Source |
|---|---|---|---|
| Atteinte | Délivrabilité, ouverture, clic | Délivrés ÷ envoyés ; ouvreurs uniques ÷ délivrés ; cliqueurs ÷ délivrés | Brevo |
| Atteinte | Plaintes, désinscriptions | Plaintes ÷ délivrés ; désinscrits ÷ délivrés | Brevo |
| Visite → compte | Taux d'inscription | Comptes gratuits ÷ visites de la page d'inscription | GA4 + WordPress |
| Activation | Taux d'activation | Comptes ayant vu une 1re capsule sous 48 h ÷ comptes créés | Plateforme de cours |
| Paiement | Conversion compte → payant | Nouveaux payants ÷ comptes créés sur la même période (cumul depuis J0) | WooCommerce, Stripe, PawaPay |
| Paiement | Mix des formules | Part mensuel / annuel / premium dans les nouveaux payants | WooCommerce |
| Paiement | Échecs de paiement | Paiements échoués ÷ tentatives, par moyen et par pays | Stripe, PawaPay |
| Rétention | Résiliation mensuelle | Résiliés du mois ÷ abonnés mensuels actifs en début de mois | WooCommerce |
| Rétention | Passage à l'annuel | Mensuels passés à l'annuel ÷ mensuels actifs | WooCommerce |
| Cash | Cash net encaissé | Encaissé − frais de paiement, par semaine et par vague | Passerelles |
| Pub | Coût par compte, coût par vente, pub ÷ cash | Dépense ÷ comptes ; dépense ÷ ventes attribuées ; dépense ÷ cash net | Adspirer + passerelles |

## 2. Cibles et seuils

| Indicateur | Cible (central) | Plancher (pessimiste) | Alerte |
|---|---|---|---|
| Nouveaux payants | nov. 158 · déc. 142 · janv. 109 [E] | 46 · 42 · 32 | < 60 % de la cible de la semaine |
| Cash net encaissé | nov. 30 k€ · déc. 30 k€ · janv. 25 k€ (≈ 85 k€ sur 3 mois) [E] | 7 · 7 · 6 k€ | < 60 % de la cible de la semaine |
| Comptes gratuits, hors bases | ≈ 3 000 / mois (≈ 700 / semaine) [H] | 1 500 / mois | < 60 % deux semaines de suite |
| Conversion compte → payant | 0,8 % à J+7 · 1,5 % à J+30 · 2,5 % à J+90 [H] | 1,5 % à J+90 | < 0,4 % à J+7 |
| Activation sous 48 h | ≥ 40 % [H] | 25 % | < 25 % |
| Part annuel + premium | ≥ 55 % | 40 % | < 40 % |
| Résiliation mensuelle | ≤ 9 % | 13 % | > 12 % |
| Échecs de paiement | < 5 % | 10 % | > 10 % |
| Délivrabilité | ≥ 97 % | 95 % | < 95 % |
| Ouverture | ≥ 35 % anciens · ≥ 25 % bases froides | 25 % · 18 % | sous le plancher |
| Plaintes | < 0,1 % | 0,3 % | > 0,3 % (arrêt de la base) |
| Coût par vente (pub) | ≤ 60 € [H] | 120 € | > 120 € sur 7 jours |
| Dépense pub ÷ cash net | ≤ 20 % | 30 % | > 30 % |

Feux : vert ≥ 90 % de la cible ; orange 60–90 % ; rouge < 60 % ou seuil d'alerte franchi.

## 3. Règles d'ajustement (si → alors)

Ordre des ajustements : du moins cher au plus cher. Un seul ajustement majeur par
indicateur et par semaine. Chaque ajustement est noté au journal avec son effet attendu.

| Signal | Diagnostic probable | Ajustements, dans l'ordre | Vérifier après |
|---|---|---|---|
| Délivrabilité < 95 % ou rebonds > 3 % | Liste ancienne, domaine froid | Stopper le lot · nettoyer la liste (validation) · réchauffer le domaine par lots de 200 en commençant par les engagés | 1 lot |
| Plaintes > 0,3 % | Message perçu comme du spam | Arrêter la base · rappeler la relation dès la 1re ligne (« vous avez suivi… ») · expéditeur au nom de Rachid · désinscription visible | Immédiat, puis 1 lot test |
| Ouverture sous le plancher | Objet, expéditeur ou moment | Test A/B d'objet sur 2 × 10 % du lot · envoi mar.–jeu. 9 h–11 h · renvoi J+3 aux non-ouvreurs avec un autre objet | 1 lot (≥ 1 000 envois) |
| Clics corrects, inscription < 15 % | Page d'inscription | Moins de champs · promesse « 1 cours offert » · preuve (témoignage, logo) au-dessus du bouton | 7 jours |
| Comptes corrects, activation < 40 % | Onboarding | Email J0 « commencez par cette capsule » · WhatsApp de bienvenue · capsule de 5 min en accès direct | 7 jours |
| Activation correcte, conversion < 0,8 % à J+7 ou < 1,5 % à J+30 | Valeur ou prix perçus | Cours à 13,90 € comme 1er achat · appel de Loubna aux 5 % les plus actifs · live Q&R de Rachid avec offre à échéance réelle | 14 jours |
| Part annuel + premium < 40 % | Valeur du certificat pas comprise | Montrer un certificat et le badge LinkedIn · rappeler 12 × 29 € = 348 € contre 299 € · bonus annuel limité dans le temps | 14 jours |
| Échecs de paiement > 10 % | Passerelle, pays, moyen de paiement | Suspendre les envois · tester carte et Mobile Money par pays · lien WhatsApp de secours avec paiement assisté | Immédiat |
| Résiliation mensuelle > 12 % | Pas de valeur perçue au 1er mois | Séquence d'activation · annonces des sorties du catalogue · offre de passage à l'annuel au 2e mois | 30 jours |
| Coût par vente > 120 € sur 7 jours | Pub mal ciblée ou mauvaise accroche | Couper l'ensemble de publicités · garder l'accroche gagnante · retester l'audience (règle de l'Orchestre) | 7 jours |
| Comptes < 60 % de la cible deux semaines de suite | Trafic insuffisant | Accélérer les lots des bases · live supplémentaire · rythme LinkedIn de Rachid · pub seulement si G3 est passée | 14 jours |
| Sortie de compétence en retard | Promesse publique tenue en retard | Prévenir les inscrits avant la date · nouvelle date · pas de silence | Immédiat |

## 4. Discipline de test

- Échantillon minimal avant de conclure : 1 000 envois (objet), 300 comptes (conversion),
  10 ventes (coût par vente).
- Pas de conclusion sur un week-end seul ; comparer à la même période de la semaine précédente.
- Chaque test a son hypothèse écrite avant (« si X, alors Y passe de A à B »).
