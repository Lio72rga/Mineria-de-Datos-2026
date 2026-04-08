import numpy as np

# Ejercicio 7: Multiplicación de matrices
matrizA = np.random.randint(1, 11, (3,3))
matrizB = np.random.randint(1, 11, (3,3))

resultado = np.dot(matrizA, matrizB)

print("Ejercicio 7:")
print("Matriz A:\n", matrizA)
print("Matriz B:\n", matrizB)
print("Resultado:\n", resultado)
print()