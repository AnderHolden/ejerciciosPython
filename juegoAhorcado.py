from random import choice

palabras = ["colombia", "argentina", "chile", "brasil", "china", "panama"]
letras_correctas = []
letras_incorrectas = []
corazones = 5
aciertos = 0
juego_terminado = False

def elegir_palabras(lista_palabras):
   palabraElegida = choice(lista_palabras)
   letrasUnicas = len(set(palabraElegida))
   return palabraElegida, letrasUnicas

def pedirLetra():
   letraElegida = ''
   EsValida = False
   abecedario = "abcdefghijklmnopqrstuvwxyz"
   
   while not EsValida:
      letraElegida = input("Elige una letra: ").lower()
      if letraElegida in abecedario and len(letraElegida)==1:
         EsValida = True
      else:
         print("No has elegido letra correcta")
   return letraElegida

def mostrar_nuevo_tablero(palabraElegida):
   lista_oculta = []
   for l in palabraElegida:
      if l in letras_correctas:
         lista_oculta.append(l)
      else:
         lista_oculta.append('-')

   print(' '.join(lista_oculta))

def chequear_letra(letraElegida, palabraOculta, vidas, coincidencias):
   fin = False
   
   if letraElegida in palabraOculta:
      letras_correctas.append(letraElegida)
      coincidencias += 1
   else:
      letras_incorrectas.append(letraElegida)
      vidas -= 1
   if vidas == 0:
      fin = perder()
   elif coincidencias == letras_unicas:
      fin = ganar(palabraOculta)
   return vidas, fin, coincidencias

def perder():
   print("te has quedado sin vidas ")
   print("La palabra oculta era: "+ palabra)
   return True

def ganar(palabraDescubierta):
   mostrar_nuevo_tablero(palabraDescubierta)
   print("Felicitaciones, has encontrado la palabra correcta")
   
   return True

palabra, letras_unicas = elegir_palabras(palabras)
while not juego_terminado:
   print("\n" + '*'*20+'\n')
   mostrar_nuevo_tablero(palabra)
   print('\n')
   print('Letras incorrectas: ' + ', '.join(letras_incorrectas))
   print(f"vidas: {corazones}")
   print("\n" + '*'*20+'\n')
   letra = pedirLetra()
   corazones, juego_terminado, aciertos = chequear_letra(letra, palabra, corazones, aciertos)
