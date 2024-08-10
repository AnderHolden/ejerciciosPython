# lista = ['a', 'b', 'c']

# for item in enumerate(lista):
#     print(item)

# for indice, elemnetos in enumerate(range(50,55)):
#     print(indice, elemnetos)

# mis_tuplas =list(enumerate(lista))
# print(mis_tuplas)

"""
ejercicio
"""
string = "Python"
lista_indices = list(enumerate(string))
print(lista_indices)

palabra = "Python"
lista = list(enumerate(palabra))
print(lista)

lista_nombres = ["Marcos", "Laura", "Mónica", "Javier", "Celina", "Marta", "Dario", "Emiliano", "Melisa"]

for indice, nombre in enumerate(lista_nombres):
    if nombre.startswith("M"):
        print(indice)
