# 🎓 Projets Master 2 - Data Scientist (2023-2024)

> 💻 **Le code des 7 projets est consultable** : [projets_Master_2](https://gitlab.com/cyril.bgs.dev/projets_Master_2) — notebooks avec leurs sorties, sans les jeux de données.

**Formation** : OpenClassrooms + Centrale Supélec  
**Alternance** : MICHELIN, Direction Opérationnelle (Fév 2023 - Fév 2024), 39h/semaine, 4 jours/5 en entreprise  
**Durée** : 12 mois  
**Projets réalisés** : 7 projets validés

**Où en est ce projet** : formation et alternance terminées et validées (2024). Le code réalisé chez Michelin reste confidentiel (données propriétaires de l'entreprise) ; les **notebooks académiques sont versionnés dans le dépôt dédié**, sans les jeux de données.

---

## 🧑‍💼 Vue d'ensemble

Cette deuxième année (2023-2024) associe une formation avancée (deep learning, NLP, séries temporelles) à une alternance d'un an chez Michelin.

**La mission Michelin en une phrase** : un POC de parsing et de matching de données complexes venant de sources multiples, à l'échelle continentale, mené de la spécification jusqu'au scoring.

**L'impact** : des demandes traitées sous 24 h contre environ 2 semaines, via la seconde chaîne de traitement exploitable (retour du Product Owner) ; qualité et clarté du code saluées par plusieurs Product Owners.

**Le reste de l'année** : projets académiques sur des cas variés (application santé publique, prévision de consommation énergétique, segmentation client e-commerce, classification automatique de texte, reconnaissance d'images).

## 🏭 Alternance Michelin - POC Parsing/Matching de Données Complexes

**Statut** : ✅ Validé - Alternance réussie  
**Durée** : 12 mois (Fév 2023 - Fév 2024)  
**Contexte** : Direction Opérationnelle ; données complexes issues de sources multiples, à l'échelle continentale

### Problématique
- Rapprocher automatiquement des données complexes issues de sources multiples et hétérogènes, à l'échelle continentale
- Fiabiliser la qualité des données en amont du rapprochement

### Missions Réalisées
- POC de parsing / matching de données complexes multi-sources, de la spécification au scoring
- Pipeline qualité : nettoyage, normalisation, expressions régulières, matching
- Travaux sur des tests de non-régression automatisés
- Explication du fonctionnement du POC en réunion d'équipe, accessible à un public non expert

### Résultats
- Demandes traitées sous 24 h contre environ 2 semaines, via la seconde chaîne de traitement exploitable (retour du Product Owner)
- Qualité et clarté du code saluées par plusieurs Product Owners
- Clarté des explications soulignée par le manager direct en fin de projet

### Feedback Michelin
Lettre de recommandation, Antoine DANIEL LAMAZIERE (Product Owner) et l'architecte data, Michelin (extraits) :
- *« Son implication et sa capacité constante à se challenger ont été particulièrement appréciées. »*
- *« Cyril a démontré une maîtrise des solutions de développement que nous utilisons, ainsi qu'une réelle compétence dans leur mise en œuvre. »*
- *« Il a également su être force de proposition. »*
- *« Parmi ses réalisations, on peut notamment souligner un POC de parsing et de mapping qu'il a mené avec succès. »*

---

## 🧠 Projets Académiques

### Projet 1 : Définissez Votre Stratégie d'Apprentissage
**Statut** : ✅ Validé

**Objectifs** :
- Définir une stratégie d'apprentissage personnalisée
- Planifier le parcours Master 2
- Identifier les ressources et outils

**Feedback** : *"Cadre de la formation bien défini, objectifs clairs. Très bonne soutenance."*

---

### Projet 2 : Concevez une Application au Service de la Santé Publique
**Statut** : ✅ Validé

**Contexte** : Application data science pour la santé publique

**Réalisation** :
- Analyse de données de santé
- Modélisation prédictive
- Visualisation et recommandations

**Feedback** : *"Livrables complets, répondent à la problématique. Analyse pertinente des données, traitements outliers et valeurs manquantes bien réalisés."*

---

### Projet 3 : Anticipez les Besoins en Consommation de Bâtiments
**Statut** : ✅ Validé

**Contexte** : Prédiction de consommation énergétique

**Réalisation** :
- Feature engineering temporel
- Modèles de régression
- Prévisions de consommation

**Feedback** : *"Valeurs manquantes très bien réalisées, beaucoup de recherches. Data leakage bien identifié et écarté. Très bon score de R². Félicitations."*

---

### Projet 4 : Segmentez des Clients d'un Site E-commerce
**Statut** : ✅ Validé

**Contexte** : Segmentation client pour e-commerce

**Réalisation** :
- Clustering (K-Means, CAH)
- Analyse comportementale
- Recommandations business

**Feedback** : *"Présentation claire et agréable, support de qualité professionnel. Bonne compréhension des approches de clustering, clusters bien interprétés."*

---

### Projet 5 : Catégorisez Automatiquement des Questions
**Statut** : ✅ Validé

**Contexte** : Classification automatique de textes (NLP)

**Réalisation** :
- Pipeline NLP (tokenization, vectorization)
- Modèles de classification de textes
- TF-IDF, embeddings, transformers

**Feedback** : *"Travail de grande qualité, répond parfaitement aux critères de validation. Bon niveau technique et solides compétences en communication."*

---

### Projet 6 : Classez des Images à l'Aide d'Algorithmes de Deep Learning
**Statut** : ✅ Validé

**Objectifs pédagogiques** :
- Maîtriser les architectures CNN (Convolutional Neural Networks)
- Transfer learning avec modèles pré-entraînés
- Data augmentation et régularisation

**Réalisation** :
- Architectures testées : CNN custom, ResNet, VGG, EfficientNet
- Framework : TensorFlow/Keras ou PyTorch
- Prétraitement d'images (normalisation, redimensionnement)
- Data augmentation (rotation, flip, zoom)
- Transfer learning et fine-tuning
- Gestion du surapprentissage (dropout, batch normalization)

**Technologies** : Python, TensorFlow/PyTorch, CNN, Transfer Learning

**Feedback** : *"Points forts : prétraitements, CNN from scratch, transfer learning, data augmentation, fine-tuning."*

---

### Projet 7 : Développez une Preuve de Concept (Option Stage)
**Statut** : ✅ Validé

**Contexte** : POC pour validation des acquis avant stage/alternance — classification sur données tabulaires, test d'une famille d'algorithmes récente (TabPFN) comparée aux approches ensemblistes (XGBoost, LightGBM, CatBoost)

**Réalisation** :
- Projet intégrateur combinant plusieurs compétences
- Démonstration de capacité à mener un projet de bout en bout
- Présentation et soutenance

**Feedback** : *"Sujet pertinent, sources sérieuses consultées et bien articulées. Présentation claire."*

---
