def media():
    try:
        cantidadNum = int(input("Ingrese una cantidad de numeros para calcular la media: "))
        lista = []

        for i in range(cantidadNum):
            num = float(input("Ingrese el numero {}: ".format(i+1)))
            lista.append(num)
        
        print("La media de los numeros es:", sum(lista)/len(lista))
    except ValueError:
        print("Debe ingresar un valor numerico")

media()
