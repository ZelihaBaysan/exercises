#include <stdio.h>

int palindromMu(int sayi) {

}

int main() {
    int i, j, maxP = 0, sonuc = 0;

    for (i = 10; i < 100; i++) {
        for (j = 10; j < 100; j++) {
            sonuc = i * j;

            if (palindromMu(sonuc)==1) {
                maxP = sonuc;
            }
        }
    }

    printf("%d\n", maxP);

    return 0;
}

/*
"En büyük palindrom ürünü (Largest palindrome product)"

9009 sayısı 2 basamaklı sayıların çarpımından elde edilebilen bir palindromdur:
91
×
99
=
9009
91×99=9009.

2 basamaklı iki sayının çarpımından elde edilebilecek en büyük palindromu bulunuz.*/

/*
ilk olarak i ve j değeri belirle ve bunları 10dan başlat
sonra bunları 1 arttıra arttıra birbirleri ile çarptır
çıkan her sonucu kontrol ettir
eğer çıkan sonuc bastan ve sondan aynı ise palindrom=sonuc yap
eşit değil iseçarptırmaya devam et i ve j 100 olana kadar

*/
