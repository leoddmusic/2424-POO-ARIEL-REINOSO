# Clase base Vehiculo
class Vehiculo:
    def __init__(self, marca, modelo):
        self._marca = marca  # Atributo protegido para demostrar encapsulación
        self.modelo = modelo

    def describir(self):
        return f"Este es un vehículo marca {self._marca} modelo {self.modelo}."

    def encender(self):
        return "El vehículo está encendiendo."

# Clase derivada Coche que hereda de Vehiculo
class Coche(Vehiculo):
    def __init__(self, marca, modelo, numero_de_puertas):
        super().__init__(marca, modelo)  # Llama al constructor de la clase base
        self.numero_de_puertas = numero_de_puertas

    # Método sobrescrito para demostrar polimorfismo
    def encender(self):
        return "El coche está encendiendo con un sonido único."

# Creando instancias de las clases
mi_vehiculo = Vehiculo("Toyota", "Corolla")
mi_coche = Coche("Honda", "Civic", 4)

# Utilizando métodos de las instancias creadas para demostrar funcionalidad
print(mi_vehiculo.describir())
print(mi_vehiculo.encender())
print(mi_coche.describir())
print(mi_coche.encender())
