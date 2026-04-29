dicionario = {"Joao" : 1, "Maria" : 2, "José" : 3}

aluno = input("Digite um aluno para alterar sua nota: ")
# print(dicionario.get(aluno))

if aluno in dicionario:
    print("A nota do ", aluno, "é ", dicionario.get(aluno))
else:
    print("Aluno não encontrado")
