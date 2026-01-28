
# Se te da una lista de números desordenados.
# El objetivo es ordenarlos de menor a mayor utilizando el método de la burbuja (bubble sort).

# Este método funciona comparando pares de elementos vecinos y intercambiándolos si están en el orden incorrecto.
# El proceso se repite varias veces hasta que la lista queda completamente ordenada.

lista=[5,3,8,2]
n=len(lista)

for i in range(n-1):  
    for j in range(n-1-i):
        print(j)
        if lista[j]>lista[j+1]:
            temporal=lista[j]
            lista[j]=lista[j+1]
            lista[j+1]=temporal
            
print(lista)
    