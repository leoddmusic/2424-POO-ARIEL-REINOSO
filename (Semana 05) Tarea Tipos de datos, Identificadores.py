# Programa para calcular el área de un rectángulo

def calcular_area_rectangulo(largo, ancho):
    """
    Calcula el área de un rectángulo.

    Parámetros:
    largo (float): El largo del rectángulo.
    ancho (float): El ancho del rectángulo.

    Retorna:
    float: El área del rectángulo.
    """
    return largo * ancho

# Solicita al usuario el largo y el ancho del rectángulo
largo = float(input("Ingrese el largo del rectángulo: "))
ancho = float(input("Ingrese el ancho del rectángulo: "))

# Calcula el área utilizando la función definida
area = calcular_area_rectangulo(largo, ancho)

# Muestra el resultado
print(f"El área del rectángulo es {area} unidades cuadradas.")
