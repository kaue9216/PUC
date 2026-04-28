matriz = ([
    [1, 2, 3],
    [1, 2, 3],
    [1, 2, 3]
])


array0 = []
array1 = []
array2 = []

for i in matriz:
    array0.append(i[0])


for i in matriz:
    array1.append(i[1])


for i in matriz:
    array2.append(i[2])


matriz2 = []
matriz2.append(array0)
matriz2.append(array1)
matriz2.append(array2)

print(matriz)
print(matriz2)
