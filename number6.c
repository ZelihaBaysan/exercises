#include <stdio.h>

int main() {
    int ogrNotlar[3][3];
    int i, j;

    printf("Notlari giriniz:\n");
    for (i = 0; i < 3; i++) {
        for (j = 0; j < 3; j++) {
            printf("Ogrenci %d'nin %d. sinav notunu giriniz: ", i + 1, j + 1);
            scanf("%d", &ogrNotlar[i][j]);
        }
    }

   
	 printf("\nEkran Cikti 2:\n");
    for (j = 0; j < 3; j++) {
        int toplam = 0;
        for (i = 0; i < 3; i++) {
            toplam += ogrNotlar[i][j];
        }
        float ortalama = (float)toplam / 3;
        printf("%d. sinav ağırlıklı not ortalamasi: %.2f\n", j + 1, ortalama);
    }

    return 0;
}
