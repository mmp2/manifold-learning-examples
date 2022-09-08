from tsne import gen_disk
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
            ax[i,j].plot(disk_embedded[:,0], disk_embedded[:,1], '.')
            ax[i,j].axis('equal')
            ax[i,j].grid(True)
            ax[i,j].set_title(f"k/n={ratios[j]},  k={k}, n={diff_n[i]}")
    fg.canvas.draw()
    plt.savefig("k_vs_n of T-SNE.png")

plot(ratios, diff_n)