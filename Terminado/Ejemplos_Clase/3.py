# Si un alumno falta a clase mas del 20% de las horas, pierde la evaluacion continua, y solo se le valora el examen.
# Con la evaluacion continua, el peso del examen el 60%, las practicas evaluables el 30%, y el trabajo en clase el 10%.
# Si la nota total es igual o mayor que 5 aprueba, si no, suspende.


#Tiempo en horas
h_totales=int(input("Introduce las horas totales que tiene el curso: "))
h_asistidas=int(input("Introduce las horas totales que has asistido: "))


#Inputs con la media de las notas
n_examen=float(input("Introduce la media de tus examenes: "))
n_practicas=float(input("Introduce la media de tus practicas: "))
n_trabajo=float(input("Introduce la media de tus trabajos: "))


#Calculo de tiempo en horas
h_faltas_max=h_totales*0.2
h_faltas_totales=h_totales-h_asistidas


#Comprobar si tiene evaluacion continua
if h_faltas_totales<h_faltas_max:
    eval_continua=True
else:
    eval_continua=False


#Calculo de nota final    
if eval_continua:
    n_final=n_examen*0.6+n_practicas*0.3+n_trabajo*0.1
else:
    n_final=n_examen
    

#Calculo de si aprueba o no
estado="apruebas" if n_final>=5 else "suspendes"


#Print
print(f"Tu media es {n_final}, {estado}")