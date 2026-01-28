import os
import random
import string


def menu():
    print ("______________Menú de opciones_________________")
    print ("1.- Ejercicio 1.")
    print ("2.- Ejercicio 2.")
    print ("3.- Ejercicio 3.") 
    print ("0.- Salir del programa.")

def ejercicio1():
    try:
        num1 = int(input("Introduce un número: "))
        num2 = int(input("Introduce otro número: "))

        if num1 > num2:
            for i in range(num1, num2-1, -1):  # cuenta hacia abajo
                if i % 2 == 0:
                    print(i)
        elif num2 > num1:
            for i in range(num1, num2+1):      # cuenta hacia arriba
                if i % 2 == 0:
                    print(i)
        else:
            print("Los números son iguales, no hay rango que recorrer.")

    except Exception as ex:
        print(f"Ha ocurrido un error: {ex}")

    finally:
        print("\nLa ejecución del código ha terminado.")
    
def ejercicio2():
    try:
        cadena="".join(random.choices(string.ascii_letters.upper(), k=3))

        cadena_usuario=input("Introduce 3 letas mayusculas: ")
        intento=1

        while cadena!=cadena_usuario:
            cadena_usuario=input("Introduce 3 letas mayusculas: ")
            intento+=1
        else:
            print(f"Has acertado en {intento} intentos")
        
    except Exception as ex:
        print(f"Ha ocurrido un error, ")

    finally:
        print("El programa ha terminado.")

def ejercicio3():
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


opcion=True
while opcion:
    os.system("cls")
    menu() 
    print()
    opcion=input("Introduzca la opción que desea: ")
    
    match opcion:
        case "0":
            opcion=False
            
        case "1":
            ejercicio1()
        
        case "2":
            ejercicio2()    
                
        case "3":
            ejercicio3()
        
        case _:
            print("Esa es una opción no válida....")
            
    input("Pulsa ENTER para continuar...")


