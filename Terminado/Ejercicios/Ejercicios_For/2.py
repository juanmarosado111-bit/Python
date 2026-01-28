# Se trata de que dado un número entero el script muestre una cuenta atrás, es decir, una
# lista de numeros separados por comas desde el número tecleado hasta el 0.Si teclea el
# número 5 deberá mostarar 5,4,3,2,1.

numero=int(input("Introduce un numero: "))

for num in range(numero, -1, -1):
    if num!=0:
        print(num, end=", ")
    else:
        print(num)
    
