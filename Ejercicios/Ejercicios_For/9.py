# Se trata de dibujar un triángulo rectángulo con asteriscos. El usuario tecleará un valor
# entero, el programa escribirá con asteriscos tantas lineas como diga ese número. Cada linea
# estará formada por una serie de astericos tan larga como diga el número de línea en el que
# está. Para separar una linea de la siguiente en console o en alert debes usar "\n". Si
# tecleamos el valor 5. El resultado será:
# *
# **
# ***
# ****
# *****


numero=int(input("Introduce un numerero entero: "))
caracter="*"
"""
for i in range(0,numero):
    for j in range(0,i+1):
        print(caracter, end="")
    print("") """
    
i=0   
while i <=numero:
    j=0
    while j<i+1:
        print(caracter, end="")
        j+=1
    print("")
    i+=1
        