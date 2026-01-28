# Rosado Trujillo, Juan Manuel

import random
import os
os.system("cls")

try:
    num_aleatorio=random.randint(1,100)
    num_usuario=int(input("Adivina el número: "))
    intento=1

    while num_aleatorio!=num_usuario:
        intento+=1
        if num_aleatorio<num_usuario:
            print("El número introducido es mayor")
        elif num_aleatorio>num_usuario:
            print("El número introducido es menor")
        num_usuario=int(input("Adivina el número: "))
    else:
        print("Número acertado.")
        print(f"Número de intentos: {intento}")
        
except Exception as ex:
    print(f"Ha ocurrido un error, {ex}")
    
finally:
    print("La ejecución del codigo ha terminado.") 


