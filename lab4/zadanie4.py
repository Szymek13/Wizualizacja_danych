class NaZakupy:
    def __init__(self, nazwa_produktu, ilosc, jednostka_miary, cena_jed):
        self.nazwa_produktu = nazwa_produktu
        self.ilosc = ilosc
        self.jednostka_miary = jednostka_miary
        self.cena_jed = cena_jed
    def wyswietl_produkt(self):
        return "Musisz kupić " + self.nazwa_produktu
    def ile_produktu(self):
        return "W ilości " + str(self.ilosc) + self.jednostka_miary
    def ile_kosztuje(self):
        return self.ilosc * self.cena_jed

obiekt = NaZakupy("Kawa", 3, "dag", 35)
print(obiekt.wyswietl_produkt())
print(obiekt.ile_produktu())
print("Musisz przygotować", obiekt.ile_kosztuje(), "zł")
