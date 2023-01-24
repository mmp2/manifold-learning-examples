import random
import numpy as np
import matplotlib.pyplot as plt
import scipy 

# Step 1
a = 10
b = 5
K = 2
sigma = b/4
n = 8000

# Step 2.a
mu_Xs = np.random.uniform(0, a, K)
mu_Ys = np.random.uniform(0, b, K)
mu = np.vstack((mu_Xs, mu_Ys)).T

# Step 2.a
mu = np.zeros((K, 2))
mu[:, 1] = b/2
for i in range(K):
    mu[i, 0] = a/(2*(K-1)+2) * (2*i+1)


# Step 3.a
pi_list = np.zeros(K)
for i in range(K):
    pi_list[i] = 1/K

# Step 4

groups = []
points = np.empty((1, 2))

for i in range(K):
    group = np.random.multivariate_normal(mu[i], sigma** 2 * np.eye(2), round(pi_list[i]*n))
    points = np.vstack((points, group))
    groups.append(group)


# Step 5 
points = np.delete(points, np.argwhere((points[:, 1] > b) | (points[:, 1]  < 0)), axis=0)
points = np.delete(points, np.argwhere((points[:, 0] > a) | (points[:, 0]  < 0)), axis=0)

for i in range(len(groups)):
    groups[i] = np.delete(groups[i], np.argwhere((groups[i][:, 1] > b) | (groups[i][:, 1]  < 0)), axis=0)
    groups[i] = np.delete(groups[i], np.argwhere((groups[i][:, 0] > a) | (groups[i][:, 0]  < 0)), axis=0)
print(points.shape)

def plot_rect():
    colors = ["green", "blue", "grey"]
    for i in range(len(groups)):
        plt.scatter(groups[i][:, 0], groups[i][:, 1], c=colors[i], s=1)
    plt.scatter(mu[:,0], mu[:,1], c="red")
    plt.vlines([0, a], 0, b, colors="red")
    plt.hlines([0, b], 0, a, colors="red")
    #plt.scatter(points[:, 0], points[:, 1], s=1)
    plt.title(f"2.b, 3.a, n={n}, K={K}, a={a}, b={b}, sigma=b/4")
    plt.show()



def make_swiss_roll(points):
    X = points[:, 0]
    Y = points[:, 1]
    length_z = 10
    t = 1.5 * np.pi * (X / a * 2 + 1)
    y = Y / b * length_z
    x = t * np.cos(t)
    z = t * np.sin(t)
    data = np.vstack((x, y, z))
    return data

def make_torus(points):
    X = points[:, 0]
    Y = points[:, 1]
    sigma = 2*np.pi*Y/b
    phi = 2*np.pi*X/a
    x = (a + b * np.cos(sigma)) * np.cos(phi)
    y = (a + b * np.cos(sigma)) * np.sin(phi)
    z = b * np.sin(sigma)
    data = np.vstack((x, y, z))
    return data

def plot_3d(data):
    fig = plt.figure(figsize=(8, 7))
    ax = plt.axes(projection="3d")
    colors = ["green", "blue", "grey"]
    for i in range(len(data)):
        ax.scatter(data[i][0, :], 
                data[i][1, :], 
                data[i][2, :], c=colors[i], s=20, alpha=0.8)
    plt.show()

# Variable Density
# Plot the rectangle in 2D
plot_rect()

# Plot the Swiss Roll transformed from the rectangle in 3D
res = []
for group in groups:
    res.append(make_swiss_roll(group))
plot_3d(res)

# Plot the torus transformed from the rectangle in 3D
res = []
for group in groups:
    res.append(make_torus(group))
plot_3d(res)
