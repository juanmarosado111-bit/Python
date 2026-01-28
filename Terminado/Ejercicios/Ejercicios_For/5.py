# Recuerda que el salto de linea es el carácter "\n" Si el usuario teclea el 4 la tabla
# mostrará diez líneas en la forma
# 4 x 1 = 4
# 4 x 2 = 8

numero=int(input("Introduce un número: "))

for i in range(0,11):
    print(f"{numero} x {i} = {numero*i}")

