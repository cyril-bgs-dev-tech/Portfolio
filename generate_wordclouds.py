#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Génération de WordClouds pour les commentaires Master 1 et Master 2
Design moderne et épuré
"""

from wordcloud import WordCloud
import matplotlib.pyplot as plt
import numpy as np

# ============================================================================
# COMMENTAIRES MASTER 1
# ============================================================================
comments_m1 = """
Très beau travail analyse data Beau rendu explications claires soft skills acquis présentation
Données chargées base données fonctionnelle Dictionnaire données complet MCD MLD valides 
Requêtes SQL valides résultats pertinents Bonus BI présentée
Conforme demande Intégration analyses supplémentaires Bonne présentation
Bonne présentation claire précise Analyse orientée métier répond besoins exprimés 
Bon choix analyse notamment stocks
Livrable complet conforme attentes projet Bonne appropriation sujet 
étudiant allé plus demandé proposant ensemble graphiques tableau bord PowerBI Bonne présentation
Tous livrables présents conformes attentes Bonne prise main KNIME Graphiques intéressants 
Présentation claire structurée Bonne compréhension sujet mission
Bonne soutenance ensemble très claire apporte bonne justification
Bonne présentation ensemble graphiques point fort
Soutenance confuse Manque structure organisation présentation projet techniquement OK 
effort présentation résultats
"""

# ============================================================================
# COMMENTAIRES MASTER 2 (Michelin)
# ============================================================================
comments_m2 = """
Implication capacité constante challenger
Maîtrise solutions développement mise en œuvre
Curiosité motivation intérêt problématiques Data Business
Force proposition assidu missions
POC parsing mapping mené succès
Sérieux volonté constante apprendre
Vitesse exécution qualité saluées Product Owners
POC validé prêt industrialisation
Réduction temps traitement manuel
Amélioration qualité données
Dashboards utilisés équipe pricing
Détection écarts significatifs
Recommandations actionnables
Gestion données grande échelle niveau continental
Rigueur méthodologique tests validation
Communication stakeholders non techniques
Autonomie force proposition
Vision produit industrialisation
"""

# ============================================================================
# FONCTION DE GÉNÉRATION WORDCLOUD MODERNE
# ============================================================================
def create_modern_wordcloud(text, title, filename, color_map='Blues'):
    """Crée un wordcloud avec design moderne"""
    
    # Configuration du wordcloud
    wordcloud = WordCloud(
        width=1600,
        height=800,
        background_color='white',
        colormap=color_map,
        max_words=150,
        max_font_size=120,
        min_font_size=12,
        prefer_horizontal=0.9,
        relative_scaling=0.5,
        contour_width=0,
        contour_color='white',
        margin=10
    ).generate(text)
    
    # Création de la figure
    fig = plt.figure(figsize=(16, 8), facecolor='white')
    ax = plt.subplot(111)
    
    # Affichage du wordcloud
    ax.imshow(wordcloud, interpolation='bilinear')
    ax.axis('off')
    
    # Titre avec style moderne
    ax.set_title(title, 
                fontsize=28, 
                fontweight='bold',
                color='#2563eb',
                pad=20,
                fontfamily='sans-serif')
    
    # Sauvegarde
    plt.tight_layout(pad=2)
    plt.savefig(filename, 
                dpi=300, 
                bbox_inches='tight',
                facecolor='white',
                edgecolor='none')
    plt.close()
    
    print(f"✓ WordCloud sauvegardé : {filename}")

# ============================================================================
# GÉNÉRATION DES WORDCLOUDS
# ============================================================================

print("Génération des WordClouds...")
print("=" * 60)

# Master 1
create_modern_wordcloud(
    text=comments_m1,
    title="Feedbacks Évaluateurs - Master 1",
    filename="wordcloud_master1.png",
    color_map='Blues'
)

# Master 2
create_modern_wordcloud(
    text=comments_m2,
    title="Feedbacks Michelin - Master 2",
    filename="wordcloud_master2.png",
    color_map='Greens'
)

print("=" * 60)
print("✓ Tous les WordClouds ont été générés avec succès !")
print("\nFichiers créés :")
print("  - wordcloud_master1.png")
print("  - wordcloud_master2.png")
