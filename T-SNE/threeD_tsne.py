import numpy as np
import matplotlib.pyplot as plt
from sklearn.manifold import TSNE
from sklearn.neighbors import NearestNeighbors

d1 = 0
m = 3

def gen_3d_disk(n=10000, d1=2, d2=10, seed=999):
    n = n
    r2 = (d1/2)**2
    R2 = (d2/2)**2
    np.random.seed(seed)
    rad = np.random.uniform(low=r2, high=R2, size=n)  # radius
    theta = np.random.uniform(low=0, high=2*np.pi, size=n)  # angle
    x = np.sqrt(rad) * np.cos(theta)
    y = np.sqrt(rad) * np.sin(theta)
    z = np.sin(np.pi*x)/x * np.sin(np.pi*y)/y
    return np.vstack((x, y, z)).T

def plot_one(disk):
    fig = plt.figure(figsize=(10,8))  # set figure size
    ax = fig.add_subplot(projection='3d')
    ax.scatter(disk[:,0], disk[:,1], disk[:,2], s=1) # plot random points
    ax.axis('on')
    #ax.grid(True)
    fig.canvas.draw()
    plt.show()

def plot_tsne(k, disk):
    fig = plt.figure(figsize=(10,8))  # set figure size
    ax = fig.add_subplot(projection='3d')
    perplex = int((k - 1) / 3)
    disk_embedded = TSNE(n_components=m, learning_rate='auto', init='random', perplexity=perplex).fit_transform(disk)
    ax.scatter(disk_embedded[:,0], disk_embedded[:,1], disk_embedded[:,1], s=3)
    plt.show()

#disk = gen_3d_disk(d1=d1)
#plot_one(disk)
#plot_tsne(10, disk)
