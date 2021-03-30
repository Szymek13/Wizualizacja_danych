#Zadanie1
class Material:
    def __init__(self, rodzaj, dlugosc, szerokosc):
        self.rodzaj = rodzaj
        self.dlugosc = dlugosc
        self.szerokosc = szerokosc

    def wyswietl_nazwe(self):
        return "Materiał {} o długości {} i szerokości {}".format(self.rodzaj, self.dlugosc, self.szerokosc)

class Ubrania(Material):
    def __init__(self, rozmiar, kolor, dla_kogo):
        self.rozmiar = rozmiar
        self.kolor = kolor
        self.dla_kogo = dla_kogo

    def wyswietl_dane(self):
        return "Ubranie o rozmiarze {} w kolorze {} jest {}".format(self.rozmiar, self.kolor, self.dla_kogo)

class Sweter(Ubrania):
    def __init__(self, rodzaj_swetra):
        self.rodzaj_swetra = rodzaj_swetra

    def wyswietl_dane(self):
        return "Rodzaj swetra: {}".format(self.rodzaj_swetra)

sklep = Material("sukno", 23, 34)
print(sklep.wyswietl_nazwe())
sklep = Ubrania("M", "czerowny", "dla Prezesa")
print(sklep.wyswietl_dane())
sklep = Sweter("rozpinany z kołnierzem")
print(sklep.wyswietl_dane())

#Zadanie2
# class Ksztalty:
    # def __init__(self, x, y):
        # self.x = x
        # self.y = y

    # def suma(self):
        # return self.x + self.y

    # def obwod(self):
        # return 2 * self.x + 2 * self.y

# kwadrat = Ksztalty(23, 43)
# print(kwadrat.suma())
# print(kwadrat.obwod())