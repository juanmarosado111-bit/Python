# Rosado Trujillo, Juan Manuel

import os

#Ejercicio 1
def contar_paridad(inicio, fin):
    global conteo_de_pares, conteo_de_impares
    limite_inferior=min(inicio, fin)
    limite_superior=max(inicio, fin)
    
    for i in range(limite_inferior, limite_superior+1):
        if i%2==0:
            conteo_de_pares+=1
        else:
            conteo_de_impares+=1


#Ejercicio 2
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
    while True:
        try:
            opcion=int(input("Introduce una opcion: "))
            break
        except ValueError:
            print("Introduce una opcion valida...")
    return opcion

def ejercicio2():
    os.system("cls")
    opcion=menu_ej2()
    while opcion!=0:
        if opcion==1:
            while True:
                try:
                    valor=int(input("Introduce el valor a sumar: "))
                    break
                except ValueError:
                    print("Introduce un valor valido.")
            sumar(valor)

        elif opcion==2:
            while True:
                try:
                    valor=int(input("Introduce el valor a restar: "))
                    break
                except ValueError:
                    print("Introduce un valor valido.")
            restar(valor)

        else:
            print("Elige una opcion valida.")
    
        input("Pulsa enter para continuar...")
        os.system("cls")
        opcion=menu_ej2()


#Ejercicio 3
def imprimir_matriz(caracter, num):
    for _ in range(num):
        for _ in range(num):
            print(caracter, end=" ")
        print()


#Menu examen
def menu():
    print("Examen C - Menu de opciones")
    print("0 - Salir")
    print("1 - Ejercicio 1 - Conteo de Pares e Impares en Secuencia")
    print("2 - Ejercicio 2 - Acumulador Numérico con Límite y Reinicio")
    print("3 - Ejercicio 3 - Impresión de Matriz Cuadrada")
    while True:
        try:
            opcion=int(input("Elige una opción: "))
            break
        except ValueError:
            print("Introduce una opcion valida.")
    return opcion

os.system("cls")
opcion=menu()
while opcion!=0:
    if opcion==1:
        conteo_de_pares=0
        conteo_de_impares=0
        while True:
            try:
                inicio=int(input("Introduce el numero de inicio: "))
                fin=int(input("Introduce el numero de fin: "))
                break
            except ValueError:
                print("Error al introducir los datos, vuelve a intentarlo...")
        contar_paridad(inicio, fin)

        print(f"En ese rango hay {conteo_de_pares} numeros pares y {conteo_de_impares} numeros impares.")
    
    elif opcion==2:
        total_acumulado=0
        limite_superior=100
        limite_inferior=0
        ejercicio2()

    elif opcion==3:
        while True:
            try:
                caracter=input("Introduce un caracter: ")
                num=int(input("Introduce un numero entero: "))
                break
            except ValueError:
                print("Error al introducir los datos, vuelve a intentarlo...")
        imprimir_matriz(caracter, num)
        
    else:
        print("Elige una opcion valida.")
    
    input("Pulsa enter para continuar...")
    os.system("cls")
    opcion=menu()
    
    
    
    
    
    
    
    
