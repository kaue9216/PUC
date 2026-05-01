# 40. Crie um dicionário e verifique se uma chave existe.

dicionario = {'chave1' : 'valor1', 'chave2' : 'valor2'}
contador = 0

teste = input("Digite uma chave e eu verificarei se ela existe no dicionário: ")


for i in dicionario:
    if teste == i:
        print('chave existe')
        contador += 1

if contador == 0:
    print("chave inexistente")
