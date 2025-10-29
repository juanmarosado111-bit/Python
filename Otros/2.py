#Minutos
tiempo_dormido=int(input("Cuantos minutos estas dormido?: "))
tiempo_sentado=int(input("Cuantos minutos estas sentado?: "))


#cal por minutos
dormido=1.08
sentado=1.66


#Cal por minutos
cal_durmiendo=int(tiempo_dormido*dormido)
cal_sentado=int(tiempo_sentado*sentado)


calorias_consumidas=print(f"Has consumido {cal_durmiendo} estando dormido y {cal_sentado} estando sentado")

