#!/usr/bin/env python
# coding: utf-8

# In[4]:


import matplotlib.pyplot as plt
import math
import numpy as np
import pandas as pd
from scipy import stats
from sklearn import manifold, datasets
from scipy.stats import gaussian_kde
import random
from sklearn.datasets import load_digits, make_s_curve

#create data sets:
###7.rectangle and rectangle with hole 20 dimension size 5000
#no hole
n=5000
x = np.random.uniform(2,8,n)
y = np.random.uniform(2,6,n)
rect = [x,y]
rect = np.reshape(rect,(2,n))
rect = np.append(rect,[[0]*n]*18,0).T
plt.scatter(rect[:,0],rect[:,1])
plt.xlim(1,9)
plt.ylim(1,7)
plt.title("Rectangle")
plt.show()
#with hole
n=5000
x1 = np.random.uniform(2,4,int(8*250))
x2 = np.random.uniform(6,8,int(8*250))
x3 = np.random.uniform(4,6,500)
x4 = np.random.uniform(4,6,500)
y1 = np.random.uniform(2,6,int(8*250))
y2 = np.random.uniform(2,6,int(8*250))
y3 = np.random.uniform(2,3,500)
y4 = np.random.uniform(5,6,500)
x = np.concatenate((x1,x2,x3,x4), axis=None)
y = np.concatenate((y1,y2,y3,y4), axis=None)
rect_hole = [x,y]
rect_hole = np.reshape(rect_hole,(2,n))
rect_hole = np.append(rect_hole,[[0]*n]*18,0).T
plt.scatter(rect_hole[:,0],rect_hole[:,1])
plt.xlim(1,9)
plt.ylim(1,7)
plt.title("Rectangle with hole")
plt.show()

#circle
n=5000
def circle(n):
    x = []
    y = []
    for i in range(0,n):
        angle = random.uniform(0,1)*(math.pi*2)
        x.append(math.cos(angle));
        y.append(math.sin(angle));
    return x,y
x,y=circle(n)
circle =[x,y]
circle =np.reshape(circle,(2,n))
circle = np.append(circle,[[0]*n]*18,0).T
plt.scatter(circle[:,0],circle[:,1])
plt.title("Circle")
plt.show()
#stage3:
sigma = 0.2
noise = np.random.uniform(-sigma,sigma,n*2).reshape((2,n))
noise = np.append(noise,[[0]*n]*18,0).T
circle_noise=circle+noise
plt.scatter(circle_noise[:,0],circle_noise[:,1])
plt.title("Circle with noise")
plt.show()
##Two datasets(20*n matrix) used for manifold learning:
#1.circle
#2.circle_noise 
#**every column to be each observation, e.g:circle[:,0] 
#plot use: axes to be e.g:circle[0,:] 

#swiss roll
n=5000

data_nohole, color_nohole = datasets.make_swiss_roll(n_samples=n,noise=0,random_state=1,hole=False)
fig = plt.figure(figsize=(8, 7))
ax = plt.axes(projection="3d")
ax.scatter(data_nohole[:, 0], data_nohole[:, 1], data_nohole[:, 2], c=color_nohole, s=50, alpha=0.8)
ax.set_title("Swiss Roll no hole, no noise")
plt.show()
#with hole
data_hole, color_hole = datasets.make_swiss_roll(n_samples=n,noise=0,random_state=1,hole=True)
fig = plt.figure(figsize=(8, 7))
ax = plt.axes(projection="3d")
ax.set_title("Swiss Roll with hole, no noise")
ax.scatter(data_hole[:, 0], data_hole[:, 1], data_hole[:, 2], c=color_hole, s=50, alpha=0.8)
plt.show()

#stage1 total dimension 20 with 17 zeros
#data of one column to be one points
data_nohole = np.append(data_nohole,[[0]*17]*n,1)
data_nohole = np.transpose(data_nohole)##

data_hole = np.append(data_hole,[[0]*17]*n,1)
data_hole = np.transpose(data_hole)##

