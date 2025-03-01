def buscar_valor(matriz, valor):
    """Busca un valor en la matriz y devuelve su posición (fila, columna)"""
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == valor:
                return (i, j)  # Retorna la posición si se encuentra
    return None  # Retorna None si no se encuentra

# Definir una matriz 3x3 con valores numéricos
matriz = [
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
]

# Solicitar al usuario un valor a buscar
valor_a_buscar = int(input("Ingrese el valor a buscar en la matriz: "))

# Realizar la búsqueda en la matriz
posicion = buscar_valor(matriz, valor_a_buscar)

# Mostrar el resultado
if posicion:
    print(f"✅ El valor {valor_a_buscar} se encontró en la posición {posicion}")
else:
    print(f"❌ El valor {valor_a_buscar} no se encuentra en la matriz.")