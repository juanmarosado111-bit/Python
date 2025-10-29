import os
opcion = 0
while opcion != 5:
    os.system("cls")
    print("1.- Sumar dos números.")
    print("2.- Restar dos números.")
    print("3.- Multiplicar dos números.")
    print("4.- Dividir dos números.")
    print("5.- Salir")
    try:
        opcion = int(input("Elige una opción (5 para salir): "))
    except Exception as excepcion:
        print(f"Algo has hecho mal: {type(excepcion)}")
    else:
        print(f"Has elegido la opción {opcion}")
    finally:
        input("Pulsa ENTER para continuar...")
else:
    print("Bucle terminado.")
print("Programa terminado.")