#stage2 rotation
#30degree
theta = np.radians(30)
rotation = np.identity(20)
rotation[2,2]=np.cos(theta)
rotation[1,2]=-np.sin(theta)
rotation[2,1]=np.sin(theta)
rotation[1,1]=np.cos(theta)

rotation1 = np.identity(20)
rotation1[0,0]=np.cos(theta)
rotation1[0,1]=-np.sin(theta)
rotation1[1,0]=np.sin(theta)
rotation1[1,1]=np.cos(theta)


rot_nohole=rotation1.dot(data_nohole)##

fig = plt.figure(figsize=(8, 7))
ax = plt.axes(projection="3d")
ax.set_title("Swiss Roll no hole, no noise, rotation")
ax.scatter(rot_nohole[0, :], rot_nohole[1, :], rot_nohole[2, :], c=color_nohole, s=50, alpha=0.8)
plt.show()

rot_hole=rotation.dot(data_hole)##

#stage3
data_noise_nohole, color_noise_nohole = datasets.make_swiss_roll(n_samples=n,noise=1,random_state=1,hole=False)
fig = plt.figure(figsize=(8, 7))
ax = plt.axes(projection="3d")
ax.scatter(data_noise_nohole[:, 0], 
           data_noise_nohole[:, 1], 
           data_noise_nohole[:, 2], 
           c=color_noise_nohole, s=50, alpha=0.8)
ax.set_title("Swiss Roll no hole, noise")
plt.show()

data_noise_hole, color_noise_hole = datasets.make_swiss_roll(n_samples=n,noise=1,random_state=1,hole=True)
fig = plt.figure(figsize=(8, 7))
ax = plt.axes(projection="3d")
ax.scatter(data_noise_hole[:, 0], 
           data_noise_hole[:, 1], 
           data_noise_hole[:, 2], 
           c=color_noise_hole, s=50, alpha=0.8)
ax.set_title("Swiss Roll with hole, noise")
plt.show()

data_noise_nohole = np.append(data_noise_nohole,[[0]*17]*n,1)
data_noise_nohole = np.transpose(data_noise_nohole)##

data_noise_hole = np.append(data_noise_hole,[[0]*17]*n,1)
data_noise_hole = np.transpose(data_noise_hole)##

rot_noise_hole = rotation.dot(data_noise_hole)##
fig = plt.figure(figsize=(8, 7))
ax = plt.axes(projection="3d")
ax.scatter(rot_noise_hole[0, :], 
           rot_noise_hole[1, :], 
           rot_noise_hole[2, :], 
           c=color_noise_hole, s=50, alpha=0.8)
ax.set_title("Swiss Roll with hole, noise and rotate")
plt.show()

##Seven datasets(20*n matrix) used for manifold learning:
#1.data_nohole 
#2.data_hole 
#3.rot_nohole
#4.rot_hole
#5.data_noise_nohole
#6.data_noise_hole
#7.rot_noise_hole
#**every column to be each observation, e.g:data_nohole[:,0] 
#plot use: axes to be e.g:data_nohole[0,:] 


# In[2]:


#Torus dimension 20
#stage1:
n = 71
theta = np.linspace(0, 2.*np.pi, n)
phi = np.linspace(0, 2.*np.pi, n)
theta, phi = np.meshgrid(theta, phi)
c, a = 4, 2
x = (c + a*np.cos(theta)) * np.cos(phi)
y = (c + a*np.cos(theta)) * np.sin(phi)
z = a * np.sin(theta)

torus = [x,y,z]
torus =np.reshape(torus,(3,n**2))
torus = np.append(torus,[[0]*n**2]*17,0)##

#stage2 with rotate:
theta = np.radians(115)
rotation = np.identity(20)
rotation[2,2]=np.cos(theta)
rotation[1,2]=-np.sin(theta)
rotation[2,1]=np.sin(theta)
rotation[1,1]=np.cos(theta)

