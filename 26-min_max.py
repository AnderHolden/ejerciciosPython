# lista = [58, 20, 30]

# nombres = ['juan', 'andres', 'luisa', 'helena']
# print(max(nombres))
# print(min(nombres))

# dic = {'c1': 45, 'c2': 11}
# print

#Ejercicio 1

lista_numeros = [45492472, 2138109, 13240473, 44355629, 121676, 6854067, 335254, 123134, 59112, 51145]
valor_maximo = max(lista_numeros)
print("El valor máximo es:", valor_maximo)


#Ejercicio 2
diccionario_edades = {
    "Carlos": 55, "María": 42, "Mabel": 78, "José A.": 44, "Lucas": 24,
    "Rocío": 35, "Sebastián": 19, "Catalina": 21, "Darío": 49
}

# Obtener la edad máxima y mínima
edad_max = max(diccionario_edades.values())
edad_min = min(diccionario_edades.values())

# Obtener el último nombre en orden alfabético
ultimo_nombre = max(diccionario_edades.keys())

print("La edad máxima es:", edad_max)
print("La edad mínima es:", edad_min)
print("El último nombre en orden alfabético es:", ultimo_nombre)
