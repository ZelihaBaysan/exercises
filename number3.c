#include <stdlib.h>
#include <stdio.h>

/*
aşağıda belirtilen işlemleri yapan bir c programı yazınız
toplama(+) ve çıkarma(-) operatörü giriniz
'+' operatörü için 1/a+1/b;
'-' operatörü için 1/a-1/b;
işlemlerinin sonucunu basit kesir cinsinden bulunuz.
girilen a veya b değerlerinden biri 0 ise işlemin yapılamayacağı mesajını veriniz
*/
int main() {
    float sonuc = 0, gir1 = 0, gir2 = 0;
    char op = 0;

    printf("Lutfen ilk olarak bir deger giriniz, sonrasinda + veya - operatorunu giriniz ve tekrar bir deger giriniz:\n");
    scanf("%f %c %f", &gir1, &op, &gir2);

    if (gir1 == 0 || gir2 == 0) {
        printf("Girmemeniz gereken bir deger girdiniz.\n");
    } else {
        if (op == '+') {
            sonuc = 1 / gir1 + 1 / gir2;
        } else if (op == '-') {
            sonuc = 1 / gir1 - 1 / gir2;
        } else {
            printf("Girilmemesi gereken bir operator girdiniz.\n");
        }

        printf("Sonuc: %.2f\n", sonuc);
    }

    return 0;
}
