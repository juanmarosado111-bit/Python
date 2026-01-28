# Juan Manuel Rosado Trujillo 2ºA

num1=float(input("Introduce el primer numero: "))
num2=float(input("Introduce el segundo numero: "))

if num1>num2:
    print(f"El primer numero es mayor que el segundo, {num1}>{num2}")
elif num1<num2:
    print(f"El primer numero es menor que el segundo, {num1}<{num2}")
else:
    print(f"El primer numero es igual al segundo. {num1}={num2}")