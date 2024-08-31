# class Animal:
#    pass
# class Pajaro(Animal):
#    pass
# print(Pajaro.__bases__)

class Animal:
   def __init__(self, edad, especie, color):
      self.edad = edad
      self.especie = especie
      self.color = color
   def nacer(self):
      print(f'Este animal ha nacido')

class Pajaro(Animal):
   pass
piolin = Pajaro(2, 'loro', 'verde')

piolin.nacer()


class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

class Alumno(Persona):
    pass

alumno = Alumno("Juan", 20)

print(f"Nombre: {alumno.nombre}")
print(f"Edad: {alumno.edad}")



class Mascota:
    def __init__(self, edad, nombre, cantidad_patas):
        self.edad = edad
        self.nombre = nombre
        self.cantidad_patas = cantidad_patas

class Perro(Mascota):
    pass

mi_perro = Perro(3, "Rex", 4)

print(f"Edad: {mi_perro.edad}")
print(f"Nombre: {mi_perro.nombre}")
print(f"Cantidad de patas: {mi_perro.cantidad_patas}")


class Vehiculo:
   
    def acelerar(self):
        print("Modo Acelerado")
    def frenar(self):
        print("Vehiculo ha parado")
class Automovil(Vehiculo):
    pass

mi_auto = Automovil()

mi_auto.acelerar()
mi_auto.frenar()
