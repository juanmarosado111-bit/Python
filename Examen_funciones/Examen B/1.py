# Rosado Trujillo, Juan Manuel

inicio=int(input("Introduce el numero de inicio del rango: "))
fin=int(input("Introduce el numero de fin del rango: "))
multiplo=int(input("Introduce el multiplo: "))


def sumar_multiplos(inicio, fin, multiplo):
    principio=min(inicio,fin)
    final=max(inicio,fin)
    suma=0


    for i in range(principio, final+1):
        if i%multiplo==0:
            suma+=i
    return suma


print(sumar_multiplos(inicio, fin, multiplo))
