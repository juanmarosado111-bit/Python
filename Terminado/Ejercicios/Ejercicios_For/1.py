# Usando un bucle for escribir un script que pida un valor entero y muestre en pantalla una
# lista de números desde el 0 al valor tecleado. Los números se separarán por comas. Si el
# usuario entra por teclado el número 5 el script devolverá la secuencia 0, 1, 2, 3, 4, 5

import os
os.system("cls")


try:
    
    numero=int(input("Introduce un numero: "))
    for num in range(0,numero+1):
        if num!=numero:
            print(num, end=", ")
        else:
            print(numero)
            
except Exception as ex:
    print(f"Ha ocurrido un error, {ex}")
finally:
    print("La ejecucion del programa ha finalizado")
