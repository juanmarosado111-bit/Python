# Un script pedirá al usuario que vaya tecleando números de manera repetida.
# cuando pulse 0, el programa muestra "La suma es " seguido de la suma de los
# números. Si esta suma es par, el programa se repite y si es impar el programa acaba.

# Si tecleo 2,6,2, 0 Me dirá suma "10" y volverá a pedir otra serie de números, si tecleo
# 2,6,3 Me dirá "suma 11" y acabará.


import os
os.system ("cls")

suma=0

while suma%2==0:
    numero=int(input("Inserta un número:" ))
    suma=0
    while numero!=0:
        suma+=numero
        numero=int(input("Inserta un número:" ))
    print(f"La suma es: {suma} ")
else:
    print("Termina el programa. ")

