ad = ""
soyad = ""
bakiye = 0
ogrenciDurumu = 0

def kayit():
    global ad, soyad
    ad = input("Lutfen adinizi giriniz: ")
    soyad = input("Lutfen soyadinizi giriniz: ")
    return ad, soyad

def bakiyeYukle():
    global bakiye
    print("Mevcut bakiyeniz: {} TL".format(bakiye))
    ekleme = int(input("Lutfen yuklemek istediginiz degeri giriniz: "))
    bakiye += ekleme
    print("Yeni bakiyeniz: {} TL".format(bakiye))

def durumGuncelleme():
    global ogrenciDurumu
    durumNo = int(input("Ogrenci iseniz 1, sivil iseniz 2, emekli iseniz 3 tusuna basiniz: "))
    if durumNo == 1:
        ogrenciDurumu = int(input("Universitede ogrenci iseniz 1, degil iseniz 0 tusuna basiniz: "))
        if ogrenciDurumu == 1:
            print("Universitede ogrencisiniz ve odemeniz gereken ucret 6 TL'dir")
        else:
            print("Universitede ogrenci degilsiniz ve odemeniz gereken ucret 6 TL'dir")
    elif durumNo == 2:
        print("Sivilsiniz ve odemeniz gereken ucret 10 TL'dir")
    elif durumNo == 3:
        print("Emeklisiniz ve ucret odemenize gerek yok")
    else:
        print("Yanlis bir deger girdiniz")

def bilgileriGoster():
    print("Adiniz: {}\nSoyadiniz: {}\nDurumunuz:\n(1=OGRENCI\n2=SIVIL\n3=EMEKLI) {}\nMevcut Bakiyeniz: {} TL".format(ad, soyad, ogrenciDurumu, bakiye))

while True:
    secim = int(input("\nLutfen bir secim yapiniz:\n1. Kayit yapmak icin\n2. Bakiye yuklemek icin\n3. Durum guncellemek icin\n4. Mevcut bilgileri gormek icin\nSeciminizi giriniz: "))
    if secim == 1:
        print("Kayit olma islemini sectiniz")
        kayit()
    elif secim == 2:
        print("Bakiye yukleme islemini sectiniz")
        bakiyeYukle()
    elif secim == 3:
        print("Durum guncelleme islemini sectiniz")
        durumGuncelleme()
    elif secim == 4:
        print("Mevcut bilgileri gorme islemini sectiniz")
        bilgileriGoster()
    else:
        print("Gecersiz bir sayi sectiniz")
