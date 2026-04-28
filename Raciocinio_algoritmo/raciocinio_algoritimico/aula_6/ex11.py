import numpy as np

matriz = np.array([
    [1, 2, 3],
    [1, 2, 3],
    [1, 2, 3]
])

soma0 = 0
resultado0 = 0
soma1 = 0
resultado1 = 0
soma2 = 0
resultado2 = 0

for i in matriz:
    # print(i[0])
    soma0 += i[0]
    # print(soma1)
    resultado0 = soma0

for i in matriz:
    # print(i[0])
    soma1 += i[1]
    # print(soma1)
    resultado1 = soma1

for i in matriz:
    # print(i[0])
    soma2 += i[2]
    # print(soma1)
    resultado2 = soma2


print(resultado0)
print(resultado1)
print(resultado2)
