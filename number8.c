#include <stdio.h>
#include <stdlib.h>

/* Dizi elemanı değeri kadar ekrana * karakteri yazdırma */

int main() {
    int i;
    int dizi[10];

    printf("10 tane sayi giriniz:\n");

    for (i = 0; i < 10; i++) {
        scanf("%d", &dizi[i]);
    }

    for (i = 0; i < 10; i++) {
        int j;
        for (j = 0; j < dizi[i]; j++) {
            printf("*");
        }
        printf("\n");
    }

    return 0;
}
