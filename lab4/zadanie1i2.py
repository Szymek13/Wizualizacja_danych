import random

lista = []

plik = open('liczby_podzielne_przez_4.txt', 'w+')

for x in range(20):
    lista.append(random.randint(0, 100))
for i in lista:
    if i % 4 == 0:
        plik.write(str(i))
        plik.write(" ")
print("Wygenerowane 20 liczb od 0 do 100")
print(lista)
print("\nOdczyt z pliku (liczby podzielne przez 4)")

with open('liczby_podzielne_przez_4.txt', 'r') as plik:
    for linia in plik:
        print(linia, end="")

plik.close()
