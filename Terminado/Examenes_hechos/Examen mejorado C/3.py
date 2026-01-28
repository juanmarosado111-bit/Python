try:
    numero = int(input("Introduce un número entero positivo: "))

    for i in range(1, numero + 1):
        suma = 0
        for j in range(1, i + 1):
            print(f"{j}", end="")
            if j != i:
                print(" + ", end="")
            suma += j
        print(f" = {suma}")
        
except Exception as ex:
    print(f"Ha ocurrido un error, ")

finally:
    print("El programa ha terminado.")
