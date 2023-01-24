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

print(mu)

# Step 3.a
pi_list = np.zeros(K)
for i in range(K):
    pi_list[i] = 1/K

print(sigma** 2 * np.eye(2))

# Step 4.a
points = np.empty((1, 2))
for i in range(K):
    points = np.vstack((points, np.random.multivariate_normal(mu[i], sigma** 2 * np.eye(2), round(pi_list[i]*n))))


points = np.delete(points, np.argwhere((points[:, 1] > b) | (points[:, 1]  < 0)), axis=0)
points = np.delete(points, np.argwhere((points[:, 0] > a) | (points[:, 0]  < 0)), axis=0)
#A = np.delete(points, np.where((points > a) | (points < 0))[0], axis=0)
#A = np.delete(A, np.where((A > b) | (A < 0))[0], axis=0)
print(points.shape)

plt.vlines([0, a], 0, b, colors="red")
plt.hlines([0, b], 0, a, colors="red")
plt.scatter(points[:, 0], points[:, 1])
plt.title(f"2.a, 3.a, n={n}, K={K}, a={a}, b={b}, sigma=b/3")
plt.show()

