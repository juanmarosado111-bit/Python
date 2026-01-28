capacidad_maxima=100
nivel=50

def menu():
    print("---OPCIONES---")
    print("0. Salir")
    print("1. Añadir agua")
    print("2. Gastar agua")
    print("3. Crear nuevo deposito")
    
def añadir_agua(cantidad):
    operacion=nivel
    if operacion+cantidad>capacidad_maxima:
        print("No se puede añadir esa cantidad. Capacidad excedida.")
    else:
        operacion+=cantidad
    return(operacion)

def gastar_agua(cantidad):
    operacion=nivel
    if operacion-cantidad<0:
        print("No se puede gastar esa cantidad. El nivel no puede ser negativo.")
    else:
        operacion-=cantidad
    return(operacion)   

def crear_deposito():
    global capacidad_maxima
    global nivel
    capacidad_maxima=float(input("Introduce la capacidad máxima de tu deposito: "))
    nivel=float(input("Introduce el nivel actual del deposito en L: "))

opcion=1
while opcion!=0:
    menu()
    opcion=int(input("Elige una opcion: "))

    if opcion==0:
        print("Programa finalizado.")
    
    elif opcion==1:
        cantidad=float(input("Introduce la cantidad de agua que quieras añadir: "))
        nivel=añadir_agua(cantidad)
        
    elif opcion==2:
        cantidad=float(input("Introduce la cantidad de agua que quieras gastar: "))
        nivel=gastar_agua(cantidad)

    elif opcion==3:
        crear_deposito()
        
    else:    
        print("Error, introduce una opcion valida.")
    
    print(f"Nivel actual: {nivel}L")

    
    
