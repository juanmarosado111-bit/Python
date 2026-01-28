# Rosado Trujillo, Juan Manuel

caracter=input("Introduce un caracter: ")
num=int(input("Introduce un numero entero: "))

def imprimir_matriz(caracter, num):
    for _ in range(num):
        for _ in range(num):
            print(caracter, end=" ")
        print()

