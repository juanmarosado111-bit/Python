# -------------------------------
# EJERCICIO 1: Caja fuerte
# -------------------------------
def caja_fuerte():
    combinacion = "1234"
    intentos = int(input("¿Cuántos intentos quieres tener? "))

    i = 0
    while i < intentos:
        codigo = input("Introduce la combinación: ")

        if codigo == combinacion:
            print("La caja fuerte se ha abierto satisfactoriamente")
            return
        else:
            print("Lo siento, esa no es la combinación")

        i = i + 1

    print("Has agotado los intentos")


# -------------------------------
# EJERCICIO 2: Pirámide de números (while)
# -------------------------------
def piramide():
    n = int(input("Introduce un número para la altura de la pirámide: "))

    fila = 1
    while fila <= n:
        # Imprimir espacios
        espacios = n - fila
        linea = ""
        e = 0
        while e < espacios:
            linea = linea + " "
            e = e + 1

        # Parte ascendente
        num = 1
        while num <= fila:
            linea = linea + str(num)
            num = num + 1

        # Parte descendente
        num = fila - 1
        while num >= 1:
            linea = linea + str(num)
            num = num - 1

        print(linea)
        fila = fila + 1


# -------------------------------
# EJERCICIO 2 (alternativa con for)
# -------------------------------
def piramide_numeros():
    n = int(input("Introduce el número de filas: "))

    for i in range(1, n + 1):
        # Espacios iniciales
        print(" " * (n - i), end="")

        # Parte ascendente
        for a in range(1, i + 1):
            print(a, end="")

        # Parte descendente
        for a in range(i - 1, 0, -1):
            print(a, end="")

        print()


# -------------------------------
# EJERCICIO 3: Pedir números y calcular datos
# -------------------------------
def datos_numeros():
    contador = 0
    suma_impares = 0
    cantidad_impares = 0
    mayor_par = None

    numero = int(input("Introduce un número (negativo para terminar): "))

    while numero >= 0:
        contador += 1

        if numero % 2 == 0:  # PAR
            if mayor_par is None or numero > mayor_par:
                mayor_par = numero
        else:  # IMPAR
            suma_impares += numero
            cantidad_impares += 1

        numero = int(input("Introduce otro número (negativo para terminar): "))

    print("Se han introducido", contador, "números")

    if cantidad_impares > 0:
        media_impares = suma_impares / cantidad_impares
        print("La media de los impares es:", media_impares)
    else:
        print("No se introdujeron números impares")

    if mayor_par is not None:
        print("El mayor de los pares es:", mayor_par)
    else:
        print("No se introdujeron números pares")


# -------------------------------
# MENÚ PRINCIPAL
# -------------------------------
def menu():
    opcion = ""

    while opcion != "4":
        print("\n--- MENÚ ---")
        print("1. Control de acceso a caja fuerte")
        print("2. Pirámide de números")
        print("3. Estadísticas de números")
        print("4. Salir")

        opcion = input("Elige una opción: ")

        if opcion == "1":
            caja_fuerte()
        elif opcion == "2":
            piramide()
        elif opcion == "3":
            datos_numeros()
        elif opcion == "4":
            print("Saliendo del programa...")
        else:
            print("Opción no válida")

# Ejecutar menú
menu()






# ---------------------------------------------------------------------------------------------------------------------------------------------------------
# EXPLICACIONES
# ---------------------------------------------------------------------------------------------------------------------------------------------------------

# Programa con 3 ejercicios y menú para seleccionar cada uno.
# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Estructura general:
# - Definimos 3 funciones independientes (cada ejercicio).
# - Definimos una función menu() que permite elegir qué ejecutar.
# - Finalmente llamamos a menu() para iniciar el programa.
#
# Comentarios importantes:
# - No usamos listas ni operaciones avanzadas, solo variables, bucles,
#   condicionales y entrada/salida (tal y como pediste).
# - Evitamos while True y usamos condiciones claras en los bucles.
# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# EJERCICIO 1: Caja fuerte
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def caja_fuerte():
    """
    Control de acceso a una caja fuerte.
    - La combinación correcta está guardada en la variable 'combinacion'.
    - Se pregunta cuántos intentos quiere el usuario.
    - Se pide la combinación ese número de veces o hasta acertar.
    """
    # Combinación correcta (cadena de 4 caracteres).
    # En un examen esto puede ser fija o pedida por el docente.
    combinacion = "1234"

    # Pedimos al usuario cuántos intentos quiere. Convertimos a int.
    # Si el usuario introduce algo no-numérico lanzará ValueError,
    # pero en clase no hemos visto manejo avanzado, así que se asume entrada correcta.
    intentos = int(input("¿Cuántos intentos quieres tener? "))

    # i será el contador de intentos usados
    i = 0
    # Bucle que se repite mientras queden intentos (i < intentos)
    while i < intentos:
        # Pedimos la combinación al usuario. La tratamos como cadena.
        codigo = input("Introduce la combinación: ")

        # Comparamos la cadena introducida con la combinación correcta
        if codigo == combinacion:
            # Si coincide, abrimos la caja y salimos de la función con return.
            print("La caja fuerte se ha abierto satisfactoriamente")
            return
        else:
            # Si no coincide, avisamos y el bucle continuará para otro intento.
            print("Lo siento, esa no es la combinación")

        # Incrementamos el contador de intentos
        i = i + 1

    # Si se sale del while sin haber hecho return, significa que se agotaron los intentos
    print("Has agotado los intentos")


# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# EJERCICIO 2: Pirámide de números
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def piramide():
    """
    Imprime una pirámide de números con n filas, por ejemplo para n=4:
       1
      121
     12321
    1234321
    - No se usan listas: las líneas se construyen con concatenación de cadenas.
    - Usamos bucles while anidados para espacios, ascenso y descenso.
    """
    # Pedimos la altura de la pirámide
    n = int(input("Introduce un número para la altura de la pirámide: "))

    # fila indica la fila actual que vamos a imprimir (empieza en 1)
    fila = 1
    # Mientras fila sea <= n imprimimos cada fila
    while fila <= n:
        # Calculamos cuántos espacios antes del primer número:
        espacios = n - fila

        # Construimos la línea en la variable 'linea' empezando vacía
        linea = ""

        # 1) Imprimir los espacios iniciales
        e = 0
        while e < espacios:
            linea = linea + " "  # añadimos un espacio
            e = e + 1

        # 2) Parte ascendente: números desde 1 hasta 'fila' (inclusive)
        num = 1
        while num <= fila:
            linea = linea + str(num)  # convertimos el número a cadena y lo añadimos
            num = num + 1

        # 3) Parte descendente: números desde fila-1 hasta 1
        num = fila - 1
        while num >= 1:
            linea = linea + str(num)
            num = num - 1

        # Imprimimos la línea completa para la fila actual
        print(linea)

        # Pasamos a la siguiente fila
        fila = fila + 1

# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# EJERCICIO 2: Pirámide de números -> Otra manera de hacerlo
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def piramide_numeros():
    # Pedimos al usuario cuántas filas tendrá la pirámide
    n = int(input("Introduce el número de filas: "))

    # Recorremos cada fila desde 1 hasta n
    for i in range(1, n + 1):

        # 1) Imprimir los espacios que van antes de los números
        espacios = n - i
        j = 0
        while j < espacios:
            print(" ", end="")  # imprimimos un espacio
            j = j + 1

        # 2) Parte ascendente: imprime 1, 2, 3, ..., i
        a = 1
        while a <= i:
            print(a, end="")
            a = a + 1

        # 3) Parte descendente: imprime i-1, i-2, ..., 1
        a = i - 1
        while a >= 1:
            print(a, end="")
            a = a - 1

        # 4) Salto de línea para pasar a la siguiente fila
        print()



# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# EJERCICIO 3: Pedir números y calcular datos
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def datos_numeros():
    """
    Va pidiendo números hasta que se introduce uno negativo.
    - Cuenta cuántos números se han introducido (sin contar el negativo).
    - Calcula la media de los impares (si hay alguno).
    - Calcula el mayor de los pares (si hay alguno).
    """
    # Inicializaciones
    contador = 0            # cuenta total de números introducidos (>=0)
    suma_impares = 0       # suma acumulada de los impares (para calcular media)
    cantidad_impares = 0   # contador de números impares
    mayor_par = None       # guardará el mayor número par (None si no hay pares)

    # Pedimos el primer número (si es negativo, el bucle no se ejecuta)
    numero = int(input("Introduce un número (negativo para terminar): "))

    # Mientras el número sea >= 0 seguimos procesando
    while numero >= 0:
        contador = contador + 1  # aumentamos el total introducido

        if numero % 2 == 0:  # si el resto al dividir entre 2 es 0 -> par
            # Actualizamos mayor_par: si era None o el número actual es mayor, lo reemplazamos.
            if mayor_par is None or numero > mayor_par:
                mayor_par = numero
        else:
            # Si es impar, lo añadimos a la suma de impares y contamos uno más
            suma_impares = suma_impares + numero
            cantidad_impares = cantidad_impares + 1

        # Pedimos el siguiente número (se repetirá el ciclo hasta introducir negativo)
        numero = int(input("Introduce otro número (negativo para terminar): "))

    # Tras salir del bucle, mostramos los resultados

    print("Se han introducido", contador, "números")

    # Media de impares: solo si se introdujo al menos uno
    if cantidad_impares > 0:
        media_impares = suma_impares / cantidad_impares
        print("La media de los impares es:", media_impares)
    else:
        print("No se introdujeron números impares")

    # Mayor de los pares: solo si mayor_par no es None
    if mayor_par is not None:
        print("El mayor de los pares es:", mayor_par)
    else:
        print("No se introdujeron números pares")


# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# MENÚ PRINCIPAL
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def menu():
    """
    Menú para seleccionar cuál de los ejercicios ejecutar.
    - Muestra las opciones.
    - Lee la opción elegida como cadena y llama a la función correspondiente.
    - La opción "4" cierra el programa.
    """
    opcion = ""  # variable para guardar la opción elegida por el usuario

    # Repetimos hasta que el usuario elija "4" (salir)
    while opcion != "4":
        # Mostramos las opciones disponibles
        print("\n--- MENÚ ---")
        print("1. Control de acceso a caja fuerte")
        print("2. Pirámide de números")
        print("3. Estadísticas de números")
        print("4. Salir")

        # Leemos la opción elegida (como cadena)
        opcion = input("Elige una opción: ")

        # Lógica para ejecutar la función según la opción
        if opcion == "1":
            # Ejecutamos el ejercicio 1
            caja_fuerte()
        elif opcion == "2":
            # Ejecutamos el ejercicio 2
            piramide()
        elif opcion == "3":
            # Ejecutamos el ejercicio 3
            datos_numeros()
        elif opcion == "4":
            # Mensaje de despedida y el while terminará
            print("Saliendo del programa...")
        else:
            # Si la opción no es válida, avisamos y volvemos a mostrar el menú
            print("Opción no válida")


# Llamada principal para iniciar el programa
menu()
