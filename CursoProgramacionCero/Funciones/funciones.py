# Funciones

def saludar():
    print("Hola, ¿cómo estás?")

def saludarParametros(nombre, edad):
    print("Hola, mi nombre es " + nombre + ", y tengo " + edad + " años")  

def sumar(a, b):
    return a + b

def concatenar(a, b):
    return a + " " + b

# Llamadas a las funciones

saludar()

saludarParametros("Wilmer", "28")

num1 = 5
num2 = 10

print(f"La suma de {num1} y {num2} es: {sumar(num1, num2)}")

nombre1 = "Wilmer"

apellido1 = "Marroquin"

nombre_completo = concatenar(nombre1, apellido1)

print(f"Mi nombre completo es: {nombre_completo}")
