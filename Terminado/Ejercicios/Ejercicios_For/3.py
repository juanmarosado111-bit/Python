# Se quiere un bucle que genere una lista con todos los números pares positivos por debajo
# del número tecleado por el usuario. Los números se aparecerán en una ventana alert con
# cambios de linea (carácter '\n').Si tecleo el número el número 9 deberá mostrar cinco lineas
# con los números 0 2 4 6 8

numero=int(input("Introduce un numero: "))

for i in range(numero+1):
    if i%2==0:
        print(i)
