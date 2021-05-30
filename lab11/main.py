import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import cm

#Zadanie 1
fig = plt.figure()
ax = fig.gca(projection='3d')
z = np.linspace(0, 2*np.pi, 50)
x = np.sin(z)
y = 2*np.cos(z)
ax.plot(x, y, z, label='Zadanie1')
ax.legend()
plt.show()

#Zadanie 2
np.random.seed(19680801)
def randrange(n, vmin, vmax):
    return(vmax-vmin) * np.random.rand(n) + vmin

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
n = 50
for c, m, zlow, zhigh in [('r', 'o', -50, -25), ('b', '^', -30, -5), ('y', '4', -27, -19), ('k', 'X', -7, 12),
                          ('m', 'd', 23, 50)]:
    xs = randrange(n, 23, 32)
    ys = randrange(n, 0, 100)
    zs = randrange(n, zlow, zhigh)
    ax.scatter(xs, ys, zs, c=c, marker=m)

ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
plt.show()

#Zadanie 3 problem z ułożeniem wykresów
fig = plt.figure(figsize = plt.figaspect(0.2))
ax = fig.add_subplot(111, projection='3d')
ax2 = fig.add_subplot(121, projection='3d')
ax3 = fig.add_subplot(131, projection='3d')
ax4 = fig.add_subplot(141, projection='3d')
ax5 = fig.add_subplot(151, projection='3d')
X = np.arange(-5, 5, 0.25)
Y = np.arange(-5, 5, 0.25)
X, Y = np.meshgrid(X, Y)
R = np.sqrt(X**2 + Y**2)
Z = np.sin(R)
surf = ax.plot_surface(X, Y, Z, cmap=cm.viridis, linewidth=0, antialiased=False)
surf2 = ax2.plot_surface(X, Y, Z, cmap=cm.plasma, linewidth=0, antialiased=False)
surf3 = ax3.plot_surface(X, Y, Z, cmap=cm.inferno, linewidth=0, antialiased=False)
surf4 = ax4.plot_surface(X, Y, Z, cmap=cm.Oranges, linewidth=0, antialiased=False)
surf5 = ax5.plot_surface(X, Y, Z, cmap=cm.YlGn, linewidth=0, antialiased=False)
ax.set_zlim(-1.01, 1.01)
fig.colorbar(surf)
fig.colorbar(surf2)
fig.colorbar(surf3)
fig.colorbar(surf4)
fig.colorbar(surf5)
plt.show()

#Zadanie5 problem z ułożeniem wykresów
fig = plt.figure(figsize = plt.figaspect(0.5))
ax = fig.add_subplot(111, projection='3d')
ax2 = fig.add_subplot(121, projection='3d')
X = np.arange(-5, 5, 0.25)
Y = np.arange(-5, 5, 0.25)
X, Y = np.meshgrid(X, Y)
R = np.sqrt(X**2 + Y**2)
Z = np.sin(R)
surf = ax.plot_surface(X, Y, Z, cmap=cm.viridis, linewidth=0, antialiased=False)
surf2 = ax2.plot_surface(X, Y, Z, cmap=cm.plasma, linewidth=0, antialiased=True)
ax.set_zlim(-1.01, 1.01)
fig.colorbar(surf)
fig.colorbar(surf2)
plt.show()
