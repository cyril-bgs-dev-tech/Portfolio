# 🔬 Research — Anomaly Detection Séries Temporelles (TSB-AD)

**Domaine** : détection d'anomalies sur séries temporelles uni- et multivariées  
**Démarche** : reproduction rigoureuse du benchmark **TSB-AD** (870 séries univariées + 200 multivariées), puis construction d'un système visant le quasi-SOTA par routage de détecteurs spécialisés.

---

## 📋 Vue d'ensemble

Deux volets complémentaires :

1. **Reproduction ancrée** : chaque détecteur est validé contre son score publié avant toute comparaison — un benchmark ne vaut que si ses témoins sont exacts
2. **Système « rails → routeur »** : familles de détecteurs spécialisés par régime de série, routées par un méta-modèle (validation LODO par dataset-source, jamais par série — pas de fuite)

## 📐 Rigueur méthodologique (choix assumés)

- **VUS-PR** en métrique primaire — le **point-adjust est banni** (il gonfle artificiellement les scores, biais documenté dans la littérature)
- Endpoint d'évaluation natif du benchmark, pas de réimplémentation de la métrique
- Validation **inductive** : leave-one-dataset-out par source, préenregistrement des claims avant réplication

## 📊 Reproductions validées (VUS-PR moyen, TSB-AD)

| Détecteur | Publié | Reproduit | Statut |
|-----------|--------|-----------|--------|
| Sub-PCA (U, 350 séries) | 0.4234 | 0.4234 | ✅ exact |
| Sub-KNN (U) | 0.3501 | 0.3501 | ✅ exact |
| POLY (U) | 0.3898 | 0.3899 | ✅ |
| CNN (M, 180 séries) | 0.313 | 0.3171 | ✅ écart diagnostiqué (artefact de couverture) |

## 🧪 SOTA récents montés et validés (RTX 5090)

**Fonctionnels** : MOMENT (zero-shot, foundation model), TranAD, AnomalyTransformer, FITS, Donut, OFA  
**Bloqués & documentés** : Chronos et TimesFM (conflits d'environnement → env isolés), TimesNet (kernel CUDA incompatible Blackwell sm_120)

## 🗺️ Feuille de route

| Phase | Contenu |
|-------|---------|
| P1 | Reproduction complète de l'ancre TSB-AD (tables publié/reproduit/Δ) |
| P2 | Corpus qualité : ≥ 800 séries, ≥ 12 domaines, gates de qualité par série |
| P3 | Rails : 6 familles de détecteurs spécialisés + ensembles + oracle par série |
| P4 | Routeur appris (validation LODO nichée, inductive) |
| P5 | Préenregistrement des claims + réplication séquestrée |

---

**Projet frère** : [Recherche tabulaire](../projets_research_Sota_AD_Tab/README.md) (ADBench)  
**Dernière mise à jour** : juillet 2026  
**Contact** : cyril.bgs.dev.tech@gmail.com
