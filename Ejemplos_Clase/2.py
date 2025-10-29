# Si un alumno falta a clase mas del 20% de las horas, pierde la evaluacion continua, y solo se le valora el examen.
# Con la evaluacion continua, el peso del examen el 60%, las practicas evaluables el 30%, y el trabajo en clase el 10%.
# Si la nota total es igual o mayor que 5 aprueba, si no, suspende.

#Inputs
horas_totales=int(input("Introduce las horas totales del curso: "))
horas_asistencia=int(input("Introduce las horas que has asistido a clase: "))

n_examen=float(input("Introduce media de tus examenes: "))
n_practicas=float(input("Introduce media de tus practicas: "))
n_trabajo=float(input("Introduce media de tu trabajo en clase: "))

#Calculos
max_faltas=horas_totales*0.2
faltas_totales=horas_totales-horas_asistencia


if faltas_totales<max_faltas:
    evaluacion_continua=True
else:
    evaluacion_continua=False

    
if evaluacion_continua:
    n_final=n_examen*0.6+n_practicas*0.3+n_trabajo*0.1
else:
    n_final=n_examen


estado="apruebas" if n_final>=5 else "suspendes"


print(f"Tu nota final es {n_final}, {estado}")
    

