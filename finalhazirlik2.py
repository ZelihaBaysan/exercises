import sqlite3 as sql

class Urun:
    def __init__(self, ürün_adi, gönderici_adi, yil, alıcı_adı, alici_adres, ürün_tipi="gıda"):
        self.ürün_tipi = ürün_tipi
        self.ürün_adi = ürün_adi        
        self.gönderici = gönderici_adi
        self.yil = yil
        self.alıcı_adi = alıcı_adı
        self.alici_adres = alici_adres

    def kaydol(self):
        try:
            # Veritabanına bağlan
            db = sql.connect("Nakliye.sqlite")
            cursor = db.cursor()

            # Tablo oluşturulur (varsa yeniden oluşturulmaz)
            query = """
                CREATE TABLE IF NOT EXISTS Gönderilen (ürün_adi TEXT, gönderici_adi TEXT, yil INTEGER, alıcı_adı TEXT, alici_adres TEXT, ürün_tipi TEXT)
            """
            cursor.execute(query)

            # Bilgileri tabloya ekle
            query = f"""
                INSERT INTO Gönderilen (ürün_adi, gönderici_adi, yil, alıcı_adı, alici_adres, ürün_tipi)
                VALUES ('{self.ürün_adi}', '{self.gönderici}', {self.yil}, '{self.alıcı_adi}', '{self.alici_adres}', '{self.ürün_tipi}')
            """
            cursor.execute(query)
            db.commit()
            db.close()

        except Exception as e:
            print(f"hata : {e}")

def main():
    counter = 0
    while True:
        ürün_adi = input("ürün adi: ")
        gönderici_adi = input("gönderici adi: ")
        yil = input("yil giriniz: ")
        alıcı_adı = input("alici adi giriniz: ")
        alici_adres = input("alici adres giriniz: ")

        # Urun sınıfından bir örnek oluştur ve kaydol metodu çağır
        obj = Urun(ürün_adi, gönderici_adi, yil, alıcı_adı, alici_adres)
        obj.kaydol()
        
        counter += 1
        print(f"gönderilen koli sayisi: {counter}")

if __name__ == "__main__":
    main()


    
    """"""
Senaryo: Bir online kırtasiyeye giren öğrenciler ihtiyaçlarına göre ürün almaktadırlar. Bu ürünleri alırken reyonlarına göre indirimler
de sepete yansıtılmaktadır. Kırtasiye indirimleri yaparken 1. 5. 9. Sınıf öğrencilerine ayrıca %20 indirimde uygulamaktadır. Kalem
reyonundan alınan ürünlerde %5, Boya reyonundan alınan ürünlerde %10, Defter reyonundan alınan ürünlerde %7,5 indirim
uygulanmaktadır. Ürünler alınırken sınıf nosu, ürünün adı, reyon adı ve fiyatı sisteme Urunler sınıfından(class) nesne türetilerek
girilmektedir. Ürünün eklenme tarihi sınıf içerisinde kurucu metotda varsayılan 2023 olarak belirlenmelidir. Sisteme girilen ürünler
veritabanına liste haline dönüştürülerek kaydedilmelidir. Veritabanı adı: Kirtasiye, Tablo adı ise Urunler olmalıdır. Urunler
tablosundaki alan adları ise tcno, sinifno, ad,reyon,tarih ve fiyat olmalıdır. Sepete atılacak başka bir ürün kalmadığında ise Ürünler
tablosundaki tüm ürün bilgileri listelenir ve ekrana yazdırılır. Listelenen ürünlerin fiyatları listelenirken indirimler bu aşamada
hesaplanmalıdır. Ürünler tablosuna kaydedilen ürünlerin indirim sonrası toplam tutarı ise sepet adında yeni bir tabloya eklenmelidir.
Bu tablodaki alanlar ise tcno, tarih ve toplamtutar olmalıdır.

Soru4: Yukarıdaki senaryoya göre ürünleri veritabanına kaydeden ve ürün kaydetme işlemi tamamlandıktan sonra kaydedilen verileri
veritabanından çekerek indirimleri hesaplayan ve tekrar sepet tablosuna kaydeden kodu python programlama dilinde yazınız.
"""

    """