rotation1 = np.identity(20)
rotation1[0,0]=np.cos(theta)
rotation1[0,1]=-np.sin(theta)
rotation1[1,0]=np.sin(theta)
rotation1[1,1]=np.cos(theta)
rot_torus=rotation.dot(torus)##
#stage3 add noise:
sigma=0.4
noise = np.random.normal(0,sigma,3*n**2).reshape((3,n**2))
noise = np.append(noise,[[0]*n**2]*17,0)

torus_noise=torus+noise###
torus_noise=torus_noise.T

#rotate with noise
noise = np.random.normal(0,sigma,3*n**2).reshape((3,n**2))
noise = np.append(noise,[[0]*n**2]*17,0)
rot_noise_torus = rot_torus+noise###
rot_noise_torus=rot_noise_torus.T
torus = torus.T
rot_torus=rot_torus.T
##Four datasets(20*n**2 matrix) used for manifold learning:
#1.torus
#2.rot_torus
#3.torus_noise
#4.rot_noise_torus


# In[29]:


#LLE KNN=8
linear_embedding = manifold.LocallyLinearEmbedding(random_state=42,n_neighbors=8, n_components=7)

rect_LLE = linear_embedding.fit_transform(rect)
rect_hole_LLE = linear_embedding.fit_transform(rect_hole)
circle_LLE = linear_embedding.fit_transform(circle)
swiss_LLE = linear_embedding.fit_transform(data_nohole.T)
torus_LLE = linear_embedding.fit_transform(torus)


# In[43]:


#swiss 2d
figure, axis = plt.subplots(3, 2,figsize=(10, 12))
figure.suptitle("Swiss Roll, All LLE", fontsize=14)

xy = np.vstack([swiss_LLE[:,0],swiss_LLE[:,1]])        
density = stats.gaussian_kde(xy)(xy) 
idx = density.argsort()
x, y,density = swiss_LLE[:, 0][idx], swiss_LLE[:, 1][idx], density[idx]
axis[0, 0].scatter(x,y,c=(-density), s=30, alpha=0.6)
axis[0, 0].set_title("V0,V1")

xy = np.vstack([swiss_LLE[:,0],swiss_LLE[:,2]])        
density = stats.gaussian_kde(xy)(xy) 
idx = density.argsort()
x, y,density = swiss_LLE[:, 0][idx], swiss_LLE[:, 2][idx], density[idx]
axis[0, 1].scatter(x,y,c=(-density), s=30, alpha=0.6)
axis[0, 1].set_title("V0,V2")

xy = np.vstack([swiss_LLE[:,0],swiss_LLE[:,3]])        
density = stats.gaussian_kde(xy)(xy) 
idx = density.argsort()
x,y,density = swiss_LLE[:, 0][idx], swiss_LLE[:, 3][idx], density[idx]
axis[1, 0].scatter(x,y,c=(-density), s=30, alpha=0.6)
axis[1, 0].set_title("V0,V3")

xy = np.vstack([swiss_LLE[:,0],swiss_LLE[:,4]])        
density = stats.gaussian_kde(xy)(xy) 
idx = density.argsort()
x,y,density = swiss_LLE[:, 0][idx], swiss_LLE[:, 4][idx], density[idx]
axis[1, 1].scatter(x,y,c=(-density), s=30, alpha=0.6)
axis[1, 1].set_title("V0,V4")

xy = np.vstack([swiss_LLE[:,0],swiss_LLE[:,5]])        
density = stats.gaussian_kde(xy)(xy) 
idx = density.argsort()
x,y,density = swiss_LLE[:, 0][idx], swiss_LLE[:, 5][idx], density[idx]
axis[2, 0].scatter(x,y,c=(-density), s=30, alpha=0.6)
axis[2, 0].set_title("V0,V5")

swiss=data_nohole.T
xy = np.vstack([swiss[:,0],swiss[:,1]])        
density = stats.gaussian_kde(xy)(xy) 
idx = density.argsort()
x,y,density = swiss[:, 0][idx], swiss[:, 1][idx], density[idx]
axis[2, 1].scatter(x,y,c=(-density), s=30, alpha=0.6)
axis[2, 1].set_title("Original 2D swiss")
plt.savefig("SwissRoll_ALL_LLE.jpg")
plt.show()


