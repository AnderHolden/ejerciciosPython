class Persona:
   def __init__(self, nombre, apellido):
      self.nombre = nombre
      self.apellido = apellido

class Cliente(Persona):
   def __init__(self, NumeroCuenta, Balance=0):
      self.NumeroCuenta = NumeroCuenta
      self.Balance = Balance

      