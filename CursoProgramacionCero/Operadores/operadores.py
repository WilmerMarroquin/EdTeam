# Tipo de operadores
# 1. Aritméticos: suma (+), resta (-), multiplicación (*), división (/), módulo (%), exponente (**)
# 2. Relacionales: igual (==), distinto (!=), mayor (>), menor (<), mayor igual (>=), menor igual (<=)
# 3. Lógicos: AND (and), OR (or), NOT (not)
# 4. Unarios: negativo (-), incremento (++), decremento (--)
# 1. Operadores aritméticos
num1 = 10
num2 = 5
print("")
print(f"Operaciones aritméticas con los números {num1} y {num2}")
print("Suma:", num1 + num2)  # Suma
print("Resta:", num1 - num2)  # Resta
print("Multiplicación:", num1 * num2)  # Multiplicación
print("División:", num1 / num2)  # División
print("Módulo:", num1 % num2)  # Módulo
print("Exponente:", num1 ** num2)  # Exponente

# 2. Operadores relacionales
print("")
print(f"Operaciones relacionales con los números {num1} y {num2}")
print(f"{num1} es igual a {num2}? ➡️", num1 == num2)  # Igualdad (comparando valores)
print(f"{num1} es diferente a {num2}? ➡️", num1 != num2)  # Diferente (comparando valores)
print(f"{num1} es mayor a {num2}? ➡️", num1 > num2)  # Mayor (comparando valores)
print(f"{num1} es menor a {num2}? ➡️", num1 < num2)  # Menor (comparando valores)
print(f"{num1} es mayor o igual a {num2}? ➡️", num1 >= num2)  # Mayor igual (comparando valores)
print(f"{num1} es menor o igual a {num2}? ➡️", num1 <= num2)  # Menor igual (comparando valores)

# 3. Operadores Lógicos
mayor = True
femenino = True
print("")
print("Operaciones lógicas:")
print(mayor and femenino)  # AND (evalúa ambos operandos)
print(not mayor)  # NOT (negación)
print(mayor or femenino)  # OR (evalúa al menos uno de los operandos)

# 4. Operadores Unarios
num = 7
print("")
print(f"Operaciones unitarias con el número {num}")
print("negativo de", num, ":", -num)  # Negativo (operador unario)
print("Aumento de una unidad a", num, ":", num + 1)  # Incremento (operador unario)
print("Decremento de una unidad a", num, ":", num - 1)  # Decremento (operador unario)