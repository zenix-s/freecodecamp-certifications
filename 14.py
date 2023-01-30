# Programación orientada a objetos

class Persona:
    nombre = ""
    edad = 0
    # Constructor
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    # toString
    def __str__(self):
        return "Nombre: " + self.nombre + " Edad: " + str(self.edad)
    # Eliminar objeto
    def __del__(self):
        print("Se ha eliminado el objeto " + self.nombre)
    # Métodos
    def hablar(self, mensaje):
        print(self.nombre + " dice: " + mensaje)

# Se crea un objeto de la clase Persona
Persona1 = Persona("Juan", 20)

# Se imprime el objeto
print(Persona1)

# Se llama al método hablar
Persona1.hablar("Hola, ¿cómo estás?")

# Se elimina el objeto
del Persona1
