class Pajaro:
    alas = True
    def __init__(self, color, especie):
      self.color = color
      self.especie = especie
      
    def piar(self):
      print(f'Pio, mi color es {self.color}')
      
    def volar(self, metros):
         print(f'El pajaro vuela {metros} metros')
         
piolin = Pajaro('amarillo', 'canario')

piolin.volar(50)
piolin.piar()

class Perro:
    def ladrar(self):
        print("¡Guau!")

balu = Perro()

balu.ladrar()

class Mago:
   def lanzar_hechizo(self):
      print("¡Abracadabra!")
merlin = Mago()
merlin.lanzar_hechizo()

class Alarma:
    def postergar(self, cantidad_minutos):
        print(f"La alarma ha sido pospuesta {cantidad_minutos} minutos")

mi_alarma = Alarma()

mi_alarma.postergar(10)
