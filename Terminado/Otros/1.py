not1=int(input("Introduce la 1º nota (sobre 100): "))
not2=int(input("Introduce la 2º nota (sobre 100): "))
not3=int(input("Introduce la 3º nota (sobre 100): "))
    
promedio=round(((not1+not2+not3)/3),2)

if promedio>=70:
    print(f"Apruebas, tu media es {promedio}")
else:
    print(f"Suspendes, tu media es {promedio}")

