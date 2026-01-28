# Rosado Trujillo, Juan Manuel

num1=int(input("Introduce un numero entero: "))
num2=int(input("Introduce otro numero entero: "))

def ejercicio1(num1,num2):
    pares=""
    inicio=max(num1, num2)
    fin=min(num1,num2)
    
    for i in range(inicio, fin-1, -1):
        if i%2==0:
            if pares!="":
                pares+=", "
            pares+=str(i)
    return pares

resultado=ejercicio1(num1, num2)
print(f"Los numeros pares en orden descendente son: \n{resultado}")
