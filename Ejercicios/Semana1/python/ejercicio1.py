while True:
    try:
        numImp = int(input("Ingrese un numero: "))
        if (numImp % 2 == 0):
            print("Debe ingresar un numero impar")
        else:
            print(numImp)
            break
    except ValueError:
        print("Debe ingresar un valor numerico")
