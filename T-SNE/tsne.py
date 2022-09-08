
import numpy as np
import matplotlib.pyplot as plt
from sklearn.manifold import TSNE
from sklearn.neighbors import NearestNeighbors


n = 10000
d1 = 2
m = 2
d2s = [2, 5, 10, 15]
n_neighs = [5, 7, 11, 22, 52, 100]

def gen_disk(n=10000, d1=2, d2=10, seed=999):
    n = n
    r2 = (d1/2)**2
    R2 = (d2/2)**2
    np.random.seed(seed)
    rad = np.random.uniform(low=r2, high=R2, size=n)  # radius
    theta = np.random.uniform(low=0, high=2*np.pi, size=n)  # angle
    x = np.sqrt(rad) * np.cos(theta)
    y = np.sqrt(rad) * np.sin(theta)
    return np.vstack((x, y)).T

def plot_one(disk):
    fg, ax = plt.subplots(1, 1)
    ax.plot(disk[:,0], disk[:,1], '.') # plot random points
    ax.axis('equal')
    ax.grid(True)
    fg.canvas.draw()
    plt.show()

def plot_one_red(disk, bounds):
    fg, ax = plt.subplots(1, 1)
    ax.plot(disk[:,0], disk[:,1], '.') # plot random points
    ax.plot(bounds[:,0], bounds[:,1], 'r.') # plot random points
    ax.axis('equal')
    ax.grid(True)
    fg.canvas.draw()
    plt.show()

def plot(n_neighs, d2s):
    fg, ax = plt.subplots(len(n_neighs), len(d2s), figsize=(30, 30))
    for i in range(len(n_neighs)):
        for j in range(len(d2s)):
            disk = gen_disk(n=n, d1=d1, d2=d2s[j])
            perplex = int((n_neighs[i] - 1) / 3)
            disk_embedded = TSNE(n_components=m, learning_rate='auto', init='random', perplexity=perplex).fit_transform(disk)
            ax[i,j].plot(disk_embedded[:,0], disk_embedded[:,1], '.')
            ax[i,j].axis('equal')
            ax[i,j].grid(True)
            ax[i,j].set_title(f"n={n}, d2={d2s[j]}, n_neighbors={n_neighs[i]}")
    fg.canvas.draw()
    plt.savefig("T-SNE for Uniform Disks.png")


def cal_radius_neigh(bound_points, disk, k):
    neigh = NearestNeighbors(n_neighbors=k)
    neigh.fit(disk)
    neigh_dist, neigh_ind = neigh.kneighbors(bound_points, return_distance=True)
    return np.max(neigh_dist)

'''
result_txt = "tsne_K_vs_N.txt"
diff_n = [1000, 2000, 4000, 8000]
diff_k = [5, 7, 22, 52, 100]
with open(result_txt, "w") as f:
    for n in diff_n:
        for k in diff_k:
            disk = gen_disk(n, d1=2, d2=5)
            bound_points = [[1,0], [0,1], [0.5, np.sqrt(3)/2], [0.5, -np.sqrt(3)/2], [-0.5, -np.sqrt(3)/2], [-0.5, np.sqrt(3)/2]]
            neigh_rad = cal_radius_neigh(bound_points, disk, k)
            f.write(f"n={n}, k={k}, neigh_rad={neigh_rad}, ratio_k/n={k/n}, ratio_area={neigh_rad**2}")
            f.write("\n")
'''

def bound_point(disk, num):
    dist = np.linalg.norm(disk, axis=1)
    indices = np.argsort(dist)[:num]
    res = disk[indices]
    return res

"""
result_txt = "tsne_K_vs_N_random.txt"
diff_n = [1000, 2000, 4000, 8000]
diff_k = [5, 7, 22, 52, 100]
with open(result_txt, "w") as f:
    for n in diff_n:
        for k in diff_k:
            disk = gen_disk(n, d1=2, d2=5)
            bound_points = bound_point(disk, 40)
            neigh_rad = cal_radius_neigh(bound_points, disk, k)
            f.write(f"n={n}, k={k}, neigh_rad={neigh_rad}, ratio_k/n={k/n}, ratio_area={neigh_rad**2}")
            f.write("\n")


disk = gen_disk(n, d1=2, d2=5)
bound_points = bound_point(disk, 40)
plot_one_red(disk, bound_points)
"""