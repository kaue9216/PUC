# 43. Crie um dicionário de produtos e aplique desconto de 10%.

produtos = {"maça" : 10, "banana" : 20, "pera" : 30}

print(produtos)

for i in produtos:
    desconto = produtos[i] - (produtos[i] * 0.1)
    produtos[i] = desconto

print(produtos)
