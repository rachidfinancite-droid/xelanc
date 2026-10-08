# Formules cash — Tête Grise

## 1. Chaîne de conversion (tunnel)

```
Dépense ads → Impressions → Clics → Leads → Leads qualifiés → RDV pris → RDV honorés → Ventes → Cash encaissé
```

| Taux | Formule |
|---|---|
| CTR | Clics ÷ Impressions |
| Taux de conversion page | Leads ÷ Clics |
| Taux de qualification | Leads qualifiés ÷ Leads |
| Taux de prise de RDV | RDV pris ÷ Leads qualifiés |
| Show-up | RDV honorés ÷ RDV pris |
| Closing | Ventes ÷ RDV honorés |
| Taux d'encaissement | Cash encaissé ÷ Montant vendu (sur la période d'échéance) |

**Ventes = Leads × Qualif × RDV × Show-up × Closing** — l'effet est multiplicatif :
+10 % sur n'importe quelle étape = +10 % de ventes. On attaque donc l'étape la
**moins chère à améliorer** pour ce +10 %, pas forcément la plus faible.

### Méthode du goulot (Δ cash)
Pour chaque étape i : `Δcash_i = Cash_30j × 10 %` ; coût d'amélioration estimé `C_i`.
Goulot = argmax(Δcash_i ÷ C_i). Ajuster si une étape est très loin de son benchmark
(le gain potentiel y dépasse 10 %).

## 2. Unit economics

| Indicateur | Formule | Seuil sain |
|---|---|---|
| CPL | Dépense ÷ Leads | selon panier |
| Coût par RDV honoré | Dépense ÷ RDV honorés | < 10–15 % du panier |
| CAC | (Dépense ads + coût commercial) ÷ Nouveaux clients | < 30 % du panier (offre unique) |
| Panier moyen (AOV) | CA ÷ Ventes | — |
| Marge de contribution | Panier − coût de delivery − CAC | > 0, idéalement > 50 % du panier |
| LTV | Panier × (1 + taux de rachat/upsell × nb achats futurs) × marge brute | LTV/CAC ≥ 3 |
| ROAS cash | Cash encaissé attribué ÷ Dépense ads | ≥ 3 pour scaler |
| Payback CAC | CAC ÷ Cash encaissé par client par mois | < 1 mois = machine à cash |

## 3. Vitesse du cash

```
Vitesse du pipeline (€/jour) = (Nb opportunités ouvertes × Taux de closing × Panier moyen) ÷ Cycle de vente (jours)
```
Leviers : plus d'opportunités, meilleur closing, panier plus élevé, cycle plus court.
**Raccourcir le cycle est souvent le levier le plus rapide** (offre limitée dans le
temps, acompte à la réservation, closing au premier appel).

```
Cash prévisionnel 30 j = Encaissements certains
                       + Σ_opportunités (Montant × Proba de closing × % payé sous 30 j × (1 − taux d'impayé))
```
Probas par défaut si non mesurées `[H]` : lead froid 2 %, lead qualifié 10 %,
RDV pris 20 %, RDV honoré 30 %, proposition envoyée 40 %, verbal OK 80 %.

```
Runway (mois) = Cash en banque ÷ (Charges fixes mensuelles + Dépense ads − Cash encaissé mensuel moyen)
```
(si le dénominateur ≤ 0 : cash-flow positif, runway infini — le dire.)

## 4. Benchmarks indicatifs `[E]` (formation/coaching/conseil haut de gamme, à remplacer par les mesures réelles dès que possible)

| Étape | Faible | Correct | Bon |
|---|---|---|---|
| CTR Meta (lead gen) | < 0,8 % | 1–1,5 % | > 2 % |
| Conversion landing → lead | < 10 % | 15–25 % | > 30 % |
| Conversion formulaire instantané Meta | < 5 % | 8–12 % | > 15 % |
| Lead → RDV pris | < 10 % | 15–25 % | > 30 % |
| Show-up | < 50 % | 60–70 % | > 80 % |
| Closing (offre > 1 000 €) | < 15 % | 20–30 % | > 35 % |
| Délai premier contact | > 24 h | < 1 h | < 5 min |

Toujours préciser que ces repères sont des ordres de grandeur ; les chiffres propres
au projet (historique dans `cash-state.yaml`) priment.
