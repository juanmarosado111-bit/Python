import os 
import math

PI = math.pi

def menu():
    print ("______________Menú de opciones_________________")
    print ("1.- Calcula el área de un triángulo.")
    print ("2.- Calcula el área de un rectángulo.")
    print ("3.- Calcula el área de un círculo.")
    print ("4.- Calcula el área de un cuadrado.")
    print ("5.- Calcula el área de un romboide.")  
    print ("0.- Salir del programa.")

def area_cuadrados(base, altura):
    return base*altura

def area_triangulo(base, altura):
    return (base*altura)/2

def area_circulo(radio):
    return PI * (radio ** 2)


opcion=1
while opcion!="0":
    os.system ("cls")
    menu() 
    print()
    opcion=input("Introduzca la opción que desea: ")

    match opcion:
        case "1":
            try:
                base=float(input("Introduce la base del triángulo: "))
                altura=float(input("Introduce la altura del triángulo: "))
            except:
                print("Has introducido mal alguno de los datos del triángulo.")
            else:    
                area=area_triangulo(base, altura)
                print("El área del triángulo es: ", area)
                
        case "2":
            try:
                base=float(input("Introduce la base del rectángulo: "))
                altura=float(input("Introduce la altura del rectángulo: "))
            except:
                print("Has introducido mal alguno de los datos del rectángulo.")
            else:    
                area=area_cuadrados(base, altura)
                print("El área del rectángulo es: ", area)
                           
        case "3":
            try:
                radio=float(input("Introduce el radio del círculo: "))
            except:
                print("Has introducido mal el dato del círculo.")
            else:    
                area=area_circulo(radio)
                print("El área del círculo es: ", area)
                
        case "4":  
            try:
                base=float(input("Introduce la base del cuadrado: "))
                altura=float(input("Introduce la altura del cuadrado: "))
            except:
                print("Has introducido mal el dato del cuadrado.")
            else:    
                area=area_cuadrados(base, altura)
                print("El área del cuadrado es: ", area)
                
        case "5":
            try:
                base=float(input("Introduce la base del romboide: "))
                altura=float(input("Introduce la altura del romboide: "))
            except:
                print("Has introducido mal alguno de los datos del romboide.")
            else:    
                area=area_cuadrados(base, altura)
                print("El área del romboide es: ", area)
                
        case "0":
            print("Fin del programa")
            
        case _ :
            print("Esa es una opción no válida....")
            
    if opcion!="0":
        input("Pulsa enter para continuar....")
