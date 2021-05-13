import pandas as pd
import xlrd
import openpyxl

#Zadanie 1
plik = pd.read_excel('imiona.xlsx', header = 0)
inny_plik = pd.read_csv('zamowienia.csv', header = 0, sep = ';')

print("Zadanie 2.1")
print(plik[plik.Liczba > 1000])

print("\nZadanie 2.2")
print(plik[plik.Imie == "SZYMON"])

print("\nZadanie 2.3")
print(plik['Liczba'].sum())

print("\nZadanie 2.4")
print(plik[(plik.Rok >= 2000) & (plik.Rok <= 2005)]['Liczba'].sum())

print("\nZadanie 3.3")
sort = inny_plik.groupby(['Sprzedawca'])
print(sort[['idZamowienia']].count())

print("\nZadanie 3.4")
print(inny_plik.groupby(['Kraj'])[['Utarg']].sum())
