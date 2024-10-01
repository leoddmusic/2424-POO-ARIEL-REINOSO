class ClimaSemanal:
    def __init__(self):
        self.temperaturas = []  # Inicializa una lista vacía para almacenar las temperaturas diarias

    def ingresar_temperaturas(self):
        for i in range(7):  # Bucle para los 7 días de la semana
            temp = float(input(f"Ingrese la temperatura del día {i+1}: "))  # Solicita al usuario la temperatura del día
            self.temperaturas.append(temp)  # Agrega la temperatura a la lista

    def calcular_promedio(self):
        return sum(self.temperaturas) / len(self.temperaturas)  # Calcula el promedio de las temperaturas

# Función principal
def main():
    clima_semanal = ClimaSemanal()  # Crea una instancia de la clase ClimaSemanal
    clima_semanal.ingresar_temperaturas()  # Llama al método para ingresar las temperaturas
    promedio = clima_semanal.calcular_promedio()  # Calcula el promedio de las temperaturas
    print(f"El promedio semanal de temperatura es: {promedio:.2f}")  # Imprime el promedio semanal

# Ejecutar la función principal
if __name__ == "__main__":
    main()
