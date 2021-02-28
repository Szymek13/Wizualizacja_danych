from math import *

print('Zadanie 1')
a = 1
b = 2
c = 4.534
d = 3.64
e = 1+67j
f = 23+5j
print(a,b,c,d,e,f)

print('\nZadanie 2')
x = int(input('Podaj pierwszą liczbę: '))
y = int(input('Podaj drugą liczbę: '))
print('Dodawanie:', x+y)
print('Odejmowanie:', x-y)
print('Mnożenie:', x*y)
print('Dzielenie:', x/y)

print('\nZadanie 3')
g = int(input("Podaj dowolną liczbę (wszystkie operacje [+, *, -, **] są wykonywane przez 3): "))
g+=3
g*=3
g-=3
g**=3
print(g)

print('\nZadanie 4')
one = e**10
three = floor(3.55)
four = ceil(4.80)
print('Pierwszy wynik:', one, '\nTrzeci wynik:', three, '\nCzwarty wynik', four)

print('\nZadanie 5')
imie = 'SZYMON'
nazwisko = 'MILEWSKI'
print(imie.capitalize(), nazwisko.capitalize())

print('\nZadanie 6')
piosenka = 'la la la la al all al la la'
print('Ilość la:', piosenka.count('la'))

print('\nZadanie 7')
marka = 'Mercedes'
print(marka)
print('Druga litera:', marka[1], '\nOstatnia litera', marka[-1])

print('\nZadanie 8')
print(piosenka.split())