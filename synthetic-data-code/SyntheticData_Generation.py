#!/usr/bin/env python
# coding: utf-8

# In[1]:


# --------------------------------------------------------------
# This file will generate four datasets used to perform manifold 
# learning: the rectangle, the rectangele with hole, swiss roll,
# and torus.
# Four datasets' variable names:
# 1.rect
# 2.rect_hole
# 3.swiss_roll
# 4.torus
# --------------------------------------------------------------
import matplotlib.pyplot as plt
import math
import numpy as np
import random
"""
a: length
b: width
n: number of points
seed: random seed, default = 10
dim: want to have 'dim' dimension square matrix with other entires zero. default dim=20
plot: whether want to show plot, default not show
"""
def make_rect(a,b,n,seed=10,dim=20,plot=False):
    np.random.seed(seed)  #set random seed to be 10
    x = np.random.uniform(2,a+2,n)
    y = np.random.uniform(2,b+2,n)
    rect = np.array([x,y]).T
    rect = np.append(rect,[[0]*(dim-2)]*n,1)
    #plot
    if plot:
        plt.scatter(rect[:,0],rect[:,1],s=2)
        plt.title("Rectangle")
        plt.show()
    return rect
#make_rect(4,3,5000)
#np.savetxt('rect_n5000_dim20_a30b1.9.csv', make_rect(4,3,5000), delimiter=',')


"""
a: length
b: width
n: number of points, but not sample size since have hole, samller than ture sampled points
seed: random seed, default = 980
dim: want to have 'dim' dimension square matrix with other entires zero. default dim=20
plot: whether want to show plot, default not show
"""
def make_rect_hole(a,b,n,seed=980,dim=20,plot=False):
    np.random.seed(seed)  
    x = np.random.uniform(2,a+2,n)
    y = np.random.uniform(2,b+2,n)
    rect_tempt = np.array([x,y])
    rect_hole = []
    for i in rect_tempt.T:
        if i[0] < 2+a/3-a/12 or i[0] > 2+(2*a)/3+a/12:
            rect_hole.append(i)
        elif i[1] < 2+b/3  or i[1] > 2+(2*b)/3:
            rect_hole.append(i)
    rect_hole = np.array(rect_hole)
    sample_size = len(rect_hole)
    print("sample size is:",sample_size)
    rect_hole = np.append(rect_hole,[[0]*(dim-2)]*sample_size,1)
    #plot
    if plot:
        plt.scatter(rect_hole[:,0],rect_hole[:,1],s=2)
        plt.show()
    return rect_hole
#make_rect_hole(4,3,6000)
#np.savetxt('rectHole_n5000_dim20_a30b1.9.csv', rect_hole, delimiter=',')


"""
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




"""
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


# In[ ]:




