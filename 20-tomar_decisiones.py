# if 10 < 9:
#     print('Es correcto')

# if True:
#     print("Es correcto")

# if 2 == 5:
#     print("Es correcto")
# else:
#     print("No es correcto")

# mascota = "perro"

# if mascota == "perro":
#     print("Tu mascota es un perro")
# elif mascota == "gato":
#     print("Tu mascota es un gato")
# elif mascota == "loro":
#     print("Tu mascota es un loro")
# else:
#     print("No tienes mascota")

# edad = 15
# calificacion = 5

# if edad < 18:
#     print("Eres menor de edad")
#     if calificacion >= 3:
#         print("Aprobaste el curso")
#     else:
#         print('No aprobaste el curso')
# else:
#     print("Eres adulto")

num1 = int(input("Ingresa un número: "))
num2 = int(input("Ingresa otro número: "))

if num1 > num2:
    print(f"{num1} es mayor que {num2}")
elif num2 > num1:
    print(f"{num2} es mayor que {num1}")
else:
    print(f"{num1} y {num2} son iguales")
