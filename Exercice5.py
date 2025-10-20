"""
TP2 - Exercice 5 : Analyse de la satisfaction client
"""

def analyser_commentaire(commentaire, mots_cles):
    score_total = 5  # Base neutre
    mots_trouves = []

    commentaire_lower = commentaire.lower()

    for char in '.,!?;:()[]{}"\'-':
        commentaire_lower = commentaire_lower.replace(char, ' ')
    mots_commentaire = commentaire_lower.split()

    # Recherche des mots-clés
    for mot, valeur in mots_cles.items():
        for mot_c in mots_commentaire:
            if mot_c == mot or mot_c.startswith(mot):
                score_total += valeur
                mots_trouves.append(mot)
                break  # éviter double comptage du même mot

    # Borner entre 0 et 10
    score_total = max(0, min(10, score_total))

    return score_total, mots_trouves


def categoriser_commentaires(liste_commentaires, mots_cles):
    categories = {'positifs': [], 'neutres': [], 'negatifs': []}

    for commentaire in liste_commentaires:
        score, mots = analyser_commentaire(commentaire, mots_cles)
        if score >= 7:
            categories['positifs'].append((commentaire, score))
        elif score >= 4:
            categories['neutres'].append((commentaire, score))
        else:
            categories['negatifs'].append((commentaire, score))

    return categories


def identifier_problemes(commentaires_negatifs, mots_cles_negatifs):
    frequence_problemes = {}

    for commentaire in commentaires_negatifs:
        commentaire_lower = commentaire.lower()
        for char in '.,!?;:()[]{}"\'-':
            commentaire_lower = commentaire_lower.replace(char, ' ')
        mots_commentaire = commentaire_lower.split()

        for mot in mots_cles_negatifs:
            for mot_c in mots_commentaire:
                if mot_c == mot or mot_c.startswith(mot):
                    frequence_problemes[mot] = frequence_problemes.get(mot, 0) + 1
                    break

    # Normaliser en pourcentage
    total_negatifs = len(commentaires_negatifs)
    if total_negatifs > 0:
        for mot in frequence_problemes:
            frequence_problemes[mot] = (frequence_problemes[mot] / total_negatifs) * 100

    # Trier décroissant
    frequence_problemes = dict(sorted(frequence_problemes.items(), key=lambda x: x[1], reverse=True))

    return frequence_problemes


def generer_rapport_satisfaction(categories, frequence_problemes):
    rapport = {
        'satisfaction_moyenne': 0.0,
        'distribution': {},
        'points_forts': [],
        'points_amelioration': [],
    }

    total_commentaires = sum(len(v) for v in categories.values())
    if total_commentaires == 0:
        return rapport

    # Satisfaction moyenne
    somme_scores = sum(score for cat in categories.values() for _, score in cat)
    rapport['satisfaction_moyenne'] = somme_scores / total_commentaires

    # Distribution
    rapport['distribution'] = {
        'positifs': len(categories['positifs']) / total_commentaires,
        'neutres': len(categories['neutres']) / total_commentaires,
        'negatifs': len(categories['negatifs']) / total_commentaires
    }

    # Points forts : mots-clés positifs dominants
    rapport['points_forts'] = [c[0][:30] for c in categories['positifs'][:3]]

    # Points d’amélioration : top 3 problèmes
    rapport['points_amelioration'] = list(frequence_problemes.keys())[:3]

    return rapport


def calculer_tendance(historique_scores):
    if len(historique_scores) < 2:
        return 'stable'

    valeurs = [score for _, score in historique_scores]
    if all(valeurs[i] < valeurs[i+1] for i in range(len(valeurs)-1)):
        return 'amélioration'
    elif all(valeurs[i] > valeurs[i+1] for i in range(len(valeurs)-1)):
        return 'dégradation'
    else:
        return 'stable'


# ========================= TESTS =========================
if __name__ == '__main__':
    mots_cles = {
        'excellent': 3, 'délicieux': 2, 'parfait': 3,
        'rapide': 1, 'frais': 2, 'savoureux': 2,
        'accueillant': 1, 'propre': 1, 'recommande': 2,
        'froid': -2, 'lent': -3, 'décevant': -2,
        'cher': -1, 'sale': -3, 'impoli': -2,
        'insipide': -2, 'attente': -1, 'déçu': -2
    }

    commentaires_test = [
        "Service excellent et plats délicieux! Je recommande vivement.",
        "Attente trop longue, et les plats étaient froids.",
        "Restaurant propre mais un peu cher pour la qualité.",
        "Très déçu, service lent et nourriture insipide.",
        "Accueil chaleureux, plats frais et savoureux!",
        "Correct, sans plus. Prix raisonnables.",
        "Parfait! Rapide, délicieux et accueillant.",
        "Sale et impoli, vraiment décevant.",
        "Bonne ambiance mais l'attente était longue.",
        "Les plats sont excellents mais le service est lent."
    ]

    print("=== Analyse individuelle ===")
    for i, comm in enumerate(commentaires_test[:3], 1):
        score, mots = analyser_commentaire(comm, mots_cles)
        print(f"{i}) Score: {score}/10 — mots trouvés: {mots}")

    print("\n=== Catégorisation ===")
    categories = categoriser_commentaires(commentaires_test, mots_cles)
    for cat, comms in categories.items():
        print(f"{cat.capitalize()}: {len(comms)} commentaires")

    print("\n=== Problèmes négatifs ===")
    mots_negatifs = {k: v for k, v in mots_cles.items() if v < 0}
    commentaires_negatifs = [c[0] for c in categories['negatifs']]
    problemes = identifier_problemes(commentaires_negatifs, mots_negatifs)
    print(problemes)

    print("\n=== Rapport général ===")
    rapport = generer_rapport_satisfaction(categories, problemes)
    for k, v in rapport.items():
        print(f"{k}: {v}")

    print("\n=== Tendance ===")
    historique = [['Janvier', 6.5], ['Février', 6.8], ['Mars', 7.1], ['Avril', 7.3]]
    print("Tendance:", calculer_tendance(historique))
