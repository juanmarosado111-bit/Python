try:
    #Kilogramos
    peso=float(input("Introduce tu peso en kg: "))


    #Minutos
    t_dormido=float(input("Introduce los minutos que has estado dormido: "))
    t_sentado=float(input("Introduce los minutos que has estado sentado: "))
    t_andando=float(input("Introduce los minutos que has estado andando: "))
    t_corriendo=float(input("Introduce los minutos que has estado corriendo: "))


    #cal por minuto
    c_dormido=1.08
    c_sentado=1.66
    c_andar=6.17
    c_correr=17.05


    #cal por minuto
    total_consumido_dormido=int(t_dormido*c_dormido*peso)
    total_consumido_sentado=int(t_sentado*c_sentado*peso)
    total_consumido_andando=int(t_andando*c_andar*peso)
    total_consumido_corriendo=int(t_corriendo*c_correr*peso)


    print(f"Has consumido {total_consumido_sentado} calorias estando sentado")
    print(f"Has consumido {total_consumido_dormido} calorias estando dormido")
    print(f"Has consumido {total_consumido_andando} calorias estando andando")
    print(f"Has consumido {total_consumido_corriendo} calorias estando corriendo")
    print("")
    print(f"En total has consumido {int(total_consumido_dormido+total_consumido_sentado+total_consumido_andando+total_consumido_corriendo)} calorias")

except ValueError:
    print("Introduce un tipo de dato valido")
except Exception as ex:
    print(f"Ha ocurrido una excepcion, {ex}")
    
    
finally:
    print("La ejecucion del programa ha finalizado")
