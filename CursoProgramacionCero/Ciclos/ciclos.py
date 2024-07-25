""" for tabla in range(1, 13):
    for num in range(1, 13):
        resultado = f"{tabla} * {num} = {tabla*num}"
        print(resultado)
    print("_____________________")  """

""" for par in range(1,13):
    if par %2 == 0:
        print (str(par) + " es par")
    else:
        print (str(par) + " es impar") """

""" edad = 0
while edad < 18:
    print(f"Hola, tienes {edad} años, aun eres menor")
    edad += 1
print(f"Hola, tienes {edad} años, ya eres mayor.")   """  

linea = "";
for casilla in range(1,9):
    for fila in range(1,9):
        if (casilla + fila) % 2 == 0:
            linea += "◻️ "
        else:
            linea += "⬛"
    linea += "\n"

print(linea)