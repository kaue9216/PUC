dicionario = {"Elemento 1" : 1, "Elemento 2" : 2, "Elemento 3" : 3}

print(dicionario)
pergunta = input("Você deseja apagar o conteúdo do dicionário? ")

if pergunta == "sim":
    dicionario.clear()
else:
    print("Sem problemas! ")

print(dicionario)
