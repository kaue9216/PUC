produtos = {"Maça" : 10, "Banana" : 20, "Amora" : 30}

print(produtos)

for i in produtos:
    print(i)

for i in produtos.values():
    print(i)

for i in produtos:
    print(i, ":", produtos[i])
