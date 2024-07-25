# Algoritmo de año bisiesto
año = 0

print ("Por favor ingresa un año");

año = int(input())

if (año % 4 == 0 and año % 100 != 0) or año % 400 == 0:
    print (f"{año} es un año bisiesto")
else:
    print (f"{año} no es un año bisiesto")