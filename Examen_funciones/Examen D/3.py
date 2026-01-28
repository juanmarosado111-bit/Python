# Rosado Trujillo, Juan Manuel

fila=int(input("Introduce el numero de filas: "))

def imprimir_piramide_inversa(fila):
    for i in range(fila,0,-1):
        for j in range(1,i+1):
            print(i, end="")
        print()
            
imprimir_piramide_inversa(fila)

