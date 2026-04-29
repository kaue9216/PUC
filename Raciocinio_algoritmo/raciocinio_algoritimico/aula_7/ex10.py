dicionario = {"Elemento 1" : 1, "Elemento 2" : 2, "Elemento 3" : 3}
print(dicionario)

remover = input("Digite a chave que deseja remover: ")

dicionario.pop(remover)
print(dicionario)

dicionario.popitem()
print(dicionario)

print("Agora vamos adicionar alguns itens: ")


dicionario1 = {}
quantidade = int(input("Digite quantos itens deseja adicionar no dicionário : "))

for i in range(quantidade):
    chave = input("Digite a chave: ")
    valor = input("Digite o valor: ")
    dicionario1[chave] = valor

dicionario.update(dicionario1)

print(dicionario)
