import numpy as np

# Crear una matriz de ejemplo
matriz = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [7, 8, 9]])

# Obtener las dimensiones de la matriz
filas, columnas = matriz.shape

# Obtener el tamaño de la segunda columna (índice 1)
tamano_columna = matriz[:, 0].size

# Imprimir el tamaño de la columna
print("El tamaño de la segunda columna es:", tamano_columna)

matriz = [
	["1", "2", "3"],
	["4", "5", "6"],
	[7, 8, 9],
    [7, 8, 9]
]

len_columna = len([fila[0] for fila in matriz])
print(len_columna)