# In[42]:


#torus 2d
figure, axis = plt.subplots(3, 2,figsize=(10, 12))
figure.suptitle("Torus, All LLE", fontsize=14)

xy = np.vstack([torus_LLE[:,0],torus_LLE[:,1]])        
density = stats.gaussian_kde(xy)(xy) 
idx = density.argsort()
x, y,density = torus_LLE[:, 0][idx], torus_LLE[:, 1][idx], density[idx]
axis[0, 0].scatter(x,y,c=(-density), s=30, alpha=0.6)
axis[0, 0].set_title("V0,V1")

xy = np.vstack([torus_LLE[:,0],torus_LLE[:,2]])        
density = stats.gaussian_kde(xy)(xy) 
idx = density.argsort()
x, y,density = torus_LLE[:, 0][idx], torus_LLE[:, 2][idx], density[idx]
axis[0, 1].scatter(x,y,c=(-density), s=30, alpha=0.6)
axis[0, 1].set_title("V0,V2")

xy = np.vstack([torus_LLE[:,0],torus_LLE[:,3]])        
density = stats.gaussian_kde(xy)(xy) 
idx = density.argsort()
x,y,density = torus_LLE[:, 0][idx], torus_LLE[:, 3][idx], density[idx]
axis[1, 0].scatter(x,y,c=(-density), s=30, alpha=0.6)
axis[1, 0].set_title("V0,V3")

xy = np.vstack([torus_LLE[:,0],torus_LLE[:,4]])        
density = stats.gaussian_kde(xy)(xy) 
idx = density.argsort()
x,y,density = torus_LLE[:, 0][idx], torus_LLE[:, 4][idx], density[idx]
axis[1, 1].scatter(x,y,c=(-density), s=30, alpha=0.6)
axis[1, 1].set_title("V0,V4")

xy = np.vstack([torus_LLE[:,0],torus_LLE[:,5]])        
density = stats.gaussian_kde(xy)(xy) 
idx = density.argsort()
x,y,density = torus_LLE[:, 0][idx], torus_LLE[:, 5][idx], density[idx]
axis[2, 0].scatter(x,y,c=(-density), s=30, alpha=0.6)
axis[2, 0].set_title("V0,V5")

xy = np.vstack([torus[:,0],torus[:,1]])        
density = stats.gaussian_kde(xy)(xy) 
idx = density.argsort()
x,y,density = torus[:, 0][idx], torus[:, 1][idx], density[idx]
axis[2, 1].scatter(x,y,c=(-density), s=30, alpha=0.6)
axis[2, 1].set_title("Original 2D torus")
plt.savefig("Torus_ALL_LLE.jpg")
plt.show()


# In[30]:


#circle
figure, axis = plt.subplots(3, 2,figsize=(10, 12))
figure.suptitle("Circle, All LLE", fontsize=14)
axis[0, 0].scatter(circle_LLE[:,0], circle_LLE[:,1])
axis[0, 0].set_title("V0,V1")

axis[0, 1].scatter(circle_LLE[:,0], circle_LLE[:,2])
axis[0, 1].set_title("V0,V2")
  
axis[1, 0].scatter(circle_LLE[:,0], circle_LLE[:,3])
axis[1, 0].set_title("V0,V3")

axis[1, 1].scatter(circle_LLE[:,0], circle_LLE[:,4])
axis[1, 1].set_title("V0,V4")

axis[2, 0].scatter(circle_LLE[:,0], circle_LLE[:,5])
axis[2, 0].set_title("V0,V5")

axis[2, 1].scatter(circle_LLE[:,0], circle_LLE[:,6])
axis[2, 1].set_title("V0,V6")
plt.savefig("Cricle_ALL_LLE.jpg")
plt.show()


# In[25]:


#rect hole plot
figure, axis = plt.subplots(3, 2,figsize=(10, 12))
figure.suptitle("Rectangule with hole, All LLE", fontsize=14)
axis[0, 0].scatter(rect_hole_LLE[:,0], rect_hole_LLE[:,1])
axis[0, 0].set_title("V0,V1")

