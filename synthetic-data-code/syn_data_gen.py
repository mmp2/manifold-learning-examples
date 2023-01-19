#!/usr/bin/env python
# coding: utf-8

# In[35]:


###### --------------------------------------------------------------
# This file will generate datasets used for performing manifold 
# learning, including both uniform and variable density datasets
# generation. The variable density contains K numbers of normal 
# distributions in different datasets.
# Contributions: Yujia Wu, Murray Kuang
# --------------------------------------------------------------
#import packages
import matplotlib.pyplot as plt
import math
import numpy as np
import random
# --------------------------------------------------------------
# Utility Functions:
def torus_prep(points, a, b):
    X = points[:, 0]
    Y = points[:, 1]
    sigma = 2*np.pi*Y/b
    phi = 2*np.pi*X/a
    x = (a + b * np.cos(sigma)) * np.cos(phi)
    y = (a + b * np.cos(sigma)) * np.sin(phi)
    z = b * np.sin(sigma)
    data = np.vstack((x, y, z))
    return data.T

def swiss_roll_prep(points, a, b):
    X = points[:, 0]
    Y = points[:, 1]
    length_z = 10
    t = 1.5 * np.pi * (X / a * 2 + 1)
    y = Y / b * length_z
    x = t * np.cos(t)
    z = t * np.sin(t)
    data = np.vstack((x, y, z))
    return data.T
#----------------------------------------------------------------


""" Return rectangle or rectangle with hole Dataset 
a: length
b: width
n: number of points. If hole=True, n is larger than the true sampled points
seed: random seed, default = 10
dim: want to have 'dim' dimension square matrix with other entires zero. default dim=20
plot: whether want to show plot, default not show
hole: if true, there would be a hole located at the center of rect
"""
def make_rect(a,b,n,seed=10,dim=20,plot=False,hole=False):
    np.random.seed(seed)  
    x = np.random.uniform(2,a+2,n)
    y = np.random.uniform(2,b+2,n)
    rect=[]
    if hole:
        for i in np.array([x,y]).T:
            if i[0] < 2+a/3-a/12 or i[0] > 2+(2*a)/3+a/12:
                rect.append(i)
            elif i[1] < 2+b/3  or i[1] > 2+(2*b)/3:
                rect.append(i)
        rect = np.array(rect)    
        sample_size = len(rect)
        print("sample size is:",sample_size)
        rect = np.append(rect,[[0]*(dim-2)]*sample_size,1)
    else:
        rect = np.array([x,y]).T
        rect = np.append(rect,[[0]*(dim-2)]*n,1)
    #plot
    if plot:
        plt.scatter(rect[:,0],rect[:,1],s=2)
        plt.title("Rectangle")
        plt.show()
    return rect
#np.savetxt('rect_n5000_dim20_a30b1.9.csv', make_rect(4,3,5000), delimiter=',')
#make_rect(4,3,6000,plot=True,hole=True,seed=980)


"""Return Uniform Swiss Roll Dataset
a: length of swiss roll in angular direction
b: length of swiss roll in z direction
n: number of points
seed: random seed, default = 101
dim: want to have 'dim' dimension square matrix with other entires zero. default dim=20
plot: whether want to show plot, default not show
"""
def make_swiss(a,b,n,seed=101,dim=20,plot=False):
    np.random.seed(seed) 
    phi = a*np.random.rand(n)
    xi = np.random.rand(n)
    Z = b*np.random.rand(n)
    X = 1./6*(phi + min(a,b))*np.sin(phi)
    Y = 1./6*(phi + min(a,b))*np.cos(phi)

    swiss_roll = np.array([X, Y, Z]).T
    swiss_roll = np.append(swiss_roll,[[0]*(dim-3)]*n,1)

    #rotate with X coordiante 90 degree
    theta = np.radians(90)
    rotation = np.identity(dim)
    rotation[2,2]=np.cos(theta)
    rotation[1,2]=-np.sin(theta)
    rotation[2,1]=np.sin(theta)
    rotation[1,1]=np.cos(theta)
    swiss_roll=rotation.dot(swiss_roll.T).T
    
    #plot
    if plot:
        fig = plt.figure(figsize=(8, 7))
        ax = plt.axes(projection="3d")
        ax.scatter(swiss_roll[:,0],swiss_roll[:,1],swiss_roll[:,2],c=Z, s=10, alpha=0.6)
        ax.set_title("Swiss roll")
        plt.show()
    return swiss_roll

