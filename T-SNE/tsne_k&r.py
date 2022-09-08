from tsne import gen_disk
import numpy as np
import matplotlib.pyplot as plt
from sklearn.manifold import TSNE

radius2 = [0.01, 0.05, 0.1, 0.2, 0.4, 0.8]
d1 = 2
m = 2
d2 = 5

dic = {}
with open("tsne_K_vs_R.txt", "r") as f:
    lines = f.read().splitlines()
    for line in lines:
        parts = line.split(", ")
        n = int(parts[0][2:])
        k = int(parts[1][2:])
        ratio = float(parts[3][11:])
        dic[(n, k)] = ratio

fg, ax = plt.subplots(1, len(radius2), figsize=(30, 5))
for i in range(len(radius2)):
    res_key, res_val = min(dic.items(), key=lambda x: abs(radius2[i] - x[1]))
    n = res_key[0]
    k = res_key[1]
    disk = gen_disk(n=n, d1=d1, d2=d2)
    perplex = int((k - 1) / 3)
    disk_embedded = TSNE(n_components=m, learning_rate='auto', init='random', perplexity=perplex).fit_transform(disk)
    ax[i].plot(disk_embedded[:,0], disk_embedded[:,1], '.')
    ax[i].axis('equal')
    ax[i].grid(True)
    ax[i].set_title(f"R={round(res_val, 3)},  k={k}, n={n}")
fg.canvas.draw()
plt.savefig("k_vs_R of T-SNE.png")

