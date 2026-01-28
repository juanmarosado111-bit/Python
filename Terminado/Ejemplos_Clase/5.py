try:
    num1=int(input("Introduce un numero: "))
    num2=int(input("Introduce otro numero: "))
    operacion=input("Introduce la operacion a realizar (+,-,/ o *): ")
    
    if operacion=="+":
        resultado=num1+num2
    elif operacion=="-":
        resultado=num1-num2
    elif operacion=="/":
        resultado=num1/num2
    elif operacion=="*":
        resultado=num1*num2
        
    print(f"El resultado de la operacion es: {resultado}")

except ZeroDivisionError:
    print("No se puede dividir entre 0")
except Exception as ex:
    print(f"Ha ocurrido una excepcion del tipo {ex}")
    
finally:
    print("La ejecucion del codigo a terminado")