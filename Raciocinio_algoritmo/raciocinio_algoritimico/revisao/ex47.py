# 47. Some todos os elementos de uma matriz 2x2.

import numpy as np
soma = 0

matriz = np.array([
    [1, 2],
    [3, 1]
])

for i in matriz:
    # print(i)
    for f in i:
        soma += f

print(soma)