#make_swiss(8,6,5000,plot=True)
#np.savetxt('swissRoll_n5000_dim20_a20b1.9.csv', swiss_roll, delimiter=',')




"""Return Uniform Torous Dataset
R: the distance from the center of the tube to the center of the torus
r: the radius of the tube.
n: number of points
seed: random seed, default = 1434
dim: want to have 'dim' dimension square matrix with other entires zero. default dim=20
plot: whether want to show plot, default not show
"""
def make_torus(R,r,n,seed=1434,dim=20,plot=False):
    np.random.seed(seed) 
    x1 = np.random.uniform(0, 2*np.pi*R,n)
    x2 = np.random.uniform(0, 2*np.pi*r,n)
    theta = (2 * np.pi * x2) / r
    phi = (2 * np.pi * x1) / R
    x = (R + r*np.cos(theta)) * np.cos(phi)
    y = (R + r*np.cos(theta)) * np.sin(phi)
    z = r * np.sin(theta)
    torus = np.array([x, y, z]).T
    torus = np.append(torus,[[0]*(dim-3)]*n,1)
    #plot
    if plot:
        fig = plt.figure(figsize=(8,7)) 
        ax = plt.axes(projection="3d")
        ax.scatter(torus[:,0], torus[:,1], torus[:,2], c=z,s=3)
        ax.axes.set_xlim3d(left=-R, right=R) 
        ax.axes.set_ylim3d(bottom=-R, top=R) 
        ax.axes.set_zlim3d(bottom=-R, top=R)
        plt.title("Torus")
        plt.show()
    return torus
#make_torus(16,1.9,10000,plot=True)
#np.savetxt('torus_n10000_dim20_R16r1.9.csv',torus, delimiter=',')


""" Return 3D brick-like Dataset
a: length
b: width
c: height
n: number of points
seed: random seed, default = 10
dim: want to have 'dim' dimension square matrix with other entires zero. default dim=20
plot: whether want to show plot, default not show
"""
def make_brick(a,b,c,n,seed=10,dim=20,plot=False):
    np.random.seed(seed) 
    x = np.random.uniform(0,a,n)
    y = np.random.uniform(0,b,n)
    Z = np.random.uniform(0,c,n)
    brick = np.array([x,y,Z]).T
    brick = np.append(brick,[[0]*(dim-3)]*n,1)
    #plot
    if plot:
        fig = plt.figure(figsize=(8, 7))
        ax = plt.axes(projection="3d")
        ax.scatter(brick[:,0],brick[:,1],brick[:,2],c=x, s=10, alpha=0.6)
        ax.set_title("Brick")
        plt.show()
    return brick


"""Return Non-Uniform Swiss Roll Dataset
a: length of swiss roll in angular direction
b: length of swiss roll in z direction
sigma: standard deviation of normal distributions
n: number of points, but not sample size since have hole, larger than ture sampled points 
K: number of centers of normal distributions, default=2
grid: if True, the centers would be aligned in a grid. Otherwise, they would be placed randomly.
seed: random seed, default = 999
dim: want to have 'dim' dimension square matrix with other entires zero. default dim=20
plot: whether want to show plot, default not show
"""
def non_uniform_swiss(a, b, sigma, n, K=2,grid=True, seed=999,dim=20,plot=False):
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
        p = swiss_roll_prep(group, a, b)
        res.append(p)
        data = np.vstack((data, p))
    data = data[1:]
    #swiss_roll = non_uniform_swiss(a=a, b=b, K=3, sigma=6/4, n=10000, grid=True, seed=999)
    m=len(data[:,0])
    data = np.append(data,[[0]*(dim-3)]*m,1)
    print(f"sample size:{m}")
    #plot
    if plot:
        fig = plt.figure(figsize=(8, 7))
        ax = plt.axes(projection="3d")
        ax.scatter(data[:,0],data[:,1],data[:,2],c=data[:,2], s=2, alpha=0.6)
        ax.set_title("Variable density swiss roll")
        plt.show()
    return data
