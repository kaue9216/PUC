# 45. Crie uma lista e inverta seus elementos sem usar reverse().

lista = [1, 2, 3, 4]
n_lista = []
cont = -1

for i in lista:
    ultimo = lista[cont]
    n_lista.append(ultimo)
    cont -= 1

print(n_lista)
