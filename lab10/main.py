import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Zadanie 1
x = np.arange(20, 40, 1)
y = (1/x)
plt.plot(x, y, 'b-', label='f(x)')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend()
plt.axis([20, 40, 0.02, 0.05])
plt.title('Wykres funkcji f(x)')
plt.show()

# Zadanie 2
x = np.arange(20, 40, 1)
y = (1/x)
plt.plot(x, y, 'bo--', label='f(x)')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend()
plt.axis([20, 40, 0.02, 0.05])
plt.title('Wykres funkcji f(x)')
plt.show()

# Zadanie 3
x1 = np.arange(0, 45, 0.1)
x2 = np.arange(0, 45, 0.1)
y1 = np.sin(x1)
y2 = np.cos(x2)
plt.plot(x1, y1, '-', label='sin(x)')
plt.plot(x2, y2, '--', label='cos(x)')
plt.axis([0, 45, -1, 1])
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend(loc='lower right')
plt.show()

# Zadanie 4
x1 = np.arange(0, 45, 0.1)
x2 = np.arange(0, 45, 0.1)
y1 = np.sin(x1+np.pi)
y2 = np.sin(x2)+2
plt.plot(x1, y1, '-', label='sin(x)')
plt.plot(x2, y2, '--', label='sin(x)')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend(loc='lower right')
plt.show()

# Zadanie 5
pliczek = pd.read_csv('iris.data', header=None, sep=',', decimal='.')
wykres = {'c': np.random.randn(150),
          'x': pliczek[0],
          'y': pliczek[1],
          's': abs(pliczek[0] - pliczek[1])}
plt.scatter('x', 'y', c='c', s='s', data=wykres)
plt.xlabel('sepal length')
plt.ylabel('sepal width')
plt.show()
