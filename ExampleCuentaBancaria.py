class Persona:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

class Cliente(Persona):
    def __init__(self, nombre, apellido, numero_cuenta, balance=0):
        super().__init__(nombre, apellido)
        self.numero_cuenta = numero_cuenta
        self.balance = balance

    def __str__(self):
        return f"Cliente: {self.nombre} {self.apellido}\nNúmero de Cuenta: {self.numero_cuenta}\nBalance: ${self.balance:.2f}"

    def depositar(self, cantidad):
        self.balance += cantidad
        print(f"Has depositado ${cantidad:.2f}. Nuevo balance: ${self.balance:.2f}")

    def retirar(self, cantidad):
        if cantidad > self.balance:
            print("Fondos insuficientes.")
        else:
            self.balance -= cantidad
            print(f"Has retirado ${cantidad:.2f}. Nuevo balance: ${self.balance:.2f}")

def crear_cliente():
    nombre = input("Introduce el nombre del cliente: ")
    apellido = input("Introduce el apellido del cliente: ")
    numero_cuenta = input("Introduce el número de cuenta: ")
    return Cliente(nombre, apellido, numero_cuenta)

def inicio():
    cliente = crear_cliente()
    print(cliente)
    
    while True:
        print("\n¿Qué deseas hacer?")
        print("1. Depositar")
        print("2. Retirar")
        print("3. Salir")
        opcion = input("Elige una opción: ")

        if opcion == "1":
            cantidad = float(input("Introduce la cantidad a depositar: "))
            cliente.depositar(cantidad)
        elif opcion == "2":
            cantidad = float(input("Introduce la cantidad a retirar: "))
            cliente.retirar(cantidad)
        elif opcion == "3":
            print("Gracias por usar el sistema bancario. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, elige una opción correcta.")

# Iniciar el programa
inicio()
