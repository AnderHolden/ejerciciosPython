#Ejercicio 1

import random
# Obtener un número aleatorio entre 1 y 10
aleatorio = random.randint(1, 10)
print("El número aleatorio es:", aleatorio)

#Ejercicio 2

import random
# Obtener un número aleatorio entre 0 y 1
aleatorio1 = random.random()
print("El número aleatorio es:", aleatorio1)

#Ejercicio 3

import random
# Lista de nombres
nombres = ["Carlos", "Julia", "Nicole", "Laura", "Mailen"]
# Obtener un nombre aleatorio de la lista
sorteo = random.choice(nombres)
print("El nombre seleccionado es:", sorteo)
