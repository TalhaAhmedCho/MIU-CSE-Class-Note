#include <stdio.h>

float calc(int radius) {
    float Area = 3.1416 * radius * radius;
    return Area;
}

int main() {
    int radius;
    printf("Enter Radius: ");
    scanf("%d", &radius);
    printf("The Area is: %f", calc(radius));
}