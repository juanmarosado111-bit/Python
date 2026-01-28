# Rosado Trujillo, Juan Manuel

num_A=int(input("Introduce el primer numero entero: "))
num_B=int(input("Introduce el segundo numero entero: "))
multiplo=int(input("Introduce el multiplo: "))

def calculadora_multiplos(num_A, num_B, multiplo):
    cadena_multiplos=""
    for i in range(num_A, num_B+1):
        if (i%multiplo)==0:
            if i==num_B:
                cadena_multiplos+=str(i)
            else:
                cadena_multiplos+=str(i)+", "
    return cadena_multiplos



print(calculadora_multiplos(num_A, num_B, multiplo))