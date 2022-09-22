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

**Uniform Density**

| ML algo | 4/3         | 5/2       | 6/1.9 | 8/1.9 | 10/1.9 | 16/1.9 | 20/1.9 | 30/1.9 |
| :---                        |    :----:   |   :---: |   :----:    |   :----:    |    :----:    |    :----:    |    :----:    |    :----:    | 
| Isomap |<img src = aspect-ratio-plots/Isomap/Rectangle/Rectangle_a4b3_Isomap_x.jpg width="111" height="168">|<img src = aspect-ratio-plots/Isomap/Rectangle/Rectangle_a5b2_Isomap_x.jpg width="111" height="168">|<img src = aspect-ratio-plots/Isomap/Rectangle/Rectangle_a6b1_9_Isomap_x.jpg width="111" height="168">|<img src = aspect-ratio-plots/Isomap/Rectangle/Rectangle_a8b1_9_Isomap_x.jpg width="111" height="168">|<img src = aspect-ratio-plots/Isomap/Rectangle/Rectangle_a10b1_9_Isomap_x.jpg width="111" height="168">|<img src = aspect-ratio-plots/Isomap/Rectangle/Rectangle_a16b1_9_Isomap_x.jpg width="111" height="168">|<img src = aspect-ratio-plots/Isomap/Rectangle/Rectangle_a20b1_9_Isomap_x.jpg width="111" height="168">|<img src = aspect-ratio-plots/Isomap/Rectangle/Rectangle_a30b1_9_Isomap_x.jpg width="111" height="168">|
| Spectral |<img src = aspect-ratio-plots/Spectral-megaman/Rectangle/Rectangle_a4b3_Spectral_x.jpg width="111" height="168">|<img src = aspect-ratio-plots/Spectral-megaman/Rectangle/Rectangle_a5b2_Spectral_x.jpg width="111" height="168">|<img src = aspect-ratio-plots/Spectral-megaman/Rectangle/Rectangle_a6b1_9_Spectral_x.jpg width="111" height="168">|<img src = aspect-ratio-plots/Spectral-megaman/Rectangle/Rectangle_a8b1_9_Spectral_x.jpg width="111" height="168">|<img src = aspect-ratio-plots/Spectral-megaman/Rectangle/Rectangle_a10b1_9_Spectral_x.jpg width="111" height="168">|<img src = aspect-ratio-plots/Spectral-megaman/Rectangle/Rectangle_a16b1_9_Spectral_x.jpg width="111" height="168">|<img src = aspect-ratio-plots/Spectral-megaman/Rectangle/Rectangle_a20b1_9_Spectral_x.jpg width="111" height="168">|<img src = aspect-ratio-plots/Spectral-megaman/Rectangle/Rectangle_a30b1_9_Spectral_x.jpg width="111" height="168">|
| LLE     | <img src = https://user-images.githubusercontent.com/91905313/187150694-030d9bb0-2c30-46a1-ad9a-ef0f2053c9f6.jpg width="111" height="168"> | <img src = https://user-images.githubusercontent.com/91905313/187153776-e81d614d-4418-4776-a30f-57e77240d274.jpg width="111" height="168"> | <img src = https://user-images.githubusercontent.com/91905313/187154086-c5930aae-f33e-49ff-9638-0c57a2ede923.jpg width="111" height="168"> | <img src = https://user-images.githubusercontent.com/91905313/187157794-6c72f0c6-6f1f-4c65-9e3f-8bc38de02bd0.jpg width="111" height="168"> | <img src = https://user-images.githubusercontent.com/91905313/187157870-b4d4f810-43cf-422c-a5e5-45b0d2f94086.jpg width="111" height="168"> | <img src = https://user-images.githubusercontent.com/91905313/187157917-a5a05caa-2dd6-4df9-b434-9da2ead4d2d9.jpg width="111" height="168"> | <img src = https://user-images.githubusercontent.com/91905313/187158320-e6ce2247-1eaa-45a6-8bf2-555327ff7be1.jpg width="111" height="168"> | <img src = https://user-images.githubusercontent.com/91905313/187158409-4fa7a8c7-ba82-44c8-8563-42bb9788e842.jpg width="111" height="168"> | 
| UMAP    | <img src = https://user-images.githubusercontent.com/81238710/187545635-a57c1574-24b4-42b1-9358-16e1f22a7862.jpeg width="111" height="168"> | <img src = https://user-images.githubusercontent.com/81238710/187545732-4950349b-9ca5-4620-83dc-7003d9862efb.jpeg width="111" height="168"> | <img src = https://user-images.githubusercontent.com/81238710/187545792-af037ace-e64c-4372-a30b-0c59a8b5f933.jpeg width="111" height="168"> | <img src = https://user-images.githubusercontent.com/81238710/187545824-4a6271db-73b4-4f5c-9a79-140b4887bb91.jpeg width="111" height="168"> | <img src = https://user-images.githubusercontent.com/81238710/187545910-91cb2a0b-a135-4cce-8078-3145881d6919.jpeg width="111" height="168"> | <img src = https://user-images.githubusercontent.com/81238710/187545953-b5945b47-414f-40aa-b8c1-e2b1af156908.jpeg width="111" height="168"> | <img src = https://user-images.githubusercontent.com/81238710/187545999-2680c19c-8a0b-445b-8b16-8a37a87f09a6.jpeg width="111" height="168"> | <img src = https://user-images.githubusercontent.com/81238710/187546037-0c5cb4f7-a95c-4810-91a1-a65e21df696d.jpeg width="111" height="168"> |

