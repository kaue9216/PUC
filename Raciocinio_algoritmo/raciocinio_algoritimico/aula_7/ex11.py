dicionario = {"Joao" : 1, "Maria" : 2, "José" : 3}

usr = input("Você acessou o banco de dados \n " \
"clique 1 para vizualizar todos os usuários: \n " \
"clique 2 para adicionar um novo usuário: \n " \
"clique 3 para atualizar os dados de um usuário: \n " \
"clique 4 para excluir um usuário: \n " \
"clique 5 para excluir o ultimo usuário: \n"
"clique 6 para criar uma cópia do dicionário e altera-la: ")

if usr == "1":
    for i in dicionario:
        print(i, ":", dicionario[i])

if usr == "2":
    quantidade = int(input("Digite quantas pessoas deseja adicionar na lista: "))
    for i in range(quantidade):
        chave = input("Digite a chave: ")
        valor = input("Digite o valor: ")
        dicionario[chave] = valor

    for i in dicionario:
        print(i, ":", dicionario[i])

if usr == "3":
    aluno = input("Digite um aluno para alterar sua idade: ")
    nota = input("Digite a nova idade: ")
    if aluno in dicionario:
        dicionario[aluno] = nota
        print("A nota do ", aluno, "é ", dicionario.get(aluno))
    else:
        print("Aluno não encontrado")

if usr == "4":
    remover = input("Digite o nome que deseja remover: ")

    dicionario.pop(remover)
    for i in dicionario:
        print(i, ":", dicionario[i])

if usr == "5":
    dicionario.popitem()
    for i in dicionario:
        print(i, ":", dicionario[i])

if usr == "6":
    dicionario1 = dicionario.copy()
    print(dicionario1)
    quantidade = int(input("Digite quantas pessoas deseja adicionar na lista: "))
    for i in range(quantidade):
        chave = input("Digite a chave: ")
        valor = input("Digite o valor: ")
        dicionario1[chave] = valor

    for i in dicionario:
        print(i, ":", dicionario[i])

    print("#---------------#")

    for i in dicionario1:
        print(i, ":", dicionario1[i])
