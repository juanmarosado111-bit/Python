# Rosado Trujillo, Juan Manuel

def menu_ej2():
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