*The best single plot for different aspect ratio*

| ML algo | 4/3         | 5/2       | 6/1.9 | 8/1.9 | 10/1.9 | 16/1.9 | 20/1.9 | 30/1.9 |
| :---                        |    :----:   |   :---: |   :----:    |   :----:    |    :----:    |    :----:    |    :----:    |    :----:    | 
| UMAP    | <img src = https://user-images.githubusercontent.com/81238710/190961595-41515ac0-3437-4c6d-b70f-56f964cfb086.jpeg width="111" height="111"> | <img src = https://user-images.githubusercontent.com/81238710/190961596-5bb5a029-5743-4b7e-9b19-defbded719a7.jpeg width="111" height="111"> | <img src = https://user-images.githubusercontent.com/81238710/190961597-dabfe06d-232b-4c8e-a4b8-fb3956a8b3d3.jpeg width="111" height="111"> | <img src = https://user-images.githubusercontent.com/81238710/190961600-de79c4df-037f-4ba4-b8c0-1880f4ef09e6.jpeg width="111" height="111"> | <img src = https://user-images.githubusercontent.com/81238710/190961601-d6a0e72b-b835-4ad5-8be8-8752c61022d8.jpeg width="111" height="111"> | <img src = https://user-images.githubusercontent.com/81238710/190961602-653e8a59-05d9-4b6a-b26b-ebf6e8443736.jpeg width="111" height="111"> | <img src = https://user-images.githubusercontent.com/81238710/190961603-81266b80-536d-4fa3-bfbb-4d89ed1d34c4.jpeg width="111" height="111"> | <img src = https://user-images.githubusercontent.com/81238710/190961604-d1b06b31-ce45-4ec2-abd2-b242a7c4efd2.jpeg width="111" height="111"> |

Swiss roll
----------
A swiss roll is just a rectangle rolled up. So, the embedding algorithms should output the same results as before, since they are getting the essentially same data, right? transformed by XXX. *explain the stretching*

**Uniform Density**

