# Se trata de pedir al usuario que teclee un número entre 1 y 5, si escribe alguno que
# esté fuera de ese rango deberá volver a pedir el número.
# Si tecleo 0 me dirá Por favor teclee un número entre 1 y 5.

import os
os.system("cls")

try:
    numero=int(input("Por favor teclee un número entre 1 y 5: "))

    while numero not in range(1,6):
        numero=int(input("Por favor teclee un número entre 1 y 5: "))
    else:
        print("FIN")

except Exception as ex:
    print(f"Ha ocurrido un error, {ex}")