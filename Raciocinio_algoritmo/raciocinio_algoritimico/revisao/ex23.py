# 23. Qual a diferença entre append() e insert()?

# R.: Ambos os étodos adicionam um elemento à lista, porém o append() sempre adiciona o elemento ao final da lista,
#  enquanto no insert() você precisa indicar a posição onde o elemento irá ser inserido

lista = [0, 1, 2, 3]

lista.insert(1, 10)

print(lista)
