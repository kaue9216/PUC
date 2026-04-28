import numpy as np

matriz = np.zeros((3,2))

transposta = matriz.T

if matriz.shape == transposta.shape:
    print("As matriz é simetrica")
else:
    print("As matriz não é simetrica")
