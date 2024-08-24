def suma(*args):
   total = 0
   for arg in args:
      total += arg
   return total
respuesta = suma(2,3,5,4,9)
print(respuesta)
