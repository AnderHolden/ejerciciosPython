#Ejercicio 1: Crear una clase Estudiante y una clase Curso Define una clase Estudiante que tenga atributos como nombre, edad y grado, y otra clase Curso que tenga atributos como nombre, profesor y una lista de estudiantes. Agrega métodos a la clase Curso para agregar un estudiante, eliminar un estudiante y mostrar todos los estudiantes inscritos.

class Estudiante:
    def __init__(self, nombre, edad, grado):
        self.nombre = nombre
        self.edad = edad
        self.grado = grado

    def __str__(self):
        return f"Nombre: {self.nombre}, Edad: {self.edad}, Grado: {self.grado}"

class Curso:
    def __init__(self, nombre, profesor):
        self.nombre = nombre
        self.profesor = profesor
        self.estudiantes = []

    def agregar_estudiante(self, estudiante):
        self.estudiantes.append(estudiante)
        print(f"Estudiante {estudiante.nombre} agregado al curso{self.nombre}")

    def eliminar_estudiante(self, nombre_estudiante):
        self.estudiantes = [est for est in self.estudiantes if est.nombre != nombre_estudiante ]
        #for estudiante in sefl.estudiantes:
         #if estudiante.nombre == nombre_estudiante:
            #

    def mostrar_estudiantes(self):
        for estudiante in self.estudiantes:
            print(estudiante)

# Ejemplo de uso
est1 = Estudiante("Juan", 20, "Segundo")
est2 = Estudiante("María", 22, "Tercero")

curso = Curso("Matemáticas", "Profesor Pérez")
curso.agregar_estudiante(est1)
curso.agregar_estudiante(est2)

print("Estudiantes inscritos en el curso:")
curso.mostrar_estudiantes()

curso.eliminar_estudiante("Juan")
print("\nEstudiantes inscritos después de eliminar a Juan:")
curso.mostrar_estudiantes()
