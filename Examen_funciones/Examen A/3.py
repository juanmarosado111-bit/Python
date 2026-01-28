# Rosado Trujillo, Juan Manuel

caracter=input("Introduce un caracter: ")
numero=int(input("Introduce un numero: "))


def ejercicio3(caracter, numero):
    for i in range(1,numero+1):
        print(caracter*i)

    for j in range(numero-1, 0, -1):
        print(caracter*j)

ejercicio3(caracter, numero)