axis[0, 1].scatter(rect_hole_LLE[:,0], rect_hole_LLE[:,2])
axis[0, 1].set_title("V0,V2")
  
axis[1, 0].scatter(rect_hole_LLE[:,0], rect_hole_LLE[:,3])
axis[1, 0].set_title("V0,V3")

axis[1, 1].scatter(rect_hole_LLE[:,0], rect_hole_LLE[:,4])
axis[1, 1].set_title("V0,V4")

axis[2, 0].scatter(rect_hole_LLE[:,0], rect_hole_LLE[:,5])
axis[2, 0].set_title("V0,V5")

axis[2, 1].scatter(rect_hole_LLE[:,0], rect_hole_LLE[:,6])
axis[2, 1].set_title("V0,V6")
plt.savefig("RectWithHole_ALL_LLE.jpg")
plt.show()


# In[24]:


#rect plot
figure, axis = plt.subplots(3, 2,figsize=(10, 12))
figure.suptitle("Rectangule, All LLE", fontsize=14)
axis[0, 0].scatter(rect_LLE[:,0], rect_LLE[:,1])
axis[0, 0].set_title("V0,V1")

axis[0, 1].scatter(rect_LLE[:,0], rect_LLE[:,2])
axis[0, 1].set_title("V0,V2")
  
axis[1, 0].scatter(rect_LLE[:,0], rect_LLE[:,3])
axis[1, 0].set_title("V0,V3")

axis[1, 1].scatter(rect_LLE[:,0], rect_LLE[:,4])
axis[1, 1].set_title("V0,V4")

axis[2, 0].scatter(rect_LLE[:,0], rect_LLE[:,5])
axis[2, 0].set_title("V0,V5")

axis[2, 1].scatter(rect_LLE[:,0], rect_LLE[:,6])
axis[2, 1].set_title("V0,V6")
plt.savefig("Rect_ALL_LLE.jpg")
plt.show()


# In[110]:


#t_sne
tsne = manifold.TSNE(random_state=42, n_components=3)
circle_tsne = tsne.fit_transform(circle)
swiss_tsne = tsne.fit_transform(data_nohole.T)
rect_tsne = tsne.fit_transform(rect)
rect_hole_tsne = tsne.fit_transform(rect_hole)
torus_tsne = tsne.fit_transform(torus)


# In[85]:


#rect-tsne
fig = plt.figure(figsize=(15,15))
ax = fig.add_subplot(121, projection='3d')
z = np.linspace(-20, 20, num=5000)
xy = np.vstack([rect_tsne[:,0],rect_tsne[:,1]])        
density = stats.gaussian_kde(xy)(xy) 
idx = density.argsort()
x, y,density = rect_tsne[:, 0][idx], rect_tsne[:, 1][idx], density[idx]
ax.scatter(x,y,z,c=-density)
ax.set_title("3D V0,V1")

ax = fig.add_subplot(122, projection='3d')
xy = np.vstack([rect_tsne[:,0],rect_tsne[:,2]])        
density = stats.gaussian_kde(xy)(xy) 
idx = density.argsort()
x, y,density = rect_tsne[:, 0][idx], rect_tsne[:, 2][idx], density[idx]
ax.scatter(x,y,z,c=(-density), s=30, alpha=0.6)
ax.set_title("V0,V2")

ax = fig.add_subplot(421)
ax.scatter(rect_tsne[:,0],rect_tsne[:, 1])
ax.set_title("2D V0,V1")

ax = fig.add_subplot(422)
ax.scatter(rect_tsne[:,0],rect_tsne[:, 2])
ax.set_title("2D V0,V2")
plt.savefig("Rect_ALL_tsne.jpg")
plt.show()


# In[98]:


