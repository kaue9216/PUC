# 41. Crie um programa que conte quantas vezes um número aparece em uma
# lista.

lista = [1, 2, 3, 4, 1, 2, 3, 4]
count = 0

print(lista)

numero = int(input("Escolha um número da lista e eu contarei quantas vezes ele aparece nela: "))

for i in lista:
    if i == numero:
        count += 1

print(f"O número {numero} aparece {count} vezes na lista")