| ML algo | 8/6         | 10/4       | 12/3.8 | 8/1.9 | 10/1.9 | 16/1.9 | 20/1.9 |
| :---                        |    :----:   |   :---: |   :----:    |   :----:    |    :----:    |    :----:    |    :----:    |
| Isomap     | <img src =aspect-ratio-plots/Isomap/SwissRoll/Swiss_Roll_a8b6_Isomap_phi.jpg width="125" height="189"> | <img src =aspect-ratio-plots/Isomap/SwissRoll/Swiss_Roll_a10b4_Isomap_phi.jpg width="125" height="189"> | <img src =aspect-ratio-plots/Isomap/SwissRoll/Swiss_Roll_a12b3_8_Isomap_phi.jpg width="125" height="189"> | <img src =aspect-ratio-plots/Isomap/SwissRoll/Swiss_Roll_a8b1_9_Isomap_phi.jpg width="125" height="189"> | <img src =aspect-ratio-plots/Isomap/SwissRoll/Swiss_Roll_a10b1_9_Isomap_phi.jpg width="125" height="189"> | <img src =aspect-ratio-plots/Isomap/SwissRoll/Swiss_Roll_a16b1_9_Isomap_phi.jpg width="125" height="189"> | <img src =aspect-ratio-plots/Isomap/SwissRoll/Swiss_Roll_a20b1_9_Isomap_phi.jpg width="125" height="189"> |
| Spectral    | <img src =aspect-ratio-plots/Spectral-megaman/SwissRoll/Swiss_Roll_a8b6_Spectral_phi.jpg width="125" height="189"> | <img src =aspect-ratio-plots/Spectral-megaman/SwissRoll/Swiss_Roll_a10b4_Spectral_phi.jpg width="125" height="189"> | <img src =aspect-ratio-plots/Spectral-megaman/SwissRoll/Swiss_Roll_a12b3_8_Spectral_phi.jpg width="125" height="189"> | <img src =aspect-ratio-plots/Spectral-megaman/SwissRoll/Swiss_Roll_a8b1_9_Spectral_phi.jpg width="125" height="189"> | <img src =aspect-ratio-plots/Spectral-megaman/SwissRoll/Swiss_Roll_a10b1_9_Spectral_phi.jpg width="125" height="189"> | <img src =aspect-ratio-plots/Spectral-megaman/SwissRoll/Swiss_Roll_a16b1_9_Spectral_phi.jpg width="125" height="189"> | <img src =aspect-ratio-plots/Spectral-megaman/SwissRoll/Swiss_Roll_a20b1_9_Spectral_phi.jpg width="125" height="189"> |
| LLE     | <img src =https://user-images.githubusercontent.com/91905313/187160692-816b16fd-1171-454b-ae5e-6f188bccd705.jpg width="125" height="189"> | <img src =https://user-images.githubusercontent.com/91905313/187160773-ad0bf641-c686-4dcb-9b7f-169efca02329.jpg width="125" height="189"> | <img src =https://user-images.githubusercontent.com/91905313/187160871-d53fc352-8881-4d6b-be4c-e79c6c362fe9.jpg width="125" height="189"> | <img src =https://user-images.githubusercontent.com/91905313/187161087-fd1ce031-a7c9-4cb5-8bcb-45fbe09c7580.jpg width="125" height="189"> | <img src =https://user-images.githubusercontent.com/91905313/187161109-2f29a644-e0a3-497a-b943-3e6700b1ce98.jpg width="125" height="189"> | <img src =https://user-images.githubusercontent.com/91905313/187161125-b7f9f81c-9e9a-4af1-b9c2-f3d08aed7088.jpg width="125" height="189"> | <img src =https://user-images.githubusercontent.com/91905313/187161534-f4c5ef69-3e6a-44f9-8dc3-0c4928445bbf.jpg width="125" height="189"> |
| UMAP    | <img src =https://user-images.githubusercontent.com/81238710/187552599-7a458012-099d-414c-9705-6bbfa97bbfd6.jpeg width="125" height="189"> | <img src =https://user-images.githubusercontent.com/81238710/187552649-757fc126-a931-4d85-aa68-5b85891a47dc.jpeg width="125" height="189"> | <img src =https://user-images.githubusercontent.com/81238710/187552670-cd369134-2530-41ca-b6ec-cc73eaa6550b.jpeg width="125" height="189"> | <img src =https://user-images.githubusercontent.com/81238710/187552560-61f85e78-c0d6-4644-88ac-1b94b55e6e0c.jpeg width="125" height="189"> | <img src =https://user-images.githubusercontent.com/81238710/187552718-1f48c64b-b812-4cd0-9d52-bd6a67a80d76.jpeg width="125" height="189"> | <img src =https://user-images.githubusercontent.com/81238710/187552747-7886c7da-0aa2-489a-8632-92cdfba6d7df.jpeg width="125" height="189"> | <img src =https://user-images.githubusercontent.com/81238710/187552757-9628d143-1ecf-4587-86e7-74cf97355032.jpeg width="125" height="189"> |

