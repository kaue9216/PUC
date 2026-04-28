import numpy as np

matriz = np.array([
    [1, 2, 3, 4],
    [4, 1, 2, 3],
    [3, 4, 1, 2],
    [2, 3, 4, 1]
])

dig = np.diag(matriz)

# print(dig)

total = sum(dig)

print(total)
