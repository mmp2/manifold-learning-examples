import numpy as np
import matplotlib.pyplot as plt
from sklearn.manifold import TSNE
from networkx import random_regular_graph, adjacency_matrix

m = 2
#n = 10000
diff_k = [10, 50, 100, 500, 1000, 2000]
diff_k = [40, 400, 4000]

def plot_k(k_list, n=40000):
    fg, ax = plt.subplots(len(k_list), figsize=(5, 30))
    for i in range(len(k_list)):
        graph = np.array(adjacency_matrix(random_regular_graph(d=k_list[i], n=n)).todense())
        perplex = int((k_list[i] - 1) / 3)
        graph_embedded = TSNE(n_components=m, learning_rate='auto', init='random', perplexity=perplex).fit_transform(graph)
        ax[i].scatter(graph_embedded[:,0], graph_embedded[:,1], s=2)
        ax[i].axis("equal")
        ax[i].set_title(f"k={k_list[i]}, n={n}")
    fg.canvas.draw()
    plt.savefig("T-SNE for k-regular_vs k.png")


#plot(diff_p, diff_n)
plot_k(k_list=diff_k)