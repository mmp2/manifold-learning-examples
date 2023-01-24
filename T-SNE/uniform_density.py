import numpy as np
import matplotlib.pyplot as plt

a = 10
b = 5
num = 8000
xlist = np.random.uniform(0, a, num) 
ylist = np.random.uniform(0, b, num)
plt.scatter(xlist, ylist, s=5)
plt.vlines([0, a], 0, b, colors="red")
plt.hlines([0, b], 0, a, colors="red")
plt.show()

points = np.vstack((xlist, ylist)).T

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

def plot_swiss_roll(data):
    fig = plt.figure(figsize=(8, 7))
    ax = plt.axes(projection="3d")
    colors = ["green", "blue", "grey"]
    ax.scatter(data[0, :], 
                data[1, :], 
                data[2, :], c=colors[0], s=10, alpha=0.8)
    plt.show()

swiss_roll = make_swiss_roll(points)
print(points.shape)
plot_swiss_roll(swiss_roll)
torus = make_torus(points)
plot_swiss_roll(torus)