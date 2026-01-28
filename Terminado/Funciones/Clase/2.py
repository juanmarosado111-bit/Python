# Escribe un programa que lea un número n e imprima una pirámide de números con n filas siguiente figura:
#    1
#   121
#  12321
# 1234321

def ejercicio2():
    n = int(input("Introduce las filas: "))

    for i in range(1, n + 1):

        # 1️⃣ Imprimir espacios (un solo bucle)
        for _ in range(n - i):
            print(" ", end="")

        # 2️⃣ Imprimir todos los números (ascendentes y luego descendentes)
        for k in range(1, 2*i):
            print(k if k <= i else 2*i - k, end="")

        print()

ejercicio2()