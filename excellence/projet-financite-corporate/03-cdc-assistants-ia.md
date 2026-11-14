# Cahier 03 · Les assistants IA · v1 · 14/11/2026

**Objet** : règles communes à toutes les fonctions d'IA (bibliothèque, copilote, simulateurs commentés, 4 assistants) et fiche de synthèse de chaque assistant.
**Fiches détaillées** : `excellence/assistants/`.

---

## 1. La base de connaissance [D]

**Principe** : les assistants apprennent la méthode de Rachid **dans ses cours, de A à Z**.

| Couche | Contenu | Rôle |
|---|---|---|
| **Les cours complets** | Scripts, transcriptions, diapositives, cas, modèles | L'assistant retrouve et cite le passage exact |
| **Le recueil de règles** | Règles extraites des cours : situation, règle, pourquoi, à éviter, source | Réponses constantes et testables |
| **Les références locales** | SYSCOHADA révisé, CGNC, fiscalité par pays, calendriers | Exactitude locale |
| **Les bases Financité** | Financeurs et options par pays, ratios sectoriels | Recommandations concrètes |

**Processus** :
1. Inventaire des cours.
2. Collecte en texte.
3. Extraction des règles par Claude.
4. **Validation par Rachid, règle par règle.**
5. Indexation.
6. Mise à jour à chaque nouveau cours.

Méthode détaillée : `excellence/assistants/base-de-connaissance-assistants.md`.

---

## 2. Les règles communes à toutes les réponses

1. **Ne jamais inventer un chiffre ni une règle.** Demander la donnée manquante.
2. **Citer la source** : cours, norme, article, base Financité.
3. **Adapter au profil** : pays, référentiel comptable, secteur.
4. **Dire quand il ne sait pas**, et proposer un expert.
5. **Envoyer automatiquement vers un expert** les sujets à risque : contentieux, contrôle fiscal en cours, procédure collective, montants au-delà d'un seuil, restructuration.
6. **Mention obligatoire** sur les livrables : « Analyse d'aide à la décision. À faire valider avant tout engagement. »
7. **Ton** : celui d'un financier senior qui conseille. Clair, direct, phrases courtes, chiffres expliqués.
8. **Confidentialité** : ne rien conserver au-delà de la question, sauf livrable enregistré par l'utilisateur.

---

## 3. Les assistants

### 3.1 Bibliothèque de compétences à la demande
- **Entrée** : une question (« Comment calculer la VAN ? »).
- **Sortie** : une fiche en 10 blocs (cahier 04).
- **Modèle** : fiches préparées et relues pour les 100 plus demandées ; génération au même format pour les autres.

### 3.2 Copilote du quotidien
- **Entrée** : une question, ou un texte ou un document collé pour la question du moment.
- **Sortie** : réponse sourcée, ou rédaction prête (email, courrier, note, réponse à un auditeur).
- **Domaines** : fiscalité, comptabilité, gestion, banque, Excel, lecture de contrats et de factures.

### 3.3 Simulateurs express
- Calcul fait par le code (exact), commentaire fait par l'IA (interprétation et recommandation).
- Liste : devis, délai client, escompte, coût réel d'un crédit, coût d'un salarié par pays, seuil de rentabilité, calculs fiscaux.

### 3.4 Assistant Crédit (dette bancaire) [D : distinct de la levée de fonds]
- **Saisie guidée** : entreprise, besoin, chiffres (états financiers ou 12 chiffres clés), dettes, garanties, banques actuelles.
- **Analyse** : indicateurs du banquier, **score de bancabilité sur 100**, produit de crédit adapté à l'objet.
- **Livrable** : stratégie de financement bancaire (ce que vous pouvez faire, ce qu'il faut éviter, votre stratégie, les banques et financeurs à approcher), note de présentation à la banque, liste des pièces, comparaison des offres, arguments de négociation.
- Fiches : `fiche-assistant-banque-credit-v1.md`, `fiche-assistant-strategie-financement-v1.md`.

### 3.5 Assistant Levée de fonds (capital)
- **Saisie guidée** : idem, plus l'actionnariat, la dilution acceptée et le stade de l'entreprise.
- **Analyse** : **score de maturité pour investisseurs**, type de financement en fonds propres adapté.
- **Livrable** : stratégie de levée de fonds (options, à éviter, montage, séquencement, investisseurs à approcher), structure de la présentation aux investisseurs, résumé de l'opportunité, liste de la salle de données.
- Fiche détaillée : à produire (v1 en cours, sur le modèle de l'assistant Crédit).

### 3.6 Assistant Valorisation
- **Analyse** : 3 méthodes (flux actualisés, comparables, patrimoniale), prime de risque pays, décote d'illiquidité, sensibilités.
- **Livrable** : note de valorisation avec une fourchette et les arguments de négociation.
- Fiche détaillée : à produire.

### 3.7 Assistant Création de valeur et business model
- **Analyse** : comparaison aux bonnes pratiques et aux ratios du secteur (marges, BFR, coûts, délais), leviers chiffrés.
- **Livrable** : diagnostic de création de valeur, liste chiffrée des gains, plan d'action à 90 jours.
- Fiche détaillée : à produire.

---

## 4. La qualité

| Élément | Règle |
|---|---|
| **Cas de référence** | 10 par assistant (20 pour la bibliothèque), avec la réponse validée par Rachid |
| **Seuil de lancement** | ≥ 80 % de réponses jugées justes |
| **Repasse** | À chaque modification d'instructions, de modèle ou de base de connaissance |
| **Retour utilisateur** | Bouton 👍/👎 et commentaire sur chaque réponse ; revue hebdomadaire des 👎 |
| **Revue mensuelle** | 20 réponses tirées au hasard, relues par un expert |

---

## 5. Les coûts [estimations au 14/11, API Claude]

| Usage | Coût estimé |
|---|---|
| Fiche compétence préparée (servie depuis la base) | ≈ 0 |
| Question au copilote | ≈ $0,02 à 0,04 |
| Analyse d'un document de 40 pages | ≈ $0,15 à 0,30 |
| Livrable d'assistant complet | ≈ $1 à 3 |

**Cible** : ≤ $6 à 8 par place DAF et par mois en moyenne. **Leviers** : crédits, choix du modèle selon la tâche, mise en cache, fiches préparées, traitement différé pour les envois périodiques.
Détail : `excellence/assistants/assistants-ia-architecture-et-couts-2026-11-14.md`.
