'''
En Python, hay varias estructuras de datos comunes que se utilizan para almacenar colecciones de valores. Aquí está la diferencia entre listas, tuplas, diccionarios, conjuntos y conjuntos congelados:
'''
#Listas (list):
'''
Son colecciones ordenadas y mutables de elementos.
Se pueden acceder a los elementos de una lista mediante índices numéricos.
Pueden contener elementos duplicados.
Los elementos de una lista pueden ser de cualquier tipo de datos.
'''
#----------------------------------------------------------------
# Crear una lista vacía
my_list = []
other_list = ["apple", "banana", "cherry"]
# Agregar elementos a la lista
my_list.append("apple")
my_list.append("banana")
my_list.append("cherry")

# Acceder a un elemento de la lista
print(my_list[0])  # Output: "apple"

# Recorrer la lista con un ciclo for
for fruit in my_list:
    print(fruit)
#----------------------------------------------------------------
#Tuplas (tuple):
"""
Son colecciones ordenadas e inmutables de elementos.
Nota: INMUTABLES = TypeError: 'tuple' object does not support item assignment
Se pueden acceder a los elementos de una tupla mediante índices numéricos.
Pueden contener elementos duplicados.
Los elementos de una tupla pueden ser de cualquier tipo de datos.
"""
#----------------------------------------------------------------
# Crear una tupla
my_tuple = ("apple", "banana", "cherry")
# my_tuple[0] = "naranja" -> TypeError: 'tuple' object does not support item assignment
# Acceder a un elemento de la tupla
print(my_tuple[1])  # Output: "banana"

# Recorrer la tupla con un ciclo for
for fruit in my_tuple:
    print(fruit)
#----------------------------------------------------------------
#Diccionarios (dict):
'''
Son colecciones no ordenadas y mutables de pares clave-valor.
Se accede a los valores de un diccionario mediante la clave asociada a cada valor.
Las claves de un diccionario deben ser únicas y deben ser de tipo hashable (por ejemplo, una cadena o un número).
Los valores de un diccionario pueden ser de cualquier tipo de datos.
'''
#----------------------------------------------------------------
# Crear un diccionario vacío
my_dict = {}
other_dict = {"name" : "John", "age" : 36}
# Agregar elementos al diccionario
my_dict["name"] = "John"
my_dict["age"] = 30
my_dict["city"] = "New York"

# Acceder a un valor del diccionario
print(my_dict["name"])  # Output: "John"

# Recorrer el diccionario con un ciclo for
for key, value in my_dict.items():
    print(key, value)

other_dict = {"name" : "John", "age" : 36}
print(other_dict["name"])
print(other_dict["age"])
for k, v in other_dict.items():
    print(k, v)
#----------------------------------------------------------------
#Conjuntos (set):
'''
Son colecciones no ordenadas y mutables de elementos únicos.
No se pueden acceder a los elementos de un conjunto mediante índices numéricos.
Los elementos de un conjunto deben ser únicos y deben ser de tipo hashable (por ejemplo, una cadena o un número).
'''
#----------------------------------------------------------------
# Crear un conjunto
my_set = set()
my_set2 = {"banana","pera","kiwi","pera","apple"}
# Agregar elementos al conjunto
my_set.add("apple")
my_set.add("banana")
my_set.add("cherry")
my_set.add("cherry")

# Acceder al conjunto completo
print(my_set)  # Output: {"apple", "banana", "cherry"}
#NOTA: solo imprime un cherry. ELEMENTOS UNICOS

# Verificar si un elemento está en el conjunto
print("banana" in my_set)  # Output: True

#Remove all elements of another set from this set.
my_set.difference_update(my_set2)
print(my_set)
#{'cherry', 'apple'}

#----------------------------------------------------------------

#Conjuntos congelados (frozenset):
'''
Son conjuntos inmutables de elementos únicos.
Los elementos de un conjunto congelado deben ser únicos y deben ser de tipo hashable (por ejemplo, una cadena o un número).
Al igual que los conjuntos, los conjuntos congelados no pueden contener elementos duplicados y 
no se pueden acceder a ellos mediante índices numéricos.
'''
# Crear un conjunto congelado
my_frozenset = frozenset(["apple", "banana", "cherry"])

# Acceder al conjunto completo
print(my_frozenset)  # Output: frozenset({"apple", "banana", "cherry"})

# Verificar si un elemento está en el conjunto congelado
print("banana" in my_frozenset)  # Output: True

#Return the difference of two or more sets as a new set.
#(i.e. all elements that are in this set but not the others.)
print(my_frozenset.difference(my_set2))
# frozenset({'cherry'})
