import numpy as np

# Ejercicio 10: Suma de filas y columnas
matriz10 = np.random.randint(1, 21, (5,5))

suma_filas = np.sum(matriz10, axis=1)
suma_columnas = np.sum(matriz10, axis=0)

print("Ejercicio 10:")
print("Matriz:\n", matriz10)
print("Suma de filas:", suma_filas)
print("Suma de columnas:", suma_columnas)