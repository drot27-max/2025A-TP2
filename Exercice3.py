"""
TP2 - Exercice 3 : Optimisation de l'inventaire
"""

def verifier_disponibilite(inventaire, recette):
    """
    Vérifie si on a assez d'ingrédients pour préparer une recette.
    """
    peut_preparer = True
    ingredients_manquants = []

    for ingredient, qte_necessaire in recette.items():
        qte_dispo = inventaire.get(ingredient, 0)
        if qte_dispo < qte_necessaire:
            peut_preparer = False
            manque = qte_necessaire - qte_dispo
            ingredients_manquants.append((ingredient, manque))

    return peut_preparer, ingredients_manquants


def mettre_a_jour_inventaire(inventaire, recette, quantite=1):
    """
    Met à jour l'inventaire après la préparation d'une recette.
    """
    nouvel_inventaire = inventaire.copy()

    for ingredient, qte_necessaire in recette.items():
        if ingredient in nouvel_inventaire:
            nouvel_inventaire[ingredient] = max(
                0, nouvel_inventaire[ingredient] - qte_necessaire * quantite
            )
        else:
            nouvel_inventaire[ingredient] = 0

    return nouvel_inventaire


def generer_alertes_stock(inventaire, seuil=10):
    """
    Génère des alertes pour les ingrédients en rupture de stock.
    """
    alertes = {}
    quantite_standard = 50  

    for ingredient, qte in inventaire.items():
        if qte < seuil:
            a_commander = quantite_standard - qte
            alertes[ingredient] = (qte, a_commander)

    return alertes


def calculer_commandes_possibles(inventaire, menu_recettes):
    """
    Calcule combien de fois chaque plat peut être préparé avec l'inventaire actuel.
    """
    commandes_possibles = {}

    for plat, recette in menu_recettes.items():
        nb_portions = float("inf")
        for ingredient, qte_necessaire in recette.items():
            qte_dispo = inventaire.get(ingredient, 0)
            if qte_necessaire == 0:
                continue
            portions_possibles = qte_dispo // qte_necessaire
            nb_portions = min(nb_portions, portions_possibles)
        commandes_possibles[plat] = int(nb_portions if nb_portions != float("inf") else 0)

    return commandes_possibles


def optimiser_achats(inventaire, menu_recettes, previsions_ventes, budget):
    """
    Optimise les achats d'ingrédients selon les prévisions de ventes.
    """
    liste_achats = {}
    cout_ingredients = {'tomates': 0.5, 'fromage': 2.0, 'pâtes': 1.0, 'sauce': 1.5, 'pain': 0.8}

    # 1. Calculer les besoins totaux d’ingrédients selon les prévisions
    besoins_totaux = {}
    for plat, recette in menu_recettes.items():
        prevision = previsions_ventes.get(plat, 0)
        for ingredient, qte_necessaire in recette.items():
            besoins_totaux[ingredient] = besoins_totaux.get(ingredient, 0) + qte_necessaire * prevision

    # 2. Soustraire l’inventaire actuel pour obtenir les manques
    manques = {}
    for ingredient, besoin in besoins_totaux.items():
        dispo = inventaire.get(ingredient, 0)
        manque = max(0, besoin - dispo)
        if manque > 0:
            manques[ingredient] = manque

    # 3. Prioriser les achats selon importance et budget
    #    tri par "besoin en unités" décroissant
    manques_tries = sorted(manques.items(), key=lambda x: x[1], reverse=True)

    reste_budget = budget
    for ingredient, manque in manques_tries:
        prix_unitaire = cout_ingredients.get(ingredient, 1.0)
        cout_total = manque * prix_unitaire

        if cout_total <= reste_budget:
            liste_achats[ingredient] = manque
            reste_budget -= cout_total
        else:
            # Acheter partiellement selon budget restant
            max_quantite = int(reste_budget // prix_unitaire)
            if max_quantite > 0:
                liste_achats[ingredient] = max_quantite
                reste_budget -= max_quantite * prix_unitaire

        if reste_budget <= 0:
            break

    return liste_achats


# ==================== TESTS ====================
if __name__ == '__main__':
    inventaire_test = {
        'tomates': 50,
        'fromage': 30,
        'pâtes': 100,
        'sauce': 25,
        'pain': 40
    }

    recettes_test = {
        'Pizza': {'tomates': 5, 'fromage': 3, 'pain': 2},
        'Pâtes': {'pâtes': 10, 'sauce': 2, 'fromage': 1},
        'Sandwich': {'pain': 2, 'tomates': 2, 'fromage': 1}
    }

    print("=== Test de disponibilité ===")
    for plat, recette in recettes_test.items():
        dispo, manquants = verifier_disponibilite(inventaire_test, recette)
        status = "✓ Disponible" if dispo else f"✗ Manque: {manquants}"
        print(f"  {plat}: {status}")

    print("\n=== Mise à jour après 3 pizzas ===")
    nouvel_inventaire = mettre_a_jour_inventaire(inventaire_test, recettes_test['Pizza'], 3)
    for ing in ['tomates', 'fromage', 'pain']:
        print(f"  {ing}: {inventaire_test[ing]} → {nouvel_inventaire[ing]}")

    print("\n=== Alertes de stock (seuil=20) ===")
    alertes = generer_alertes_stock(nouvel_inventaire, seuil=20)
    for ingr, (actuel, commander) in alertes.items():
        print(f"  {ingr}: {actuel} unités (commander {commander})")

    print("\n=== Portions possibles ===")
    portions = calculer_commandes_possibles(inventaire_test, recettes_test)
    for plat, nb in portions.items():
        print(f"  {plat}: {nb} portions")

    print("\n=== Optimisation des achats ===")
    previsions = {'Pizza': 20, 'Pâtes': 15, 'Sandwich': 10}
    budget = 100.0
    achats = optimiser_achats(inventaire_test, recettes_test, previsions, budget)
    for ingr, qte in achats.items():
        print(f"  {ingr}: {qte} unités")
