import sqlite3

# Urunler sınıfı
class Urunler:
    def __init__(self, tcno, sinifno, ad, reyon, fiyat, tarih='2023'):
        self.tcno = tcno
        self.sinifno = sinifno
        self.ad = ad
        self.reyon = reyon
        self.fiyat = fiyat
        self.tarih = tarih

# Veritabanı bağlantısı oluşturma ve tabloları oluşturma
def create_database():
    conn = sqlite3.connect('Kirtasiye.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS Urunler
                 (tcno TEXT, sinifno INTEGER, ad TEXT, reyon TEXT, tarih TEXT, fiyat REAL)''')
    c.execute('''CREATE TABLE IF NOT EXISTS Sepet
                 (tcno TEXT, tarih TEXT, toplamtutar REAL)''')
    conn.commit()
    conn.close()

# Ürünleri veritabanına kaydetme
def add_urun_to_db(urun):
    conn = sqlite3.connect('Kirtasiye.db')
    c = conn.cursor()
    c.execute("INSERT INTO Urunler (tcno, sinifno, ad, reyon, tarih, fiyat) VALUES (?, ?, ?, ?, ?, ?)",
              (urun.tcno, urun.sinifno, urun.ad, urun.reyon, urun.tarih, urun.fiyat))
    conn.commit()
    conn.close()

# İndirim hesaplama fonksiyonu
def apply_discounts(sinifno, reyon, fiyat):
    if reyon == 'Kalem':
        fiyat *= 0.95
    elif reyon == 'Boya':
        fiyat *= 0.90
    elif reyon == 'Defter':
        fiyat *= 0.925

    if sinifno in [1, 5, 9]:
        fiyat *= 0.80

    return fiyat

# Veritabanından ürün bilgilerini çekme ve indirimleri hesaplayarak sepet tablosuna kaydetme
def process_cart():
    conn = sqlite3.connect('Kirtasiye.db')
    c = conn.cursor()
    c.execute("SELECT tcno, sinifno, ad, reyon, tarih, fiyat FROM Urunler")
    urunler = c.fetchall()
    
    for urun in urunler:
        tcno, sinifno, ad, reyon, tarih, fiyat = urun
        indirimli_fiyat = apply_discounts(sinifno, reyon, fiyat)
        c.execute("INSERT INTO Sepet (tcno, tarih, toplamtutar) VALUES (?, ?, ?)",
                  (tcno, tarih, indirimli_fiyat))
    
    conn.commit()
    conn.close()

# Ürünleri listeden çekme ve yazdırma
def list_urunler():
    conn = sqlite3.connect('Kirtasiye.db')
    c = conn.cursor()
    c.execute("SELECT * FROM Urunler")
    urunler = c.fetchall()
    for urun in urunler:
        tcno, sinifno, ad, reyon, tarih, fiyat = urun
        indirimli_fiyat = apply_discounts(sinifno, reyon, fiyat)
        print(f"TC: {tcno}, Sınıf No: {sinifno}, Ad: {ad}, Reyon: {reyon}, Tarih: {tarih}, Fiyat: {indirimli_fiyat:.2f}")
    conn.close()

# Ana program
if __name__ == "__main__":
    create_database()

    # Ürün ekleme örnekleri
    urun1 = Urunler('12345678901', 1, 'Kalem Seti', 'Kalem', 20.0)
    urun2 = Urunler('12345678902', 5, 'Sulu Boya', 'Boya', 35.0)
    urun3 = Urunler('12345678903', 9, 'Defter', 'Defter', 15.0)

    add_urun_to_db(urun1)
    add_urun_to_db(urun2)
    add_urun_to_db(urun3)

    # Ürünleri listele
    list_urunler()

    # Sepeti işleme
    process_cart()

    
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
