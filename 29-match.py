serie = input("Ingresa la serie de tu celular: ")
if serie == 'N-01':
   print("Samsumg")
elif serie == 'N-02':
   print('Nokia')
elif serie == 'N-03':
   print("Motorola")
else:
   print('No es una serie de celular aceptada')
match serie:
   case 'N-01':
      print("Samsung")
   case 'N-02':
      print("Nokia")
   case 'N-03':
      print("Motorola")
   case _:
      print("No es una serie de celular aceptada")
