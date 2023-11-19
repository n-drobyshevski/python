# ┌─────────────────────────────────────┐
# │        4. Fonctions                 │
# │                                     │
# └─────────────────────────────────────┘

# 4.1 Définition des Fonctions :

# En Python, les fonctions sont définies à l'aide du mot-clé def.
# Une fonction peut prendre ou non des paramètres et peut ou non renvoyer une valeur.

def saluer(nom):
    """Cette fonction salue la personne passée en paramètre."""
    print(f"Bonjour, {nom} !")

# Appel de la fonction
saluer("Alice")

# La fonction saluer déclare une fonction appelée saluer qui prend un paramètre (nom).
# La chaîne de documentation (docstring) entre triples guillemets immédiatement
# après la déclaration de la fonction fournit une brève description de l'objectif de la fonction.

# 4.2 Arguments de Fonction et Valeurs de Retour :

# Les fonctions peuvent prendre plusieurs paramètres, et vous pouvez spécifier des
# valeurs par défaut pour ces paramètres. Elles peuvent également renvoyer des valeurs
# à l'aide de l'instruction return.

def additionner_nombres(x, y=0):
    """Cette fonction additionne deux nombres et renvoie le résultat."""
    return x + y

resultat = additionner_nombres(5, 3)
print(resultat)  # Sortie : 8

resultat_avec_defaut = additionner_nombres(5)
print(resultat_avec_defaut)  # Sortie : 5

# La fonction additionner_nombres prend deux paramètres, x et y (avec une valeur par défaut de 0).
# La fonction renvoie la somme de x et y.

# 4.3 Fonctions Lambda :

# Les fonctions lambda, ou fonctions anonymes, sont des moyens concis de définir de petites fonctions.
# Elles sont créées à l'aide du mot-clé lambda.

multiplier = lambda x, y: x * y
resultat = multiplier(4, 6)
print(resultat)  # Sortie : 24

# La fonction lambda multiplier prend deux paramètres, x et y, et renvoie leur produit.
# Les fonctions lambda sont souvent utilisées pour des opérations de courte durée.

# 4.4 Utilisation de Fonctions avec Différents Types de Données :

# Les fonctions peuvent fonctionner sur divers types de données, offrant une flexibilité d'utilisation.

# Types Numériques :

def carre(x):
    """Renvoie le carré d'un nombre."""
    return x ** 2

resultat_carre = carre(4)
print(resultat_carre)  # Sortie : 16

# Chaînes de Caractères :

def repetition_chaine(s, n):
    """Répète une chaîne de caractères n fois."""
    return s * n

resultat_repetition = repetition_chaine("Bonjour", 3)
print(resultat_repetition)  # Sortie : BonjourBonjourBonjour

# Listes :

def somme_liste(nombres):
    """Renvoie la somme d'une liste de nombres."""
    return sum(nombres)

resultat_somme = somme_liste([1, 2, 3, 4])
print(resultat_somme)  # Sortie : 10
