# 32. Crie um programa que conte quantos números pares existem em uma lista.

lista = [1, 2, 3, 4, 5, 6]
cont = 0

for i in lista:
    if i % 2 == 0:
        cont += 1

print(f"A lista tem {cont} números pares")
