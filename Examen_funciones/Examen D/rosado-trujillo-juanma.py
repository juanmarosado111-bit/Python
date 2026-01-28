# Rosado Trujillo, Juan Manuel
import os


def menu():
    print("---OPCIONES---")
    print("0. Salir")
    print("1. Ejercicio 1")
    print("2. Ejercicio 2")
    print("3. Ejercicio 3")


def calculadora_multiplos(num_A, num_B, multiplo):
    cadena_multiplos=""
    for i in range(num_A, num_B+1):
        if (i%multiplo)==0:
            if i==num_B:
                cadena_multiplos+=str(i)
            else:
                cadena_multiplos+=str(i)+", "
    return cadena_multiplos


def es_perfecto(n):
    global perfecto
    suma=0
    
    for i in range(1,n):
        if n%i==0:
            suma+=i

    if suma==n:
        perfecto=True
    else:
        perfecto=False


def imprimir_piramide_inversa(fila):
    for i in range(fila,0,-1):
        for _ in range(1,i+1):
            print(i, end="")
        print()


opcion = 1
while opcion!=0:
    os.system("cls")
    menu()
    try:
        opcion=int(input("Elige una opcion: "))
    except Exception as ex:
        print(f"Ha ocurrido una excepción, {ex}.")


    if opcion==0:
        break


    elif opcion == 1:
        try:
            num_A=int(input("Introduce el primer numero entero: "))
            num_B=int(input("Introduce el segundo numero entero: "))
            multiplo=int(input("Introduce el multiplo: "))
        except Exception as ex:
            print(f"Ha ocurrido una excepción, {ex}.")
        print(calculadora_multiplos(num_A, num_B, multiplo))


    elif opcion == 2:
        try:
            n=int(input("Introduce un número entero positivo: "))
        except Exception as ex:
            print(f"Ha ocurrido una excepción, {ex}.")
        perfecto=False
        es_perfecto(n)
        if perfecto:
            print("Es perfecto")
        else:
            print("No es perfecto")


    elif opcion == 3:
        try:
            fila=int(input("Introduce el numero de filas: "))
        except Exception as ex:
            print(f"Ha ocurrido una excepción, {ex}.")
        imprimir_piramide_inversa(fila)


    else:
        print("Opción no válida")

    input("Pulsa para continuar...")
    
print("Programa finalizado")




