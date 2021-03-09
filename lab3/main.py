print("Zadanie 1")
A = [1-x for x in range(1, 11)]
print(A)
B = [4**y for y in range(1, 8)]
print(B)
C = [z for z in B if z % 2 == 0]
print(C)

print("\nZadanie 2")
lista1 = [3, 5, 76, 2, 8, 61, 22, 12, 5, 3]
D = [a for a in lista1 if a % 2 == 0]
print(D)

# print("\nZadanie 3")
# slownik = {"kg": "mąka", "kg": "cukier", "szt": "czekolada", "szt": "żelki", "l": "sok"}
# E = {a for a in slownik if slownik.key == "szt"}
# print(E)

print("\nZadanie 4")
def trojkat_prostokatny(a, b, c):
    if(a**2 + b**2 == c**2):
        print("Trójkąt jest prostokątny")
        return 0
    else:
        print("Trójkąt nie jest prostokątny")
        return 1
print(trojkat_prostokatny(3, 4, 5))
print(trojkat_prostokatny(1, 3, 2))

print("\nZadanie 5")
def trapez(a=5, b=3, h=6):
    pole = ((a+b)*h)/2
    print("Pole trapezu wynosi:")
    return pole
print(trapez())

print("\nZadanie 6")
def ciag(a=1, b=4, ile=10):
    iloczyn = a
    for x in range(a, ile, b):
        iloczyn *= x
    else:
        return iloczyn
print(ciag())

print("\nZadanie 7")
def ciag1(* dane):
    if len(dane) == 0:
        return 0
    elif len(dane) == 3:
        iloczyn = 1
        for x in dane:
            iloczyn *= x
        else:
            return iloczyn
    else:
        return 0
print(ciag1(1, 10, 4))

# print("\nZadanie 8")
# def zakupy(** lista):
#     for produkt in lista:
#         print("Lista zakupów: ")
#         print(produkt)
#         print("Koszt zakupów: ")
#         print(lista[produkt])
# zakupy(nabiał = 'mleko', mięso = 'szynka', koszt = [23, 45])
