# Rosado Trujillo, Juan Manuel

import os

#Ejercicio 1
def sumar_multiplos(inicio, fin, multiplo):
    principio=min(inicio,fin)
    final=max(inicio,fin)
    suma=0


    for i in range(principio, final+1):
        if i%multiplo==0:
            suma+=i
    return suma


#Ejercicio 2
def ingreso_stock(cantidad):
    global stock_actual
    if cantidad+stock_actual<=capacidad_max:
        stock_actual+=cantidad
        print("Operación correcta")
    else:
        fuera=(stock_actual+cantidad)-capacidad_max
        stock_actual=capacidad_max
        print(f"Limite superado se han quedado fuera {fuera} unidades")
    print(f"Stock actual: {stock_actual}")

def salida_stock(cantidad):
    global stock_actual
    if cantidad>stock_actual:
        print(f"La cantidad indicada es mayor que el stock actual, cantidad entragada: {stock_actual}")
        stock_actual=0
    else:
        stock_actual-=cantidad
        print("Operacion correcta")
    print(f"Stock actual: {stock_actual}")

def menu_ej2():
    print("Ejercicio 2 - Control de Stock en Almacén - Opciones: ")
    print("0 - Salir")
    print("1 - Ingresar stock")
    print("2 - Salida stock")
    while True:
        try:
            opcion=int(input("Introduce una opción: "))
            break
        except ValueError:
            print("Introduce una opcion valida")
    return opcion

def ejercicio2():
    os.system("cls")
    opcion_ej2=menu_ej2()
    while opcion_ej2!=0:
        if opcion_ej2==1:
            while True:
                try:
                    cantidad=int(input("Introduce la cantidad a ingresar: "))
                    if cantidad>0:
                        break
                except ValueError:
                    print("Introduce una cantidad valida")
            ingreso_stock(cantidad)

        elif opcion_ej2==2:
            while True:
                try:
                    cantidad=int(input("Introduce la cantidad a sacar: "))
                    if cantidad>0:
                        break
                except ValueError:
                    print("Introduce una cantidad valida")   
            salida_stock(cantidad)

        else:
            print("Introduce una opción valida")
    
        input("Pulsa para continuar...")
        os.system("cls")
        opcion_ej2=menu_ej2()


#Ejercicio 3
def imprimir_tablero(caracter, num):
    for i in range(num):
        if i%2==0:
            for _ in range(num):
                print(caracter, end=" ")
        else:
            for _ in range(num-1):
                print(" "+caracter, end="")
        print()


#Estructura menu examen

def menu():
    print("Examen B - Menu de opciones")
    print("0 - Salir")
    print("1 - Ejercicio 1 - Suma de Múltiplos en un Rango")
    print("2 - Ejercicio 2 - Control de Stock en Almacén")
    print("3 - Ejercicio 3 - Patrón de Tablero de Ajedrez")
    while True:
        try:
            opcion=int(input("Elige una opción: "))
            break
        except ValueError:
            print("Elige una opcion valida.")
    return opcion

os.system("cls")
opcion=menu()
while opcion!=0:
    if opcion==1:
        while True:
            try:
                inicio=int(input("Introduce el numero de inicio del rango: "))
                fin=int(input("Introduce el numero de fin del rango: "))
                multiplo=int(input("Introduce el multiplo: "))
                break
            except ValueError:
                print("Error al introducir uno de los datos, vuelve a intentarlo.")

        print(sumar_multiplos(inicio, fin, multiplo))
        
    elif opcion==2:
        stock_actual=0
        capacidad_max=500
        ejercicio2()
        
    elif opcion==3:
        while True:
            try:
                caracter=input("Introduce un caracter: ")
                num=int(input("Introduce un numero entero: "))
                break
            except ValueError:
                print("Error al introducir uno de los datos, vuelve a intentarlo.")
        
        imprimir_tablero(caracter,num)
    
    else:
        print("Elige una opcion valida")

    input("Pulsa enter para continuar...")
    os.system("cls")
    opcion=menu()