# Juan Manuel Rosado Trujillo 2ºA

precio_producto=float(input("Introduce el precio de un producto en €: "))
tipo_producto=input("Introduce el tipo de producto (A, B o C): ")

if tipo_producto=="A" or tipo_producto=="B" or tipo_producto=="C":
    if tipo_producto=="A":
        precio_final=precio_producto
        print(f"El precio final es {precio_final}€")
    elif tipo_producto=="B":
        precio_final=precio_producto-(precio_producto*0.1)
        print(f"El precio final es {precio_final}€")
    else:
        precio_final=precio_producto-(precio_producto*0.2)
        print(f"El precio final es {precio_final}€")
else:
    print("Error: Introduce un tipo de producto valido (A, B o C)")