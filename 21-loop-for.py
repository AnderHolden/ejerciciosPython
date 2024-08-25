# name  = ['Juan', 'Ander', 'Carlos', 'Belén']
# for elemento in name:
#     print("hola")

# lista = ['a','b', 'c']
# for letra in lista:
#     print("Esta es la letra "+letra)

# for letra in lista:
#     numero_letra = lista.index(letra) + 1
#     print(f"Letra {numero_letra}: {letra}")

# lista2 = ['Pablo', 'Juan', 'Andres', 'lucia']
# for nombre in lista2:
#     if nombre.startswith('l'):
#         print(nombre)
#     else:
#         print("Este nombre no comienza con l")

# for letra in 'python':
#     print(letra)

# for numero in [1,2,3,4]:
#     print(numero)
# for numero in (1,2,3,4,5):
#     print(numero)

# for a,b,c in [[1,2,3], [3,4,0],[5,6,7]]:
#     print(a)
#     print(b)
#     print(c)

# dic = {'clave1': 'a', 'clave2': 'b'}
# for item in dic:
#     print(item)

# for item in dic.values():
#     print(item)
    
# for a,b in dic.items():
#     print(a,b)


#1
lista1 = ['María', 'José', 'Carlos', 'Martina', 'isabel', 'Tomás', 'Daniela']
for nombre in lista1:
     print("Hola " +nombre)

#2
lista_numeros = [1, 5, 8, 7, 6, 8, 2, 5, 2, 6, 4, 8, 5, 9, 8, 3, 5, 4, 2, 5, 6, 4]
suma_numeros = 0

for numero in lista_numeros:
    suma_numeros = suma_numeros + numero
print(suma_numeros)


#3
suma_pares = 0
suma_impares = 0

for numero in lista_numeros:
    if numero % 2 == 0:
        suma_pares += numero
    else:
        suma_impares += numero

print("Suma de números pares:", suma_pares)
print("Suma de números impares:", suma_impares)
