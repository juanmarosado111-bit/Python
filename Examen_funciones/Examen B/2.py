# Rosado Trujillo, Juan Manuel

import os

stock_actual=0
capacidad_max=500


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
            opcion_ej2=int(input("Introduce una opción: "))
            break
        except ValueError:
            print("Introduce una opcion valida")
    return opcion_ej2


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