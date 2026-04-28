import numpy as np

numero = int(input("Digite um número: "))

matriz = np.array([
    [1, 1, 1],
    [1, 1, 1],
    [1, 1, 1]
])

if numero in matriz:
    print("Numero na matriz")
else:
    print("Número não está na matriz")
