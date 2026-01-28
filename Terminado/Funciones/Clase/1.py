# Realiza el control de acceso a una caja fuerte. La combinación será un número de 4 cifras.
# El programa nos pedirá la combinación para abrirla. Si no acertamos, se nos mostrará el mensaje "Lo siento, esa no es la combinación"
# y si acertamos se nos dirá "La caja fuerte se ha abierto satisfactoriamente" tendremos 4 oportunidades para abrir la caja fuerte


def abrir_caja():
    combinacion_real=1103
    combinacion_usuario=int(input("Introduce la combinacion de la caja fuerte (4 digitos): "))
    contador=1
    while combinacion_real!=combinacion_usuario:
        if contador==4:
            print("Has acabado las oportunidades")
            break
        else:
            print("Lo siento, esa no es la combinación")
            combinacion_usuario=int(input("Introduce la combinacion de la caja fuerte (4 digitos): "))
            contador+=1
    else:
       print("La caja fuerte se ha abierto satisfactoriamente") 

abrir_caja()

