saldo = 1000

def consignar(valor):
    global saldo  # Acceso global al saldo desde fuera de la función
    if valor < 10:
        print("El valor debe ser mayor a 10.")
        return False
    saldo += valor
    return True

def retirar(valor):
    global saldo  # Acceso global al saldo desde fuera de la función
    if saldo >= valor:
        saldo -= valor
        return True
    else:
        return False
    

def realizarAccion(accion):
    if accion == "1":
        valor = int(input("Digite el valor a consignar: "))
        return consignar(valor)
    elif accion == "2":
        valor = int(input("Digite el valor a retirar: "))
        return retirar(valor)
    else:
        return False
    
def main():
    while True:
        print("1. Consignar")
        print("2. Retirar")
        print("3. Salir")
        
        accion = input("¿Qué desea hacer? \n")
        
        if accion == "3":
            print("Gracias por su visita.")
            break
        
        resultado = realizarAccion(accion)
        if resultado == False:
            print("\n No se puedo realizar la operación. \n")
        elif resultado == True:
            print(f"\n El nuevo saldo es {saldo} \n")

main()
