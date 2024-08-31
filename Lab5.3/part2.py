import numpy as np
from matplotlib import pyplot as plt

fig = plt.figure()
fig.set_size_inches(12, 8)
fig.subplots_adjust(wspace=0.3, hspace=0.3)
x = np.linspace(0, 10, 100)
y = np.linspace(0, 10, 100)
x, y = np.meshgrid(x, y)

z = x**(1/4) + y**(1/4)
ax = fig.add_subplot(231, projection='3d')
ax.plot_surface(x, y, z, cmap="viridis")
# ax.plot(x, y, z)
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
ax.set_title('z=x**(1/4)+y**(1/4)')

z = x**2 - y**2
ax = fig.add_subplot(232, projection='3d')
ax.plot_surface(x, y, z, cmap="viridis")
# ax.plot(x, y, z)
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
ax.set_title('z=x**2+y**2')

z = 2*x - 3*y
ax = fig.add_subplot(233, projection='3d')
ax.plot_surface(x, y, z, cmap="viridis")
# ax.plot(x, y, z)
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
ax.set_title('z=2x+3y')

z = x**2 + y**2
ax = fig.add_subplot(234, projection='3d')
ax.plot_surface(x, y, z, cmap="viridis")
# ax.plot(x, y, z)
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
ax.set_title('z=x**2+y**2')

z = 2 + 2*x + 2*y - x**2 - y**2
ax = fig.add_subplot(235, projection='3d')
ax.plot_surface(x, y, z, cmap="viridis")
# ax.plot(x, y, z)
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
ax.set_title('z=2+2x+2y-x**2-y**2')

plt.show()
