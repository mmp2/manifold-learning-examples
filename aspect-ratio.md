The effect of manifold aspect ratio
=====================================

What is aspect ratio? 
---------------------
Below we see two examples of rectangles with different aspect ratios. 

*figures here, just rectangles 4/3 and ~ 8/1.9 *-- (ALL FIGURES: same units on all axes. no numbers on the axes. Color by the longest dimension in all plots)

<img width="700" height="200" alt="1" src="https://user-images.githubusercontent.com/91905313/187146916-762d03f4-e78e-4be8-92e3-5ad79cc5a771.png">

Below we see data sampled uniformly from these 2 rectangles.

<img width="700" height="200" alt="2" src="https://user-images.githubusercontent.com/91905313/187147225-efeb300f-ab0d-4141-b68a-97218dfc74bb.png">

Aspect ratio can be defined for other simple manifolds, that can be obtained by "rolling up" these rectangles. 

Two Swiss Rolls:

<img width="700"  height="300" alt="3" src="https://user-images.githubusercontent.com/91905313/187147263-02e73146-6fe8-4ab4-ab79-26c45ff1e14d.png">

Two Tori:

<img width="700" height="300" alt="截屏2022-08-29 15 35 52" src="https://user-images.githubusercontent.com/91905313/187148724-467b6638-8f40-42da-8e77-dbb4e8ee5d9d.png">

These manifolds all have *intrinsic dimension* $d=2$, because they are obtained by a transformation of a rectangle. Later we will discuss examples of manifolds with $d=3$, such as the sphere. Note however that the torus and swiss roll live in $m=3$ coordinates, and we call $m$ the *embedding dimension*. Of course not all manifolds are obtained from rectangles. Qualitatively, we think of the aspect ratio of a manifold as the aspect ratio of the data, after the manifold is "unfolded" in $d$ dimensions. *a figure here*

Most real data is not generated form rectangles, but most real data, when unfolded, has aspect ratio $>2$, in other words, not close to 1. The following examples illustrate how this affects the embeddings produced by different embedding algorithms. 

*todo: a section on what is a good embedding. continuous map with continuous inverse, smooth map with smooth inverse. with examples*.

*?? a table with links to subsets of results*

Rectangle
---------

The rectangle is the simplest possible manifold. The embedding algorithm will map data sampled from rectangles $(x_1,x_2)$ to points in $m=2$ with coordinates $v_1,v_2$ **MMP decision point: use 0-indexed coordinates? I think YES**

*figure -- see handwritten notes *  embedding alg x aspect ratio x complete figures (all pairs e-vectors) 

*Isomap Embedding:*

Aspect ratio 4/3, 5/2, 6/1.9:

<img src = aspect-ratio-plots/Isomap/Rectangle/Rectangle_a4b3_Isomap_x.jpg width="350" height="500"><img src = aspect-ratio-plots/Isomap/Rectangle/Rectangle_a5b2_Isomap_x.jpg width="350" height="500"><img src = aspect-ratio-plots/Isomap/Rectangle/Rectangle_a6b1_9_Isomap_x.jpg width="350" height="500">



*Locally Linear Embedding(LLE):*

Aspect ratio 4/3, 5/2, 6/1.9:

<img src = https://user-images.githubusercontent.com/91905313/187150694-030d9bb0-2c30-46a1-ad9a-ef0f2053c9f6.jpg width="330" height="500"> <img src =https://user-images.githubusercontent.com/91905313/187153776-e81d614d-4418-4776-a30f-57e77240d274.jpg width="330" height="500"><img src = https://user-images.githubusercontent.com/91905313/187154086-c5930aae-f33e-49ff-9638-0c57a2ede923.jpg  width="330" height="500">

Aspect ratio 8/1.9, 10/1.9, 16/1.9:

<img src =https://user-images.githubusercontent.com/91905313/187157794-6c72f0c6-6f1f-4c65-9e3f-8bc38de02bd0.jpg width="330" height="500"> <img src =https://user-images.githubusercontent.com/91905313/187157870-b4d4f810-43cf-422c-a5e5-45b0d2f94086.jpg width="330" height="500"><img src =https://user-images.githubusercontent.com/91905313/187157917-a5a05caa-2dd6-4df9-b434-9da2ead4d2d9.jpg width="330" height="500">

Aspect ratio 20/1.9, 30/1.9:

<img src =https://user-images.githubusercontent.com/91905313/187158320-e6ce2247-1eaa-45a6-8bf2-555327ff7be1.jpg width="330" height="500"><img src =https://user-images.githubusercontent.com/91905313/187158409-4fa7a8c7-ba82-44c8-8563-42bb9788e842.jpg width="330" height="500">


