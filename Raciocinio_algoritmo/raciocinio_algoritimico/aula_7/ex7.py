nomes = input("Digite 3 nomes separados por virgula")
array = [i.strip() for i in nomes.split(",")]
print(array)

dicionário = {}
dicionário = {}.fromkeys([array[0], array[1],array[2]], 0)

print(dicionário)
