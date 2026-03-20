#include <stdio.h>

int main(void){
    int fahr, celsius, lower, upper, step;

    lower = 0; /* temperatura mas baja */
    upper = 300; /* temperatura mas alta */
    step = 20; /* incremento */

    celsius = lower;
    printf("   ºC:    ºF: \n");

    while (celsius <=upper) {
        fahr = celsius * (9/5) + 32;
        printf("%6d %6d\n", celsius, fahr);
        celsius = celsius + step;
    }
}