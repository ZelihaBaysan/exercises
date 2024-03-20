'''kullanıcıdan alınan sayılar bir liste içine eklensin kullanıcı bitir dediğinde ayrı bir döngüde ortalama hesabının yapılması
ilk kişiden sayi al ve her seferinde bitsin mi diye sor, evet diyene kadar girdiği rakamlarılisteye ekle
sonra listedekei rakamları for döngüsü ile toplat ve toplamn ortalamasını al

'''

print("Lütfen istediğiniz kadar sayı giriniz")

liste = []

while True:
    sayi = int(input("Sayı girin: "))
    liste.append(sayi)
    
    cevap = int(input("Tekrar sayı girmek istiyorsanız 1'e, istemiyorsanız 0'a basın: "))
    
    if cevap == 0:
        break
    elif cevap == 1:
        continue
    else:
        print("yanlış bir değer girdiniz")

toplam = sum(liste)
ortalama = toplam / len(liste)
print(ortalama)

    
    