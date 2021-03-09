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
# E = {value: key for key in slownik if slownik.key == "szt"}
# print(E)

print("\nZadanie 4")
def trojkat_prostokatny(a, b, c):
    if(a**2 + b**2 == c**2):
        print("Trójkąt jest prostokątny")
    else:
        print("Trójkąt nie jest prostokątny")
print(trojkat)
