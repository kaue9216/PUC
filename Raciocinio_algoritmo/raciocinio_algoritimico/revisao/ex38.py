# 38. Crie uma lista e remova todos os números negativos.

lista = [-1, -2, -3, 0, 1, 2, 3]
nova_lista = []

for x in lista:
    if x >= 0:
        nova_lista.append(x)

lista = nova_lista

print(lista)
