#!/usr/bin/env python
# coding: utf-8

# In[38]:


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


# In[153]:


#rectangle no hole, 20 dimension, sample size 5000
n=5000  #sample size
a=30   #length of the rectangle
b=1.9    #wide of the rectangle
np.random.seed(10)  #set random seed to be 10
x = np.random.uniform(2,a+2,n)
y = np.random.uniform(2,b+2,n)
rect = np.array([x,y]).T
rect = np.append(rect,[[0]*18]*n,1)
#plot
plt.scatter(rect[:,0],rect[:,1],s=2)
plt.title("Rectangle")
plt.show()
#np.savetxt('rect_n5000_dim20_a30b1.9.csv', rect, delimiter=',')


# In[161]:


#rectangle with hole, 20 dimension, sample size roughly 5000
n=6000 
a=30   #length of the rectangle
b=1.9    #wide of the rectangle
np.random.seed(980)  #set random seed to be 980
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
rect_hole = np.append(rect_hole,[[0]*18]*sample_size,1)
#plot
plt.scatter(rect_hole[:,0],rect_hole[:,1],s=2)
plt.show()
#np.savetxt('rectHole_n5000_dim20_a30b1.9.csv', rect_hole, delimiter=',')


# In[185]:


#swiss roll, 20 dimension, sample size 5000

##set parameter
length_phi = 8 #length of swiss roll in angular direction
length_Z = 6 #length of swiss roll in z direction
sigma = 0      #noise strength
m = 5000        #number of samples

##generate dataset
np.random.seed(101) #set random seed to be 101
phi = length_phi*np.random.rand(m)
xi = np.random.rand(m)
Z = length_Z*np.random.rand(m)
X = 1./6*(phi + min(length_Z,length_phi) + sigma*xi)*np.sin(phi)
Y = 1./6*(phi + min(length_Z,length_phi) + sigma*xi)*np.cos(phi)

swiss_roll = np.array([X, Y, Z]).T
swiss_roll = np.append(swiss_roll,[[0]*17]*m,1)
#rotate with X coordiante
theta = np.radians(90)
rotation = np.identity(20)
rotation[2,2]=np.cos(theta)
rotation[1,2]=-np.sin(theta)
rotation[2,1]=np.sin(theta)
rotation[1,1]=np.cos(theta)
swiss_roll=rotation.dot(swiss_roll.T).T
#plot
fig = plt.figure(figsize=(8, 7))
ax = plt.axes(projection="3d")
ax.scatter(swiss_roll[:,0],swiss_roll[:,1],swiss_roll[:,2],c=Z, s=20, alpha=0.6)
ax.set_title("Swiss roll")
plt.show()
plt.scatter(swiss_roll[:,0],swiss_roll[:,2],s=1)
plt.show()
#np.savetxt('swissRoll_n5000_dim20_a10b4.csv', swiss_roll, delimiter=',')


# In[141]:


#torus, 20 dimensions, 10000 sample size
##set parameter
n = 10000 
R, r = 4, 3 
##Generate dataset
np.random.seed(1434) #set seed to be 1434
x1 = np.random.uniform(0, 2*np.pi*R,n)
x2 = np.random.uniform(0, 2*np.pi*r,n)
theta = 2 * np.pi * x1 / R
phi = 2 * np.pi * x2 / r
x = (R + r*np.cos(theta)) * np.cos(phi)
y = (R + r*np.cos(theta)) * np.sin(phi)
z = r * np.sin(theta)
torus = np.array([x, y, z]).T
torus = np.append(torus,[[0]*17]*n,1)
#plot
fig = plt.figure(figsize=(8,7)) 
ax = plt.axes(projection="3d")
ax.scatter(torus[:,0], torus[:,1], torus[:,2], c=z,s=1)
ax.axes.set_xlim3d(left=-R, right=R) 
ax.axes.set_ylim3d(bottom=-R, top=R) 
ax.axes.set_zlim3d(bottom=-R, top=R)
plt.title("Torus")
plt.show()
#np.savetxt('torus_n10000_dim20_R4r3.csv',torus, delimiter=',')


# In[ ]:




