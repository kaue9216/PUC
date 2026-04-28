import numpy as np
from random import randint

# x = np.zeros((2, 3))
# print(x)

# y = np.eye(5)
# print(y)

# z = np.ones((5, 4))
# print(z)

# #--------------------#

# matriz = [
#     [1, 2, 3],
#     [4, 5, 6]
# ]

# elemento = matriz[0][1]

# print(elemento)

# #------------------#

# x = np.zeros((2, 3))
# print(x)


# for i in x:
#     for j in i:
#         j += 1
#         print(j)

# # x = x+1

# print(x)

# #------------------#

# arr_float = np.array([1, 2, 3], dtype=float)

# arr_tuple = np.array((4, 5, 6))

# print(arr_float)
# print(arr_tuple)

# #------------------#

# cidade = np.array([
#     [1, 2, 3],
#     [1, 1, 1],
#     [2, 2, 2]
# ])

# chuva = np.array([
#     [1, 1, 1],
#     [2, 2, 2],
#     [3, 3, 3]
# ])

# resultado = cidade + chuva

# print("Cidade \n", cidade)
# print("\n")
# print("Chuva \n", chuva)
# print("\n")
# print("Chuva na cidade \n", resultado)

# #------------------#

# contador = 0
# estoque = np.array([
#     [10, 20, 30],
#     [10, 20, 30],
#     [10, 20, 30]
# ])

# vendidos = np.zeros((3, 3))

# for i in vendidos:
#     contador = randint(0,9)
#     i += contador

# resultado = estoque - vendidos

# print("Estoque inicial: \n", estoque)
# print("Numero de vendas \n", vendidos)
# print("\n")
# print("O estoque, após as vendas, ficou: \n", resultado)

# #------------------#

# ingredientes = np.array([
#     [2, 2, 2],
#     [1, 1, 1]
# ])

# pedidos = np.array([
#     [1, 1],
#     [2, 2],
#     [3, 3]
# ])

# vendas = np.dot(ingredientes, pedidos)

# print(vendas)

# #------------------#

# salarios = np.array([
#     [2000, 2000, 2000],
#     [3000, 3000, 3000],
#     [4500, 4500, 4500]
# ])

# aumento = salarios * 1.10

# print("Salarios: \n", salarios)
# print("\n")
# print("Salários pós aumento: \n", aumento)

# #------------------#

# matriz = np.array([
#     [10, 10, 10],
#     [10, 10, 10],
#     [10, 10, 10]
# ])

# zerada = matriz * 0

# print(zerada)

# #------------------#

# matriz = np.array([
#     [10, 10, 10, 10],
#     [10, 10, 10, 10],
#     [10, 10, 10, 10],
#     [10, 10, 10, 10]
# ])

# um = (matriz * 0) + 1

# print(um)

# #------------------#

# matriz = np.array([
#     [1, 2, 3, 4, 5],
#     [6, 7, 8, 9, 10],
#     [11, 12, 13, 14, 15],
#     [16, 17, 18, 19, 20],
#     [21, 22, 23, 24, 25]
# ])

# print(matriz)

# matriz[0][1] = 3
# matriz[2][4] = 3


# print(matriz)
