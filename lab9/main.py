import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import xlrd
import openpyxl

#Zadanie 1
plik1 = pd.read_excel('imiona.xlsx', header = 0)
grupa1 = plik1.groupby(['Rok']).agg({'Liczba':['sum']})
wykres1 = grupa1.plot()
wykres1.set_xlabel('Rok')
wykres1.set_ylabel('Liczba urodzonych dzieci')
plt.show()

#Zadanie 2
grupa2 = plik1.groupby(['Plec']).agg({'Liczba':['sum']})
wykres2 = grupa2.plot.bar()
wykres2.set_xlabel('Płeć')
wykres2.set_ylabel('Liczba urodzonych dzieci [mln]')
plt.xticks(rotation = 0)
plt.show()

#Zadanie 3
warunek = plik1[(plik1.Rok >= 2012) & (plik1.Rok <= 2017)]
grupa3 = warunek.groupby(['Plec']).agg({'Liczba':['sum']})
wykres3 = grupa3.plot.pie(subplots = True, autopct = '%.2f %%', fontsize = 20, figsize = (6, 6), legend = (0, 0))
plt.legend(loc = 'upper right')
plt.title('Liczba urodzonych dzieci w latach 2012-2017')
plt.show()

#Zadanie 4
plik2 = pd.read_csv('zamowienia.csv', header = 0, sep = ';', decimal = '.')
data = pd.DataFrame(plik2)
grupa4 = data.groupby(['Sprzedawca'])
wykres4 = grupa4[['idZamowienia']].count().plot.bar()
wykres4.set_xlabel('Sprzedawca')
wykres4.set_ylabel('Liczba zamówień')
plt.xticks(rotation = 0)
plt.show()
