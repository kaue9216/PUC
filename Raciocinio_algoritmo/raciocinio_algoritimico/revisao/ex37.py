# 37. Crie um programa que calcule a média de uma lista.

lista = [1, 1, 1, 3, 3, 3]
soma = 0
cont = 0

for i in lista:
    soma += i
    cont += 1

media = soma/cont

print(media)
