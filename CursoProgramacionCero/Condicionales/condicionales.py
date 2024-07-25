# Condiciones simples
edad = 18
if edad >= 18:
    print("Puedes votar")
else:
    print("No puedes votar")

# Condiciones anidadas
nota = 80
if nota >= 90:
    print("Aprobaste con una calificación de:", nota)
elif nota >= 80:
    print("Tienes un buen resultado con una calificación de:", nota)
else:
    print("Tienes un mal resultado con una calificación de:", nota)

# Switch
diaSemana = "Domingo"
if diaSemana == "Lunes":
    print("Hoy es Lunes")
elif diaSemana == "Martes":
    print("Hoy es Martes")
elif diaSemana == "Miércoles":
    print("Hoy es Miércoles")
elif diaSemana == "Jueves":
    print("Hoy es Jueves")
elif diaSemana == "Viernes":
    print("Hoy es Viernes")
elif diaSemana == "Sábado":
    print("Hoy es Sábado")
elif diaSemana == "Domingo":
    print("Hoy es Domingo")
else:
    print("Día inválido")