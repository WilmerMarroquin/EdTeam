def cajero():
    # Definir variables
    saldo = 1000
    # Ciclo para realizar las opciones del cajero
    while True:
        opcion = input("¿Qué desea hacer? \n1. Consignar \n2. Retirar \n3. Salir \n")
        if opcion == "3":
            print("Gracias por su visita.")
            break
        # Ejecutar la acción correspondiente
        if opcion == "1":
            valor = int(input("Digite el valor a consignar: "))
            saldo += valor
            print(f"Acción realizada con éxito, Saldo {saldo}")
        elif opcion == "2":
            valor = int(input("Digite el valor a retirar: "))
            if valor <= saldo:
                saldo -= valor
                print(f"Acción realizada con éxito, Saldo {saldo}")
            else:
                print("No hay suficiente saldo para retirar.")
        else:
            print("Opción inválida.")

# Llamar a la función
cajero()