#Ejercicio 2: Crear una clase Banco y una clase Cuenta Define una clase Cuenta que tenga atributos como titular, saldo y un método para realizar retiros. Luego, define una clase Banco que tenga una lista de cuentas y métodos para agregar una cuenta, eliminar una cuenta y mostrar todas las cuentas.

class Cuenta:
   def __init__(self, titular, saldo=0):
      self.titular = titular
      self.saldo = saldo
   def retirar(self, monto):
      if monto > self.saldo:
         print("Estás pobre, por favor deposita")
      else:
         self.saldo -= monto
         print(f"Tu retiro se hizo con exito, tu nuevo saldo ahoara es {self.saldo}")

class Banco:
    def __init__(self):
        self.cuentas = []

    def agregar_cuenta(self, cuenta):
        self.cuentas.append(cuenta)

    def eliminar_cuenta(self, titular):
        for cuenta in self.cuentas:
            if cuenta.titular == titular:
                self.cuentas.remove(cuenta)
                print(f"Cuenta de {titular} eliminada")
                return
        print(f"No se encontró cuenta de {titular}")

    def mostrar_cuentas(self):
        for cuenta in self.cuentas:
            print(f"Titular: {cuenta.titular}, Saldo: {cuenta.saldo}")

# Crear un banco y cuentas
banco = Banco()
cuenta1 = Cuenta("Juan", 1000)
cuenta2 = Cuenta("Maria", 500)

# Agregar cuentas al banco
banco.agregar_cuenta(cuenta1)
banco.agregar_cuenta(cuenta2)

# Mostrar cuentas
banco.mostrar_cuentas()

# Realizar retiro
cuenta1.retirar(500)

# Eliminar cuenta
banco.eliminar_cuenta("Maria")

# Mostrar cuentas nuevamente
banco.mostrar_cuentas()
 