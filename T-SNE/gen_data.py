"""
Functions to generate density variable datasets of swiss roll and torus.

from gen_data import non_uniform_swiss
from gen_data import non_uniform_torus
from gen_data import uniform_swiss_roll
from gen_data import uniform_torus

a = longer side of the rectangle in 2d
b = shorter side of the rectangle in 2d
K = number of centers
sigma = standard deviation
grid: if True, the centers would align in a grid. Otherwise, they would align randomly.
n = number of points
seed = random seed
"""

import numpy as np

def make_torus(points, a, b):
    X = points[:, 0]
    Y = points[:, 1]
    sigma = 2*np.pi*Y/b
    phi = 2*np.pi*X/a
    x = (a + b * np.cos(sigma)) * np.cos(phi)
    y = (a + b * np.cos(sigma)) * np.sin(phi)
    z = b * np.sin(sigma)
    data = np.vstack((x, y, z))
    return data.T

def make_swiss_roll(points, a, b):
    X = points[:, 0]
    Y = points[:, 1]
    length_z = 10
    t = 1.5 * np.pi * (X / a * 2 + 1)
    y = Y / b * length_z
    x = t * np.cos(t)
    z = t * np.sin(t)
    data = np.vstack((x, y, z))
    return data.T

def non_uniform_swiss(a=10, b=5, K=2, sigma=5/4, n=10000, grid=True, seed=999):
    # Step 2.a
    if not grid:
        np.random.seed(seed)
        mu_Xs = np.random.uniform(0, a, K)
        mu_Ys = np.random.uniform(0, b, K)
        mu = np.vstack((mu_Xs, mu_Ys)).T
    else:
        # Step 2.b
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
        group = np.random.multivariate_normal(mu[i], sigma**2 * np.eye(2), round(pi_list[i]*n))
        points = np.vstack((points, group))
        groups.append(group)


    # Step 5 
    points = np.delete(points, np.argwhere((points[:, 1] > b) | (points[:, 1]  < 0)), axis=0)
    points = np.delete(points, np.argwhere((points[:, 0] > a) | (points[:, 0]  < 0)), axis=0)

    for i in range(len(groups)):
        groups[i] = np.delete(groups[i], np.argwhere((groups[i][:, 1] > b) | (groups[i][:, 1]  < 0)), axis=0)
        groups[i] = np.delete(groups[i], np.argwhere((groups[i][:, 0] > a) | (groups[i][:, 0]  < 0)), axis=0)

    res = []
    data = np.empty((1, 3))
    for group in groups:
        p = make_swiss_roll(group, a, b)
        res.append(p)
        data = np.vstack((data, p))
    data = data[1:]
    return data

def non_uniform_torus(a=10, b=5, K=2, sigma=5/4, n=10000, grid=True, seed=999):

    if not grid:
        # Step 2.a
        np.random.seed(seed)
        mu_Xs = np.random.uniform(0, a, K)
        mu_Ys = np.random.uniform(0, b, K)
        mu = np.vstack((mu_Xs, mu_Ys)).T
    else:
        # Step 2.b
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
        group = np.random.multivariate_normal(mu[i], sigma**2 * np.eye(2), round(pi_list[i]*n))
        points = np.vstack((points, group))
        groups.append(group)


    # Step 5 
    points = np.delete(points, np.argwhere((points[:, 1] > b) | (points[:, 1]  < 0)), axis=0)
    points = np.delete(points, np.argwhere((points[:, 0] > a) | (points[:, 0]  < 0)), axis=0)

    for i in range(len(groups)):
        groups[i] = np.delete(groups[i], np.argwhere((groups[i][:, 1] > b) | (groups[i][:, 1]  < 0)), axis=0)
        groups[i] = np.delete(groups[i], np.argwhere((groups[i][:, 0] > a) | (groups[i][:, 0]  < 0)), axis=0)

    res = []
    data = np.empty((1, 3))
    for group in groups:
        p = make_torus(group, a, b)
        res.append(p)
        data = np.vstack((data, p))
    data = data[1:]
    return data

def uniform_swiss_roll(a=10, b=5, num=10000, seed=999):
    np.random.seed(seed)
    xlist = np.random.uniform(0, a, num) 
    ylist = np.random.uniform(0, b, num)
    points = np.vstack((xlist, ylist)).T
    swiss_roll = make_swiss_roll(points, a, b)
    return swiss_roll

def uniform_torus(a=10, b=5, num=10000, seed=999):
    np.random.seed(seed)
    xlist = np.random.uniform(0, a, num) 
    ylist = np.random.uniform(0, b, num)
    points = np.vstack((xlist, ylist)).T
    torus = make_torus(points, a, b)
    return torus
