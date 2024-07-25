// Se define la función
function cajero() {
    // Definir variables
    let saldo = 1000;

    // Ciclo para realizar la opciones del cajero
    while (true) {
        let opcion = prompt("¿Qué desea hacer? \n1. Consignar \n2. Retirar \n3. Salir ");
        if (opcion === "3"){
            alert("Gracias por su visita.");
            break;
        }
        // Ejecutar la acción correspondiente
        if (opcion === "1") {
            let valor = parseInt(prompt("Digite el valor a consignar"));
            saldo += valor;
            alert(`Acción realizada con éxito, Saldo ${saldo}`);
        } else if (opcion === "2") {
            let valor = parseInt(prompt("Digite el valor a retirar"));
            if (valor <= saldo) {
                saldo -= valor;
                alert(`Acción realizada con éxito, Saldo ${saldo}`);
            } else {
                alert("No hay suficiente saldo para retirar.");
            }
        } else {
            alert("Opción inválida.");
        }
    }
}

// Llamar a la función

cajero();