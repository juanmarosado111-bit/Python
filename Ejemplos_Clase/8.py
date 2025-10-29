import os
os.system("cls")
lado = int(input("¿De cuantos caracteres de lado quieres el cuadrado?: "))
caracter = input("¿Qué carácter quieres pintar?: ")

for fila in range(0, lado):
    for columna in range(0, lado):
        print(caracter, end="")
    print("")
    
    