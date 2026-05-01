# 48. Exiba apenas a diagonal principal de uma matriz 3x3.

import numpy as np

matriz = np.array([
    [1, 2, 3],
    [3, 1, 2],
    [2, 3, 1]
])
count = 0

for i in matriz:
    print(i[count])
    count += 1
