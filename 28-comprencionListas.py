palabra = 'python'

lista = []
for letra in palabra:
   lista.append(letra)
print(lista)

lista = [letra for letra in palabra]
print(lista)


#Ejercicio 1

valores = [1, 2, 3, 4, 5, 6, 9.5]
valores_cuadrado = [x**2 for x in valores]
print(valores_cuadrado)

#Ejercicio 2
#Tomaré la lista de valores

valores_pares = [par for par in valores if par % 2 == 0]
print(valores_pares)