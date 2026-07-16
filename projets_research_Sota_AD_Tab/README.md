# 🔬 Research — Anomaly Detection Tabulaire (Benchmark de Reproduction)

**Domaine** : détection d'anomalies sur données tabulaires  
**Démarche** : avant de prétendre battre l'état de l'art, le **reproduire exactement** — mêmes données, mêmes protocoles, mêmes hyperparamètres que les papiers — et diagnostiquer chaque écart.

---

## 📋 Vue d'ensemble

Benchmark de reproduction sur **ADBench** (47 datasets tabulaires classiques, extensible CV/NLP), avec un harnais d'évaluation maison :

- **Runner parallèle CPU** : pool de processus (~28 workers, 1 thread BLAS par worker pour éviter l'oversubscription), cache JSON **reprenable par tâche** — un crash ou un redémarrage machine ne perd aucun calcul
- **Routage GPU** : modèles deep envoyés sur RTX 5090 (torch + CUDA), files CPU/GPU séparées
- **Protocoles officiels** : hyperparamètres et splits repris des dépôts de référence, pas réinventés

## 📊 Reproductions validées (score moyen, protocole ADBench, 47 datasets)

| Détecteur | Score reproduit |
|-----------|-----------------|
| IsolationForest | 0.762 |
| COPOD | 0.744 |
| ECOD | 0.742 |
| PCA | 0.740 |
| KNN | 0.699 |

Chaque écart avec les valeurs publiées passe par une checklist de diagnostic : métrique exacte, split/seeds, hyperparamètres, préprocessing, version des données, variance inter-runs, versions de librairies.

## 🧪 En cours

- **DeepSVDD** (GPU) monté et validé sur échantillon — passage full ADBench
- **DTE, FoMo-0D** (SOTA récents) en file de montage
- Rapport final : tables **publié / reproduit / Δ** avec cause identifiée pour chaque écart

## 🛠️ Pièges documentés (le vrai savoir-faire)

- Ne pas installer le package `adbench` officiel (dépendances TensorFlow + downgrade forcé de pyod)
- Contraintes numpy < 2 imposées par certaines références — environnements isolés par famille de modèles
- Kernels CUDA non compilés pour architecture Blackwell (sm_120) sur certains modèles → suivi par modèle

---

**Projet frère** : [Recherche time series](../projets_research_Sota_AD_TS/README.md) (TSB-AD, VUS-PR)  
**Dernière mise à jour** : juillet 2026  
**Contact** : cyril.bgs.dev.tech@gmail.com
