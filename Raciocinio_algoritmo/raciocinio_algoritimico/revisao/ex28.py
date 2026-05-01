# Qual a diferença entre for elemento in lista e for i in range(len(lista))?

# A primeira opção corre pelos elementos da lista, enquanto a segunda corre pelo índice

lista = [2, 2, 3, 4]

for elemento in lista:
    print(elemento)

for i in range(len(lista)):
    print(i)
