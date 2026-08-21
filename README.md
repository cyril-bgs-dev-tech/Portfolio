<div align="center">

# 🚀 Cyril BOURGEOIS

### Data scientist — qualité de l'air, détection d'anomalies, systèmes MLOps observables

![License](https://img.shields.io/badge/License-MIT-10B981?style=for-the-badge)

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-0077B5?style=for-the-badge&logo=linkedin)](https://www.linkedin.com/in/cyril-bourgeois-65a739150/)
[![Email](https://img.shields.io/badge/Email-Contact-D14836?style=for-the-badge&logo=gmail)](mailto:cyril.bgs.dev@gmail.com)
[![Kaggle](https://img.shields.io/badge/Kaggle-Top%201%25-20BEFF?style=for-the-badge&logo=kaggle)](https://www.kaggle.com/cyrilbourgeois)

---

</div>

## 🎯 À Propos

Je construis et j'audite des chaînes de données de bout en bout : des prévisions européennes de qualité de l'air corrigées **sans aucune observation du lieu prédit**, du routage de détecteurs d'anomalies par domaine, des pipelines temps réel où l'humain garde la décision. Chaque chiffre publié ici est relié à son protocole et régénérable par un script nommé.


### 🏆 Faits Marquants

<table>
<tr>
<td width="33%" valign="top">
  
**🥇 Kaggle Top 1%**
- 35+ compétitions
- 3 top 1% mondial
- Meilleur rang : #14/3022

</td>
<td width="33%" valign="top">
  
**🔬 Benchmarks SOTA**
- ADBench : 47 datasets
- TSB-AD : 870 séries U + 200 M
- TSB-AD : 2 scores reproduits à l'identique<br>ADBench : 5 détecteurs réexécutés

</td>
<td width="33%" valign="top">
  
**⚙️ MLOps Temps Réel**
- DAG 9 workers · pool de 3 réplicas CPU + 1 GPU
- Dashboard 40+ pages RASCI
- Observabilité Prometheus/Grafana

</td>
</tr>
</table>

---

## 💼 Expérience Professionnelle

<div align="center">

### 🏭 Data Scientist - MICHELIN (Alternance)
*Février 2023 - Février 2024 · 39h/semaine, 4 jours/5 en entreprise*

</div>

**POC Parsing/Matching de Données Complexes — Niveau Continental**

🎯 **Mission** : Réalisation d'un POC de parsing/matching de données complexes, niveau continental

✨ **Réalisations** :
- 🎯 Augmentation considérable du taux de détection des correspondances
- 🧹 Nettoyage et qualité des données, analyses spécifiques autour du pricing niveau mondial
- ✅ Tests de non régression

💡 **Impact** :
- Vitesse d'exécution et résultats jugés excellents d'après plusieurs Product Owners
- Accélération considérable des temps de traitement par rapport au processus manuel
- POC mené jusqu'au bout et préparé pour la mise en production, adapté et utilisé par les équipes par la suite

🗣️ **Feedback** :
> *"Implication et capacité constante à se challenger. Force de proposition, assidu dans les missions. POC parsing/mapping mené avec succès."*  
> — Antoine DANIEL LAMAZIERE (PO) + Architecte Data

---

<div align="center">

### 🧪 Data Scientist / ML Engineer - DELTAMU (CDD)
*Octobre 2024 - Octobre 2025*

</div>

**Recherche en Détection d'Anomalies — Capteurs Industriels (Pharma)**

🎯 **Contexte** : Industrie pharma, plusieurs centaines de capteurs

✨ **Missions** :
- 🔬 Tests de recherche en clustering et détection d'anomalies
- 📊 Analyse et interprétation d'insights et de cycliques
- 🧠 Nouvel algorithme de détection, validé par le responsable scientifique

💡 **Impact** :
- 📈 Analyses statistiques avancées sur ensemble de bon fonctionnement
- ⚡ Cœur calculatoire haute vitesse optimisé en **Rust**
- 🔍 Caractérisation des régimes de fonctionnement sur plusieurs centaines de capteurs

🗣️ **Feedback** :
> *"Réelle passion pour la data science et les algorithmes d'IA. Investissement dans les missions. Contribution active au produit logiciel."*  
> — Nuno DOS REIS, Président, DELTAMU

---

## 🎓 Formation

<div align="center">

| Master 2 - Data Scientist | Master 1 - Data Analyst |
|:---:|:---:|
| **OpenClassrooms + Centrale Supélec** (2024) | **OpenClassrooms + ENSAE** (2022) |
| 7 projets validés | 10 projets validés |
| Alternance Michelin (12 mois) | — |
| Deep Learning, NLP, Time Series | ML classique, SQL, BI |

</div>

---

## 🛠️ Stack Technique

<div align="center">

**Principal** — Python · SQL · scikit-learn · LightGBM/XGBoost · PyTorch · pandas/Polars

**Mise en production** — Docker · Redis · PostgreSQL · Prometheus/Grafana · Streamlit

**IA générative** — Claude · ChatGPT · Gemini · Mistral · Grok · Kimi K3 · *agentique* : Claude Code, Codex, OpenCode

**Aussi** — Rust (cœur calculatoire), CUDA, RealMLP, modèles pré-entraînés, TensorFlow, Tableau/Power BI

</div>

---

## 🚀 Projets Phares

### 🌬️ [Correction apprise des prévisions de qualité de l'air](projets_Qualite_Air/)
**Apprendre l'erreur du modèle européen, et la corriger** — 36 mois, 28 M de mesures horaires, 4 polluants

<div align="center">

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/v1_gain_polluants_sombre.svg">
  <img alt="Réduction de l'erreur CAMS à J+1 sans observation locale : NO₂ 39,6 %, PM10 20,2 %, ozone 17,9 % et PM2,5 11,8 %." src="assets/v1_gain_polluants_clair.svg" width="100%">
</picture>

</div>

✨ **Highlights** :
- 🎯 **Prévoir là où personne ne mesure** : aucune observation du lieu corrigé n'entre dans le modèle — et il est testé sur des stations *et* des mois qu'il n'a jamais vus
- 📅 **En 2030 l'Europe divise ses seuils par deux** : à pollution inchangée, les stations en dépassement passent de **6 à 109** — et 4 départements d'Occitanie n'ont aucune station pour le constater
- ✅ **Utilisable au sens réglementaire&nbsp;?** **Sans aucune observation du point**, la part des stations NO₂ qui satisfait le critère européen passe de 41,4 % à **87,9 %** — encore sous le seuil de 90 %. **Aux stations instrumentées**, elle atteint **96,2 %**


- 🔍 **Les limites sont publiées comme les résultats** : 3 épisodes de pollution réels détectés sur 33 — l'observation directe elle-même n'en attrape que 21, et le produit officiel 1
- 💻 **Code** : [github.com/cyril-bgs-dev-tech/correction-previsions-qualite-air](https://github.com/cyril-bgs-dev-tech/correction-previsions-qualite-air)

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/v3_fairmode_no2_sombre.svg">
  <img alt="Pour le NO₂, 41,4 % des stations satisfont le critère européen avec CAMS brut, 87,9 % après correction sans observation locale et 96,2 % avec l'historique de station ; le seuil est à 90 %." src="assets/v3_fairmode_no2_clair.svg" width="100%">
</picture>

---

### 🔧 [Système MLOps Temps Réel](vigilance/)
**Détection d'anomalies industrielle** - 1 200+ heures

<div align="center">

![Architecture](https://img.shields.io/badge/Architecture-Event--Driven-2563eb?style=for-the-badge)
![Workers](https://img.shields.io/badge/Workers-9%20%C3%97%204%20r%C3%A9plicas-10B981?style=for-the-badge)
![Dashboard](https://img.shields.io/badge/Dashboard-40%2B%20pages-8B5CF6?style=for-the-badge)
![Observabilité](https://img.shields.io/badge/Observabilit%C3%A9-Prometheus%20%7C%20Grafana-F59E0B?style=for-the-badge)

</div>

✨ **Highlights** :
- 🏗️ DAG event-driven : 9 workers, barrières Redis atomiques, DLQ, reprise après crash
- 🤖 3 canaux décorrélés (IsolationForest + Ridge temporel + PCA séquentiel) fusionnés par XGBoost + détection de nouveauté
- 🎫 Cycle de vie d'alarme en épisode unique : hystérésis, escalade, SLA par sévérité
- 📊 Dashboard Streamlit 40+ pages avec rôles RASCI
- 🔭 Observabilité par étape du DAG : Prometheus + Grafana + cAdvisor
- 💻 **Code** : [github.com/cyril-bgs-dev-tech/vigilance](https://github.com/cyril-bgs-dev-tech/vigilance)

---

### 🕵️ [Aegis-RCA — Agent de Diagnostic de Causes Racines](aegis-rca/)
**Prototype de recherche actif** — extension de vigilance, 3 jours de développement (juillet 2026)

✨ **Highlights** :
- 🤖 Agent LLM local (Qwen3.6:27B) qui investigue les incidents ouverts par vigilance : contexte métriques, RAG sur procédures, diagnostic + recommandation validés par un humain
- 🔬 Décisions d'architecture confrontées à des avis externes (Gemini, ChatGPT) **puis vérifiées par des bancs de mesure réels** — une erreur de méthodologie détectée et corrigée en cours de route, documentée telle quelle
- 🛡️ Sandbox d'auto-correction durci (Docker jetable, réseau isolé, cgroups) — 1 succès réel mesuré
- 💻 **Code** : [github.com/cyril-bgs-dev-tech/aegis-rca](https://github.com/cyril-bgs-dev-tech/aegis-rca)

---

### 🔬 [Recherche Compositionnelle - Anomaly Detection](anomaly_tabular/)
**Composer les SOTA et router par domaine — ADBench (tabulaire) + TSB-AD (séries temporelles)**

<div align="center">

![Corpus](https://img.shields.io/badge/Corpus-502%20datasets%20%C2%B7%2019%20domaines-2563eb?style=for-the-badge)
![PaAno](https://img.shields.io/badge/PaAno%20(ICLR'26)-%231%20des%202%20volets%20TSB--AD-10B981?style=for-the-badge)
![Repro](https://img.shields.io/badge/Reproductions-exactes%20valid%C3%A9es-8B5CF6?style=for-the-badge)
![Métrique](https://img.shields.io/badge/VUS--PR-point--adjust%20banni-F59E0B?style=for-the-badge)

</div>

✨ **Highlights** :
- 🎯 Démarche : reproduire l'ancre (égalités exactes : Sub-PCA 0.4234, Sub-KNN 0.3501) → monter les SOTA → **caractériser les domaines** → router
- 🥇 PaAno (ICLR 2026) intégré à TSB-AD et certifié : **#1 des volets U et M** (0.58 / 0.46 VUS-PR vs 0.42 / 0.31 pour les leaders publiés)
- 📈 Tabulaire : **routeur source-strict 72,8 AUROC** (pré-enregistré, LODO groupé par source), soit **+1,48 point** sur l'ensemble fixe de 18 détecteurs — et **+1,00** sur la spécialisation par domaine ; le plafond de sélection parfaite est à **+7,40**
- 💡 Leçon : même avec un système SOTA, la composition par domaine ajoute jusqu'à +0.33 VUS-PR localement
- 🔬 Volets : [tabulaire](anomaly_tabular/) · [séries temporelles](anomaly_tsad/) — dépôts : [anomaly_tabular](https://github.com/cyril-bgs-dev-tech/anomaly_tabular) · [anomaly_tsad](https://github.com/cyril-bgs-dev-tech/anomaly_tsad)

---

### 🏆 [Compétitions Kaggle - Top 1% Mondial](projets_Competitions/)
**35+ compétitions** | **3 top 1%**

<div align="center">

| Compétition | Rang | Top % |
|:---|:---:|:---:|
| 🏎️ Prediction F1 Pit Stop | #14 / 3 022 | 0.5% |
| 🌾 Predicting Irrigation Need | #32 / 4 315 | 0.7% |
| 🎧 Predict Podcast Listening | #20 / 3 310 | 0.6% |
| 🏠 Regression California Housing | #14 / 689 | 2% |

</div>

✨ **Approche** :
- 🔧 Feature engineering intensif (centaines de features)
- 🤝 Ensembling/stacking de modèles diversifiés
- ⚡ Optimisation bayésienne (Optuna)
- 🔬 Veille active (TabM, TabICL2, RealMLP)
- 🤖 La stratégie gagnante se déplace vers l'**agentique** — des systèmes d'agents qui explorent et sélectionnent les pistes en autonomie
- 🏅 **Palmarès vérifiable** : [kaggle.com/cyrilbourgeois](https://www.kaggle.com/cyrilbourgeois/competitions)

---

## 🗂️ Tous les projets

« Projets Phares » ci-dessus est une sélection. Voici la liste complète — les **17 projets de formation** n'apparaissent nulle part ailleurs.

| Projet | Ce qu'on y trouve |
|---|---|
| 🌬️ **[Correction des prévisions de qualité de l'air](projets_Qualite_Air/)** | 36 mois, 28 M de mesures horaires, 4 polluants — évalué sans aucune observation du lieu corrigé |
| 🔧 **[Système MLOps temps réel](vigilance/)** | Détection d'anomalies industrielle — dashboard 40+ pages, rôles RASCI |
| 🕵️ **[Agent de diagnostic de causes racines](aegis-rca/)** | Extension de vigilance — architecture confrontée à des bancs de mesure réels |
| 🔬 **[Recherche compositionnelle — tabulaire](anomaly_tabular/)** | Composer les détecteurs SOTA et router par domaine, sur le banc ADBench |
| 🔬 **[Recherche compositionnelle — séries temporelles](anomaly_tsad/)** | Le même routage porté sur le banc TSB-AD |
| 🏆 **[Compétitions Kaggle](projets_Competitions/)** | 35+ engagées, 3 top 1 %, meilleur rang #14 / 3 022 |
| 🎓 **[Master 2 — Data Scientist](projets_Master_2/)** | 7 projets, et l'alternance Michelin — [code](https://gitlab.com/cyril.bgs.dev/projets_Master_2) |
| 🎓 **[Master 1 — Data Analyst](projets_Master_1/)** | 10 projets — SQL, Python, KNIME, Tableau — [code](https://gitlab.com/cyril.bgs.dev/projets_Master_1) |

> 💻 **Le code** — trois dépôts sont lisibles sans compte : [qualité de l'air](https://gitlab.com/cyril.bgs.dev/correction-previsions-qualite-air) · [Master 1](https://gitlab.com/cyril.bgs.dev/projets_Master_1) · [Master 2](https://gitlab.com/cyril.bgs.dev/projets_Master_2). Les liens GitHub de cette page dépendent d'un compte actuellement indisponible aux visiteurs non connectés.

---

## 🎯 Ce Que Je Recherche

<div align="center">

### 🚀 Opportunités

</div>

- **Data Scientist** : Projets ML/DL complexes, détection d'anomalies
- **MLOps Engineer** : Mise en production de modèles, systèmes temps réel
- **Research Engineer** : État de l'art, benchmark, nouvelles architectures

### 🌟 Environnement Idéal

- ✅ Équipe technique passionnée et collaborative
- ✅ Problématiques business à fort impact
- ✅ Stack moderne (Python, cloud, MLOps)
- ✅ Culture data-driven et innovation

---

## 📫 Contact

<div align="center">

**📧 Email** : [cyril.bgs.dev@gmail.com](mailto:cyril.bgs.dev@gmail.com)  
**💼 LinkedIn** : [linkedin.com/in/cyril-bourgeois-65a739150](https://www.linkedin.com/in/cyril-bourgeois-65a739150/)  
**🏆 Kaggle** : [kaggle.com/cyrilbourgeois](https://www.kaggle.com/cyrilbourgeois)  
**🐙 GitHub** : [github.com/cyril-bgs-dev-tech](https://github.com/cyril-bgs-dev-tech)

</div>

---

<div align="center">

*Sources et résultats bruts versionnés — chaque chiffre publié est relié à son protocole.*


*Dernière mise à jour : Août 2026*

</div>
