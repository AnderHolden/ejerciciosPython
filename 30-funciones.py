# def saludar(nombre):
#    '''
#    Esta funcion sirve apra saludar una persona
#    '''
#    print("Hola " + nombre)
# saludar('Ander')
# saludar('Holden')
# saludar('Jimmy')
# saludar('Candascia')

# def multiplicar(numero1,numero2):
#    return numero1*numero2

# resultado = multiplicar(5,10)
# print(resultado)

# def chequear_3_cifras(numero):
#    return numero in range(100,1000)

# resultado = chequear_3_cifras(500)
# print(resultado)

def chequear_3_cifras(lista):
   lista_3_cifras = []
   for n in lista:
      if n in range(100,1000):
         lista_3_cifras.append(n)
      else:
         pass
   return lista_3_cifras
      

resultado = chequear_3_cifras([500,100,45,150,65])
print(resultado)