# Rosado Trujillo, Juan Manuel


n=int(input("Introduce un número entero positivo: "))
perfecto=False

def es_perfecto(n):
    global perfecto
    suma=0
    
    for i in range(1,n):
        if n%i==0:
            suma+=i

    if suma==n:
        perfecto=True
    else:
        perfecto=False

es_perfecto(n)

if perfecto:
    print("Es perfecto")
else:
    print("No es perfecto")
    
