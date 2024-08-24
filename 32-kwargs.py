
# def suma(**kwargs):
#     total = 0
#     for clave, valor in kwargs.items():
#         print(f"{clave}={valor}")
#         total += valor
#     print(f"La suma total es {total}")

# suma(x=1, y=3, Z=7)

def prueba(num1, num2, *args, **kwargs):
   print(f"El numero 1 es {num1}")
   print(f"El numero 1 es {num2}")
   for arg in args:
      print(f"args = {arg}")
   for clave, valor in kwargs.items():
      print(f"{clave} = {valor}")

prueba(15, 50, 100, 200, 300, x=1, y=5, z=2)