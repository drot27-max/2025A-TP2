"""
TP2 - Exercice 4 : Système de réservation
"""

# Fonction fournie - ne pas modifier
def afficher_salle(salle):
    """Affiche la salle du restaurant de manière formatée."""
    print("\n=== Plan de la salle ===")
    print("   ", end="")
    for j in range(len(salle[0])):
        print(f" {j}", end="")
    print()
    for i, rangee in enumerate(salle):
        print(f"{i}: ", end="")
        for table in rangee:
            print(f" {table}", end="")
        print()
    print("=" * 25)


# PARTIE 1: Initialisation (2 points)
def initialiser_salle(nb_rangees, nb_colonnes, positions_tables):
    """
    Initialise la salle du restaurant.
    """
    # Créer une grille remplie de 'X'
    salle = [["X" for _ in range(nb_colonnes)] for _ in range(nb_rangees)]

    # Placer les tables
    for (r, c, taille) in positions_tables:
        if 0 <= r < nb_rangees and 0 <= c < nb_colonnes:
            salle[r][c] = f"L{taille}"

    return salle


def marquer_reservation(salle, position, taille_groupe):
    """
    Marque une table comme réservée.
    """
    nouvelle_salle = [ligne[:] for ligne in salle]  # copie indépendante
    r, c = position

    if 0 <= r < len(salle) and 0 <= c < len(salle[0]):
        table = salle[r][c]
        if table.startswith("L"):  # libre
            taille_table = int(table[1])
            if taille_groupe <= taille_table:
                nouvelle_salle[r][c] = f"R{taille_table}"
    return nouvelle_salle


# PARTIE 2: Recherche de table (3 points)
def calculer_score_table(position, taille_table, taille_groupe, nb_colonnes):
    """
    Calcule le score d'une table pour un groupe.
    """
    r, c = position

    if taille_table < taille_groupe:
        return -1  # table trop petite

    score = 100
    score -= 10 * (taille_table - taille_groupe)  # pénalité pour places vides

    # Bonus fenêtre
    if c == 0 or c == nb_colonnes - 1:
        score += 20

    # Bonus proximité entrée
    if r < 3:
        score += 5

    return score


def trouver_meilleure_table(salle, taille_groupe):
    """
    Trouve la meilleure table disponible pour un groupe.
    """
    meilleure_table = None
    meilleur_score = -1
    nb_colonnes = len(salle[0])

    for i, rangee in enumerate(salle):
        for j, table in enumerate(rangee):
            if table.startswith("L"):
                taille_table = int(table[1])
                score = calculer_score_table((i, j), taille_table, taille_groupe, nb_colonnes)
                if score > meilleur_score:
                    meilleur_score = score
                    meilleure_table = ((i, j), taille_table)

    return meilleure_table


def generer_rapport_occupation(salle):
    """
    Génère un rapport sur l'occupation de la salle.
    """
    rapport = {
        'tables_libres_2': 0,
        'tables_libres_4': 0,
        'tables_reservees_2': 0,
        'tables_reservees_4': 0,
        'tables_occupees_2': 0,
        'tables_occupees_4': 0,
        'taux_occupation': 0.0
    }

    total_tables = 0
    occupees = 0

    for rangee in salle:
        for table in rangee:
            if table.startswith("L"):
                total_tables += 1
                taille = int(table[1])
                rapport[f"tables_libres_{taille}"] += 1
            elif table.startswith("R"):
                total_tables += 1
                taille = int(table[1])
                rapport[f"tables_reservees_{taille}"] += 1
                occupees += 1
            elif table.startswith("O"):  # pour "occupée" (optionnel)
                total_tables += 1
                taille = int(table[1])
                rapport[f"tables_occupees_{taille}"] += 1
                occupees += 1

    if total_tables > 0:
        rapport["taux_occupation"] = occupees / total_tables

    return rapport


# ===========================
# TESTS
# ===========================
if __name__ == '__main__':
    nb_rangees = 5
    nb_colonnes = 6
    positions_tables = [
        (0, 0, 2), (0, 2, 2), (0, 5, 2),
        (1, 1, 4), (1, 4, 4),
        (2, 0, 2), (2, 2, 4), (2, 5, 2),
        (3, 1, 4), (3, 3, 4),
        (4, 0, 2), (4, 2, 2), (4, 4, 2), (4, 5, 2)
    ]

    print("=== PARTIE 1: Initialisation ===")
    salle = initialiser_salle(nb_rangees, nb_colonnes, positions_tables)
    afficher_salle(salle)

    print("\nRéservation d'une table pour 4 personnes en position (1,1):")
    salle = marquer_reservation(salle, (1, 1), 4)
    afficher_salle(salle)

    print("\n=== PARTIE 2: Recherche de table ===")
    score_test = calculer_score_table((0, 0), 2, 2, nb_colonnes)
    print(f"Score table (0,0) pour 2 personnes: {score_test}")

    groupes_test = [2, 3, 4, 6]
    for taille in groupes_test:
        resultat = trouver_meilleure_table(salle, taille)
        if resultat:
            pos, taille_table = resultat
            print(f"Groupe de {taille}: Meilleure table en {pos} (capacité {taille_table})")
        else:
            print(f"Groupe de {taille}: Aucune table disponible")

    print("\n=== Rapport d'occupation ===")
    rapport = generer_rapport_occupation(salle)
    for cle, valeur in rapport.items():
        if 'taux' in cle:
            print(f"  {cle}: {valeur:.1%}")
        else:
            print(f"  {cle}: {valeur}")
