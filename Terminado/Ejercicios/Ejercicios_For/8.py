# Se quiere tener un contador de dos dígitos en base 5. El funcionamiento es simple: el dígito
# de la derecha irá aumentando y cuando pase de 4 su valor se pondrá a 0 y el dígito de la
# izquierda se incrementa en 1. El contador debe deternerse cuando alcancemos el valor 1:4.
# Usamos el console log para ir imprimiendo los valores de los dígitos, deberá quedar algo así:
# 0:0
# 0:1
# 0:2


# for izquierda in range(5):
#     for derecha in range(5):
#         print(f"{izquierda}:{derecha}")
#     if izquierda==1 and derecha==4:
#         break


izquierda = 0

while izquierda < 5:
    derecha = 0
    while derecha < 5:
        print(f"{izquierda}:{derecha}")
        derecha += 1
    if izquierda == 1 and derecha == 5:
        break
    izquierda += 1

    
i=0
d=0

while i<2:
    d=0
    while d<5:
        print(f"{i}:{d}")
        d+=1
    i+=1
    
    