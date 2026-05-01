# 42. Crie um programa que encontre o maior valor em uma lista.

lista = [1, 2, 3, 4, 5, 1, 72]
m_numero = 0

for i in lista:
    if i > m_numero:
        m_numero = i

print(m_numero)
