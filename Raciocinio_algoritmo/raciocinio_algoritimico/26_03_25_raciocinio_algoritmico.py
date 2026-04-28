#Diga o resultado do código. Você precisa informar o que acontece em cada algoritimo

# # EX1.
# x = 2
# if x * 2 > 3:
#     print("A")

# # R. Na primeira linha é definida a variável x como 2
# # na segunda linha testamos se x multiplicado por dois é mior que 3, a resposta é true
# # como a resposta da condicional é true o código printa a sting "A"

# # EX2.

# for i in range(1,4):
#     print(i * 2)

# # R. Na primeira linha criamos o loop for com range de 1 a 4
# # na segunda linha multiplicamos o numero i por 2 enquanto o loop for true, como o intervalo é definido d 1 a 4 esse processo ocorrerá 3 vezes.

# # EX3.

# n = 7
# if n % 2 == 0:
#     print("Rar")
# else:
#     print("Ímpar")

# # R. Na primeira linha criamos a variável n e a definimos como 7
# # na segunda linha criamos a condicional e definimos que caso ela seja verdadeira o programa deve printar a string "Par"
# # caso a condicional seja falsa o código deve eprintar a string "Ímpar"
# # como o resto da divisão de 7 por 2 é 1, a condicional será falsa e o código ira imprimir a string "Ímpar"

# # EX4.

# s = 0

# for i in range(3):
#     s += 2

# print(s)

# # R. Na primeia linha definimos a variavel s e atribuimos o valor 0 a ela
# # na segunda linha criamos um loop for, esse loop irá somar dois ao valor de s até o contador atingir 3
# # após o loop for o programa imprime o valor de s, como o loop roda 4 veses esse valor será 6

# # EX5.

# i = 0

# while i < 2:
#     print(i)
#     i += 1

# # R.Na primeira linha iniciamos a variável i e atibuimos o valor de 0 a ela
# # na segunda linha iniciamos um loop while, e definimos que ele deve rodar enquanto i for menor que 2
# # na terceira linha imprimimos o valor de i
# # na quarta linha adicionamos 1 ao valor de i
# # o código vai imprimir, em ordem: 0, 1

# # EX6.

# x = 10
# if x < 5:
#     print("A")
# elif x < 15:
#     print ("B")

# # R. Na primeira linha definimos a variavel x e atribuimos o valor de 10 a lea
# # na segunda linha criamos uma codicional que resultará em verdadeiro caso x seja menor que 5
# # na terceira linha imprimimos a string "A" caso a primeira condicional seja verdadeira
# # na quarta linha definimos mais uma regra para a condicional, utlilzando elif, que resultará em verdadeiro caso x seja menor que 5
# # na quinta linha imprimimos a string "B" caso a segunda condicional seja verdadeira
# # o programa irá retornar "B" pois a variável x é maior que 5 e menor que 15

# # EX7.

# n = 0
# if n:
#     print("True")
# else:
#     print("False")

# # R. Na primeira linha criamos a variável n e definimos o valor de 0 a ela
# # na segunda linha criamos uma condicional que retorna true caso o valor de n
# # na terceira linha printamos a string "True" caso a condicional seja verdadeira
# # caso ela seja falsa o código imprime a sting "False"
# # como 0 é false o código imprime a string "False"


# # EX8.

# for i in range(2, 6):
#     print(i)

# # R. Na primeira linha criamos um loop for com limites delimitados
# # na segunda linha printamos o valor de i enquanto o loop for true
# # O código irá printar os valores 2, 3, 4 e 5

# # EX9.

# soma = 0

# for i in range(1, 4):
#     soma += i
# print(soma)

# # R. Na primeira linha iniciamos a variável "soma"
# # na segunda linha iniciamos um loop for e definimos os limites 1 e 4
# # na terceira linha incrementamos o valor de i enquanto o loop for true e armazenamos esse valor na variavél "soma"
# # na quarta linha printamos o valor de "soma" quando o loop retornar false
# # O código retornará "6"

# # EX10.

# x = 3
# y = 4

# if x == y:
#     print("1")
# else:
#     print("2")

# # R. Na primeira linha iniciamos a variável x e atribuimos a ela o valor de 3
# # na segunda linha iniciamos a variável y e atribuimos a ela o valor de 4
# # na terceira linha criamos uma condicional que caso retorne true, imprimirá o valo "1"
# # na quinta e na sexta linha configuramos que caso a condicional retorne false, o valor impresso será "2"
# # o código imprimirá: "2"

# #EX11. Verifique se um número é múltiplo de 3 (com interação do usuário).
# # R.

# numero = int(input("Digite um número e eu direi se ele é multiplo de 3: "))
# multiplo = numero % 3

# if multiplo == 0:
#     print("O número é multiplo de 3")
# else:
#     print("O número não é multiplo de 3")

# # EX12. Verifique se um número está entre 10 e 20 (com interação do usuário).

# #R.
# numero = int(input("Digite um número e eu direi se ele está entre 10 e 20: "))

# if 20 > numero > 10:
#     print("O número é menor que 20 e maior que 10")
# else:
#     print("O numero é maior que 20 ou menor que 10")

# # EX13. Leia idade e classifique: menor, adulto, idoso (com interação do usuário).

# #R.

# idade = int(input("Digite a sua idade: "))

# if idade < 18:
#     print("Você é menor")
# elif idade < 65:
#     print("Você é um adulto")
# else:
#     print("Você é um idoso")

# # EX14. Verifique se um número é positivo e par (com interação do usuário).

# #R.
# numero = int(input("Digite um número "))
# par = numero % 2

