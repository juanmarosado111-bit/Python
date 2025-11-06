import os
os.system ("cls")

suma=0

while suma%2==0:
    try:
        numero=int(input("Inserta un número:" ))
    except Exception as fallo:
        print(fallo)
    else:
        while numero!=0:
            suma+=numero
            try:
                numero=int(input("Inserta un número:" ))
            except Exception as fallo:
                print(fallo)
    print(f"La suma es: {suma} ")
else:
    print("Termina el programa. ")