# Rosado Trujillo, Juan Manuel

caracter=input("Introduce un caracter: ")
num=int(input("Introduce un numero entero: "))

def imprimir_tablero(caracter, num):
    for i in range(num):
        if i%2==0:
            for _ in range(num):
                print(caracter, end=" ")
        else:
            for _ in range(num-1):
                print(" "+caracter, end="")
        print()
            
imprimir_tablero(caracter,num)