# Rosado Trujillo, Juan Manuel

import os

total_acumulado=0
limite_superior=100
limite_inferior=0


def sumar(valor):
    global total_acumulado
    if (total_acumulado+valor)>limite_superior:
        total_acumulado=0
        print("Límite superior excedido y reinicio")
    else:
        total_acumulado+=valor
    print(f"Total acumulado actual: {total_acumulado}")


def restar(valor):
    global total_acumulado
    if (total_acumulado-valor)<0:
        print(f"No se pudieron restar {valor-total_acumulado} unidades")
        total_acumulado=0
    else:
        total_acumulado-=valor
    print(f"Total acumulado actual: {total_acumulado}")
    

def menu_ej2():
    print("Ejercicio 2 - Acumulador Numérico con Límite y Reinicio")
    print("0 - Salir")
    print("1 - Sumar")
    print("2 - Restar")
    opcion=int(input("Introduce una opcion: "))
    return opcion


def ejercicio2():
    os.system("cls")
    opcion=menu_ej2()
    while opcion!=0:
        if opcion==1:
            valor=int(input("Introduce el valor a sumar: "))
            sumar(valor)

        elif opcion==2:
            valor=int(input("Introduce el valor a restar: "))
            restar(valor)

        else:
            print("Elige una opcion valida.")
    
        input("Pulsa enter para continuar...")
        os.system("cls")
        opcion=menu_ej2()
        

ejercicio2()