#swiss_tsne
fig = plt.figure(figsize=(15,15))
ax = fig.add_subplot(121, projection='3d')
xyz = np.vstack([swiss_tsne[:,0],swiss_tsne[:,1],swiss_tsne[:,2]])        
density = stats.gaussian_kde(xyz)(xyz) 
idx = density.argsort()
x, y,z,density = swiss_tsne[:, 0][idx],swiss_tsne[:, 1][idx], swiss_tsne[:,2],density[idx]
ax.scatter(x,y,z,c=-density)
ax.set_title("3D V0,V1,V2")

ax = fig.add_subplot(421)
ax.scatter(swiss_tsne[:,0],swiss_tsne[:, 1])
ax.set_title("2D V0,V1")

ax = fig.add_subplot(422)
ax.scatter(swiss_tsne[:,0],swiss_tsne[:, 2])
ax.set_title("2D V0,V2")

plt.savefig("Swiss_ALL_tsne.jpg")
plt.show()


# In[111]:


#torus_tsne
figure, axis = plt.subplots(2,figsize=(10, 12))
figure.suptitle("Torus, All TSNE", fontsize=14)

xy = np.vstack([torus_tsne[:,0],torus_tsne[:,1]])        
density = stats.gaussian_kde(xy)(xy) 
idx = density.argsort()
x, y,density = torus_tsne[:, 0][idx], torus_tsne[:, 1][idx], density[idx]
axis[0].scatter(x,y,c=(-density), s=30, alpha=0.6)
axis[0].set_title("V0,V1")

xy = np.vstack([torus_tsne[:,0],torus_tsne[:,2]])        
density = stats.gaussian_kde(xy)(xy) 
idx = density.argsort()
x, y,density = torus_tsne[:, 0][idx], torus_tsne[:, 2][idx], density[idx]
axis[1].scatter(x,y,c=(-density), s=30, alpha=0.6)
axis[1].set_title("V0,V2")
plt.savefig("Torus_all_TSNE.jpg")
plt.show()


# In[112]:


#circle_tsne
figure, axis = plt.subplots(2,figsize=(10, 12))
figure.suptitle("Circle, All TSNE", fontsize=14)

xy = np.vstack([circle_tsne[:,0],circle_tsne[:,1]])        
density = stats.gaussian_kde(xy)(xy) 
idx = density.argsort()
x, y,density = circle_tsne[:, 0][idx], circle_tsne[:, 1][idx], density[idx]
axis[0].scatter(x,y,c=(-density), s=30, alpha=0.6)
axis[0].set_title("V0,V1")

xy = np.vstack([circle_tsne[:,0],circle_tsne[:,2]])        
density = stats.gaussian_kde(xy)(xy) 
idx = density.argsort()
x, y,density = circle_tsne[:, 0][idx], circle_tsne[:, 2][idx], density[idx]
axis[1].scatter(x,y,c=(-density), s=30, alpha=0.6)
axis[1].set_title("V0,V2")
plt.savefig("Circle_all_TSNE.jpg")
plt.show()


# In[17]:


#spectral embedding KNN=8
spectral_embedding = manifold.SpectralEmbedding(random_state=42, n_components=10,affinity="nearest_neighbors",
                                               n_neighbors=8)
rect_spectral = spectral_embedding.fit_transform(rect)
rect_hole_spectral = spectral_embedding.fit_transform(rect_hole)
torus_spectral = spectral_embedding.fit_transform(torus)


# In[68]:


plt.scatter(rect_spectral[:,0], rect_spectral[:,1])
plt.show()
plt.scatter(rect_hole_spectral[:, 0], rect_hole_spectral[:, 1])
plt.show()
plt.scatter(torus_spectral[:, 0],torus_spectral[:, 1])
plt.show()
plt.scatter(torus[:,0],torus[:,1])
plt.show()
fig = plt.figure(figsize=(8, 7))
ax = plt.axes(projection="3d")
xyz = np.vstack([torus_spectral[:, 0],torus_spectral[:, 1],torus_spectral[:, 2]])
density = stats.gaussian_kde(xyz)(xyz) 
idx = density.argsort()
x, y, z, density = torus_spectral[:, 0][idx], torus_spectral[:, 1][idx], torus_spectral[:, 2][idx], density[idx]
ax.scatter(x,y,z,c=-density, s=30, alpha=0.6)
#ax.set_title("Torus with noise, no rotation")
plt.show()


