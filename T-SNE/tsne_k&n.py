from tsne import gen_disk
from threeD_tsne import gen_3d_disk
import numpy as np
import matplotlib.pyplot as plt
from sklearn.manifold import TSNE

ratios = [0.2, 0.1, 0.05, 0.02, 0.01, 0.002]
diff_n = [500, 1000, 2000, 5000, 10000, 20000]
d1 = 2
m = 2
d2 = 5

def plot(ratios, diff_n):
    fg, ax = plt.subplots(len(diff_n), len(ratios), figsize=(30, 30))
    for i in range(len(diff_n)):
        for j in range(len(ratios)):
            disk = gen_disk(n=diff_n[i], d1=d1, d2=d2)
            k = int(ratios[j] * diff_n[i])
            perplex = int((k - 1) / 3)
            disk_embedded = TSNE(n_components=m, learning_rate='auto', init='random', perplexity=perplex).fit_transform(disk)
            ax[i,j].scatter(disk_embedded[:,0], disk_embedded[:,1], s=1)
            ax[j, i].set_xlim([-130, 130])
            ax[j, i].set_ylim([-130, 130])
            ax[j, i].axis("off")
            ax[i,j].set_title(f"k/n={ratios[j]},  k={k}, n={diff_n[i]}")
    fg.canvas.draw()
    #fg.suptitle('T-SNE Display with Respect to the Ratio of k/n in 2D', fontsize=20)
    plt.savefig("k_vs_n of T-SNE_3D.png")


def plot_3d2(ratios, diff_n):
    fig, ax = plt.subplots(len(diff_n), len(ratios), figsize=(30, 30))
    for i in range(len(diff_n)):
        for j in range(len(ratios)):
            disk = gen_3d_disk(n=diff_n[i], d1=d1, d2=d2)
            k = int(ratios[j] * diff_n[i])
            perplex = int((k - 1) / 3)
            disk_embedded = TSNE(n_components=m, learning_rate='auto', init='random', perplexity=perplex).fit_transform(disk)
            ax[i, j].scatter(disk_embedded[:,0], disk_embedded[:,1], s=1)
            ax[i, j].set_xlim([-130, 130])
            ax[i, j].set_ylim([-130, 130])
            ax[i, j].axis("off")
            ax[i, j].set_title(f"k/n={ratios[j]},  k={k}, n={diff_n[i]}")
    fig.canvas.draw()
    #fig.suptitle('T-SNE Display with Respect to the Ratio of k/n in 3D', fontsize=20)
    plt.savefig("k_vs_n of_T-SNE in 3D.png")

def plot_3d(ratios, diff_n):
    fig = plt.figure(figsize=(30, 30))
    for i in range(len(diff_n)):
        for j in range(len(ratios)):
            disk = gen_3d_disk(n=diff_n[i], d1=d1, d2=d2)
            k = int(ratios[j] * diff_n[i])
            perplex = int((k - 1) / 3)
            disk_embedded = TSNE(n_components=m, learning_rate='auto', init='random', perplexity=perplex).fit_transform(disk)
            ax = fig.add_subplot(len(diff_n), len(ratios), i*len(diff_n)+j+1, projection='3d')
            ax.scatter(disk_embedded[:,0], disk_embedded[:,1], disk_embedded[:,2], s=1)
            ax.set_xlim([-130, 130])
            ax.set_ylim([-130, 130])
            ax.axis("off")
            #ax.set_title(f"k/n={ratios[j]},  k={k}, n={diff_n[i]}")
    fig.canvas.draw()
    fig.suptitle('T-SNE Display with Respect to the Ratio of k/n in 3D', fontsize=20)
    plt.savefig("k_vs_n of_T-SNE_3D.png")

#plot(ratios, diff_n)

plot_3d2(ratios, diff_n)