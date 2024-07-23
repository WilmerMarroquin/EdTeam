// Condiciones simples
let edad = 18;

if (edad >= 18) {
    console.log("Puedes votar");
} else {
    console.log("No puedes votar");
}

// Condiciones anidadas
let nota = 80;

if (nota >= 90) {
    console.log("Aprobaste con una calificación de:", nota);
} else if (nota >= 80) {
    console.log("Tienes un buen resultado con una calificación de:", nota);
} else {
    console.log("Tienes un mal resultado con una calificación de:", nota);
}

// Switch
let diaSemana = "Domingo";

switch (diaSemana) {
    case "Lunes":
        console.log("Hoy es Lunes");
        break;
    case "Martes":
        console.log("Hoy es Martes");
        break;
    case "Miércoles":
        console.log("Hoy es Miércoles");
        break;
    case "Jueves":
        console.log("Hoy es Jueves");
        break;
    case "Viernes":
        console.log("Hoy es Viernes");
        break;
    case "Sábado":
        console.log("Hoy es Sábado");
        break;
    case "Domingo":
        console.log("Hoy es Domingo");
        break;
    default:
        console.log("Día inválido");
}

