# class Pajaro:
#    alas = True
#    def __init__(self, color, especie):
#       self.color = color
#       self.especie = especie
# piolin = Pajaro('amarillo', 'Loro')
# print(piolin.color)
# print(piolin.especie)
# print(piolin.alas)
# print(f'Mi pajaro es de color {piolin.color} y es de especie {piolin.especie}')

# print(Pajaro.alas)

class Casa:
   def __init__(self, color, cantidad_pisos):
      self.color = color
      self.cantidad_pisos = cantidad_pisos

casa_blanca = Casa('blanco', 4)
print("El objeto Casa_blaca tiene lo sigueinte: ")
print(f"Color de la casa: {casa_blanca.color}")
print(f"Cantidad de pisos: {casa_blanca.cantidad_pisos}")

class Cubo:
   caras = 6
   def __init__(self, color ):
      self.color = color
cubo_rojo = Cubo('rojo')
print("El objeto cubo_rojo  tiene lo sigueinte: ")
print(f"Color del cubo: {cubo_rojo.color}")
print(f"Cantidad de caras: {Cubo.caras}")


class Personaje:
   real = False
   def __init__(self, especie, magico, edad):
      self.especie = especie
      self.magico = magico
      self.edad = edad
harry_potter = Personaje('humano', 'True', '17')
print("El objeto harry_potter tiene lo sigueinte: ")
print(f"Especie: {harry_potter.especie}")
print(f"Es mágico: {harry_potter.magico}")
print(f"Edad: {harry_potter.edad}")
print(f"Es real: {Personaje.real}")

