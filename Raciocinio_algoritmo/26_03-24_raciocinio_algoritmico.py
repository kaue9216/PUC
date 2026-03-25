# idade = int(input("Digite sua idade: "))

# if idade >= 16:
#     print("Pode votar")
# else:
#     print("Não pode votar")

# #----------------------------------#

# numero = int(input("Digite um número: "))

# if numero > 0:
#     print("Número positivo")
# elif numero == 0:
#     print("Número é zero")
# else:
#     print("Número negativo")

# #----------------------------------#

# compra = float(input("Digite o valor da sua compra "))

# if compra > 100:
#     desconto = compra - (compra * 0.1)
#     print("O valor da sua compra com desconto é: ", desconto)
# else:
#     print("Nas compras acima de R$ 100, você ganha 10% de desconto!")

# #----------------------------------#

# nota = float(input("Digite a sua nota da prova "))

# if nota > 9:
#     print("Parabéns, você foi aprovado!!!")
# elif nota > 7:
#     print("Aprovado")
# elif nota > 4:
#     print("Você está de recuperação")
# else:
#     print("Reprovado")

# #----------------------------------#

# numero = int(input("Digite um número inteiro: "))
# par_impar = numero % 2

# if par_impar == 0:
#     print("Número par")
# else:
#     print("Número impar")

# #----------------------------------#

# numero1 = int(input("Digite um número: "))
# numero2 = int(input("Digite outro número: "))

# if numero1 > numero2:
#     print("O primeiro número é maior")
# elif numero1 < numero2:
#     print("O segundo número é maior")
# else:
#     print("Os números são iguais")

# #----------------------------------#

# usuario = input("Digite o nome de usuário: ")
# usuario_correto = "admin"

# if usuario == usuario_correto:
#     print("Acesso concedido!!")
# else:
#     print("Usuário desconhecido")

# #----------------------------------#

# peso = float(input("Digite seu peso: "))
# altura = float(input("Dgite sua altura: "))
# imc = peso * (altura ** 2)

# if imc > 25:
#     print("Acima do peso ideal")
# else:
#     print("Peso dentro da normalidade")

# #----------------------------------#

# lado1 = float(input("Digite o valor de um lado de um triângulo: "))
# lado2 = float(input("Digite o valor de outro lado de um triângulo: "))
# lado3 = float(input("Digite o valor de mais um lado de um triângulo: "))

# if lado1 == lado2 and lado2 == lado3:
#     print("Triangulo Equilátero")
# elif lado1 == lado2 or lado2 == lado3 or lado1 == lado3:
#     print("Triangulo Isósceles")
# else:
#     print("Triangulo Escaleno")

# #----------------------------------#

# numero = float(input("Digite um número: "))
# multiplo_de_5 = numero % 5

# if multiplo_de_5 == 0:
#     print("Seu número é multiplo de 5")
# else:
#     print("Não é multiplo de 5")

# #----------------------------------#

# nadador = int(input("Digite a idade do nadador: "))

# if 5 <= nadador <= 7:
#     print("Classificação: Infantil A")
# elif 8 <= nadador <= 10:
#     print("Classificação: Infantil B")
# elif 11 <= nadador <= 13:
#     print("Classificação: Juvenil A")
# elif 14 <= nadador <= 17:
#     print("Classificação: Juvenil B")
# elif nadador >= 18:
#     print("Classificação: Adulto")
# else:
#     print("Novo demais para nadar")

# #----------------------------------#

# ano = int(input("Digite um ano: "))
# bissexto = ano % 4

# if bissexto == 0:
#     print("Ano bissexto")
# else:
#     print("Não é um ano bissexto")

# #----------------------------------#

# salario = float(input("Digite seu salário: "))

# if salario > 1621:
#     aumento = salario + (salario * 0.1)
#     print(f"Seu novo salário é {aumento}")
# else:
#     aumento = salario + (salario * 0.15)
#     print(f"Seu novo salário é {aumento}")

# #----------------------------------#

# velocidade = int(input("Digite a sua velocidade: "))

# if velocidade > 80:
#     sobra = velocidade - 80
#     multa = sobra * 7
#     print(f"O valor da sua multa foi: {multa}")
# else:
#     print("Não tomou multa")

#  #----------------------------------#

# temperatura = float(input("Digite uma temperatura em celcius: "))
# resposta = input("Você quer converter a temperatura para Fahrenheit ou Kevin? \nDigite \n'F' para Fahrenheit \n'K' para Kelvin \n: ")

# if resposta == "F":
#     conversao = (temperatura * (9/5)) + 32
#     print(f"A temperatura em Fahrenheit é {conversao}")
# elif resposta == "K":
#     conversao = temperatura + 273.15
#     print(f"A temperatura em Kelvin é {conversao}")
# else:
#     print("ERRO")

# #----------------------------------#

# tamanho = float(input("Digite a área a ser pintada: "))
# area_coberta = 54
# numero_latas = tamanho/area_coberta
# inteiro = numero_latas % 1

# if inteiro == 0:
#     print(f"Você vai precisar de {numero_latas} latas, isso irá te custar R$ {numero_latas * 80},00")
# else:
#     numero_latas_int = int(numero_latas)
#     qtd_real_latas = numero_latas_int +1
#     print(f"Você vai precisar de {qtd_real_latas}, isso irá te custar {qtd_real_latas * 80}")

# #----------------------------------#

# salario = float(input("Digite o seu salário: "))
# preco_casa = float(input("Digite o valor da casa: "))
# tempo = float(input("Digite quanto tempo você vai demorar para pagar: "))
# trinta_por_cento = salario - (salario * 0.7)
# prestacao = salario / tempo

# if prestacao > trinta_por_cento:
#     print("Emprestimo negado")
# else:
#     print(f"Emprestimo aprovado, o valor da prestação é: {prestacao}")
