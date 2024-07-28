# Listas
canciones = ["Los mandados", "Yo quiero ser tu marido", "La ley del monte", "Que chulada de mujer"]

print(canciones)  # Imprimir la lista de canciones
print(len(canciones))  # Imprimir el tamaño de la lista

tamañoLista = len(canciones)
print("El tamaño de la lista es: " + str(tamañoLista))

# Acceder a un elemento específico de la lista
print(canciones[0])  # Imprimir la primera canción
print(canciones[tamañoLista - 1])  # Imprimir la última canción

# Añadir un elemento a la lista
canciones.append("Esta es una canción nueva")  # Añadir al final de la lista
print(canciones)
canciones.insert(0, "Esta es otra canción nueva")  # Añadir al principio de la lista
print(canciones)

# Modificar un elemento de la lista
canciones[0] = "Me gustas mucho"  # Modificar el segundo elemento
print(canciones)
canciones[-1] = "Aunque me duela el alma"
print(canciones)

# Eliminar un elemento de la lista
canciones.pop(0)
print(canciones)
canciones.pop()
print(canciones)

# Recorrer la lista
print("Recorrer la lista con un bucle for:")
for cancion in canciones:
    print("- ", cancion)
print("Recorrer la lista con un bucle while:")
indice = 0

while indice < len(canciones):
    print("- ", canciones[indice])
    indice += 1

print("Recorrer la lista con un bucle forEach:")
for cancion in canciones:
    print("- ", cancion)