# 44. Crie um programa que some apenas os números ímpares de uma lista.

lista = [1, 2, 1, 4, 1]
soma = 0

for i in lista:
    if i % 2 != 0:
        soma += i

print(soma)
