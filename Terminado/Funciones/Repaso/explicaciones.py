# -----------------------------------------
# APUNTES DE PYTHON - FUNCIONES Y BUCLES
# -----------------------------------------

# Una función es un bloque de código reutilizable.
# Se define con 'def' y se puede llamar múltiples veces.
# Puede usar 'return' para devolver un valor o finalizar su ejecución.

# Sintaxis:
# def nombre_funcion(parámetros):
#     # código
#     return valor

# -----------------------------------------
# ENTRADA DE DATOS
# -----------------------------------------
# input() siempre devuelve texto (str).
# Si necesitas un número, debes convertirlo con int() o float().
# Ejemplo:
# n = int(input("Introduce un número: "))

# -----------------------------------------
# CONDICIONALES
# -----------------------------------------
# if, elif, else permiten ejecutar código según condiciones.
# Operadores:
# == igual, != distinto, < menor, > mayor, % resto.

# Ejemplo:
# if numero % 2 == 0:
#     print("Es par")
# else:
#     print("Es impar")

# -----------------------------------------
# BUCLE WHILE
# -----------------------------------------
# Repite mientras la condición sea verdadera.
# Se usa cuando NO sabemos cuántas veces se repetirá.

# Ejemplo:
# i = 0
# while i < 5:
#     print(i)
#     i += 1

# -----------------------------------------
# BUCLE FOR
# -----------------------------------------
# Recorre un rango conocido de valores.
# Muy útil cuando sabemos cuántas veces repetir algo.

# Ejemplo:
# for i in range(1, 6):
#     print(i)

# -----------------------------------------
# CONTADORES Y ACUMULADORES
# -----------------------------------------
# contador = contador + 1     → para contar elementos
# suma = suma + valor         → para sumar datos

# -----------------------------------------
# NÚMEROS PARES E IMPARES
# -----------------------------------------
# Usamos el operador %:
# numero % 2 == 0 → es par
# numero % 2 != 0 → es impar

# -----------------------------------------
# NONE
# -----------------------------------------
# None representa "sin valor".
# Útil para inicializar el mayor o menor número.

# Ejemplo:
# mayor = None
# if mayor is None or numero > mayor:
#     mayor = numero

# -----------------------------------------
# BUCLES ANIDADOS
# -----------------------------------------
# Un bucle dentro de otro (muy usado en pirámides).

# Ejemplo de dos niveles:
# for fila in range(5):
#     for col in range(3):
#         print("*", end="")
#     print()

# -----------------------------------------
# MENÚS
# -----------------------------------------
# Se usa un while para mostrar opciones hasta que el usuario elige "Salir".

# Ejemplo:
# opcion = ""
# while opcion != "3":
#     print("1. Opción A")
#     print("2. Opción B")
#     print("3. Salir")
#     opcion = input("Elige: ")
