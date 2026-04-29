meu_dicionario = {}

meu_dicionario["cidade"] = input("Digite sua cidade: ")
meu_dicionario["nome"] = input("Digite seu nome: ")
meu_dicionario["idade"] = input("Digite sua idade: ")

print(meu_dicionario)

while True:
    chave = input("Digite a chave que deseja pesquisar, ou 0 para sair: ")
    if chave != "0":
        print(meu_dicionario.get(chave))
    else:
        break
