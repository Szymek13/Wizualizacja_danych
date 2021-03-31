import numpy as np

print("Zadanie 1")
a3 = np.arange(3, 48, 3)
print(a3)

print("\nZadanie 2")
b = np.arange(2, 3, 0.1)
print(b)
b2 = np.arange(2, 3, 0.1, dtype='int64')
print(b2)

print("\nZadanie 4")
def macpoteg(m, n):
    mpoteg = np.logspace(1, n, num=n, base=m)
    return np.array(mpoteg, dtype='int')

print(macpoteg(2, 4))