Swiss roll
----------
A swiss roll is just a rectangle rolled up. So, the embedding algorithms should output the same results as before, since they are getting the essentially same data, right? transformed by XXX. *explain the stretching*

*Locally Linear Embedding(LLE):*

Aspect ratio 8/6, 10/4, 12/3.8:

<img src =https://user-images.githubusercontent.com/91905313/187160692-816b16fd-1171-454b-ae5e-6f188bccd705.jpg width="330" height="500"><img src =https://user-images.githubusercontent.com/91905313/187160773-ad0bf641-c686-4dcb-9b7f-169efca02329.jpg width="330" height="500"><img src =https://user-images.githubusercontent.com/91905313/187160871-d53fc352-8881-4d6b-be4c-e79c6c362fe9.jpg width="330" height="500">

Aspect ratio 8/1.9, 10/1.9, 16/1.9:

<img src =https://user-images.githubusercontent.com/91905313/187161087-fd1ce031-a7c9-4cb5-8bcb-45fbe09c7580.jpg width="330" height="500"><img src =https://user-images.githubusercontent.com/91905313/187161109-2f29a644-e0a3-497a-b943-3e6700b1ce98.jpg width="330" height="500"><img src =https://user-images.githubusercontent.com/91905313/187161125-b7f9f81c-9e9a-4af1-b9c2-f3d08aed7088.jpg width="330" height="500">

Aspect ratio 20/1.9:

<img src =https://user-images.githubusercontent.com/91905313/187161534-f4c5ef69-3e6a-44f9-8dc3-0c4928445bbf.jpg width="330" height="500">


Rectangle with hole
-------------------

*Locally Linear Embedding(LLE):*

Aspect ratio 4/3, 5/2, 6/1.9:

<img src =https://user-images.githubusercontent.com/91905313/187161794-2cc44e55-3132-45cd-b5e4-5e9e96c4b053.jpg width="330" height="500"><img src =https://user-images.githubusercontent.com/91905313/187161811-d07ce796-826c-48cd-a08d-9fddb627964a.jpg width="330" height="500"><img src =https://user-images.githubusercontent.com/91905313/187161835-48186cce-5851-489c-bf48-3258b5d65d2e.jpg width="330" height="500">

Aspect ratio 8/1.9, 10/1.9, 16/1.9:

<img src =https://user-images.githubusercontent.com/91905313/187162474-3dde90eb-9f47-44fc-8c06-915cdd830707.jpg width="330" height="500"><img src =https://user-images.githubusercontent.com/91905313/187162483-7ce5deaa-b57e-4799-bafd-0173964da361.jpg width="330" height="500"><img src =https://user-images.githubusercontent.com/91905313/187162500-97cf7400-c108-4df7-809f-34f43f527f0d.jpg width="330" height="500">

Aspect ratio 20/1.9, 30/1.9:

<img src =https://user-images.githubusercontent.com/91905313/187163057-9c975adc-0227-46a4-9ea3-3903ce8df5a1.jpg width="330" height="500"><img src =https://user-images.githubusercontent.com/91905313/187163070-49c87663-04d6-4447-9505-23ad440f3490.jpg width="330" height="500">


Torus
-----
*Locally Linear Embedding(LLE):*

Aspect ratio 4/3, 5/2, 6/1.9:

<img src =https://user-images.githubusercontent.com/91905313/187164202-be80d354-54e7-46b4-8729-edebf1f7632e.jpg width="330" height="800"><img src =https://user-images.githubusercontent.com/91905313/187164220-7fda116a-8d3a-47e2-af95-46284467f4e1.jpg width="330" height="800"><img src =https://user-images.githubusercontent.com/91905313/187164236-cd5da8dc-c537-44d4-8180-049c62f52ce3.jpg width="330" height="800">

Aspect ratio 8/1.9, 10/1.9, 16/1.9:

<img src =https://user-images.githubusercontent.com/91905313/187164753-0a59f9ed-8d33-49b7-ac8b-f0c2fe84b0be.jpg width="330" height="800"><img src =https://user-images.githubusercontent.com/91905313/187164761-db0019de-175c-4f67-bf39-a60bbfc793be.jpg width="330" height="800"><img src =https://user-images.githubusercontent.com/91905313/187164770-c311b4c7-a624-4282-91c5-4316ac323f28.jpg width="330" height="800">


+ single plot of best embedding (aspect ratio x alg )
+ 1-2 complete examples

A manifold with $d=3$ 
---------------------
(brick?, ellipsoid? swiss roll?)

A "cute" manifold
------------------

An example with real data (maybe)
---------------------------------

This paper https://arxiv.org/pdf/1907.01651.pdf discusses the problems in the case of Spectral Embedding and proposes a solution. 




