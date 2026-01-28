# Un script que preguntará al usuario si desea continuar con el programa. Si el usuario
# pulsa una letra n (mayúscula o minúscula), el programa finalizará. Cualquier otra
# entrada repetirá la pregunta. El usuario teclea Si, como no es la letra s pues
# dirá Error, ¿Desa seguir con el programa?

import os
os.system("cls")


try:
    respuesta=input("Quieres continuar con la ejecucion del programa? (s o n): ")

    while respuesta!="n" and respuesta!="N" and respuesta!="s" and respuesta!="S":
        print("Error, escribe s o n")
        respuesta=input("Quieres continuar con la ejecucion del programa? (s o n): ")

    if respuesta=="s" or respuesta=="S":
        print("El programa continua ejecutandose")
    else:
        print("El programa ha finalizado")
        
        
except Exception as ex:
    print(f"Ha ocurrido un error, {ex}")
