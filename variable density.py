import random
import numpy as np
import matplotlib.pyplot as plt
import scipy 

a = 10
b = 5
K = 3
sigma = b/3
n = 100

# Step 2.a
mu_Xs = np.random.uniform(0, a, K)
mu_Ys = np.random.uniform(0, b, K)
mu = np.vstack((mu_Xs, mu_Ys)).T


# Step 3.a
pi_list = np.zeros(K)
for i in range(K):
    pi_list[i] = 1/K


# Step 4.a
points = np.empty((1, 2))
groups = []

for i in range(K):
    group = np.random.multivariate_normal(mu[i], sigma** 2 * np.eye(2), round(pi_list[i]*n))
    points = np.vstack((points, group))
    groups.append(group)


points = np.delete(points, np.argwhere((points[:, 1] > b) | (points[:, 1]  < 0)), axis=0)
points = np.delete(points, np.argwhere((points[:, 0] > a) | (points[:, 0]  < 0)), axis=0)
print(points.shape)


colors = ["green", "blue", "grey"]
plt.vlines([0, a], 0, b, colors="red")
plt.hlines([0, b], 0, a, colors="red")
plt.scatter(mu[:, 0], mu[:, 1], c="red")
for i in range(len(groups)):
    plt.scatter(groups[i][:, 0], groups[i][:, 1], c=colors[i])
#plt.scatter(points[:, 0], points[:, 1])
plt.title(f"2.a, 3.a, n={n}, K={K}, a={a}, b={b}, sigma=b/3")
plt.savefig("rectangle_random.png")
plt.show()
plt.close()

plt.vlines([0, a], 0, b, colors="red")
plt.hlines([0, b], 0, a, colors="red")
plt.scatter(mu[:, 0], mu[:, 1], c="red")
plt.scatter(points[:, 0], points[:, 1])
plt.title(f"2.a, 3.a, n={n}, K={K}, a={a}, b={b}, sigma=b/3")
plt.savefig("rectangle_random_cut.png")
plt.show()



