# Escribir un script que pida al usuario una contraseña. Si coincide con la clave definida
# en el script le devolverá el mensaje "Acceso concedido" y si no coincide le devolverá
# el mensaje "Acceso Denegado”. Si falla tres veces se emitirá el mensaje "Alerta,
# intruso" La contraseña es por ejemplo pasar. Tecleo tres veces otra distinta: Acceso
# Intruso.

import os
os.system("cls")

contraseña_real="123456"
contraseña_usuario=input("Introduce la contraseña: ")
intento=1

try:
    while contraseña_real!=contraseña_usuario:
        intento+=1
        print("Acceso denegado")
        contraseña_usuario=input("Introduce la contraseña: ")
        if intento==3:
            print("Alerta, intruso")
            break
    else:
        print("Acceso concedido")
        
except Exception as ex:
    print(f"Ha ocurrido un error, {ex}")

