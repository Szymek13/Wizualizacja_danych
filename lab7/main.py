import numpy as np
from math import *

print("Zadanie1")
a = np.array([[1], [2], [3]])
b = np.array([[4], [5], [6]])
print(a)
print(b)
print(a*b)

print("\nZadanie2")
c = np.array([[9, 5, 4], [12, 34, 7], [22, 5, 0]])
d = np.arange(16).reshape(4, 4)
print(c)
print(d)
print(c.min(axis=1))
print(c.min(axis=0))
print(d.min(axis=1))
print(d.min(axis=0))

print("\nZadanie3")
b = b.reshape(1, 3)
print(a.dot(b))

print("\nZadanie4")
e = np.array([5, 8, 4])
f = np.array([3.75, 9., 0.13])
print(e*f)

# print("\nZadanie5")
# g = np.array([[1, 0.5, 0.75], [1, 0, 1]])
# aa = []
# for x in g:
#     aa = aa.append([sin(x)])
# print(aa)

# print("\nZadanie6")
# h = np.array([[1, 0.5, 0.75], [1, 0, 1]])
# bb = []
# for y in h:
#     bb = bb.append([cos(y)])
# print(bb)

# print("\nZadanie7")
# print(np.add(aa, bb))

print("\nZadanie8")
i = np.arange(9).reshape(3, 3)
print(i)
for z in i:
    print(z)
    print("")

print("\nZadanie9")
j = np.arange(9).reshape(3, 3)
print(j)
for zmienna in j.flat:
    print(zmienna)
    print("")

print("\nZadanie10")
k = np.arange(81).reshape(9, 9)
print(k)
kk = k.reshape(3, 27)
print(kk)
print("Macierze możemy przekształcać w takie wymiary, aby kolumny*wiersze = ilość elementów w macierzy")

print("\nZadanie11")
l = np.arange(12)
print(l)
ll = l.reshape(3, 4)
print(ll)
for m in ll.flat:
    print(m)
    print("")
lll = l.reshape(4, 3)
print(lll)
for n in lll.flat:
    print(n)
    print("")
llll = l.reshape(2, 6)
print(llll)
for o in llll.flat:
    print(o)
    print("")
print("Po spłaszczeniu, wyniki są identyczne")
