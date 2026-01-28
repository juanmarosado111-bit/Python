import os
os.system("cls")

try:
    num1 = int(input("Introduce un número: "))
    num2 = int(input("Introduce otro número: "))

    if num1 > num2:
        for i in range(num1, num2-1, -1):  # cuenta hacia abajo
            if i % 2 == 0:
                print(i)
    elif num2 > num1:
        for i in range(num1, num2+1):      # cuenta hacia arriba
            if i % 2 == 0:
                print(i)
    else:
        print("Los números son iguales, no hay rango que recorrer.")

except Exception as ex:
    print(f"Ha ocurrido un error: {ex}")

finally:
    print("\nLa ejecución del código ha terminado.")