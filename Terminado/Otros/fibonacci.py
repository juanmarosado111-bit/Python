import os
os.system("cls")

num1=0
num2=1
resultado=num1+num2

print(num1)
print(num2)

while resultado<=100:
    print(f"{num1} + {num2} = {resultado}")
    num1=num2
    num2=resultado
    resultado=num1+num2


