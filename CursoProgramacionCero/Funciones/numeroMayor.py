def mayor(a,b):
    if a > b:
        return a
    else:
        return b
    
num1 = 80
num2 = 10
num3 = 11
num4 = 2

numeroMayor1 = mayor(num1,num2)
numeroMayor2 =mayor (num3, num4)
numeroMayor = mayor(numeroMayor1, numeroMayor2)

print(f"El número mayor es: {numeroMayor}")