*The best single plot for different aspect ratio*

| ML algo | 8/6         | 10/4       | 12/3.8 | 8/1.9 | 10/1.9 | 16/1.9 | 20/1.9 |
| :---                        |    :----:   |   :---: |   :----:    |   :----:    |    :----:    |    :----:    |    :----:    |
| UMAP    | <img src =https://user-images.githubusercontent.com/81238710/190962239-ba4b96ec-5b65-4a84-a8f3-f70b3d46bde5.jpeg width="125" height="189"> | <img src =https://user-images.githubusercontent.com/81238710/190962241-9b9ee4ce-ba3a-4327-8d0c-1f4099e9de89.jpeg width="125" height="189"> | <img src =https://user-images.githubusercontent.com/81238710/190962244-b710a3aa-053f-4af2-8d58-f2256d54100d.jpeg width="125" height="189"> | <img src =https://user-images.githubusercontent.com/81238710/190962238-03541129-ef57-4fab-944e-b8c14b988e90.jpeg width="125" height="189"> | <img src =https://user-images.githubusercontent.com/81238710/190962240-619ccf87-f876-414f-9af2-4d81f600c4f5.jpeg width="125" height="189"> |  |  |

**Variable Density**

| ML algo | 8/6         | 10/4       | 12/3.8 | 8/1.9 | 10/1.9 | 16/1.9 | 20/1.9 |
| :---                        |    :----:   |   :---: |   :----:    |   :----:    |    :----:    |    :----:    |    :----:    |
| UMAP    | <img src =https://user-images.githubusercontent.com/81238710/190932516-a07d940d-90bb-4a37-bc8c-39c4fa318eb5.jpeg width="125" height="189"> | <img src =https://user-images.githubusercontent.com/81238710/190932523-c81f77bf-15c1-4996-b354-0f9c9d8e3d49.jpeg width="125" height="189"> | <img src =https://user-images.githubusercontent.com/81238710/190932526-1d658138-d178-466b-b678-7b04aa244222.jpeg width="125" height="189"> | <img src =https://user-images.githubusercontent.com/81238710/190932506-7a37bd1d-27c8-4700-ab6b-0df0b6b6936e.jpeg width="125" height="189"> | <img src =https://user-images.githubusercontent.com/81238710/190932519-0984ba8e-3e37-49fc-8da0-aa0d0be19c23.jpeg width="125" height="189"> | <img src =https://user-images.githubusercontent.com/81238710/190932528-8d56799a-bbd4-4bd2-8323-f852403ae94c.jpeg width="125" height="189"> | <img src =https://user-images.githubusercontent.com/81238710/190932539-cd005b07-7b2a-4ce4-a52b-c86a6bc1f0a5.jpeg width="125" height="189"> |

Rectangle with hole
-------------------

**Uniform Density**

