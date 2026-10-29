# Classement des prospects et fiche par personne · Méthode

**Version** : 29/10/2026 · Ce document donne la méthode et les modèles, sans données personnelles.
Les fiches nominatives restent sur le Mac de Rachid (`~/Travail/GTM-XELANC/prospects/`), jamais dans ce dépôt.

## 1. Les signaux que l'on relève pour chaque personne

| Signal | Source | Poids |
|---|---|---|
| A payé | WooCommerce | Client |
| Commande créée, non payée (virement, Mobile Money) | WooCommerce | +5 |
| Panier avec email saisi sur la page de paiement | FunnelKit | +4 |
| A écrit sur WhatsApp, a appelé, a demandé un prix ou un moyen de paiement | WhatsApp, Loubna | +4 |
| A regardé au moins une capsule | LearnWorlds | +3 |
| A vu la page des formules ou une page certificat | Site (pixel, GA4) | +2 |
| A ouvert ou cliqué un email Xelanc | Brevo | +1 (ouverture) · +2 (clic) |
| Inscription gratuite | WordPress (xelanc_signup_source) | +1 |
| Profil en poste dans la finance ou la banque (RAF, chargé d'affaires, analyste…) | Formulaire, LinkedIn, appel | +2 |
| Ancien client ou contact Financité | Thinkific, Stripe, Pipedrive | +3 |
| Inactif depuis plus de 14 jours | Toutes sources | −2 |

## 2. Les niveaux de chaleur

| Niveau | Score | Exemple | Action | Délai |
|---|---|---|---|---|
| 🔥 **Brûlant** | 8 et plus, ou commande non payée | A voulu payer et a été bloqué | **Appel immédiat**, paiement accompagné | Sous 24 h |
| 🟠 **Chaud** | 5 à 7 | Panier ou WhatsApp, a regardé l'offre | Appel, lien de paiement prêt | Sous 48 h |
| 🟡 **Tiède** | 3 à 4 | Inscrit, a regardé une capsule ou une page certificat | Appel de découverte, puis relance | Sous 5 jours |
| 🔵 **Froid** | 1 à 2 | Inscrit sans autre signal | WhatsApp de bienvenue, relance automatique | Sous 7 jours |
| ⚪ **Perdu ou hors cible** | — | Pas intéressé, étudiant sans projet, numéro faux | Relance automatique seulement | — |

**Comportements à distinguer** (une étiquette par personne, en plus de la chaleur) :
- **Bloqué au paiement** : il voulait payer, le parcours l'en a empêché. Priorité absolue.
- **Acheteur réfléchi** : regarde beaucoup, compare, revient. A besoin de preuves.
- **Payeur employeur** : en poste, mentionne son entreprise. A besoin d'une facture ou d'un devis.
- **Curieux** : inscrit, rien d'autre. A besoin d'une première capsule.
- **Ancien de Financité** : connaît la maison. A besoin du pont « Financité devient Xelanc ».

## 3. La fiche globale (tableau de pilotage)

Une ligne par personne, triée par chaleur puis par score :

| Chaleur | Score | Prénom Nom | Pays / ville | Poste | Source | Date d'inscription | Dernier signal (date) | Comportement | Objection connue | Prochaine action | Qui | Date |
|---|---|---|---|---|---|---|---|---|---|---|---|---|

## 4. La fiche individuelle (modèle)

```
# [Prénom NOM] · [chaleur] · score [x]

## Identité
- Pays, ville :
- Téléphone / WhatsApp :
- Email :
- Poste, structure (si connus) :
- Profil LinkedIn (si trouvé) :

## D'où il vient
- Source : pub Meta [campagne, pub], email, WhatsApp, recherche, bouche-à-oreille, ancien Financité
- Date et heure d'inscription :
- Page d'arrivée et cours d'origine (xelanc_cours_origine) :

## Ce qu'il a fait (chronologie datée)
- [date] inscription gratuite
- [date] capsule regardée : …
- [date] page formules / certificat vue : …
- [date] panier : formule, montant
- [date] commande : n°, statut, moyen de paiement
- [date] email ouvert / cliqué : …
- [date] message WhatsApp : …

## Ce qu'on sait de lui
- Objectif de carrière :
- Certificat qui l'intéresse :
- Ancien client Financité : oui / non (cours, montant, année)
- Objection connue :
- Moyen de paiement probable :

## Ce qu'on lui propose
- Formule conseillée et pourquoi :
- Argument principal (dans ses mots) :
- Ce qu'on lui envoie avant ou pendant l'appel :

## Historique des appels
| Date | Joint | Résultat | Objection | Prochaine action |
```
