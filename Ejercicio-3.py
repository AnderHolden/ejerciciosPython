#Paso 1: Ingresar texto

texto = input("Ingrese un texto de su preferencia, ya sea un párrafo, una frase etc: ")

#Paso 2: Ingresar 3 letras

letras = [letra.lower() for letra in input("Ingresa tres letras a analizar separadas por espacios: ").split()]

#Paso 3: Contar cuántas veces aparece cada una de las letras elegidas
for letra in letras:
    cantidad = texto.lower().count(letra)
    print(f"La letra '{letra}' aparece {cantidad} veces en el texto.")

#Paso 4: Contar la cantidad de palabras en el texto
palabras = texto.split()
cantidad_palabras = len(palabras)
print(f"El texto tiene {cantidad_palabras} palabras.")

#Paso 5: Mostrar la primera y última letra del texto
primera_letra = texto[0]
ultima_letra = texto[-1]
print(f"La primera letra del texto es '{primera_letra}' y la última es '{ultima_letra}'.")

#Paso 6: Invertir el orden de las palabras en el texto
palabras_invertidas = " ".join(palabras[::-1])
print(f"El texto con las palabras invertidas quedaría así:\n{palabras_invertidas}")

# Paso 5: Verificar si la palabra "Python" está en el texto
if "python" in texto.lower():
    print("La palabra 'Python' se encuentra en el texto.")
else:
    print("La palabra 'Python' no se encuentra en el texto.")