#non_uniform_swiss(plot=True)


"""Return Non-Uniform Torous Dataset
a: the distance from the center of the tube to the center of the torus
b: the radius of the tube.
sigma: standard deviation of normal distributions
n: number of points, but not sample size since have hole, larger than ture sampled points 
K: number of centers of normal distributions
grid: if True, the centers would be aligned in a grid. Otherwise, they would be placed randomly.
seed: random seed, default = 999
dim: want to have 'dim' dimension square matrix with other entires zero. default dim=20
plot: whether want to show plot, default not show
"""
def non_uniform_torus(a, b,  sigma, n,K=2,grid=True, seed=999,dim=20,plot=False):
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
        p = torus_prep(group, a, b)
        res.append(p)
        data = np.vstack((data, p))
    data = data[1:]
    #torus=non_uniform_torus(a=a, b=b, K=2, sigma=sigma, n=33000, grid=True, seed=99)
    m=len(data[:,0])
    print(f"sample size:{m}")
    data = np.append(data,[[0]*(dim-3)]*m,1)
    #plot
    if plot:
        fig = plt.figure(figsize=(8,7)) 
        ax = plt.axes(projection="3d")
        ax.scatter(data[:,0], data[:,1], data[:,2], c=data[:,2],s=3)
        plt.title("Variable density Torus")
        plt.show()
    return data
#non_uniform_torus(plot=True)


"""Return Non-Uniform Rectangle or Non-Uniform Rectangle with Hole Dataset
a: length
b: width
sigma: standard deviation of normal distributions
n: number of points, but not sample size since have hole, larger than ture sampled points 
K: number of centers of normal distributions, default=2
random: if true, the center will be random in space. Otherwise, centers are arranges some way
seed: random seed, default = 999
dim: want to have 'dim' dimension square matrix with other entires zero. default dim=20
plot: whether want to show plot, default not show
hole: if true, there would be a hole located at the center of rect
"""
def non_uniform_rect(a,b,sigma,n,K=2,random=False,seed=10,dim=20,plot=False,hole=False):
    if random:
        mu_Xs = np.random.uniform(0, a, K)
        mu_Ys = np.random.uniform(0, b, K)
        mu = np.vstack((mu_Xs, mu_Ys)).T
        #print(mu)
    else:
        mu = np.zeros((K, 2))
        mu[:, 1] = b/2
        for i in range(K):
            mu[i, 0] = a/(2*(K-1)+2) * (2*i+1)
        #print(mu)
    # Step 3.a
    pi_list = np.zeros(K)
    for i in range(K):
        pi_list[i] = 1/K
    # Step 4
    groups = []
    points = np.empty((1, 2))
    np.random.seed(10)
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

    def plot_rect():
        colors = ["green", "blue", "grey","firebrick"]
        #print(len(groups))
        for i in range(len(groups)):
            plt.scatter(groups[i][:, 0], groups[i][:, 1], c=colors[i], s=1)
        plt.scatter(mu[:,0], mu[:,1], c="red")
        plt.vlines([0, a], 0, b, colors="red")
        plt.hlines([0, b], 0, a, colors="red")
        #plt.scatter(points[:, 0], points[:, 1], s=1)
        plt.title(f"2.b, 3.a, n={n}, K={K}, a={a}, b={b}, sigma={sigma}")
        plt.show()

    if hole:
        for i in range(len(groups)):
            groups[i] = np.delete(groups[i], 
                              np.argwhere(((groups[i][:, 1] < (2*b)/3) & (groups[i][:, 1]  > b/3))&
                                         ((groups[i][:, 0] < (2*a)/3+a/12) & (groups[i][:, 0]  > a/3-a/12))), axis=0)
    if plot: plot_rect()

    rect0 = np.vstack((groups[0], groups[1],group[2]))
    m = len(rect0[:,0])
    rect = np.append(rect0,[[0]*(dim-2)]*m,1)
    print(f"sample size:{m}")
    return rect
#non_uniform_rect(a=36,b=1.9,sigma=36/8,n=18000,plot=True,hole=True)


# In[ ]:




