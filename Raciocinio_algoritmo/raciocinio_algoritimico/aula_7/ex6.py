dicionario = {"Elemento 1" : 1, "Elemento 2" : 2, "Elemento 3" : 3}
dicionario1 = {}

for chave, valor in dicionario.items():
    # print("chave: ", chave)
    # print("valor:", valor )
    dicionario1[chave] = valor

dicionario1["Elemento 1"] = 4

print(dicionario)
print(dicionario1)
