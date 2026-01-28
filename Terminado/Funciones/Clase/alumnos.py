n_de_alumnos=int(input("Introduce el numero de alumnos: "))
alumno=None
aprobado=0
suspenso=0
suma_medias=0
contador=0

def calcular_media(nota1, nota2, nota3):
    media=(nota1+nota2+nota3)/3
    return media

def calcula_global(media_alumno):
    global suma_medias
    suma_medias += media_alumno

def aprobados(media_alumno):
    global suspenso, aprobado
    if media_alumno>=5:
        aprobado+=1
    else:
        suspenso+=1

bandera=True
while contador<n_de_alumnos:
    alumno=(input("Introduce el nombre del alumno, fin para salir: "))
    if alumno=="fin":
        break
    nota1=int(input("Introduce la nota del primer modulo: "))
    nota2=int(input("Introduce la nota del primer modulo: "))
    nota3=int(input("Introduce la nota del primer modulo: "))
    
    media_alumno=calcular_media(nota1,nota2,nota3)
    calcula_global(media_alumno)
    aprobados_y_suspensos=aprobados(media_alumno)
    contador+=1

if contador > 0:
    media_clase = suma_medias / contador
else:
    media_clase = 0

print(f"Se han introducido {contador} alumnos")
print(f"Alumnos aprobados: {aprobado}")
print(f"Alumnos suspensos: {suspenso}")
print(f"El promedio de la clase es {media_clase}")

