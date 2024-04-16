ana_menu = {
    "stok girişi": "",
    "kasada ürün sat": "",
    "gün sonu al": "",
    "çıkış yap": ["evet", "hayır"]
}

stok = {}
satis = []
toplam_liste = []

while True:
    print("ANA MENU")
    for item in ana_menu.keys():
        print(f"{item}")
        
    secim = input("Yapmak istediğiniz işlemi seçiniz: ").lower()
    
    if secim == "çıkış yap":
        cikis_secim = input("Emin misiniz? (evet/hayır): ").lower()
        if cikis_secim == "evet":
            print("Programdan çıkış yapılıyor...")
            break
        else:
            continue

    elif secim == "stok girişi":
        while True:
            urun_bilgileri = input("Ürün adı, kodu, tedarikçi adı, stok adedi, kategori adı (aralarında virgül ile ayırın): ")
            urun_ozellikleri = urun_bilgileri.split(",")
            urun_ozellikleri[3] = int(urun_ozellikleri[3])
            urun_adı = urun_ozellikleri[0]
            stok[urun_adı] = urun_ozellikleri

            devam = input("Başka bir ürün girmek istiyor musunuz? (evet/hayır): ").lower()
            if devam == "hayır":
                break
    elif secim == "kasada ürün sat":
        while True:
            urunler = input("Satılan ürün adı, birim fiyatı, adeti (aralarında virgül ile ayırın): ")
            urun_bilgileri = urunler.split(",")
            urun_adı, birim_fiyat, adet = urun_bilgileri
            toplam_fiyat = int(birim_fiyat) * int(adet)
            satis.append([urun_adı, toplam_fiyat, adet])

            devam = input("Başka bir ürün satmak istiyor musunuz? (evet/hayır): ").lower()
            if devam == "hayır":
                toplam_liste.extend(satis)
                satis.clear()
                break
    
    elif secim == "gün sonu al":
        urun_adi = input("Gün sonu almak istediğiniz ürünün adını girin: ")
        if urun_adi in stok:
            print(f"{urun_adi} ürününden kalan miktar: {stok[urun_adi][3]}")
            toplam_kazanc = sum([satis[1] for satis in toplam_liste if satis[0] == urun_adi])
            print(f"{urun_adi} ürününden elde edilen toplam kazanç: {toplam_kazanc}")
        else:
            print(f"{urun_adi} ürünü bulunamadı.")
