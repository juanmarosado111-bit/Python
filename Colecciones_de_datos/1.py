
lista=[1,2,3,4]

# Encontrar el Máximo/Mínimo

def max_min1(lista):
    max1=max(lista)
    min1=min(lista)
    return max1,min1

def max_min2(lista):
    max2=lista[0]
    min2=lista[0]
    for i in lista:
        if i>max2:
            max2=i
        if i<min2:
            min2=i
    return max2, min2

# max1,min1=max_min1(lista)
# max2,min2=max_min2(lista)

# print(f"El max y min segun python es {max1} y {min1}")
# print(f"El max y min segun yo es {max2} y {min2}")



# Contar Frecuencias

def contar_frecuencias(lista, num_a_contar):
    repeticiones=0
    for i in lista:
        if i==num_a_contar:
            repeticiones+=1
    return repeticiones

# num_a_contar=int(input("Introduce el numero que quieras saber si se repite en la lista: "))
# repeticiones=contar_frecuencias(lista)

# print(f"El numero {num_a_contar} se repite {repeticiones} vez/veces")


# Filtrar Pares/Impares

def filtrar_pares_e_impares(lista):
    lista_pares=[]
    lista_impares=[]
    
    for i in lista:
        if i%2==0:
            lista_pares.append(i)
        else:
            lista_impares.append(i)
    return lista_pares, lista_impares

# lista_pares,lista_impares=filtrar_pares_e_impares(lista)

# print(f"Los numeros pares son: {lista_pares}")
# print(f"Los numeros impares son: {lista_impares}")




# Slicing

# elementos = int(input("Cuantos elementos de la lista quieres ver: "))
elementos=3

def slicing(lista, elementos):
    subsecuencia=lista[:elementos]
    return subsecuencia

# subsecuencia=slicing(lista, elementos)
# print(f"La subsecuencia es {subsecuencia}")


def slicing2(lista, elementos):
    subsecuencia=[]
    for i in range(elementos):
        subsecuencia.append(lista[i])
    return subsecuencia

subsecuencia=slicing2(lista, elementos)

print(f"La subsecuencia es {subsecuencia}")