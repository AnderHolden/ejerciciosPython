class Joya:
    def __init__(self, nombre, material, precio):
        self.nombre = nombre  #encapsulamiento
        self.material = material
        self.precio = precio
        
    def mostrarInfo(self):
        raise NotImplementedError("este metodo se debe implementar en las clase hijas")
    
    def obtenerNombre(self):
        return self.nombre
    
    def obtenerPrecio(self):
        return self.precio
    

class Anillo(Joya):
    def mostrarInfo(self):
       return f"Anillo: {self.nombre}, Material: {self.material}, Precio: ${self.precio}"
   
class Collar(Joya):
    def mostrarInfo(self):
       return f"Collar: {self.nombre}, Material: {self.material}, Precio: ${self.precio}"
   

class Inventario:
    def __init__(self):
        self.joyas = [] 
        
    def agregarJoya(self, joya):
        self.joyas.append(joya)
    
    def mostraInventario(self):
        if not self.joyas:
            return "no hay joyas en el inventario"
        return "\n".join([joya.mostrarInfo() for joya in self.joyas])
    
    def buscarJoya(self, nombre):
        for joya in self.joyas:
            if joya.obtenerNombre() == nombre:
                return joya
        return None
    
class Ventas:
    def __init__(self):
        self.totalVentas = 0
        self.ventas = []
        
    def realizarVenta(self, joya):
        self.ventas.append(joya)
        self.totalVentas += joya.obtenerPrecio()
        return f"Venta realizada: {joya.mostrarInfo()}"
    
    def mostrarVentas(self):
        if not self.ventas:
            return "no se han realizado ventas"
        return "\n".join([venta.mostrarInfo() for venta in self.ventas])
    
    def totalIngresos(self):
        return f"Total de ingresos: ${self.totalVentas}"


def main():
    inventario = Inventario()
    venta = Ventas()
    
    while True:
        print("\n1. Agregar joya al inventario")
        print("2. Mostrar inventario")
        print("3. Realizar venta")
        print("4. Mostrar ventas")
        print("5. Mostrar ingresos totales")
        print("6. salir")
        
        opcion = int(input("Ingrese la opcion del menu: "))
        
        if opcion == 1:
            tipo = input("Tipo de joya (anillo/collar): ").capitalize()
            nombre = input("Digite el nombre de la joya: ")
            material = input("Digite el material de la joya: ")
            precio = float(input("Digite el precio de la joya: "))
            
            if tipo == "Anillo":
                joya = Anillo(nombre, material, precio)
            elif tipo == "Collar":
                joya = Collar(nombre, material, precio)
            else:
                print("tipo de joya no reconocido")
                continue
            
            inventario.agregarJoya(joya)
            print(f"Joya {nombre} agregado al inventario")
            
        elif opcion == 2:
            print("INVENTARIO")
            print(inventario.mostraInventario())
        
        elif opcion == 3:
            nombre = input("nombre de la joya a vender: ")
            joyaAVender = inventario.buscarJoya(nombre)
            
            if joyaAVender:
                print(venta.realizarVenta(joyaAVender))
            else:
                print("Joya no encontrada en el inventario")
        
        elif opcion == 4:
            print("\nVentas realizadas: ")
            print(venta.mostrarVentas())
            
        elif opcion == 5:
            print(venta.totalIngresos())
            
        elif opcion == 6:
            print("hasta la proxima....")
            break
        else:
            print("Opcion no valida, intente de nuevo")
            
            
if __name__ == "__main__":
    main()

            
            