# if numero > 0 and par == 0:
#     print("O número é positivo e par")
# else:
#     print("O número não é positivo ou não é par, ou ambos")

# #EX15. Verifique se três números são iguais (com interação do usuário).

# #R.
# numero1 = int(input("Digite um número: "))
# numero2 = int(input("Digite outro número: "))
# numero3 = int(input("Digite mais um número: "))

# if numero1 == numero2 and numero2 == numero3:
#     print("Os três números são iguais")
# else:
#     print("Pelo menos um dos números não é igual aos outros")

# # EX16. Leia dois números e informe o menor (com interação do usuário).

# #R.
# numero1 = int(input("Digite um número: "))
# numero2 = int(input("Digite outro número: "))

# if numero1 < numero2:
#     print("O primeiro número é o menor")
# elif numero2 < numero1:
#     print("O segundo número é o menor")
# else:
#     print("Os números são iguais")

# #EX17. Leia uma temperatura e informe se está fria, sendo <15ºC: agradável ou >30ºC quente (com interação do usuário).

# #R.
# temperatura = float(input("Digite uma temperatura: "))

# if temperatura < 15:
#     print("Temperatura fria")
# elif temperatura < 30:
#     print("Temperatura agradável")
# else:
#     print("Temperatura quente")

# #EX18. Simule login com usuário e senha (com interação do usuário).

# #R.
# login = input("Digite seu login: ")
# senha = input("Digite sua senha: ")

# if login == "admin" and senha == "12345":
#     print("Login efetuado com sucesso!")
# else:
#     print("Login ou senha errados, tente novamente")

# #EX19. Leia valor e aplique desconto progressivo, sendo: 10% acima de 100, 20% acima de 200 (com interação do usuário).

# valor = float(input("Digite o valor da compra: "))

# if valor >= 200:
#     desconto = valor - (valor * 0.2)
#     print(f"A sua compra com desconto ficou R${desconto}")
# elif valor >= 100:
#     desconto = valor - (valor * 0.1)
#     print(f"A sua compra com desconto ficou R${desconto}")
# else:
#     print(f"O valor da sua compra ficou R${valor}")

# #EX20. Leia 3 números e informe o maior (com interação do usuário).

# numero1 = int(input("Digite um número: "))
# numero2 = int(input("Digite outro número: "))
# numero3 = int(input("Digite mais um número: "))

# if numero1 > numero2 and numero1 > numero3:
#     print("O maior número é o primeiro")
# elif numero2 > numero1 and numero2 > numero3:
#     print("O maior número é o segundo")
# else:
#     print("O maior número é o terceiro")

# #EX21. Some os números de 1 a 10 (com interação do usuário).

# numero = int(input("Digite o número 0: "))
# soma = 0

# for i in range(0, 10):
#     numero = numero + 1
#     soma = numero + soma

# print(soma)

#EX22. Mostre apenas números pares de 1 a 20 (com interação do usuário).

# numero = int(input("Digite o número 0: "))


# while numero < 21:
#     numero = numero + 1
#     par = numero % 2
#     if par == 0:
#         print(numero)

#EX23. Leia 5 números e calcule a média (com interação do usuário).
# soma = 0

# for i in range(5):
#     numero = float(input("Digite um número: "))
#     soma = numero + soma
# print(soma)
# media = soma / 5
# print(f"A média dos números digitados é: {media}")

#EX24. Conte quantos números negativos foram digitados (com interação do usuário).
# contador = 0

# for i in range(5):
#     numero = int(input("Digite um número: "))
#     if numero < 0:
#         contador = contador + 1

# print(f"Você digitou {contador} números negativos")

#EX25. Leia números até digitar 0 e calcule soma (com interação do usuário).
# soma = 0
# numero = 1

# while numero != 0:
#     numero = 0
#     numero = int(input("Digite um número, ou 0 para sair: "))
#     soma = numero + soma

# print(f"A soma dos números digitados é: {soma}")

# #EX26. Leia 10 números e conte quantos são maiores que 5 (com interação do usuário).
# contador = 0

# for i in range(10):
#     numero = int(input("Digite um número e ao final eu direi quantos foram maior que 5: "))
#     if numero > 5:
#         contador = contador + 1
# print(contador)

#EX27. Leia números até negativo e conte pares (com interação do usuário).
# contador = 0
# par = 0

# for i in range(10):
#     numero = int(input("Digite um número positivo ou negativo e ao final contarei os pares: "))
#     par = numero % 2
#     if par == 0:
#         contador = contador + 1

# print("A quantidade de números pares é: ", contador)

# #EX28. Calcule o fatorial de um número (ex: 5! = 120) (com interação do usuário).
# numero = int(input("Digite um número e eu irei calcular o fatorial dele: "))
# contador = 0
# fatorial = 1

# while numero > contador:
#     fatorial = fatorial * (contador + 1)
#     contador = contador + 1

# print("O fatorial do número digitado é: ", fatorial)

# #EX29. Mostre a tabuada de um número (com interação do usuário)

# numero = int(input("Digite um número inteiro e eu direi a tabuada dele: "))
# contador = 0

# while contador <= 10:
#     print(contador, " * ", numero, " = ", contador * numero)
#     contador = contador + 1

# #EX30. Leia 5 notas e informe quantas são ≥ 7 (com interação do usuário).
# contador = 0

# for i in range(5):
#     nota = int(input("Digite uma nota: "))
#     if nota >= 7:
#         contador = contador + 1

# print(f"Você teve {contador} notas maiores ou iguais a 7")
