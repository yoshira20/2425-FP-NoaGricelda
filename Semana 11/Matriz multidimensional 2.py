def bubble_sort(fila):
    """Ordena una lista (fila de la matriz) usando el algoritmo Bubble Sort"""
    n = len(fila)
    for i in range(n):
        for j in range(0, n - i - 1):
            if fila[j] > fila[j + 1]:
                fila[j], fila[j + 1] = fila[j + 1], fila[j]  # Intercambio de valores

# Definir una matriz 3x3 con valores numéricos desordenados
matriz = [
    [30, 10, 20],
    [60, 50, 40],
    [90, 70, 80]
]

# Mostrar la matriz original
print("📌 Matriz original:")
for fila in matriz:
    print(fila)

# Elegir la fila a ordenar (por ejemplo, la segunda fila - índice 1)
fila_a_ordenar = 1

# Aplicar Bubble Sort en la fila elegida
bubble_sort(matriz[fila_a_ordenar])

# Mostrar la matriz después de ordenar la fila
print("\n✅ Matriz después de ordenar la fila seleccionada:")
for fila in matriz:
    print(fila)