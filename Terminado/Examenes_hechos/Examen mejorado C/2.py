import random
import string

try:
    cadena="".join(random.choices(string.ascii_letters.upper(), k=3))
    print(cadena)

    cadena_usuario=input("Introduce 3 letas mayusculas: ")
    intento=1

    while cadena!=cadena_usuario:
        cadena_usuario=input("Introduce 3 letas mayusculas: ")
        intento+=1
    else:
        print(f"Has acertado en {intento} intentos")
        
except Exception as ex:
    print(f"Ha ocurrido un error, ")

finally:
    print("El programa ha terminado.")