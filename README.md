# TP2: Simulateur de Restaurant "Python Bistro" 🍳

#### :alarm_clock: Date de remise : Dimanche 19 octobre 2025 à 23h59

## Objectif
Ce TP vous permettra d'apprendre la programmation Python à travers la création d'un simulateur de gestion de restaurant. Vous allez découvrir et maîtriser :
- Les structures de contrôle (boucles, conditions)
- Les structures de données (listes, dictionnaires, tuples)
- Les algorithmes de base (tri, recherche, optimisation)
- La manipulation de données complexes

## Introduction
Félicitations ! Vous venez d'hériter du restaurant familial "Python Bistro". Pour moderniser l'établissement, vous devez créer un système de gestion informatisé qui permettra de :
- Gérer les commandes des clients
- Optimiser l'inventaire des ingrédients
- Calculer les profits
- Créer un système de réservation
- Gérer la satisfaction client

## Structure du TP
Le TP est divisé en 5 exercices indépendants qui simulent différents aspects de la gestion du restaurant.

## Exercice 1: Gestion du Menu (3 points)
Vous devez créer un système pour gérer le menu du restaurant. Le menu est représenté par un dictionnaire où les clés sont les noms des plats et les valeurs sont des tuples contenant (prix, temps_preparation, popularité).

Complétez la fonction `analyser_menu` qui :
- Trouve le plat le plus rentable (rapport popularité/temps_preparation le plus élevé)
- Calcule le prix moyen du menu
- Retourne un dictionnaire avec ces statistiques

**Exemple :**
```python
menu = {
    'Pizza Margherita': (12.50, 15, 8),  # (prix, temps en min, popularité sur 10)
    'Pâtes Carbonara': (14.00, 12, 9),
    'Salade César': (9.50, 5, 6),
    'Tiramisu': (6.00, 3, 10)
}
# Résultat attendu:
# {'plat_plus_rentable': 'Tiramisu', 'prix_moyen': 10.50}
```

## Exercice 2: File d'attente des commandes (3 points)
Les commandes arrivent dans votre cuisine et doivent être traitées selon un algorithme de priorité. Implémentez un système de file d'attente qui trie les commandes selon leur urgence.

**L'algorithme de priorité :**
- Score = (temps_attente × 2) + (nombre_items × 1) + (client_vip × 10)
- Les commandes avec le score le plus élevé sont traitées en premier

Complétez la fonction `trier_commandes` qui implémente cet algorithme de tri.

## Exercice 3: Optimisation de l'inventaire (4 points)
Vous devez gérer l'inventaire des ingrédients. Créez un système qui :
1. Vérifie si vous avez assez d'ingrédients pour une commande
2. Met à jour l'inventaire après chaque commande
3. Génère des alertes pour les ingrédients en rupture de stock (< 10 unités)

**Format des données :**
```python
inventaire = {'tomates': 50, 'fromage': 30, 'pâtes': 100}
recette = {'tomates': 5, 'fromage': 3}  # Ingrédients nécessaires
```

## Exercice 4: Système de réservation (5 points)
Créez un système de réservation de tables pour votre restaurant avec les fonctionnalités suivantes :

### Partie 1: Initialisation (2 points)
Créez une grille représentant la salle du restaurant où :
- `O` = table occupée
- `L` = table libre  
- `R` = table réservée
- `X` = espace non disponible (couloir, cuisine)

### Partie 2: Recherche de table (3 points)
Implémentez un algorithme qui trouve la meilleure table disponible selon :
- La taille du groupe (petites tables pour 2, grandes pour 4+)
- La position (près de la fenêtre = bonus)
- L'état de disponibilité

## Exercice 5: Analyse de la satisfaction client (5 points)
Analysez les commentaires clients pour améliorer votre service. 

Créez un système qui :
1. Analyse les mots-clés dans les commentaires
2. Calcule un score de satisfaction (0-10)
3. Identifie les points à améliorer
4. Génère un rapport de synthèse

**Mots-clés et scores :**
- Positifs : "excellent"(+3), "délicieux"(+2), "rapide"(+1)
- Négatifs : "froid"(-2), "lent"(-3), "décevant"(-2)

## Bonus: Mini-jeu de service (2 points)
Créez un mini-jeu en mode console où le serveur doit :
- Se déplacer dans le restaurant (grille 5x5)
- Prendre les commandes aux tables
- Les apporter à la cuisine
- Servir les plats
- Le tout avec un système de score basé sur la rapidité

**Commandes :**
- `z` : haut
- `s` : bas
- `q` : gauche  
- `d` : droite
- `p` : prendre commande/plat
- `l` : livrer

## Consignes importantes
- Ne modifiez que les sections marquées `TODO`
- N'importez pas de librairies supplémentaires
- Testez votre code avec les exemples fournis
- Respectez les formats de sortie demandés

## Barème
- Exercice 1: 3 points
- Exercice 2: 3 points  
- Exercice 3: 4 points
- Exercice 4: 5 points
- Exercice 5: 5 points
- Bonus: +2 points
- **Total: 20 points (+2 bonus)**

Bonne chance et bon appétit ! 🍽️
