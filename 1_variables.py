
# ┌─────────────────────────────────────┐
# │1. Variables et Types de Données     │
# │                                     │
# └─────────────────────────────────────┘

# Variables :
# Explication : Les variables sont utilisées pour stocker et gérer les données dans un programme.
# Elles agissent comme des conteneurs pour stocker des valeurs.
# Opérations Possibles :
# Affectation : nom_variable = valeur
# Réaffectation : nom_variable = nouvelle_valeur
# Affectation Multiple : x, y = 10, 20

nom_variable = "Bonjour"
print("Contenu de nom_variable :", nom_variable)

nouvelle_valeur = "Salut"
nom_variable = nouvelle_valeur
print("Nouveau contenu de nom_variable :", nom_variable)

x, y = 10, 20
print("Valeur de x :", x)
print("Valeur de y :", y)

# Types Numériques (int, float) :
# Explication : Les entiers (int) représentent des nombres entiers, et les flottants (float) représentent des nombres décimaux.
# Opérations Possibles :
# Opérations Arithmétiques : +, -, *, /, //, %
# Opérations de Comparaison : >, <, >=, <=, ==, !=
# Conversion de Type : int(x), float(y)

entier = 5
flottant = 3.14

# Opérations arithmétiques
somme = entier + flottant
print("Somme :", somme)

# Opération de comparaison
comparaison = entier > flottant
print("Comparaison :", comparaison)

# Conversion de type
conversion_entier = int(flottant)
conversion_flottant = float(entier)
print("Conversion Entier :", conversion_entier)
print("Conversion Flottant :", conversion_flottant)

# Chaînes de Caractères :
# Explication : Les chaînes de caractères sont des séquences de caractères et sont utilisées pour représenter du texte.
# Opérations Possibles :
# Concaténation : "Bonjour" + " " + "le Monde"
# Indexation et Tranchage : variable_chaine[0], variable_chaine[1:5]
# Méthodes sur les Chaînes : len(), lower(), upper()

chaine1 = "Hello"
chaine2 = "World"

# Concaténation
concatenation = chaine1 + " " + chaine2
print("Concaténation :", concatenation)

# Indexation et tranchage
indexation = chaine1[0]
tranchage = chaine2[1:3]
print("Indexation :", indexation)
print("Tranchage :", tranchage)

# Méthodes sur les chaînes
longueur_chaine = len(concatenation)
chaine_minuscules = concatenation.lower()
chaine_majuscules = concatenation.upper()
print("Longueur de la chaîne :", longueur_chaine)
print("En minuscules :", chaine_minuscules)
print("En majuscules :", chaine_majuscules)

# Conversion de Type :
# Explication : Conversion d'un type de données à un autre.
# Opérations Possibles :
# int(), float(), str(), list(), tuple(), set(), dict()

nombre_entier = 42
nombre_flottant = 3.14

# Conversion de type vers int
conversion_entier = int(nombre_flottant)
print("Conversion Flottant vers Entier :", conversion_entier)

# Conversion de type vers float
conversion_flottant = float(nombre_entier)
print("Conversion Entier vers Flottant :", conversion_flottant)
