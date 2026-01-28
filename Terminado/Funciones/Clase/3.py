# Realiza un programa que vaya pidiendo números hasta que se introduzca un numero negativo y
# nos diga cuantos números se han introducido, la media de los impares y el mayor de los pares.
# El número negativo sólo se utiliza para indicar el final de la introducción de datos pero no se incluye en el cómputo.


def ejercicio3():
    num=int(input("Introduce un numero (Negativo para salir): "))
    mayor_par=0
    suma_impares=0
    contador=0
    contador_impares=0
    
    while num>=0:
        contador+=1
        if num%2==0:
            if num>mayor_par:
                mayor_par=num
        else:
            contador_impares+=1
            suma_impares+=num
        num=int(input("Introduce un numero (Negativo para salir): "))
        
    print(f"Has introducido {contador} numeros, {suma_impares/contador_impares} es la media de los impares y el mayor de los pares es {mayor_par}")

ejercicio3()




