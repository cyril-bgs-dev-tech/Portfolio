# 🏆 Compétitions Kaggle & Machine Learning

<div align="center">

[![Profil Kaggle](https://img.shields.io/badge/Profil%20Kaggle-cyrilbourgeois-20BEFF?style=for-the-badge&logo=kaggle&logoColor=white)](https://www.kaggle.com/cyrilbourgeois/competitions)

**35+ compétitions** · **7 top 4 %** · **3 top 1 %** · meilleur rang **#14 / 3 022**

*Palmarès complet et vérifiable sur le profil.*

</div>

---

### 📖 Comment lire ce palmarès

**Toutes ces compétitions n'ont pas reçu le même investissement — autant le dire que le laisser deviner.**

La majorité ont été menées sérieusement, du début à la fin. D'autres ont été engagées puis
laissées de côté : une semaine de travail initial, puis le temps a manqué. Sur celles-là,
**moins de 25 % du temps disponible a été réellement exploité**, et le classement retenu est
celui d'une soumission arrêtée en fin de mois.

Le rang de ces compétitions-là ne mesure donc pas le plafond de la méthode : il mesure ce
qu'elle rend en une semaine. **La démarche qui mène au top 1 % est comprise et reproduite** —
trois fois, sur trois domaines sans rapport entre eux : course automobile, irrigation agricole,
écoute de podcasts.

**499 notebooks** dans l'espace de travail Kaggle, dont la grande majorité restent privés :
brouillons, essais écartés, itérations qui n'ont pas vocation à être publiées. Le chiffre
donne l'ordre de grandeur du travail réel derrière les rangs affichés — il ne désigne pas
499 publications consultables, et il n'est pas vérifiable de l'extérieur.

### 🤖 Ce qui change en ce moment

La stratégie gagnante se déplace vers l'**agentique**. Là où l'on itérait à la main sur les
variables et les modèles, les compétiteurs déploient de plus en plus des **systèmes d'agents**
qui explorent, testent et sélectionnent les pistes en autonomie. C'est le même mouvement que
celui suivi par ailleurs sur mes projets — agent de diagnostic, orchestration de modèles — et
il est en train de redéfinir ce que veut dire « bien travailler » sur une compétition.

---

**Où en est ce projet** : activité continue — nouvelle compétition engagée régulièrement, en parallèle des autres projets.

---

::: {.panel-tabset}

## 🧑‍💼 Vue d'ensemble

**Le principe** : sur Kaggle, des milliers d'équipes dans le monde s'affrontent sur le même problème, avec les mêmes données, dans un délai fixé — un peu comme un concours d'algorithmes à l'échelle mondiale. Le classement final est objectif : même données pour tout le monde, un seul score qui compte.

**Pourquoi c'est une preuve utile** : contrairement à un projet personnel où on choisit son propre problème et ses propres critères de réussite, ici la difficulté et les règles sont imposées, et la comparaison se fait contre des milliers d'autres personnes, du débutant à l'expert. Finir dans le 1% mondial sur plusieurs compétitions différentes (course automobile, agriculture, écoute de podcasts...) montre une capacité à s'adapter vite à un nouveau domaine et à en extraire les bonnes informations, plutôt qu'une simple connaissance apprise par cœur sur un seul sujet.

**Ce que ça démontre concrètement** :
- Capacité d'apprentissage rapide sur des domaines très différents (35+ sujets distincts en 5 ans)
- Rigueur méthodologique (éviter de "tricher" en apprenant par cœur les données de test, une erreur fréquente chez les débutants)
- Veille technique active : intégration des toutes dernières techniques de recherche dès leur publication

## 🔧 Détails techniques

## 📊 Statistiques Globales

| Métrique | Valeur |
|----------|--------|
| Compétitions complétées | 35+ |
| Notebooks dans l'espace de travail | 499 *(majorité privés)* |
| Top 4% mondial | 7 compétitions |
| Top 1% mondial | 3 compétitions |
| Meilleur rang | #14 / 3 022 (Top 0.5%) |
| Domaines couverts | Régression, classification, NLP, time series, vision, anomalies |

---

## 🥇 Compétitions Top 1% Mondial

### 1. Predicting Irrigation Need - #32 / 4 315 équipes (Top 0.7%)
**Type** : Classification binaire/multi-classes  
**Contexte** : Prédiction des besoins en irrigation agricole

**Approche Feature Engineering** :
- Features temporelles : cumul de précipitations, évapotranspiration
- Indices de végétation dérivés (NDVI, NDWI)
- Lag features sur données météo (J-7, J-14, J-30)
- Rolling statistics (moyennes, écarts-types sur fenêtres glissantes)
- Encodages cycliques : jour de l'année, heure

**Modélisation** :
- Modèles dominants : LightGBM, XGBoost, CatBoost
- Feature selection : importance des features, SHAP
- Validation : Time series split

**Technologies** : Python, LightGBM, XGBoost, Pandas, Polars

---

### 2. Prediction F1 Pit Stop - #14 / 3 022 équipes (Top 0.5%)
**Type** : Régression/Classification  
**Contexte** : Prédiction de la durée ou du moment des arrêts aux stands en F1

**Approche Feature Engineering** :
- Features course : position, écart avec concurrents, tours restants
- Features pilote : historique pit stops, style de conduite
- Features équipe : performance moyenne aux stands
- Features conditions : température piste, météo, safety car
- Lag features : performance derniers tours

**Modélisation** :
- Modèles : XGBoost, LightGBM, CatBoost, réseaux neuronaux
- Feature importance : SHAP values pour interprétation
- Validation : K-fold stratifié par course
- Ensembling : Stacking avec régression métique

**Technologies** : Python, XGBoost, LightGBM, SHAP, Optuna

---

### 3. Predict Podcast Listening Time - #20 / 3 310 équipes (Top 0.6%)
**Type** : Régression  
**Contexte** : Prédiction du temps d'écoute de podcasts

**Approche Feature Engineering** :
- Features utilisateur : historique d'écoute, préférences, engagement
- Features podcast : durée, catégorie, popularité, invité
- Features interaction : match utilisateur-podcast
- Features temporelles : jour de la semaine, heure, saison
- Text features : NLP sur titres et descriptions (TF-IDF, embeddings)

**Modélisation** :
- Modèles tabulaires : LightGBM, XGBoost, CatBoost
- NLP : Embeddings de texte + concaténation avec features tabulaires
- Validation : Group K-fold (par utilisateur)

**Technologies** : Python, LightGBM, HuggingFace Transformers, Scikit-learn

---

## 🥈 Autres Compétitions Notables

### 4. Regression — California Housing - #14 / 689 équipes (Top 2%)
**Type** : Régression  
**Contexte** : Prédiction de prix immobiliers en Californie

**Approche** :
- Feature engineering : interactions géographiques, ratios
- Modèles : XGBoost, LightGBM, CatBoost, réseaux neuronaux
- Validation : K-fold stratifié par région

---

### 5. Regression — Abalone Dataset - #61 / 2 606 équipes (Top 2%)
**Type** : Régression  
**Contexte** : Prédiction de l'âge d'ormeau à partir de caractéristiques physiques

**Approche** :
- Feature engineering : ratios de mesures, transformations non-linéaires
- Modèles : Gradient Boosting, SVR, réseaux neuronaux

---

### 6. Steel Plate Defect Prediction - #88 / 2 199 équipes (Top 4%)
**Type** : Classification multi-label  
**Contexte** : Détection de défauts sur des plaques d'acier (industrie)

**Approche** :
- Feature engineering : features géométriques, statistiques de capteurs
- Gestion déséquilibre : SMOTE, class weights
- Modèles : XGBoost, LightGBM, Random Forest

---

### 7. Multi-Label Classification — Enzyme Substrate - #44 / 1 047 équipes (Top 4%)
**Type** : Classification multi-label  
**Contexte** : Prédiction de substrats enzymatiques (biologie/chimie)

**Approche** :
- Feature engineering : descripteurs moléculaires, fingerprints
- Gestion multi-label : Binary Relevance, Label Powerset
- Modèles : One-vs-Rest XGBoost, Classifier Chains

---

## 🛠️ Méthodologie Générale

### 1. Analyse Exploratoire (EDA)
- Statistiques descriptives (moyenne, médiane, écart-type, quantiles)
- Visualisations : distributions, corrélations, pair plots
- Détection de valeurs manquantes et outliers
- Analyse de la variable cible (distribution, déséquilibre)

**Outils** : Pandas, NumPy, Matplotlib, Seaborn, Plotly

### 2. Feature Engineering

#### Features Tabulaires
- **Interactions** : Multiplication, division, ratio entre features
- **Transformations** : Log, sqrt, polynomial, binning
- **Agrégations** : Group by + mean/std/min/max/count
- **Encodages** : One-hot, target encoding, frequency encoding
- **Normalisation** : StandardScaler, RobustScaler, MinMaxScaler

#### Features Temporelles
- **Lag features** : Valeurs à J-1, J-7, J-30, etc.
- **Rolling statistics** : Moyenne, écart-type sur fenêtres glissantes
- **Encodages cycliques** : Sin/cos pour jour, mois, heure
- **Date features** : Jour de la semaine, mois, trimestre, année

#### Features Textuelles (NLP)
- **Bag of Words** : CountVectorizer, TfidfVectorizer
- **Embeddings** : Word2Vec, GloVe, FastText
- **Transformers** : BERT, CamemBERT (fine-tuning ou features extraites)

### 3. Modélisation

#### Algorithmes Utilisés
**Gradient Boosting** (dominants en tabulaire) :
- **XGBoost** : Robuste, rapide, bien supporté
- **LightGBM** : Plus rapide sur gros datasets, leaf-wise growth
- **CatBoost** : Excellent pour catégorielles, peu de preprocessing

**Réseaux Neuronaux** :
- **TabM** : Architecture récente, state-of-the-art tabulaire
- **TabICL2** : In-context learning pour tabulaire
- **RealMLP** : MLP avec améliorations récentes
- **LSTM/GRU** : Séquences temporelles
- **Transformers** : NLP, time series

#### Stratégies d'Ensembling
**Stacking** :
- Niveau 1 : Modèles de base (XGBoost, LightGBM, CatBoost, NN)
- Niveau 2 : Méta-modèle (régression linéaire, Ridge)
- Validation : Out-of-fold predictions pour éviter overfitting

### 4. Validation et Optimisation

#### Validation Croisée
- **K-Fold** : Standard, Stratifié, Group K-fold, Time Series Split

#### Optimisation Hyperparamètres
- **Optuna** : Optimisation bayésienne (TPE sampler), pruning, 100-500 trials
- **Grid Search** : Ajustements fins après Optuna

### 5. Interprétabilité

#### SHAP (SHapley Additive exPlanations)
- Feature importance globale
- Visualisation des impacts (summary plot, dependence plot)
- Explication de prédictions individuelles (force plot)

---

## 📊 Répartition par Type de Problème

| Type | Nombre | Meilleur Top % |
|------|--------|----------------|
| Régression | 10+ | 2% |
| Classification binaire | 12+ | 0.7% |
| Classification multi-classes | 6+ | 0.7% |
| Classification multi-label | 4+ | 4% |
| Time Series | 5+ | 0.5% |
| NLP | 3+ | 0.6% |

---

## 📈 Évolution des Performances

| Période | Performance | Approche |
|---------|-------------|----------|
| **2021-2022** | Top 20-30% | Modèles standards, peu de feature engineering |
| **2023-2024** | Top 5-10% | Feature engineering intensif, ensembling |
| **2025-2026** | Top 1-2% | Approche systématique, veille active (TabM, TabICL2) |

---

## 🛠️ Technologies Maîtrisées

| Catégorie | Technologies |
|-----------|-------------|
| **Langages** | Python (avancé), SQL |
| **ML/DL** | Scikit-learn, XGBoost, LightGBM, CatBoost, PyTorch, TensorFlow, HuggingFace |
| **Feature Engineering** | Pandas, NumPy, Polars, RAPIDS (GPU) |
| **Optimisation** | Optuna, Scikit-learn GridSearch |
| **Visualisation** | Matplotlib, Seaborn, Plotly |
| **Versioning** | Git, DVC |

---

## 🎯 Valeur Ajoutée pour l'Entreprise

### Compétences Démontrées
1. **Capacité d'apprentissage rapide** : Top 1% sur des domaines variés (agriculture, F1, podcasts)
2. **Feature engineering avancé** : Création de features pertinentes dans tous les domaines
3. **Maîtrise état de l'art** : Test et intégration des dernières avancées (TabM, TabICL2, RealMLP)
4. **Rigueur expérimentale** : Validation croisée, reproductibilité, interprétabilité
5. **Optimisation systématique** : Optimisation bayésienne, ensembling, stacking

### Applications Business
- **Pricing** : Prédiction de prix
- **Détection de fraude** : Classification binaire et détection d'anomalies
- **Segmentation clients** : Clustering et classification multi-classes
- **Prévision demande** : Time series et feature engineering temporel
- **NLP** : Analyse de sentiments, classification de textes
- **Recommandation** : Features d'interaction, modèles de ranking

---

## 🎓 Leçons Apprises

### Leçons Techniques
1. **Feature engineering > Modèle complexe** : De bonnes features battent souvent un modèle sophistiqué
2. **Validation rigoureuse** : Une bonne validation évite l'overfitting et les surprises
3. **Diversité des modèles** : L'ensembling de modèles diversifiés est puissant
4. **Domain knowledge** : Comprendre le domaine aide à créer de meilleures features
5. **Itération rapide** : Mieux vaut tester beaucoup d'idées simples que peu d'idées complexes

### Leçons Stratégiques
1. **Choisir ses batailles** : Se concentrer sur les compétitions où on a un avantage
2. **Collaboration** : Rejoindre des équipes pour combiner les forces
3. **Partage** : Partager ses approches apprend aux autres et renforce sa propre compréhension
4. **Veille** : Rester à jour sur les dernières avancées est crucial
5. **Patience** : Les améliorations marginales s'accumulent

:::

---

**Dernière mise à jour** : Août 2026  
**Contact** : cyril.bgs.dev.tech@gmail.com
