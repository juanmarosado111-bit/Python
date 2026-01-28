# =========================================================
# 9. SUMA DE LOS N PRIMEROS NÚMEROS
# =========================================================
def sumar_numeros():
    n = int(input("Introduce un número positivo: "))
    suma = 0
    i = 1

    while i <= n:
        suma = suma + i
        i = i + 1

    print("La suma es:", suma)



# =========================================================
# 10. FACTORIAL DE UN NÚMERO
# =========================================================
def factorial():
    n = int(input("Introduce un número no negativo: "))
    if n < 0:
        print("No existe factorial de negativos")
        return

    resultado = 1
    i = 1
    while i <= n:
        resultado = resultado * i
        i = i + 1

    print("Factorial:", resultado)



# =========================================================
# 11. SUMAR SOLO LOS PARES HASTA N
# =========================================================
def sumar_pares():
    n = int(input("Introduce un número positivo: "))
    suma = 0
    i = 2

    while i <= n:
        suma = suma + i
        i = i + 2

    print("Suma de pares:", suma)



# =========================================================
# 12. CONTAR CIFRAS PARES E IMPARES DE UN NÚMERO
# =========================================================
def cifras_par_impar():
    n = abs(int(input("Introduce un número: ")))
    pares = 0
    impares = 0

    if n == 0:
        pares = 1
    else:
        while n > 0:
            cifra = n % 10
            if cifra % 2 == 0:
                pares = pares + 1
            else:
                impares = impares + 1
            n = n // 10

    print("Cifras pares:", pares)
    print("Cifras impares:", impares)



# =========================================================
# 13. MOSTRAR TODOS LOS DIVISORES DE UN NÚMERO
# =========================================================
def divisores():
    n = int(input("Introduce un número positivo: "))
    i = 1

    while i <= n:
        if n % i == 0:
            print(i)
        i = i + 1



# =========================================================
# 14. COMPROBAR SI ES UN NÚMERO PERFECTO
# =========================================================
def numero_perfecto():
    n = int(input("Introduce un número: "))
    suma = 0
    i = 1

    while i < n:
        if n % i == 0:
            suma = suma + i
        i = i + 1

    if suma == n:
        print("Es perfecto")
    else:
        print("No es perfecto")



# =========================================================
# 15. CONTAR LETRAS "a" (SIN USAR count)
# =========================================================
def contar_a():
    texto = input("Texto: ")
    contador = 0
    i = 0

    while i < len(texto):
        if texto[i] == "a":
            contador = contador + 1
        i = i + 1

    print("Número de 'a':", contador)



# =========================================================
# 16. CONTAR VOCALES Y CONSONANTES
# =========================================================
def vocales_consonantes():
    texto = input("Introduce un texto en minúsculas: ")

    v = 0
    c = 0
    i = 0

    while i < len(texto):
        letra = texto[i]
        if letra >= "a" and letra <= "z":
            if letra in "aeiou":
                v = v + 1
            else:
                c = c + 1
        i = i + 1

    print("Vocales:", v)
    print("Consonantes:", c)



# =========================================================
# 17. MAYOR Y MENOR HASTA NEGATIVO
# =========================================================
def mayor_menor():
    print("Introduce números (negativo para terminar):")
    n = int(input("Número: "))

    if n < 0:
        print("No hay datos")
        return

    mayor = n
    menor = n

    n = int(input("Número: "))
    while n >= 0:
        if n > mayor:
            mayor = n
        if n < menor:
            menor = n
        n = int(input("Número: "))

    print("Mayor:", mayor)
    print("Menor:", menor)



# =========================================================
# 18. SUMA DE LOS DÍGITOS DE UN NÚMERO
# =========================================================
def suma_digitos():
    n = abs(int(input("Introduce un número: ")))
    suma = 0

    while n > 0:
        suma = suma + (n % 10)
        n = n // 10

    print("Suma de cifras:", suma)



# =========================================================
# 19. CONTAR CUÁNTAS VECES APARECE UNA LETRA
# =========================================================
def contar_letra():
    texto = input("Texto: ")
    letra = input("Letra a buscar: ")

    contador = 0
    i = 0

    while i < len(texto):
        if texto[i] == letra:
            contador = contador + 1
        i = i + 1

    print("Aparece", contador, "veces")



# =========================================================
# 20. REPETIR TEXTO N VECES
# =========================================================
def repetir_texto():
    texto = input("Texto: ")
    n = int(input("Veces: "))
    salida = ""
    i = 0

    while i < n:
        salida = salida + texto
        i = i + 1

    print(salida)
