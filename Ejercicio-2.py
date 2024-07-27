# Primero: Pedir al usuario al usuario su nombre y ventas totales

nombre = input("¿Cuál es tu nombre?")
ventas = float(input("¿Cuánto has vendido este mes?"))

#Segundo: Calacular la comisión del 13% de las ventas

comision = ventas * 0.13

#formatear

mensaje = f"Hola{nombre}, tu comision es ${comision: .2f}"
#Imprimir mensaje
print(mensaje)
