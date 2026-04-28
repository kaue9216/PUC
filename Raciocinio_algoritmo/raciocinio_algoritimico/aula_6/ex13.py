import numpy as np

matriz = np.array ([
    [1, 2, 3, 4, 5],
    [2, 3, 4, 5, 1],
    [3, 4, 5, 1, 2],
    [4, 5, 1, 2, 3],
    [5, 1, 2, 3, 4]
])

i_diag = np.diag(np.fliplr(matriz))

print(i_diag)
