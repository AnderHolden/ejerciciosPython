monedas = 5
while monedas >0:
    print(f"Tengo {monedas} monedas")
    monedas -= 1

respuesta = 's'

while respuesta == 's':
    respuesta = input("Quieres salir? (s/n)")


numero = 0
while numero <= 10:
    print(numero)
    numero += 1  # Incrementa el valor de numero en 1 en cada iteración

numero = 50
while numero >= 0:
    if numero % 5 == 0:
        print(numero)
    numero -= 1  # Decrementa el valor de numero en 1 en cada iteración
