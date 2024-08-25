nombre = ["Ana", "Ander", "Lorena"]
edades = [20, 50, 15, 20, 40]

combinados = list(zip(nombre, edades))
print(combinados)

for nombre, edad in combinados:
    print(f"{nombre} tiene {edad} años" )