# Definimos la clase Estudiante
class Estudiante:
    # Método constructor con 3 atributos: nombre, edad, carrera
    def __init__(self, nombre, edad, carrera):
        self.nombre = nombre
        self.edad = edad
        self.carrera = carrera
        self.notas = []  # Atributo adicional para almacenar notas

    # Método 1: Mostrar información del estudiante
    def mostrar_informacion(self):
        print(f" Estudiante: {self.nombre}")
        print(f" Edad: {self.edad} años")
        print(f" Carrera: {self.carrera}")

    # Método 2: Agregar y calcular promedio de notas
    def agregar_nota(self, nota):
        if 0 <= nota <= 10:
            self.notas.append(nota)
            print(f" Nota {nota} agregada correctamente.")
        else:
            print(" Nota inválida. Debe estar entre 0 y 10.")

    def calcular_promedio(self):
        if len(self.notas) > 0:
            promedio = sum(self.notas) / len(self.notas)
            return f" Promedio de notas: {promedio:.2f}"
        else:
            return " No hay notas registradas aún."


# --- Creación de objetos (mínimo 1) ---
estudiante = Estudiante("Ana Karina Ezpinoza", 21, "Licenciada en Comunicación")

# --- Prueba del funcionamiento ---
print("=== INFORMACIÓN DEL ESTUDIANTE ===")
estudiante.mostrar_informacion()
estudiante.agregar_nota(9.6)
estudiante.agregar_nota(9.8)
estudiante.agregar_nota(10)
print(estudiante.calcular_promedio())
print("--")
