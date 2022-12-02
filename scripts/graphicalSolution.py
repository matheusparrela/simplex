from scipy.spatial import HalfspaceIntersection, ConvexHull
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
import numpy as np


def f(x1, x2):
    return 3 * x1 + 5 * x2


resticoes = [
    [-1, 0., 0.],  # x₁ ≥ 0
    [0., -1., 0.],  # x₂ ≥ 0
    [1., 0., -4.],  # x₁ ≤ 4
    [0., 2., -12.],  # 2x₁ ≤ 12
    [3., 2., -18.]  # 3x₁ + x₂ ≤ 18
]

pp = [0.5, 0.5]
xlim = (-1, 10)


def plotagraf(resticoes, pp, xlim, ylim):
    hs = HalfspaceIntersection(np.array(resticoes), np.array(pp))
    fig = plt.figure()
    ax = fig.add_subplot(aspect='equal')
    ax.set_xlim(xlim)
    ax.set_ylim(ylim)

    k = np.linspace(-15, 10, 100)
    i = np.linspace(-15, 10, 100)

    X, Y = np.meshgrid(k, i)
    Z = f(X, Y)

    x = np.linspace(*xlim, 100)

    for h in resticoes:
        if h[1] == 0:
            ax.axvline(-h[2] / h[0], color="#2c3e50")
        else:
            ax.plot(x, (-h[2] - h[0] * x) / h[1], color="#2c3e50")

    x, y = zip(*hs.intersections)
    points = list(zip(x, y))
    convex = ConvexHull(points)
    polygon = Polygon([points[v] for v in convex.vertices], color="#FF69B4")
    ax.add_patch(polygon)
    ax.contour(X, Y, Z, 50)
    ax.plot(x, y, 'o', color="#e67e22")


plotagraf(resticoes, pp, xlim, xlim)
plt.show()