| ML algo | 4/3         | 5/2       | 6/1.9 | 8/1.9 | 10/1.9 | 16/1.9 | 20/1.9 | 30/1.9 |
| :---                        |    :----:   |   :---: |   :----:    |   :----:    |    :----:    |    :----:    |    :----:    |    :----:    | 
| Isomap     | <img src = aspect-ratio-plots/Isomap/RectangleHole/Rectangle_hole_a4b3_Isomap_x.jpg width="111" height="168"> | <img src = aspect-ratio-plots/Isomap/RectangleHole/Rectangle_hole_a5b2_Isomap_x.jpg width="111" height="168"> | <img src = aspect-ratio-plots/Isomap/RectangleHole/Rectangle_hole_a6b1_9_Isomap_x.jpg width="111" height="168"> | <img src = aspect-ratio-plots/Isomap/RectangleHole/Rectangle_hole_a8b1_9_Isomap_x.jpg width="111" height="168"> | <img src = aspect-ratio-plots/Isomap/RectangleHole/Rectangle_hole_a10b1_9_Isomap_x.jpg width="111" height="168"> | <img src = aspect-ratio-plots/Isomap/RectangleHole/Rectangle_hole_a16b1_9_Isomap_x.jpg width="111" height="168"> | <img src = aspect-ratio-plots/Isomap/RectangleHole/Rectangle_hole_a20b1_9_Isomap_x.jpg width="111" height="168"> | <img src = aspect-ratio-plots/Isomap/RectangleHole/Rectangle_hole_a30b1_9_Isomap_x.jpg width="111" height="168"> |
| LLE     | <img src = https://user-images.githubusercontent.com/91905313/187161794-2cc44e55-3132-45cd-b5e4-5e9e96c4b053.jpg width="111" height="168"> | <img src = https://user-images.githubusercontent.com/91905313/187161811-d07ce796-826c-48cd-a08d-9fddb627964a.jpg width="111" height="168"> | <img src = https://user-images.githubusercontent.com/91905313/187161835-48186cce-5851-489c-bf48-3258b5d65d2e.jpg width="111" height="168"> | <img src = https://user-images.githubusercontent.com/91905313/187162474-3dde90eb-9f47-44fc-8c06-915cdd830707.jpg width="111" height="168"> | <img src = https://user-images.githubusercontent.com/91905313/187162483-7ce5deaa-b57e-4799-bafd-0173964da361.jpg width="111" height="168"> | <img src = https://user-images.githubusercontent.com/91905313/187162500-97cf7400-c108-4df7-809f-34f43f527f0d.jpg width="111" height="168"> | <img src = https://user-images.githubusercontent.com/91905313/187163057-9c975adc-0227-46a4-9ea3-3903ce8df5a1.jpg width="111" height="168"> | <img src = https://user-images.githubusercontent.com/91905313/187163070-49c87663-04d6-4447-9505-23ad440f3490.jpg width="111" height="168"> | 
| UMAP    | <img src = https://user-images.githubusercontent.com/81238710/187547422-fc55c21a-5e2a-44e4-a1a3-9206bb326786.jpeg width="111" height="168"> | <img src = https://user-images.githubusercontent.com/81238710/187547455-2186efe7-6a8a-4502-ba8d-a42ee9884538.jpeg width="111" height="168"> | <img src = https://user-images.githubusercontent.com/81238710/187547489-e8a71bc2-7731-426b-b500-ffc66d6391d6.jpeg width="111" height="168"> | <img src = https://user-images.githubusercontent.com/81238710/187547539-4952fef8-61bb-4f20-a786-9388168b2612.jpeg width="111" height="168"> | <img src = https://user-images.githubusercontent.com/81238710/187547591-b0461342-c5b1-40b3-8ad4-2189c637a602.jpeg width="111" height="168"> | <img src = https://user-images.githubusercontent.com/81238710/187547621-bbdce286-2da6-4741-b137-5142c7415720.jpeg width="111" height="168"> | <img src = https://user-images.githubusercontent.com/81238710/187547671-25ba99fb-3e85-486d-a4cc-ff10db7630f0.jpeg width="111" height="168"> | <img src = https://user-images.githubusercontent.com/81238710/187547799-368e24c9-c819-4082-a6cf-8f0e6279d52a.jpeg width="111" height="168"> | 

*The best single plot for different aspect ratio*

