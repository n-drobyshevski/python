# ┌─────────────────────────────────────┐
# │       2. Structures de données      │
# │                                     │
# └─────────────────────────────────────┘

# 2.1 Listes :
# Explication :
#   Les listes sont des séquences ordonnées et modifiables.
#   Méthodes :
#       append(élément) : Ajoute un élément à la fin de la liste.
#       extend(itérable) : Étend la liste en ajoutant des éléments d'un itérable.
#       insert(index, élément) : Insère un élément à l'index spécifié.
#       remove(élément) : Supprime la première occurrence de l'élément spécifié.
#       pop([index]) : Supprime et renvoie l'élément à l'index spécifié (ou le dernier élément si l'index n'est pas fourni).

# Exemples :
ma_liste = [1, 2, 'trois', 4.0, [5, 6]]

# Append et extend
ma_liste.append(7)
print(ma_liste)           # Sortie : [1, 2, 'trois', 4.0, [5, 6], 7]

ma_liste.extend([8, 9])
print(ma_liste)           # Sortie : [1, 2, 'trois', 4.0, [5, 6], 7, 8, 9]

# Insert et remove
ma_liste.insert(2, 'nouveau')
print(ma_liste)           # Sortie : [1, 2, 'nouveau', 'trois', 4.0, [5, 6], 7, 8, 9]

ma_liste.remove('trois')
print(ma_liste)           # Sortie : [1, 2, 'nouveau', 4.0, [5, 6], 7, 8, 9]

# Pop
élément_supprimé = ma_liste.pop(4)
print(ma_liste)           # Sortie : [1, 2, 'nouveau', 4.0, 7, 8, 9]
print(élément_supprimé)    # Sortie : [5, 6]

# Cas d'utilisation :
#   Lorsque l'ordre et la mutabilité des éléments sont importants.
#   Utile pour des collections susceptibles de changer de taille.

# 2.2 Tuples :
# Explication :
#   Les tuples sont des séquences ordonnées et immuables.
#   Méthodes :
#       count(élément) : Renvoie le nombre d'occurrences de l'élément spécifié.
#       index(élément) : Renvoie l'index de la première occurrence de l'élément spécifié.

# Exemples :
mon_tuple = (1, 2, 'trois', 4.0, 'trois')

# Count et index
compter_trois = mon_tuple.count('trois')
print(compter_trois)        # Sortie : 2

index_trois = mon_tuple.index('trois')
print(index_trois)          # Sortie : 2

# Cas d'utilisation :
#   Lorsque les données ne doivent pas être modifiées après leur création.
#   Utile pour renvoyer plusieurs valeurs depuis une fonction.

# 2.3 Ensembles :
# Explication :
#   Les ensembles sont des collections non ordonnées d'éléments uniques.
#   Méthodes :
#       add(élément) : Ajoute un élément à l'ensemble.
#       remove(élément) : Supprime l'élément spécifié.
#       discard(élément) : Supprime l'élément spécifié s'il est présent.
#       pop() : Supprime et renvoie un élément arbitraire.

# Exemples :
mon_ensemble = {1, 2, 3, 4, 5}

# Ajouter et supprimer
mon_ensemble.add(6)
print(mon_ensemble)             # Sortie : {1, 2, 3, 4, 5, 6}

mon_ensemble.remove(3)
print(mon_ensemble)             # Sortie : {1, 2, 4, 5, 6}

# Discard et pop
mon_ensemble.discard(2)
print(mon_ensemble)             # Sortie : {1, 4, 5, 6}

élément_supprimé = mon_ensemble.pop()
print(élément_supprimé)         # Sortie : 1

# Cas d'utilisation :
#   Lorsque l'unicité et l'absence d'ordre sont essentielles.
#   Utile pour des opérations mathématiques comme l'union, l'intersection, etc.

# 2.4 Dictionnaires :
# Explication :
#   Les dictionnaires sont des collections non ordonnées de paires clé-valeur.
#   Méthodes :
#       keys() : Renvoie une vue des clés du dictionnaire.
#       values() : Renvoie une vue des valeurs du dictionnaire.
#       items() : Renvoie une vue des paires clé-valeur du dictionnaire.
#       get(clé, valeur_par_défaut) : Renvoie la valeur pour la clé spécifiée ou une valeur par défaut si la clé n'est pas trouvée.
#       pop(clé[, valeur_par_défaut]) : Supprime et renvoie la valeur pour la clé spécifiée.

# Exemples :
mon_dictionnaire = {'nom': 'John', 'âge': 25, 'ville': 'New York'}

# Clés, valeurs et items
print(mon_dictionnaire.keys())         # Sortie : dict_keys(['nom', 'âge', 'ville'])
print(mon_dictionnaire.values())       # Sortie : dict_values(['John', 25, 'New York'])
print(mon_dictionnaire.items())        # Sortie : dict_items([('nom', 'John'), ('âge', 25), ('ville', 'New York')])

# Get et pop
âge = mon_dictionnaire.get('âge')
print(âge)                             # Sortie : 25

ville_supprimée = mon_dictionnaire.pop('ville')
print(ville_supprimée)                 # Sortie : 'New York'

# Cas d'utilisation :
#   Lorsque les données doivent être stockées sous forme de paires clé-valeur.
#   Récupération, mise à jour et suppression de valeurs en fonction des clés.

# 2.5 Conversion de types :
# Explication :
#   Conversion d'un type de données en un autre.
#   Méthodes :
#       str(objet) : Convertit l'objet en une chaîne de caractères.
#       int(objet, base) : Convertit l'objet en un entier.
#       float(objet) : Convertit l'objet en un nombre flottant.

# Exemples :
# Entier en chaîne
num_entier = 123
num_chaine = str(num_entier)
print(num_chaine)                      # Sortie : '123'

# Chaîne en entier
chaine_num = "456"
num_entier = int(chaine_num)
print(num_entier)                      # Sortie : 456

# Cas d'utilisation :
#   Lorsque des données d'un type doivent être utilisées dans un contexte nécessitant un autre type.
#   Opérations d'entrée/sortie où le type de données doit correspondre.

# 2.6 bytes :
# Explication :
#   Les bytes représentent une séquence d'octets.
#   Méthodes :
#       decode(encodage) : Décode les bytes en utilisant l'encodage spécifié.
#       hex() : Convertit les bytes en une chaîne de nombres hexadécimaux.

# Exemples :
mes_bytes = b'hello'

# Décode et hexadécimal
chaîne_décodée = mes_bytes.decode('utf-8')
print(chaîne_décodée)                  # Sortie : 'hello'

représentation_hexa = mes_bytes.hex()
print(représentation_hexa)             # Sortie : '68656c6c6f'

# Cas d'utilisation :
#   Manipulation de données binaires, comme la lecture/écriture de fichiers.
#   Communication avec des systèmes ou des appareils externes.
