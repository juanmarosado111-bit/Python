#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# 1. Función que devuelva el mayor de dos números
# Enunciado:

# Escribe una función mayor(a, b) que devuelva el número mayor.

# ✔ Solución:
def mayor(a, b):
    if a > b:
        return a
    else:
        return b

# Ejemplo:
x = int(input("Primer número: "))
y = int(input("Segundo número: "))
print("El mayor es:", mayor(x, y))

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# 2. Función que determine si un número es par
# Enunciado:

# Crear una función es_par(n) que devuelva True si el número es par.

# ✔ Solución:
def es_par(n):
    if n % 2 == 0:
        return True
    else:
        return False

n = int(input("Número: "))
print(es_par(n))

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# 3. Función que calcule el área de un triángulo
# Enunciado:

# Pedir base y altura, y usar una función.

# ✔ Solución:
def area_triangulo(base, altura):
    return (base * altura) / 2

b = float(input("Base: "))
h = float(input("Altura: "))
print("Área:", area_triangulo(b, h))

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# 4. Función que repita un mensaje n veces

# (Sin usar listas ni multiplicación de cadenas)

# ✔ Solución:
def repetir(mensaje, veces):
    resultado = ""
    contador = 0
    while contador < veces:
        resultado = resultado + mensaje
        contador = contador + 1
    return resultado

print(repetir("Hola ", 3))

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# 5. Función que valide si un número es positivo, negativo o cero
# ✔ Solución:
def tipo_numero(n):
    if n > 0:
        return "Positivo"
    elif n < 0:
        return "Negativo"
    else:
        return "Cero"

n = int(input("Número: "))
print(tipo_numero(n))

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# 6. Función que calcule el factorial

# (sin listas, usando un bucle normal)
# El factorial de n es: 1×2×3×…×n.

# ✔ Solución:
def factorial(n):
    resultado = 1
    i = 1
    while i <= n:
        resultado = resultado * i
        i = i + 1
    return resultado

n = int(input("Número: "))
print("Factorial:", factorial(n))

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# 7. Función para sumar los números desde 1 hasta n

# Típico en exámenes.

# ✔ Solución:
def suma_hasta(n):
    total = 0
    i = 1
    while i <= n:
        total = total + i
        i = i + 1
    return total

n = int(input("Número: "))
print("Suma:", suma_hasta(n))

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# 8. Función que verifique una contraseña sencilla

# (sin listas, solo comparaciones)

# ✔ Solución:
def comprobar(password):
    if password == "python123":
        return True
    else:
        return False

pw = input("Introduce contraseña: ")
print(comprobar(pw))

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# 9. Función que convierta grados Celsius a Fahrenheit
# ✔ Solución:
def celsius_a_fahrenheit(c):
    return c * 9/5 + 32

c = float(input("Celsius: "))
print("Fahrenheit:", celsius_a_fahrenheit(c))

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# 10. Función que maneje una excepción simple (división segura)
# ✔ Solución:
def division_segura(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Error: No se puede dividir por cero"

x = float(input("Numerador: "))
y = float(input("Denominador: "))
print(division_segura(x, y))