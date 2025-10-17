"""
TP2 - Exercice 1 : Gestion du Menu
"""

def analyser_menu(menu):
    """
    Analyse le menu du restaurant pour extraire des statistiques importantes.
    
    Args:
        menu (dict): Dictionnaire avec nom_plat: (prix, temps_preparation, popularité)
    
    Returns:
        dict: Dictionnaire contenant:
            - 'plat_plus_rentable': Le plat avec le meilleur ratio popularité/temps
            - 'prix_moyen': Le prix moyen de tous les plats
            - 'temps_moyen': Le temps de préparation moyen
    """
    stats = {}
    
    # TODO: Calculer le plat le plus rentable (ratio popularité/temps_preparation)
    # Attention: gérer le cas où temps_preparation pourrait être 0
    ratio_de_base = 0 

    for nom_plat, (prix, temps_preparation, popularite) in menu.items():
        if temps_preparation ==0:
            print('Erreur : temps de preparation nul!')
            continue

        ratio_calculé = popularite / temps_preparation
        if ratio_calculé > ratio_de_base:
            ratio_de_base = ratio_calculé
            plat_plus_rentable = nom_plat

    stats['plat_plus_rentable'] = plat_plus_rentable

    
    # TODO: Calculer le prix moyen du menu
    
    prix_total = 0
    nombre_de_plats = 0

    for nom_plat, (prix, temps_preparation, popularite) in menu.items():
        prix_total += prix
        nombre_de_plats += 1 
        prix_moyen = float(prix_total)/nombre_de_plats
    stats['prix_moyen'] = prix_moyen

    # TODO: Calculer le temps de préparation moyen
    
    temps_preparation_total = 0
    
    for nom_plat, (prix, temps_preparation, popularite) in menu.items():
        temps_preparation_total += temps_preparation
        temps_preparation_moyen = float(temps_preparation_total)/nombre_de_plats
    
    stats['temps_moyen'] = temps_preparation_moyen

    return stats


def filtrer_menu_par_categorie(menu, categories):
    """
    Filtre le menu par catégories de plats.
    
    Args:
        menu (dict): Menu complet
        categories (dict): Dictionnaire nom_plat: catégorie
    
    Returns:
        dict: Menu organisé par catégories
    """
    menu_filtre = {}
    
    # TODO: Organiser les plats par catégorie
    # Exemple: {'entrées': [...], 'plats': [...], 'desserts': [...]}
    
    entrees = ''
    plats = ''
    desserts = ''

    for nom_plat, categorie in categories.items():
        if categorie == 'entrées':
            entrees += str(nom_plat) + ', '
        if categorie == 'plats':
            plats += str(nom_plat) + ', '
        if categorie == 'desserts':
            desserts += str(nom_plat) + ', '
        else :
            continue
    menu_filtre['entrées'] = entrees
    menu_filtre['plats'] = plats
    menu_filtre['desserts'] = desserts
    
    return menu_filtre


def calculer_profit(menu, ventes_jour):
    """
    Calcule le profit total de la journée.
    
    Args:
        menu (dict): Menu avec prix
        ventes_jour (dict): Nombre de ventes par plat
    
    Returns:
        float: Profit total
    """
    profit = 0
    
    # TODO: Calculer le profit total
    # profit = somme(prix_plat * nombre_ventes) pour chaque plat vendu

    for nom_plat, (prix, temps_preparation, popularite) in menu.items():
        if nom_plat in ventes_jour:
            profit += float(prix*ventes_jour[nom_plat])

    return profit


if __name__ == '__main__':
    # Test de la fonction analyser_menu
    menu_test = {
        'Pizza Margherita': (12.50, 15, 8),
        'Pâtes Carbonara': (14.00, 12, 9),
        'Salade César': (9.50, 5, 6),
        'Tiramisu': (6.00, 3, 10),
        'Burger Classique': (11.00, 10, 7),
        'Soupe du jour': (5.50, 8, 5)
    }
    
    resultats = analyser_menu(menu_test)
    print("Analyse du menu:")
    print(f"  Plat le plus rentable: {resultats.get('plat_plus_rentable')}")
    print(f"  Prix moyen: {resultats.get('prix_moyen'):.2f}€")
    print(f"  Temps de préparation moyen: {resultats.get('temps_moyen'):.1f} min")
    
    # Test de la fonction filtrer_menu_par_categorie
    categories_test = {
        'Pizza Margherita': 'plats',
        'Pâtes Carbonara': 'plats',
        'Salade César': 'entrées',
        'Tiramisu': 'desserts',
        'Burger Classique': 'plats',
        'Soupe du jour': 'entrées'
    }
    
    menu_filtre = filtrer_menu_par_categorie(menu_test, categories_test)
    print("\nMenu par catégories:")
    for categorie, plats in menu_filtre.items():
        print(f"  {categorie}: {plats}")
    
    # Test de la fonction calculer_profit
    ventes_test = {
        'Pizza Margherita': 15,
        'Pâtes Carbonara': 20,
        'Salade César': 10,
        'Tiramisu': 25
    }
    
    profit_jour = calculer_profit(menu_test, ventes_test)
    print(f"\nProfit du jour: {profit_jour:.2f}€")
