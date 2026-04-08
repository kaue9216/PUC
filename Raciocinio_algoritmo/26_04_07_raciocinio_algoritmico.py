# quantidade = int(input("Digite quantos alunos existem na turma: "))
# turma = []

# for i in range(quantidade):
#     aluno = input("Nome do aluno: ")
#     turma.append(aluno)

# for i in turma:
#     print(i)

# #---------------------------------#

# a = []

# for i in range(10):
#     numero = int(input("Digite um número: "))
#     a.append(numero)

# for i in a:
#     print(i)

# #---------------------------------#

# a = []

# for i in range(10):
#     numero = int(input("Digite um número: "))
#     a.append(numero)

# print(max(a))
# print(min(a))

# #---------------------------------#

# quantidade = int(input("Digite quantos alunos existem na turma: "))
# turma = []
# abaixo = 0
# acima = 0

# for i in range(quantidade):
#     nota = int(input("Nota do aluno (0 a 100): "))
#     turma.append(nota)

# for i in turma:
#     if i < 60:
#        abaixo += 1
#     else:
#         acima += 1

# print(f"{acima} aluno(s) ficaram acima da média")
# print(f"{abaixo} aluno(s) ficaram abaixo da média")

# #---------------------------------#

# print("Você deverá digitar 5 números")
# a = []
# pares = []
# impares = []
# soma = 0

# for i in range(5):
#     numero = int(input("Digite um número: "))
#     a.append(numero)

# for i in a:
#     if i % 2 == 0:
#         pares.append(i)
#     else:
#         impares.append(i)
#     soma += i

# if len(pares) == 0:
#     print("Você não digitou números pares")
# else:
#     print("O maior núero par é: ", max(pares))

# if len(impares) == 0:
#     print("Você não digitou números impares")
# else:
#     print("O maior numero impar é: ", max(impares))

# print("A soma dos números é: ", soma)
# print("A média dos valores é: ", soma / 5)
