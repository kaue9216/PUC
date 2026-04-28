import numpy as np

matriz = np.array([
    [2, 3, 1],
    [1, 3, 2],
    [3, 3, 3]
])

for i in matriz:
    media = np.mean(i)
    print(media)
