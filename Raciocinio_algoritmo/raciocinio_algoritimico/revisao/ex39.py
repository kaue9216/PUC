# 39. Solicite nomes e armazene em uma lista até digitar 'fim'.

lista = []

nome = 0

while nome != "fim":
    nome = input("Digite um nome para adicionar na lista, ou fim para sair: ")
    lista.append(nome)
    if nome == "fim":
        lista.remove(nome)

print(lista)

