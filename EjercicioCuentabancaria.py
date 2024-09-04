class Persona:
   def __init__(self, nombre, apellido):
      self.nombre = nombre
      self.apellido = apellido

class Cliente(Persona):
   def __init__(self, nombre, apellido, NumeroCuenta, Balance=0):
      super().__init__(nombre, apellido)
      self.NumeroCuenta = NumeroCuenta
      self.Balance = Balance
   def __str__(self):
        return f"Nombre: {self.nombre} {self.apellido}\nNúmero de cuenta: {self.numero_cuenta}\nBalance: {self.balance}"
  

      