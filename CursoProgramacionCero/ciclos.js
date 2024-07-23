/* for (let tabla = 1; tabla <= 12; tabla++) {
    for (let num = 1; num <= 12; num++) {
        let resultado = tabla +" * " + num + " = " + tabla*num;
        console.log(resultado);
    }
    console.log("-------------------");
} */


/* for (let par = 0; par <= 12; par++) {
    if (par % 2== 0) {  
        console.log(par + " es par");
    }
    else {
        console.log(par + " es impar");
    }
} */


/* let edad = 0;
while (edad < 18){
    console.log("tienes "+ edad +" años, aun eres un niño");
    edad++
}
console.log("tienes "+ edad +" años, ya eres un adulto"); */


// Blancas = ◻️
// Negras = ⬛

let linea = "";
for (let casilla = 0; casilla < 8; casilla++) {
    for (let fila = 0; fila < 8; fila ++)
        if ((casilla + fila) % 2 === 0) {
            linea += "◻️";
        } else {
            linea += "⬛";
        }
    linea += "\n";  // Salto de línea para la siguiente fila   
}
console.log(linea);