// Listas
let canciones = ["Los mandados", "Yo quiero ser tu marido", "La ley del monte", "Que chulada de mujer"];

console.log(canciones); // Imprimir la lista de canciones
console.log(canciones.length); // Imprimir el tamaño de la lista

// Añadir el tamaño de la lista en una variable
let tamañoLista = canciones.length;
console.log("El tamaño de la lista es: " + tamañoLista);

// Acceder a un elemento específico de la lista
console.log(canciones[0]); // Imprimir la primera canción
console.log(canciones[tamañoLista - 1]); // Imprimir la última canción

// Añadir un elemento a la lista
canciones.push("Esta es una canción nueva"); // Añadir al final de la lista
console.log(canciones);

canciones.unshift("Esta es otra canción nueva"); // Añadir al principio de la lista
console.log(canciones);

// Modificar un elemento de la lista
canciones[0] = "Me gustas mucho"; // Modificar el segundo elemento
console.log(canciones);
canciones[canciones.length -1] = "Aunque me duela el alma";
console.log(canciones);

// Eliminar un elemento de la lista
canciones.shift();
console.log(canciones);

canciones.pop();
console.log(canciones);

// Recorrer la lista
console.log("Recorrer la lista con un bucle for:");
for (let i = 0; i < canciones.length; i++) {
    console.log("- ", canciones[i]);
}

console.log("Recorrer la lista con un bucle while:");
let indice = 0;
while (indice < canciones.length) {
    console.log("- ", canciones[indice]);
    indice++;
}

console.log("Recorrer la lista con un bucle forEach:");
canciones.forEach(cancion => console.log("- ", cancion));
