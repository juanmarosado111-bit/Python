h_trabajadas=float(input("Introduce las horas que has trabajado esta semana: "))


#Salario normal=paga=16€ / salario extra=extra=20€
paga=16
extra=20


#Calculos
if h_trabajadas<=40:
    salario=h_trabajadas*paga
else:
    h_extras=h_trabajadas-40
    salario=paga*40+extra*h_extras


#Prints
print(f"Tu salario semanal es {salario}€")

 
