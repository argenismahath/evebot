def calcular_kilometros(numero):
    # Valores conocidos
    x1, y1 = 480, 100
    x2, y2 = 450, 84
    x3, y3 = 440, 80

    # Calcular la pendiente (m)
    m = (y2 - y1) / (x2 - x1)

    # Calcular el término independiente (b) usando uno de los puntos
    b = y1 - m * x1

    # Calcular el valor de y (kilómetros) para el número dado (x)
    kilometros = m * numero + b
    return kilometros

# Ejemplo de uso:
numero_dado = 230  # Número para el que deseamos calcular los kilómetros
kilometros_calculados = calcular_kilometros(numero_dado)
print(f"{numero_dado} = {kilometros_calculados:.2f} km")