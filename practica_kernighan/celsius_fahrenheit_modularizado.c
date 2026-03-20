#include <stdio.h>

double celsius_fahrenheit(double c) {
    return c * 9.0/5.0 + 32.0;
}

int main(void) {
    int lower = 0, upper = 300, step = 20;
    printf("   ºC:    ºF: \n");
    for (int c = lower; c <= upper; c += step) {
        printf("%6d %6.1f\n", c, celsius_fahrenheit(c));
    }
    return 0;
}