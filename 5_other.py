# ┌─────────────────────────────────────┐
# │  5. PROGRAMMATION ORIENTÉE OBJET (POO) │
# └─────────────────────────────────────┘

# Fondamentaux des classes et des objets :
# En Python, les classes sont utilisées pour créer des objets, qui regroupent données et fonctionnalités. 
# Créons une classe Personne simple :

# Définition de la classe
class Personne:
    def __init__(self, nom, age):
        self.nom = nom
        self.age = age

    def se_presenter(self):
        print(f"Salut, je m'appelle {self.nom}, et j'ai {self.age} ans.")

# Explication :
#   - La méthode __init__ est une méthode spéciale appelée constructeur, utilisée pour initialiser les attributs de l'objet.
#   - self fait référence à l'instance de l'objet en cours de création.
#   - se_presenter est une méthode qui imprime une introduction simple.

# Exemple d'utilisation :
# Création d'instances
personne1 = Personne("Alice", 25)
personne2 = Personne("Bob", 30)

# Invocation des méthodes
personne1.se_presenter()  # Résultat : Salut, je m'appelle Alice, et j'ai 25 ans.
personne2.se_presenter()  # Résultat : Salut, je m'appelle Bob, et j'ai 30 ans.

# ┌─────────────────────────────────────┐
# │           6. GESTION DES FICHIERS     │
# └─────────────────────────────────────┘

# Lecture et écriture dans les fichiers :
# Créons un exemple simple de lecture depuis et écriture dans un fichier :

# Écriture dans un fichier
with open("exemple.txt", "w") as fichier:
    fichier.write("Bonjour, ceci est un texte d'exemple.\nBienvenue dans la gestion de fichiers en Python !")

# Lecture depuis un fichier
with open("exemple.txt", "r") as fichier:
    contenu = fichier.read()
    print(contenu)

# Explication :
#   - open est utilisé pour ouvrir un fichier. Le premier argument est le nom du fichier, et le deuxième argument est le mode ("w" pour écrire, "r" pour lire).
#   - with est utilisé pour le nettoyage automatique (fermeture du fichier).

# Exemple d'utilisation :
# Le contenu du fichier sera imprimé.

# ┌─────────────────────────────────────┐
# │      7. GESTION DES EXCEPTIONS       │
# └─────────────────────────────────────┘

# Try, Except, Else et Finally :
# Créons un exemple de gestion des exceptions :

# Fonction pour diviser des nombres
def diviser(x, y):
    try:
        resultat = x / y
    except ZeroDivisionError:
        print("Erreur : Division par zéro !")
    else:
        print(f"Le résultat est : {resultat}")
    finally:
        print("Cela sera toujours exécuté.")

# Exemple d'utilisation
diviser(10, 2)   # Résultat : Le résultat est : 5.0 \n Cela sera toujours exécuté.
diviser(10, 0)   # Résultat : Erreur : Division par zéro ! \n Cela sera toujours exécuté.

# Explication :
#   - Le bloc try contient le code qui pourrait générer une exception.
#   - Le bloc except est exécuté si une exception spécifique se produit.
#   - Le bloc else est exécuté s'il n'y a pas d'exceptions.
#   - Le bloc finally est toujours exécuté.

# Exemple d'utilisation :
# Appeler diviser(10, 2) et diviser(10, 0) démontre les résultats différents.
