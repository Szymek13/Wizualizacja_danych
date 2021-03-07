import sys as system
from math import *

print('Zadanie 1')
sport = ["Piłka nożna", "Siatkówka", "Skoki narciarskie", "Koszykówka"]
print(sport)
sport.reverse()
print(sport)
sport.extend(('Tenis stołowy', 'Bieg na 100m'))
print(sport)

print('\nZadanie 2')
slownik = {'pt.': 'Pod tytułem', 'tzn.': 'To znaczy', 'm.in.': 'Między innymi'}
print(slownik)

print('\nZadanie 3')
gry = {1: 'Rayman Legends', 2: 'The Binding of Isaac', 3: 'Far Cry 3', 4: 'HITMAN 3'}
for m in gry.keys():
    m += 1
else:
    print("Ilość gier w słowniku:", m - 1)

print('\nZadanie 4')
napis = input("Podaj dowolne zdanie: ")
x = napis.count('a')
print("Wystąpiło tyle liter a: ", x)

print('\nZadanie 5')
system.stdout.write("Podaj trzy dowolne liczby, zostanie wykonana operacja a^b + c\n")
a = system.stdin.readline()
b = system.stdin.readline()
c = system.stdin.readline()
a = int(a)
b = int(b)
c = int(c)
x = a**b + c
x = str(x)
system.stdout.write(x)

print('\nZadanie 6')
print("Podaj trzy liczby, program wyświetli największą z nich:")
f = int(input("Pierwsza liczba: "))
g = int(input("Druga liczba: "))
h = int(input("Trzecia liczba: "))
if f >= g:
    if f >= h:
        print("Największa liczba:", f)
if g >= f:
    if g >= h:
        print("Największa liczba:", g)
if h >= f:
    if h >= g:
        print("Największa liczba:", h)

print('\nZadanie 7')
cyferki = [2, 5, 6.7, 9, 9, 0.34]
for x in cyferki:
    print(x**2)

print('\nZadanie 8')
cyferki2 = []
n = int(input("Podaj 10 liczb a zostaną wypisane tylko parzyste: \n"))

for n in range(1, 10):
    ele = int(input())
    cyferki2.append(ele)

for n in cyferki2:
    if (n % 2) == 0:
        print(n)

print('\nZadanie 10')
pierw = int(input("Podaj liczbę, z której ma być obliczony pierwiastek: "))
try:
    wynik = sqrt(pierw)
    print(wynik)
finally:
    if pierw < 0:
        print("Podałeś ujemną liczbę")
