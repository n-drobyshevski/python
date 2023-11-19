# ┌─────────────────────────────────────┐
# │        3. Flux de Contrôle :        │
# │                                     │
# └─────────────────────────────────────┘

# a. Instructions Conditionnelles :

# Les instructions conditionnelles permettent à votre programme de prendre des décisions en fonction de certaines conditions.
# Vous pouvez les considérer comme "si cette condition est vraie, fais ceci ; sinon, fais quelque chose d'autre."

# Instruction if (Si) :
# Explication : Exécute un bloc de code uniquement si une condition spécifiée est vraie.
# Exemple :
age = 20
if age >= 18:
    print("Vous êtes majeur.")

# Instruction else (Sinon) :
# Explication : Fournit un bloc de code alternatif à exécuter si la condition dans l'instruction if n'est pas vraie.
# Exemple :
age = 15
if age >= 18:
    print("Vous êtes majeur.")
else:
    print("Vous êtes mineur.")

# Instruction elif (Sinon Si) :
# Explication : Utilisée lorsque vous avez plusieurs conditions à vérifier. Signifie "sinon si".
# Exemple :
score = 75
if score >= 90:
    print("A")
elif score >= 80:
    print("B")
else:
    print("C")

# b. Boucles :

# Les boucles vous permettent de répéter un bloc de code plusieurs fois.
# Considérez-les comme une façon d'automatiser des tâches répétitives.

# Boucle for :
# Explication : Itère sur une séquence (par exemple, une liste, un tuple, une chaîne de caractères) 
# et exécute un bloc de code pour chaque élément de la séquence.
# Exemple :
fruits = ["pomme", "banane", "orange"]
for fruit in fruits:
    print(fruit)

# Boucle while :
# Explication : Répète un bloc de code tant qu'une condition spécifiée est vraie.
# Exemple :
count = 0
while count < 3:
    print("Compte :", count)
    count += 1

# c. Instructions break et continue :

# Instruction break :
# Explication : Utilisée pour sortir prématurément d'une boucle si une certaine condition est remplie.
# Exemple :
for i in range(10):
    if i == 5:
        break
    print(i)

# Instruction continue :
# Explication : Passe le reste du code à l'intérieur de la boucle pour l'itération en cours 
# et passe à l'itération suivante.
# Exemple :
for i in range(10):
    if i % 2 == 0:
        continue
    print(i)

# d. Cas d'utilisation pour Différents Types de Données et Situations :

# Listes :
# Explication : Une collection d'éléments. Les boucles peuvent itérer sur chaque élément d'une liste.
# Exemple :
nombres = [1, 2, 3, 4, 5]
for num in nombres:
    print(num)

# Chaînes de Caractères :
# Explication : Une séquence de caractères. Les boucles peuvent itérer sur chaque caractère d'une chaîne de caractères.
# Exemple :
message = "Bonjour, Python !"
for char in message:
    print(char)

# Tuples :
# Explication : Similaires aux listes mais immuables (ne peuvent pas être modifiées). Extraction des valeurs d'un tuple.
# Exemple :
coordonnees = (3, 4)
x, y = coordonnees
print("X :", x, "Y :", y)

# Ensembles :
# Explication : Une collection d'éléments uniques. Les boucles peuvent itérer sur chaque élément unique d'un ensemble.
# Exemple :
nombres_uniques = {1, 2, 3, 1, 2, 3}
for num in nombres_uniques:
    print(num)

# Dictionnaires :
# Explication : Une collection de paires clé-valeur. Les boucles peuvent itérer sur les clés et les valeurs.
# Exemple :
notes_eleves = {"Alice": 85, "Bob": 92, "Charlie": 78}
for nom, note in notes_eleves.items():
    print(nom, ":", note)

# Combinaison du Flux de Contrôle et des Fonctions :
# Explication : Les fonctions peuvent être utilisées à l'intérieur des boucles pour un code plus organisé et réutilisable.
# Exemple :
def traiter_nombres(nombres):
    for num in nombres:
        if num > 0:
            print("Positif :", num)
        else:
            print("Non-positif :", num)

liste_nombres = [2, -5, 8, -3, 0]
traiter_nombres(liste_nombres)