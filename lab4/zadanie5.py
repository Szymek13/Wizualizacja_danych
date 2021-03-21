class CiagAryt():
    def __init__(self, a, ile, r):
        self.a = a
        self.ile = ile
        self.r = r

    def pobierz_parametry(self):
        self.a = int(input("Podaj pierwszy wyraz ciągu: "))
        self.ile = int(input("Podaj ilość wyrazów, które chcesz policzyć: "))
        self.r = int(input("Podaj różnicę ciągu: "))
    def wyswietl_dane(self):
        return "Właściwości ciągu: " + str(self.a) + ", " + str(self.ile) + ", " + str(self.r)

obiekt = CiagAryt(2, 5, 3)
print(obiekt.wyswietl_dane())
print(obiekt.pobierz_parametry())
print(obiekt.wyswietl_dane())