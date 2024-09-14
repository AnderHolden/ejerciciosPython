#Definir la clase Persona con atributos
class Persona:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

# Definir la clase Cliente que hereda de Persona
class Cliente(Persona):
    def __init__(self, nombre, apellido, numero_cuenta, balance=0):
        super().__init__(nombre, apellido)
        self.numero_cuenta = numero_cuenta
        self.balance = balance
    def __str__(self):
        return f"Nombre: {self.nombre} {self.apellido}\nNúmero de cuenta: {self.numero_cuenta}\nBalance: {self.balance}"
    def depositar(self, monto):
        self.balance += monto
        print(f"Depósito exitoso, vaya cuanto dinero. Tu numero nuevo balance es: {self.balance}")

    def retirar(self, monto):
        if monto > self.balance:
            print("No tiene suficiente saldo para realizar la operación.")
        else:
            self.balance -= monto
            print(f"Retiro exitoso, ten presente que te estas quedando pobre. Nuevo balance: {self.balance}")
#En esta linea es un Función para crear un cliente
def crear_cliente():
      nombre = input("Ingrese su nombre: ")
      apellido = input("Ingrese su apellido: ")
      numero_cuenta = input("Ingrese su número de cuenta: ")
      print("Hola, ¿qué tal?, bienvenid@" "\n" + "Estos son tus datos ingresados: ")
      return Cliente(nombre, apellido, numero_cuenta)

#En esta linea se crea la función principal
def inicio():
   cliente = crear_cliente()
   print(cliente)
   while True:
        print("\nTus opciones:")
        print("1. Depositar")
        print("2. Retirar")
        print("3. Salir")
        opcion = input("Elige una opción: ")
        if opcion == "1":
            monto = float(input("Ingrese el monto a depositar: "))
            cliente.depositar(monto)
        elif opcion == "2":
            monto = float(input("Ingrese el monto a retirar: "))
            cliente.retirar(monto)
        elif opcion == "3":
            print("Gracias por ustilizar nuesta APP, vuelve pronto con dinero ¡POR FAVOR!")
            break
        else:
            print("Opción inválida. Intente nuevamente.")

# Iniciar el programaAnder
inicio()