dicionario = {}

quantidade = int(input("Digite quantas pessoas você deseja incluir no dicionário: "))

for i in range(quantidade):
    nome = input("Digite o nome da pessoa: ")
    idade = input("Digite a idade: ")
    dicionario[nome] = idade

print(dicionario)
