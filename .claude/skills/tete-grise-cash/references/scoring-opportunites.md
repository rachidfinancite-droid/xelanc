# Grille d'opportunités — marchés, bassins, pays, villes, fonctions

Un **bassin** = une combinaison *zone géographique × fonction/métier cible × offre*.
Exemples : « Casablanca × directeurs financiers PME × Programme Excellence »,
« Diaspora France × cadres bancaires × Coaching Excellence ».

## Étape 1 — Dimensionner (TAM → SAM → SOM)

| Niveau | Calcul | Source typique |
|---|---|---|
| **TAM** (marché total) | Population de la fonction dans la zone × panier annuel | Stats nationales de l'emploi, LinkedIn (taille d'audience), associations pro, rapports sectoriels |
| **SAM** (adressable) | TAM × % solvable (revenu ≥ seuil ou employeur payeur) × % atteignable par nos canaux (langue, ciblage ads possible) | Grilles de salaires, audience Meta/LinkedIn réelle |
| **SOM 12 mois** (captable) | SAM × part de marché réaliste (0,1–2 % la 1re année) | Historique de conversion, concurrence |

Règle : partir **toujours** du nombre de personnes exerçant la fonction, jamais de la
population générale. Vérifier avec la taille d'audience estimée par la plateforme ads
quand c'est possible.

## Étape 2 — Cash Potentiel 90 jours

```
CP90 = Audience atteignable × Taux lead × Taux de conversion lead→vente × Panier × % encaissé sous 90 j
```
Les taux viennent de l'historique (`cash-state.yaml`) ; à défaut des benchmarks de
`formules.md` §4, ajustés par les facteurs ci-dessous.

## Étape 3 — Score Cash Bassin (SCB)

Noter chaque facteur de 1 à 5 :

| Facteur | 1 | 5 |
|---|---|---|
| **S** Solvabilité | Pouvoir d'achat faible vs prix, pas de financement employeur | Prix < 10 % du revenu mensuel, ou entreprise payeuse |
| **A** Accessibilité | Pas de ciblage ads précis, pas de réseau | Ciblage précis + réseau/communauté existante + langue maîtrisée |
| **V** Vitesse | Cycle > 60 j, plusieurs décideurs | Décision individuelle < 14 j |
| **D** Douleur/urgence | « Nice to have » | Enjeu carrière/revenu immédiat, deadline réglementaire |
| **C** Concurrence (inversée) | Marché saturé, prix cassés | Peu d'offres crédibles au même niveau |
| **E** Coût d'entrée (inversé) | CPM élevé, nouvelle langue/logistique | CPM bas, infrastructure déjà en place |

```
SCB = CP90_normalisé × (S × A × V × D × C × E)^(1/6)
```
(`CP90_normalisé` = CP90 du bassin ÷ CP90 max de la liste, donc entre 0 et 1 ;
la moyenne géométrique pénalise fortement un facteur à 1.)

Un facteur noté **1 sur S ou A est éliminatoire** pour un objectif cash à 90 jours —
le signaler même si le score global est bon.

## Étape 4 — Recommandation et test

Pour le bassin n°1, fournir systématiquement :
- **Test minimal** : budget (en général 10–15 × CPL cible pour avoir ~10–15 leads),
  durée (7–14 j), canal, créa/angle.
- **Critère go/no-go chiffré** : ex. « CPL ≤ X € et ≥ 2 RDV honorés → on scale ×3 ;
  sinon on coupe ».
- **Cash attendu si go** sur 90 j (scénario central + pessimiste).

## Gabarit de tableau de sortie

| # | Bassin (zone × fonction) | SAM [E] | CP90 [E] | S | A | V | D | C | E | SCB | Verdict |
|---|---|---|---|---|---|---|---|---|---|---|---|

Verdicts possibles : **Attaquer maintenant** · **Tester** · **Plus tard** · **Non**.
