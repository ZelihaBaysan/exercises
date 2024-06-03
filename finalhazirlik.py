kayit = {}
urunler = {}
urun_listesi = []

def giris():
    while True:
        secim = input("Üye olmak için 1'e\ngiriş yapmak için 2'ye\nçıkış yapmak için 3'e tıklayınız\n")
        if secim == '1':
            uye_ol()
        elif secim == '2':
            giris_yap()
        elif secim == '3':
            print("Programdan çıkılıyor...")
            break
        else:
            print("Yanlış bir değer girdiniz")

def uye_ol():
    ad = input("Kullanıcı adı: ")
    sifre = input("Şifre: ")
    isletme_adi = input("İşletme adı: ")
    id = input("ID: ")
    
    if ad in kayit:
        print("Bu kullanıcı adı kullanılıyor")
    else:
        kayit[ad] = [sifre, isletme_adi, id]
        print(f"{ad} kullanıcısı başarıyla kaydedildi")

def giris_yap():
    ad = input("Kullanıcı adı: ")
    sifre = input("Şifre: ")
    
    if ad in kayit:
        if kayit[ad][0] == sifre:
            print(f"{ad} sisteme başarıyla giriş yaptı.")
            alt_menu()
        else:
            print("Hatalı şifre.")
    else:
        print("Kullanıcı adı bulunamadı.")

def alt_menu():
    while True:
        secim = input("A-Ürün Ekle\nB-Ürün Fiyatı Güncelle\nC-Ürün Sil\nD-Ana Menüye Dön\n")
        if secim.upper() == 'A':
            urun_ekle()
        elif secim.upper() == 'B':
            urun_fiyat_guncelle()
        elif secim.upper() == 'C':
            urun_sil()
        elif secim.upper() == 'D':
            break
        else:
            print("Yanlış bir değer girdiniz")

def urun_ekle():
    while True:
        urun_adi = input("Ürün adı: ")
        urun_kodu = input("Ürün kodu: ")
        urun_fiyati = float(input("Ürün fiyatı: "))
        urun_kategorisi = input("Ürün kategorisi: ")
        
        urun_bilgileri = [urun_adi, urun_fiyati, urun_kategorisi]
        yeni_urun = urun_ekle_fonksiyonu(urun_kodu, urun_bilgileri)
        
        urunler.update(yeni_urun)
        urun_listesi.append(yeni_urun)
        
        devam = input("Başka bir ürün eklemek ister misiniz? (E/H): ")
        if devam.upper() == 'H':
            break

def urun_ekle_fonksiyonu(urun_kodu, urun_bilgileri):
    return {urun_kodu: urun_bilgileri}

def urun_fiyat_guncelle():
    urun_adi = input("Fiyatını güncellemek istediğiniz ürünün adı: ")
    yeni_fiyat = float(input("Yeni fiyat: "))
    mesaj = urun_guncelle_fonksiyonu(urun_adi, yeni_fiyat, urunler)
    print(mesaj)

def urun_guncelle_fonksiyonu(urun_adi, yeni_fiyat, urunler):
    for kod, bilgiler in urunler.items():
        if bilgiler[0] == urun_adi:
            urunler[kod][1] = yeni_fiyat
            return f"{urun_adi} ürününün yeni fiyatı {yeni_fiyat} olarak güncellendi."
    return "Ürün bulunamadı."

def urun_sil():
    urun_adi = input("Silmek istediğiniz ürünün adı: ")
    for kod in list(urunler.keys()):
        if urunler[kod][0] == urun_adi:
            del urunler[kod]
            print(f"{urun_adi} ürünü silindi.")
            return
    print("Bu isimde bir ürün bulunamadı.")

giris()
