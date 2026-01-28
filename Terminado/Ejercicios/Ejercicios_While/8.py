# Este script le pide al usuario que vaya tecleando números una y otra vez, pero solo
# números pares, en caso de que teclee un número impar el programa acabará y dirá
# la cantidad de números pares ingresados (el 0 cuenta como par). Muestra Si escribo
# 2,8,12,1 el script me dirá "Ha escrito 3 números pares")

numero=int(input("Introduce un numero par: "))
contador=0

try:
    while numero%2==0:
        contador+=1
        numero=int(input("Introduce un numero par: "))
    
    print(f"Has introducido {contador} numeros pares")

except Exception as ex:
    print(f"Ha ocurrido un error, {ex}")
finally:
    print("El programa ha finalizado")
    
    
    