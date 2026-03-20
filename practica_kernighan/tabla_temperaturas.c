#include <stdio.h>
/* Este programa usa la formula C = (5/9)(F-32)
para imprimir una tabla de temperaturas Farenheit-Celsius
La tabla se muestra con Farenheit en la primera columna y Celsius en la segunda.
El programa imprime las temperaturas de 0 a 300 grados Farenheit, en incrementos de 20 grados.
*/

int main(void){
    float fahr, celsius;
    int lower, upper, step;

    lower = 0; /* temperatura mas baja */
    upper = 300; /* temperatura mas alta */
    step = 20; /* incremento */

    fahr = lower;
    while (fahr <=upper) {
        celsius = (5.0/9.0) * (fahr-32.0);
        printf("%3.0f %6.1f\n", fahr, celsius);
        fahr = fahr + step;
    }
}

/* La salida es:
  0  -17.8
 20   -6.7
 40    4.4
 60   15.6
 80   26.7
100   37.8
120   48.9
140   60.0
160   71.1
180   82.2
200   93.3
220  104.4
240  115.6
260  126.7
280  137.8
300  148.9
*/