| ML algo | 4/3         | 5/2       | 6/1.9 | 8/1.9 | 10/1.9 | 16/1.9 | 20/1.9 | 30/1.9 |
| :---                        |    :----:   |   :---: |   :----:    |   :----:    |    :----:    |    :----:    |    :----:    |    :----:    | 
| UMAP    | <img src = https://user-images.githubusercontent.com/81238710/190962576-5093604c-3e4c-4ad5-a78e-59d1bd10b0ba.jpeg width="111" height="168"> | <img src = https://user-images.githubusercontent.com/81238710/190962577-24613454-b43d-489a-b8bd-85d779bfe297.jpeg width="111" height="168"> | <img src = https://user-images.githubusercontent.com/81238710/190962578-8dba2f01-3077-4e2b-b0e8-78f192dde5a6.jpeg width="111" height="168"> | <img src = https://user-images.githubusercontent.com/81238710/190962579-43019d04-e61a-4027-961d-a69d7bf9c138.jpeg width="111" height="168"> | <img src = https://user-images.githubusercontent.com/81238710/190962580-f4000ab3-7f66-4974-8343-8e86405b7347.jpeg width="111" height="168"> | <img src = https://user-images.githubusercontent.com/81238710/190962582-d49c09be-abed-43ab-93c1-076e17d818fb.jpeg width="111" height="168"> | <img src = https://user-images.githubusercontent.com/81238710/190962586-157a127b-d72e-46bf-b3a1-251c7c844e0e.jpeg width="111" height="168"> | <img src = https://user-images.githubusercontent.com/81238710/190962587-19b65f01-aef4-4186-af6a-6483e03ddc3b.jpeg width="111" height="168"> |


Torus
-----

| ML algo | 4/3         | 5/2       | 6/1.9 | 8/1.9 | 10/1.9 | 16/1.9 |
| :---                        |    :----:   |   :---: |   :----:    |   :----:    |    :----:    |    :----:    |
| Isomap     | <img src = aspect-ratio-plots/Isomap/Torus/Torus_a4b3_Isomap_z.jpg width="142" height="150"> | <img src = aspect-ratio-plots/Isomap/Torus/Torus_a5b2_Isomap_z.jpg width="142" height="150"> | <img src = aspect-ratio-plots/Isomap/Torus/Torus_a6b1_9_Isomap_z.jpg width="142" height="150"> | <img src = aspect-ratio-plots/Isomap/Torus/Torus_a8b1_9_Isomap_z.jpg width="142" height="150"> | <img src = aspect-ratio-plots/Isomap/Torus/Torus_a10b1_9_Isomap_z.jpg width="142" height="150"> | <img src = aspect-ratio-plots/Isomap/Torus/Torus_a16b1_9_Isomap_z.jpg width="142" height="150"> | 
| LLE     | <img src = https://user-images.githubusercontent.com/91905313/187164202-be80d354-54e7-46b4-8729-edebf1f7632e.jpg width="142" height="346"> | <img src = https://user-images.githubusercontent.com/91905313/187164220-7fda116a-8d3a-47e2-af95-46284467f4e1.jpg width="142" height="346"> | <img src = https://user-images.githubusercontent.com/91905313/187164236-cd5da8dc-c537-44d4-8180-049c62f52ce3.jpg width="142" height="346"> | <img src = https://user-images.githubusercontent.com/91905313/187164753-0a59f9ed-8d33-49b7-ac8b-f0c2fe84b0be.jpg width="142" height="346"> | <img src = https://user-images.githubusercontent.com/91905313/187164761-db0019de-175c-4f67-bf39-a60bbfc793be.jpg width="142" height="346"> | <img src = https://user-images.githubusercontent.com/91905313/187164770-c311b4c7-a624-4282-91c5-4316ac323f28.jpg width="142" height="346"> | 
| UMAP    | <img src = https://user-images.githubusercontent.com/81238710/187553518-82f92e8f-ddac-4a01-a6d9-026d3ac8c886.jpeg width="142" height="150"> | <img src = https://user-images.githubusercontent.com/81238710/187553524-c44b6716-a36d-43be-b947-3611a23acf2a.jpeg width="142" height="150"> | <img src = https://user-images.githubusercontent.com/81238710/187553532-d7134782-a5bf-4846-aeca-b6972fd82ce7.jpeg width="142" height="150"> | <img src = https://user-images.githubusercontent.com/81238710/187553542-1bcb3ba3-35a6-4980-a36c-4c185875d1dc.jpeg width="142" height="150"> | <img src = https://user-images.githubusercontent.com/81238710/187553552-a961540d-8f80-4713-a05d-b7a13fa0d997.jpeg width="142" height="150"> | <img src = https://user-images.githubusercontent.com/81238710/187553562-60920c61-1d2b-43c6-bb23-bbf822e153ac.jpeg width="142" height="150"> |

