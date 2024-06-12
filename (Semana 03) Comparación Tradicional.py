# Función para ingresar datos diarios de temperatura
def ingresar_temperaturas():
    temperaturas = []  # Lista para almacenar las temperaturas diarias
    for i in range(7):  # Bucle para los 7 días de la semana
        temp = float(input(f"Ingrese la temperatura del día {i+1}: "))  # Solicita al usuario la temperatura del día
        temperaturas.append(temp)  # Agrega la temperatura a la lista
    return temperaturas

# Función para calcular el promedio semanal
def calcular_promedio(temperaturas):
    return sum(temperaturas) / len(temperaturas)  # Calcula el promedio de las temperaturas

# Función principal
def main():
    temperaturas = ingresar_temperaturas()  # Llama a la función para ingresar las temperaturas
    promedio = calcular_promedio(temperaturas)  # Calcula el promedio de las temperaturas
    print(f"El promedio semanal de temperatura es: {promedio:.2f}")  # Imprime el promedio semanal

# Ejecutar la función principal
if __name__ == "__main__":
    main()
