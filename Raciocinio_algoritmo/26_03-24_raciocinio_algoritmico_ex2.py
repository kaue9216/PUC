# cont = 0
# soma_medias = 0

# while cont < 3:
#     n1 = float(input("Digite a primeira nota: "))
#     n2 = float(input("Digite a segunda nota: "))
#     n3 = float(input("Digite a terceira nota: "))
#     n4 = float(input("Digite a quarta nota: "))

#     media = (n1 + n2 + n3 + n4) / 4
#     soma_medias += media
#     print("Média anual: ", media)

#     if media >= 7:
#         print("Aprovado")
#     else:
#         print("Reprovado")

#     cont += 1
#     media_total = soma_medias / cont

# print(f"A média total é: {media_total: .2f}")

# #----------------------------------#

# acumulador = 0
# contador = 0

# while True:
#     n = float(input("Digite um numeo (se for positivo o programa irá parar): "))

#     if n < 0:
#         break

#     if n % 2 == 0:
#         acumulador += n
#         contador += 1

# if contador > 0:
#     media = acumulador / contador
#     print("A soma dos números pares é: ", acumulador)
#     print("A média dos números pares é: ", media)
# else:
#     print("Nenhum número par foi digitado")

# #----------------------------------#

computador = ['Processador', 'teclado', 'mouse']

for item in computador:
    print(item)
