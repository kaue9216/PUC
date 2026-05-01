# 25. Qual a diferença entre dados['chave'] e dados.get('chave')?

# Na primeira opção, se a chave não existir, o códio quebra,
# já na segunda, se ela não existir o código imprime um valor atribuido ou None, caso não haja
# Nenhuma delas altera a lista

dados = {"chave" : "valor"}

print(dados['chave'])
print(dados)
print(dados.get('chave2', 'valor2'))
print(dados)
