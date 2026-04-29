produtos = {"Maça" : 10, "Banana" : 20, "Amora" : 30}

print(produtos)

produto = input("Qual dos produtos você deseja alterar? ")
preco = input("Qual o novo valor você deseja? ")

for i in produtos:
    if i == produto:
        produtos[produto] = preco
    else:
        print("Produto não encontrado")

print(produtos)
