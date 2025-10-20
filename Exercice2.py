"""
TP2 - Exercice 2 : File d'attente des commandes
"""

def calculer_priorite(commande):
    """
    Calcule la priorité d'une commande selon l'algorithme défini.
    
    Args:
        commande (dict): Dictionnaire contenant:
            - 'temps_attente': temps d'attente en minutes
            - 'nombre_items': nombre d'items dans la commande
            - 'client_vip': booléen, True si client VIP
    
    Returns:
        int: Score de priorité
    """
    score = 0
    
    # TODO: Implémenter l'algorithme de priorité
    # Score = (temps_attente × 2) + (nombre_items × 1) + (client_vip × 10)
    
    for i in commande.items():
        temps_attente = commande['temps_attente']
        nombre_items = commande['nombre_items']
        vip = commande['client_vip']
        score = temps_attente*2 + nombre_items*1 + vip*10
    
    return score


def trier_commandes(liste_commandes):
    """
    Trie les commandes par ordre de priorité décroissante.
    Utilise l'algorithme de tri à bulles adapté.
    
    Args:
        liste_commandes (list): Liste de dictionnaires de commandes
    
    Returns:
        list: Liste triée par priorité décroissante
    """
    # TODO: Implémenter un algorithme de tri (suggestion: tri à bulles)
    # Les commandes avec le score le plus élevé doivent être en premier
    
    def tri_bulles_commandes(liste_commandes):
        n = len(liste_commandes)
        for i in range(n):
            for j in range (0, n-i-1):
                if calculer_priorite(liste_commandes[j])<calculer_priorite(liste_commandes[j+1]):
                    liste_commandes[j], liste_commandes[j+1] = liste_commandes[j+1], liste_commandes[j]
    
    tri_bulles_commandes(liste_commandes)

    return liste_commandes


def estimer_temps_total(liste_commandes_triee):
    """
    Estime le temps total pour traiter toutes les commandes.
    
    Args:
        liste_commandes_triee (list): Liste triée de commandes
    
    Returns:
        dict: Temps total et temps moyen par commande
    """
    temps_stats = {}
    
    # TODO: Calculer le temps total et moyen
    # Chaque item prend en moyenne 3 minutes à préparer
    
    temps_total = 0
    nombre_items = 0 
    nombre_commandes = 0
    temps_moyen = 0

    for commande in liste_commandes_triee:
        nombre_items += commande['nombre_items']
        nombre_commandes += 1
        temps_total = nombre_items *3
        temps_moyen = temps_total / int(nombre_commandes)

    temps_stats['temps_total'] = temps_total
    temps_stats['temps_moyen'] = temps_moyen
    return temps_stats


def identifier_commandes_urgentes(liste_commandes, seuil_attente=30):
    """
    Identifie les commandes urgentes (attente > seuil).
    
    Args:
        liste_commandes (list): Liste de commandes
        seuil_attente (int): Seuil d'attente en minutes
    
    Returns:
        list: Liste des numéros de commandes urgentes
    """
    commandes_urgentes = []
    
    # TODO: Identifier les commandes avec temps_attente > seuil

    for commande in liste_commandes:
        if commande['temps_attente'] > seuil_attente:
            commandes_urgentes.append(commande['numero'])

    return commandes_urgentes


if __name__ == '__main__':
    # Test des fonctions
    commandes_test = [
        {'numero': 1, 'temps_attente': 10, 'nombre_items': 3, 'client_vip': False},
        {'numero': 2, 'temps_attente': 25, 'nombre_items': 2, 'client_vip': True},
        {'numero': 3, 'temps_attente': 5, 'nombre_items': 5, 'client_vip': False},
        {'numero': 4, 'temps_attente': 35, 'nombre_items': 1, 'client_vip': False},
        {'numero': 5, 'temps_attente': 15, 'nombre_items': 4, 'client_vip': True},
    ]
    
    # Test de calcul de priorité
    print("Priorités des commandes:")
    for cmd in commandes_test:
        priorite = calculer_priorite(cmd)
        print(f"  Commande {cmd['numero']}: priorité = {priorite}")
    
    # Test du tri
    commandes_triees = trier_commandes(commandes_test.copy())
    print("\nCommandes triées par priorité:")
    for cmd in commandes_triees:
        print(f"  Commande {cmd['numero']} (priorité: {calculer_priorite(cmd)})")
    
    # Test estimation temps
    temps_stats = estimer_temps_total(commandes_triees)
    print(f"\nTemps de traitement estimé:")
    print(f"  Total: {temps_stats.get('temps_total', 0)} minutes")
    print(f"  Moyen: {temps_stats.get('temps_moyen', 0):.1f} minutes/commande")
    
    # Test commandes urgentes
    urgentes = identifier_commandes_urgentes(commandes_test)
    print(f"\nCommandes urgentes (>30 min): {urgentes}")
