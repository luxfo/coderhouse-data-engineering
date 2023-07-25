lista1 = [1, 2, 3, 3, 4]
lista2 = [3, 3, 4, 5]

lista3 = []

for element in lista1:
    if element in lista2:
        lista3.append(element)

print(list(set(lista3)))
