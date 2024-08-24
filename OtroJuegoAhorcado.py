import random

def elegir_palabra():
    palabras = ['Colombia', 'Argentina', 'China', 'Corea', 'Brasil']
    return random.choice(palabras)

def pedir_letra():
    letra = input("Por favor, elige una letra: ")
    while not letra.isalpha() or len(letra) != 1:
        letra = input("Entrada inválida. Por favor, elige una letra: ")
    return letra.lower()

def actualizar_estado(palabra, intentos, estado):
    if intentos in palabra:
        return "".join([letra if letra == intentos else estado[i] for i, letra in enumerate(palabra)])
    return estado

def jugar_ahorcado():
    palabra = elegir_palabra()
    estado = "_" * len(palabra)
    vidas = 6

    while vidas > 0 and estado != palabra:
        print(f"\nPalabra: {estado}")
        print(f"Vidas restantes: {vidas}")
        intentos = pedir_letra()

        estado_anterior = estado
        estado = actualizar_estado(palabra, intentos, estado)

        if estado == estado_anterior:
            vidas -= 1

    if vidas > 0:
        print(f"\n¡Felicidades! Has adivinado la palabra: {palabra}")
    else:
        print(f"\nLo siento, has perdido. La palabra era: {palabra}")

jugar_ahorcado()
