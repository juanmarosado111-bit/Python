valores = (50000,20000,10000,5000,2000,1000,500,200,100,50,20,10,5,2,1)

dinero = 87
dinero = int(dinero * 100)

for valor in valores:
    if dinero >= valor:
        cantidad = dinero // valor
        dinero = dinero - (cantidad * valor)

        if cantidad > 0:
            if valor >= 500:
                print(f"{cantidad} billetes de {valor//100} €")
            else:
                print(f"{cantidad} monedas de {valor/100} €")
