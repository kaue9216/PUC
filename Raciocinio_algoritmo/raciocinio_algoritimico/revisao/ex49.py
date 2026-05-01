# 49. Multiplique todos os elementos de uma matriz por 2.

import numpy as np

matriz = np.array([
    [1, 2, 3],
    [3, 1, 2],
    [2, 3, 1]
])
# count = 0

for i in matriz:
    mult = i * 2
    print(mult)

