def contar(lista, elemento):
    cant = 0
    for i in lista:
        if (elemento == i):
            cant = cant + 1

    return cant

lista = [1, 4, 2, 2, 5, 3, 3, 3, 4, 4, 4, 4, 4, 6, 7, 8]
elemento = 4

cantidad = contar(lista, elemento)

print("elemento", elemento, "aparece", cantidad, "veces")
