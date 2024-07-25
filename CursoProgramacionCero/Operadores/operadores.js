/* Tipo de operadores

1. Aritméticos: suma (+), resta (-), multiplicación (*), división (/), módulo (%), exponente (**)
2. Relacionales: igual (==), distinto (!=), mayor (>), menor (<), mayor igual (>=), menor igual (<=)
3. Lógicos: AND (&&), OR (||), NOT (!)
4. Unarios: negativo (-), incremento (++), decremento (--) */

// 1. Operadores aritméticos
let num1 = 10;
let num2 = 5;

console.log("");
console.log(`Operaciones aritméticas con los números ${num1} y ${num2}`);
console.log("Suma:", num1 + num2); // Suma
console.log("Resta:",num1 - num2); // Resta
console.log("Multiplicación:",num1 * num2); // Multiplicación
console.log("División:",num1 / num2); // División
console.log("Módulo:",num1 % num2); // Módulo
console.log("Exponente:",num1 ** num2); // Exponente

// 2. Operadores relacionales
console.log("");
console.log(`Operaciones relacionales con los números ${num1} y ${num2}`);
console.log(`${num1} es igual a ${num2}? ➡️`,num1 == num2); // Igualdad (comparando valores)
console.log(`${num1} es diferente a ${num2}? ➡️`,num1 != num2); // Diferente (comparando valores)
console.log(`${num1} es mayor a ${num2}? ➡️`,num1 > num2); // Mayor (comparando valores)
console.log(`${num1} es menor a ${num2}? ➡️`,num1 < num2); // Menor (comparando valores)
console.log(`${num1} es mayor o igual a ${num2}? ➡️`,num1 >= num2); // Mayor igual (comparando valores)
console.log(`${num1} es menor o igual a ${num2}? ➡️`,num1 <= num2); // Menor igual (comparando valores)

// 3. Operadores Lógicos
let mayor = true;
let femenino = true;

console.log("");
console.log(`Operaciones lógicas:`);
console.log(mayor && femenino); // AND (evalúa ambos operandos)
console.log(!mayor); // NOT (negación)
console.log(mayor || femenino); // OR (evalúa al menos uno de los operandos)


// 4. Operadores Unarios
let num = 7;

console.log("");
console.log(`Operaciones unitarias con el números ${num}`);
console.log("negativo de",num,":",-num); // Negativo (operador unario)
console.log("Aumento de una unidad a",num,":",++num); // Incremento (operador unario)
console.log("Decremento de una unidad a",num,":",--num); // Decremento (operador unario)
