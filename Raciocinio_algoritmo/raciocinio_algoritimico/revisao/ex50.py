# 50. Crie duas matrizes 2x2 e some seus valores (A + B).
import numpy as np

m1 = np.array([
    [1, 2],
    [3, 1]
])

m2 = np.array([
    [1, 2],
    [2, 1]
])

m100 = m1[0][0]
m200 = m2[0][0]
m101 = m1[0][1]
m201 = m2[0][1]
m110 = m1[1][0]
m210 = m2[1][0]
m111 = m1[1][1]
m211 = m2[1][1]

m300 = m100 + m200
m301 = m101 + m201
m310 = m110 + m210
m311 = m111 + m211

m3 = np.array([
    [m300, m301],
    [m310, m311]
])

print(m3)