*The best single plot for different aspect ratio*

| ML algo | 4/3         | 5/2       | 6/1.9 | 8/1.9 | 10/1.9 | 16/1.9 |
| :---                        |    :----:   |   :---: |   :----:    |   :----:    |    :----:    |    :----:    |
| UMAP    | <img src = https://user-images.githubusercontent.com/81238710/190962979-c6568816-e574-42ad-b8eb-9564c66afad3.jpeg width="142" height="150"> | <img src = https://user-images.githubusercontent.com/81238710/190962983-37b2e8ef-dc1b-4bb6-b5f8-2218c6769e66.jpeg width="142" height="150"> | <img src = https://user-images.githubusercontent.com/81238710/190962985-39688127-a1fa-45fa-bd8c-fb8343d4f8bb.jpeg width="142" height="150"> | <img src = https://user-images.githubusercontent.com/81238710/190962986-f4e05eb9-b00e-4e55-b065-561680dd0a2d.jpeg width="142" height="150"> | <img src = https://user-images.githubusercontent.com/81238710/190962989-d1f6081f-98ff-4064-881b-360bebcb8ba5.jpeg width="142" height="150"> | <img src = https://user-images.githubusercontent.com/81238710/190962990-b72fb3ae-a058-4e87-bae1-78f650581d58.jpeg width="142" height="150"> |

+ single plot of best embedding (aspect ratio x alg )
+ 1-2 complete examples

**Variable Density**

| ML algo | 4/3         | 5/2       | 6/1.9 | 8/1.9 | 10/1.9 | 16/1.9 |
| :---                        |    :----:   |   :---: |   :----:    |   :----:    |    :----:    |    :----:    |
| UMAP    | <img src = https://user-images.githubusercontent.com/81238710/190932642-a5d50246-10a8-4843-8faa-524f2015c18d.jpeg width="142" height="150"> | <img src = https://user-images.githubusercontent.com/81238710/190932643-8c622a2c-f80b-41b2-a052-f704ec550d09.jpeg width="142" height="150"> | <img src = https://user-images.githubusercontent.com/81238710/190932644-b6ade052-e47c-4ddd-b2ab-ad7f6ddb2956.jpeg width="142" height="150"> | <img src = https://user-images.githubusercontent.com/81238710/190932645-b2acf0a9-86ee-4cb9-96e2-e672a4f299d7.jpeg width="142" height="150"> | <img src = https://user-images.githubusercontent.com/81238710/190932646-e09da5dd-a387-4a05-8bc1-3bd1f6d3b35a.jpeg width="142" height="150"> | <img src = https://user-images.githubusercontent.com/81238710/190932647-3c2d1f16-35d4-4a24-a1d3-6ce8e03d4326.jpeg width="142" height="150"> |


A manifold with $d=3$ 
---------------------
(brick?, ellipsoid? swiss roll?)

A "cute" manifold
------------------

An example with real data (maybe)
---------------------------------

This paper https://arxiv.org/pdf/1907.01651.pdf discusses the problems in the case of Spectral Embedding and proposes a solution. 




