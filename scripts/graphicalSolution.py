from scipy.spatial import HalfspaceIntersection, ConvexHull
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
import numpy as np

'''
z = [3, 5]
restr = [[1, 0], [0, 2], [3, 2]]
b = [[4], [12], [18]]
pp = [0.5, 0.5]
xlim = (-1, 10)
'''


def formatTable(restr, b):
    restr = np.vstack([restr, [[-1, 0], [0, -1]]])
    b = np.vstack([np.array(b) * -1, [[0], [0]]])
    table = np.hstack([restr, b])
    return table


def plotagraf(z, table, pp, xlim, ylim, solution):
    hs = HalfspaceIntersection(np.array(table), np.array(pp))
    fig = plt.figure()
    ax = fig.add_subplot(aspect='equal')


    k = np.linspace(-15, 30, 100)
    i = np.linspace(-15, 30, 100)

    X, Y = np.meshgrid(k, i)
    Z = z[0] * X + z[1] * Y

    x = np.linspace(*xlim, 100)

    for h in table:
        if h[1] == 0:
            ax.axvline(-h[2] / h[0], color="#2c3e50")
        else:
            ax.plot(x, (-h[2] - h[0] * x) / h[1], color="#2c3e50")

    x, y = zip(*hs.intersections)
    points = list(zip(x, y))
    xlim = (-1, max([p[0] for p in points]) + 1)
    ylim = (-1, max([p[1] for p in points]) + 1)
    ax.set_xlim(xlim)
    ax.set_ylim(ylim)
    convex = ConvexHull(points)
    polygon = Polygon([points[v] for v in convex.vertices], color="#6A95BF")
    ax.add_patch(polygon)
    ax.contour(X, Y, Z, 50)
    ax.plot(x, y, 'o', color="#e67e22")
    plt.show()


'''
plotagraf(z, formatTable(restr, b), pp, xlim, xlim)
plt.show()
'''
