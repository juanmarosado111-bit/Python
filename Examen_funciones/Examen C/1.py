# Rosado Trujillo, Juan Manuel

conteo_de_pares=0
conteo_de_impares=0

inicio=int(input("Introduce el numero de inicio: "))
fin=int(input("Introduce el numero de fin: "))


def contar_paridad(inicio, fin):
    global conteo_de_pares, conteo_de_impares
    limite_inferior=min(inicio, fin)
    limite_superior=max(inicio, fin)
    
    for i in range(limite_inferior, limite_superior+1):
        if i%2==0:
            conteo_de_pares+=1
        else:
            conteo_de_impares+=1


contar_paridad(inicio, fin)

print(f"En ese rango hay {conteo_de_pares} numeros pares y {conteo_de_impares} numeros impares.")
