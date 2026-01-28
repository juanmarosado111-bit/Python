# Rosado Trujillo, Juan Manuel

import os

#Ejercicio 1
def ejercicio1(num1,num2):
    pares=""
    inicio=max(num1, num2)
    fin=min(num1,num2)
    
    for i in range(inicio, fin-1, -1):
        if i%2==0:
            if pares!="":
                pares+=", "
            pares+=str(i)
    return pares


#Ejercicio 2
def menu_ej2():
    print("\nEjercicio 2 - El ascensor - Elige una opción: ")
    print("Opcion 0 - Salir")
    print("Opcion 1 - Subir personas al ascensor")
    print("Opcion 2 - Bajar personas del ascensor")
    opcion=int(input("Elige una opción: "))
    return opcion

def subir(num):
    global personas
    capacidad_max=8
    
    if personas+num<=capacidad_max:
        personas+=num
        print(f"Nadie se queda fuera, actualmente hay {personas} personas")
    else:
        personas=8
        fuera=(personas+num)-8
        print(f"Se quedan fuera {fuera} personas, actualmente hay {personas} personas")

def bajar(num):
    global personas
    if num<=personas:
        personas-=num
        print(f"Han bajado {num} personas, actualmente hay {personas} personas")
    else:
        personas=0
        print(f"Se han intentado bajar {num} personas, actualmente hay {personas} personas")


# Ejercicio 3
def ejercicio3(caracter, numero):
    for i in range(1,numero+1):
        print(caracter*i)

    for j in range(numero-1, 0, -1):
        print(caracter*j)


def menu():
    os.system("cls")
    print("Examen A - Menu de opciones:")
    print("0 - Salir")
    print("1 - Ejercicio 1 - Contador descendente")
    print("2 - Ejercicio 2 - El ascensor")
    print("3 - Ejercicio 3 - Triángulo doble")
    opcion=int(input("Elige una opción: "))
    return opcion


opcion=menu()
while opcion!=0:
    if opcion==1:
        num1=int(input("Introduce un numero entero: "))
        num2=int(input("Introduce otro numero entero: "))
        resultado=ejercicio1(num1, num2)
        print(f"Los numeros pares en orden descendente son: \n{resultado}")


    elif opcion==2:
        personas=0
        opcion=menu_ej2()
        while opcion!=0:
            if opcion==1:
                num=int(input("¿Cuantas personas van a subir?: "))
                subir(num)
            elif opcion==2:
                num=int(input("¿Cuantas personas van a bajar?: "))
                bajar(num)
            else:
                print("Introduce una opcion valida.")
    
            print() 
            opcion=menu_ej2()


    elif opcion==3:
        caracter=input("Introduce un caracter: ")
        numero=int(input("Introduce un numero: "))
        ejercicio3(caracter, numero)


    else:
        print("Elige una opcion valida")

    input("Pulsa para continuar...")
    opcion=menu()
