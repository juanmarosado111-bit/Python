# El programa pide al usuario que le diga de cuantos numeros va a hacer la numeros_media
# Este teclea un numero y se le empiezan a pedir esos numeros.
# Si dice cuatro y escribe 5,9,10,12. El programa dira "La media es 9"

import os
os.system("cls")


try:
    numeros_media=float(input("Introduce de cuantos numeros quieres hacer la media: "))
    suma=0

    for _ in range(numeros_media):
        numero=float(input("Introduce un numero: "))
        suma+=numero

    print(f"La media es {suma/numeros_media}")
    
    
except Exception as ex:
    print(f"Ha ocurrido una excepcion, {ex}")
    
    
finally:
    print("El programa a finalizado")
    
    
    