// Algoritmo de año bisiesto
let year;

year = 2023;

if ((year % 4 == 0 && year % 100 != 0) || year % 400 == 0) {
    console.log(year + " es un año bisiesto");
} else {
    console.log(year + " no es un año bisiesto");
}