# In[19]:


#iso map KNN=8
iso = manifold.Isomap(n_neighbors=8, n_components=10)
rect_iso = iso.fit_transform(rect)
rect_hole_iso = iso.fit_transform(rect_hole)
torus_iso = iso.fit_transform(torus)


# In[67]:


plt.scatter(rect_iso[:,0], rect_iso[:,1])
plt.show()
plt.scatter(rect_hole_iso[:,0], rect_hole_iso[:,1])
plt.show()
plt.scatter(torus_iso[:, 0],torus_iso[:, 1])
plt.show()
plt.scatter(torus[:,0],torus[:,1])
plt.show()
fig = plt.figure(figsize=(8, 7))
ax = plt.axes(projection="3d")
xyz = np.vstack([torus_iso[:, 0],torus_iso[:, 1],torus_iso[:, 2]])
density = stats.gaussian_kde(xyz)(xyz) 
idx = density.argsort()
x, y, z, density = torus_spectral[:, 0][idx], torus_spectral[:, 1][idx], torus_spectral[:, 2][idx], density[idx]
ax.scatter(x,y,z,c=-density, s=30, alpha=0.6)
#ax.set_title("Torus with noise, no rotation")
plt.show()


# In[51]:


#LLE KNN=8
linear_embedding = manifold.LocallyLinearEmbedding(random_state=42,n_neighbors=8, n_components=6)
rect_LLE = linear_embedding.fit_transform(rect)
rect_hole_LLE = linear_embedding.fit_transform(rect_hole)
torus_LLE = linear_embedding.fit_transform(torus)


# In[94]:


plt.scatter(rect_LLE[:,0], rect_LLE[:,1])
plt.show()
plt.scatter(rect_hole_LLE[:,0], rect_hole_LLE[:,1])
plt.show()
plt.scatter(torus_LLE[:, 0],torus_LLE[:, 1])
plt.show()
plt.scatter(torus[:,0],torus[:,1])
plt.show()
fig = plt.figure(figsize=(8, 7))
ax = plt.axes(projection="3d")
xyz = np.vstack([torus_LLE[:, 0],torus_LLE[:, 1],torus_LLE[:, 2]])
density = stats.gaussian_kde(xyz)(xyz) 
idx = density.argsort()
x, y, z, density = torus_LLE[:, 0][idx], torus_LLE[:, 1][idx], torus_LLE[:, 2][idx], density[idx]
ax.scatter(x,y,z,c=-density, s=30, alpha=0.6)
#ax.set_title("Torus with noise, no rotation")
plt.show()


# In[73]:


#t-sne
tsne = manifold.TSNE(random_state=42, n_components=3)
rect_tsne = tsne.fit_transform(rect)
rect_hole_tsne = tsne.fit_transform(rect_hole)
torus_tsne = tsne.fit_transform(torus)


# In[101]:


plt.scatter(rect_tsne[:,0], rect_tsne[:,2])
plt.show()
plt.scatter(rect_hole_tsne[:,0], rect_hole_tsne[:,2])
plt.show()
plt.scatter(torus_tsne[:, 0],torus_tsne[:, 1])
plt.show()
plt.scatter(torus[:,0],torus[:,1])
plt.show()
fig = plt.figure(figsize=(8, 7))
ax = plt.axes(projection="3d")
xyz = np.vstack([torus_tsne[:, 0],torus_tsne[:, 1],torus_tsne[:, 2]])
density = stats.gaussian_kde(xyz)(xyz) 
idx = density.argsort()
x, y, z, density = torus_tsne[:, 0][idx], torus_tsne[:, 1][idx], torus_tsne[:, 2][idx], density[idx]
ax.scatter(x,y,z,c=-density, s=30, alpha=0.6)
#ax.set_title("Torus with noise, no rotation")
plt.show()


# In[ ]:




