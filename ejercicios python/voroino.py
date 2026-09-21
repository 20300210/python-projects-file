import matplotlib.pyplot as plt
import numpy as np
from scipy.spatial import Voronoi, voronoi_plot_2d

#p = np.random.rand(30, 2)
#plt.triplot(p[:, 0], p[:, 1])
#plt.show()

#p = np.random.rand(30, 2)

#vor = Voronoi(p)
#voronoi_plot_2d(vor)
#plt.show()

p = np.random.rand(30, 2)

fig, axes = plt.subplots(1, 2, figsize=(12, 6))

# Triangulación de Delaunay
axes[0].triplot(p[:, 0], p[:, 1])
axes[0].plot(p[:, 0], p[:, 1], 'o')
axes[0].set_title("Triangulación de Delaunay")

# Diagrama de Voronoi
vor = Voronoi(p)
voronoi_plot_2d(vor, ax=axes[1])
axes[1].set_title("Diagrama de Voronoi")

plt.show()
