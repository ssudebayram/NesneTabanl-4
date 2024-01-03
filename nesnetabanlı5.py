class Film:
    def __init__(self, ad, yonetmen, yil):
        self.ad = ad
        self.yonetmen = yonetmen
        self.yil = yil

    def film_bilgileri(self):
        return f"{self.ad} ({self.yil}), Yönetmen: {self.yonetmen}"


class FilmKutuphanesi:
    def __init__(self):
        self.filmler = []

    def film_ekle(self, film):
        self.filmler.append(film)
        print(f"{film.ad} filmi kütüphaneye eklendi.")

    def film_listele(self):
        print("Kütüphanedeki Filmler:")
        for film in self.filmler:
            print(film.film_bilgileri())


kutuphane = FilmKutuphanesi()

while True:
    print("Film Eklemek için 1'e basın")
    print("Çıkış için 2'ya basın")
    secim = input("Seçiminizi yapın: ")

    if secim == "1":
        ad = input("Film adını girin: ")
        yonetmen = input("Yönetmen adını girin: ")
        yil = input("Film yılını girin: ")

        yeni_film = Film(ad, yonetmen, yil)
        kutuphane.film_ekle(yeni_film)
    elif secim == "2":
        print("Programdan çıkılıyor...")
        break
    else:
        print("Geçersiz seçim. Lütfen tekrar deneyin.")

kutuphane.film_listele()
