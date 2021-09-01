from pylab import *
from mpl_toolkits.mplot3d import Axes3D

A = np.array([[1, 2, -1],
              [8, -5, 2]]
             )
B = np.array([1, 12])


def q(a, y, z):
    return a ** 2 + y ** 2 + z ** 2


print(f'нормальное псевдорешение: {np.linalg.lstsq(A, B, rcond=None)}')

fig = figure()
ax = Axes3D(fig, auto_add_to_figure=False)
fig.add_axes(ax)
X = np.arange(-50, 50, 1)
Y = np.arange(-50, 50, 1)
X, Y = np.meshgrid(X, Y)
ax.plot_surface(X, Y, q(X, 5 * X - 14, 21 * X - 1))
show()
