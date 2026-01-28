import os
os.system("cls")
lado = int(input("¿De cuantas filas quieres el triángulo?: "))
caracter = input("¿Qué carácter quieres pintar?: ")

for i in range(0, lado):
    for j in range(0, i+1):
        print(caracter, end="")
    print("")
