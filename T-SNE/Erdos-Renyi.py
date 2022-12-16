import numpy as np
import matplotlib.pyplot as plt
from sklearn.manifold import TSNE
import random

m = 2
diff_n = [500, 1000, 2000]
diff_p = [0.25, 0.5, 0.75]
#n = 10000
diff_k = [50, 100, 200, 500, 1000]

#diff_n = [1000, 2000]
#diff_p = [0.1, 0.3, 0.5]

def gen_erdos_renyi(p, n=10000):
    A = np.zeros((n, n))
    for i in range(n):
        for j in range(i):
            A[i, j] = np.random.choice([0, 1], size=1, p=[1-p, p])
            A[j, i] = A[i, j]
    return A

def plot_k(k_list, n_list):
    fg, ax = plt.subplots(len(k_list), len(n_list), figsize=(30, 30))
    for i in range(len(k_list)):
        for j in range(len(n_list)):
            p = k_list[i]/n_list[j]
            graph = gen_erdos_renyi(p=p, n=n_list[j])
            perplex = int((k_list[i] - 1) / 3)
            graph_embedded = TSNE(n_components=m, learning_rate='auto', init='random', perplexity=perplex).fit_transform(graph)
            ax[i,j].scatter(graph_embedded[:,0], graph_embedded[:,1], s=2)
            ax[i,j].axis("equal")
            ax[i,j].set_title(f"k={k_list[i]}, n={n_list[j]}, p={p}")
    fg.canvas.draw()
    plt.savefig("T-SNE for Erdos Renyi_vs k.png")

def plot(p_list, n_list):
    fg, ax = plt.subplots(len(p_list), len(n_list), figsize=(30, 30))
    for i in range(len(p_list)):
        for j in range(len(n_list)):
            graph = gen_erdos_renyi(p=p_list[i], n=n_list[j])
            k = (n_list[j]-1)*p_list[i]
            perplex = int((k - 1) / 3)
            graph_embedded = TSNE(n_components=m, learning_rate='auto', init='random', perplexity=perplex).fit_transform(graph)
            ax[i,j].scatter(graph_embedded[:,0], graph_embedded[:,1], s=2)
            ax[i,j].axis("equal")
            ax[i,j].set_title(f"p={p_list[i]}, n={n_list[j]}, n_neighbors={int(k)}")
    fg.canvas.draw()
    plt.savefig("T-SNE for Erdos Renyi_vs p.png")

#plot(diff_p, diff_n)
plot_k(k_list=diff_k, n_list=diff_n)