#include <stdio.h>

int asalMi(int sayi) {
	int i = 2;
    for (i = 2; i < sayi; i++) {
        if (sayi % i == 0)
            return 0;
    }
    return 1;
}

int main() {
    long long deger = 600851475143;
    int ikinciDeger = 0;
    int ilkDeger = 2;

    for (ilkDeger = 2; ilkDeger <= deger; ilkDeger++) {
        while (deger % ilkDeger == 0) {
            if (asalMi(ilkDeger)) {
                ikinciDeger = ilkDeger;
            }
            deger /= ilkDeger;
        }
    }

    printf("600851475143 sayisinin en buyuk asal boleni: %d\n", ikinciDeger);

    return 0;
}

/*
sayıyı sırasıyla sayılara böldürürüz,
 onu bölmeyen bir sayı gelirse başka sayıya geçer,
 bölen bir sayıysa bölebildiği kadar böler.
en son bölen sayı ardığımız sayıdır
*/