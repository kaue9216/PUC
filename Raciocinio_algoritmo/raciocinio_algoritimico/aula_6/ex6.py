import numpy as np

contador = 0
matriz = np.array ([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [0, 1, 2]
])

for i in matriz:
    for j in i:
        # print(j)
        if j % 2 == 0:
            contador = contador + 1
            # print("(", contador, ")")

print("A matriz tem", contador, "números pares")
