# Este script debe escribir la tabla de multiplicar del número que el usuario teclee. La tabla
# mostrará en diferentes líneas cada producto y el resultado en la forma a x b = ab.

numero=int(input("Introduce un numero: "))

for i in range(11):
    print(f"{numero} x {i} = {numero*i}")