The effect of manifold aspect ratio: seeing "horseshoes" everywhere
====================================================================

> Hangliang Ren, Murray Kang, Qirui Wang, Yujia Wu, Marina Meila

Below is an embedding of a real data set, spectra of galaxies in $D=3750$ dimensions (described <a href="https://arxiv.org/abs/1603.02763">here</a> or <a href="https://www.jmlr.org/papers/v17/16-109.html">here</a>), and embedded by <a href="https://proceedings.neurips.cc/paper/2019/hash/6a10bbd480e4c5573d8f3af73ae0454b-Abstract.html">this paper</a> with DiffusionMaps, into $m=2$ dimensions. Next to it is an embedding of a synthetic data set, a rectangle with length $7\times$ width by UMAP. This paper <a href="https://projecteuclid.org/journals/annals-of-applied-statistics/volume-2/issue-3/Horseshoes-in-multidimensional-scaling-and-local-kernel-methods/10.1214/08-AOAS165.full">Horeshoes in multidimensional scaling and local kernel methods</a> presents an embedding of the <a href="https://archive.ics.uci.edu/ml/datasets/Congressional+Voting+Records">UCI Congressional voting records data</a> $D=16$ in $m=2$ dimensions with an algorithm called *Multi-Dimensional Scaling (MDS)*. All these embeddings look like horseshoes, but for the last 2 cases *we know* that there is no horseshoe in the data (the congressional data is approximately one-dimensional, with the congressmen ordered by degree of partisanship, plus significant noise). Thus the horseshoe  is an *artefact* of the algorithm used. What is causing it?

<img width="300" height="200" alt="galaxy spectra v0, v1, with horseshoe" src="other-figures/galaxy_1_2.png"> <img width="200" height="200" alt="rectangle 7 x 1, horseshoe and clusters " src="other-figures/umap_kneigh_comp-crop1.png">

Fortunately, horseshoes are easily recognized. Below we show the simple fix, for a more sophisticated algorithm look at <a href="https://proceedings.neurips.cc/paper/2019/hash/6a10bbd480e4c5573d8f3af73ae0454b-Abstract.html">Selecting the independent coordinates of manifolds with large aspect ratios </a>.

<img width="300" height="200" alt="galaxy spectra v0, v2, no horseshoe" src="other-figures/galaxy_1_3.png"> <img width="200" height="200" alt="rectangle 7 x 1, no horseshoe" src="other-figures/umap_kneigh_comp-crop2.png">

What is aspect ratio? 
---------------------
Below we see two examples of rectangles with different *aspect ratios*. For the left rectangle, the aspect ratio $a=4/3$, representing its length over  and  for the right rectangle it is $a=8/1.9=4.21$ (we avoid choosing aspect ratios that are integers). 
<img width="700" height="200" alt="截屏2023-01-16 14 13 26" src="https://user-images.githubusercontent.com/91905313/212610533-68ccd0c9-7944-4fe1-bcbe-532bb9b0b889.png">

Below we see data sampled uniformly from these 2 rectangles.
<img width="700" height="200" alt="截屏2023-01-16 14 14 59" src="https://user-images.githubusercontent.com/91905313/212610635-dc128dd0-dde8-4044-aacd-65be9e9de188.png">

Aspect ratio can be defined for other simple manifolds, that can be obtained by "rolling up" these rectangles. 

Two Swiss Rolls. The aspect ratio is inherited from the original rectangles (left $a=4/3$, right $a=8/1.9=4.21$ ).

<img width="600"  height="250" alt="截屏2023-01-16 14 19 37" src="https://user-images.githubusercontent.com/91905313/212611133-39188188-ee2b-4559-accd-d7dd84e2c7aa.png">

Two Tori. A torus is a rectangle that is first rolled up (and glued) into a tube, then rolled again to form a tubular ring. The aspect ratio is then the ratio of the original rectangle, equal to the ratio of the larger and smaller radii of the torus (left $R/r=4/3$, right $R/r=8/1.9=4.21$). 

<img width="600" height="200" alt="截屏2023-01-16 14 19 46" src="https://user-images.githubusercontent.com/91905313/212611596-c14a8121-f96f-4025-8e4e-3ffb9032e005.png">

These manifolds all have *intrinsic dimension* $d=2$, because they are obtained by a transformation of a rectangle, which is itself a 2 dimensional manifold. Even though they are 2 dimensional manifold, the torus and swiss roll live in $m=3$ coordinates, and we call $m$ the *embedding dimension*. Of course not all manifolds are obtained from rectangles. Qualitatively, we think of the aspect ratio of a manifold as the aspect ratio of the data, after the manifold is "unfolded" in $d$ dimensions. 

Most real data is not generated from rectangles, but most real data, when unfolded, has aspect ratio $>2$, in other words, not close to 1. The following examples illustrate how this affects the embeddings produced by different embedding algorithms. 

Before embarking on the examples, the readers are invited to take a detour dealing with the question: what is a good embedding? And what isn't?



*a table with links to subsets of results*

Rectangle
---------

The rectangle is the simplest manifold example. The embedding algorithm will map _input data_  $(x_1,x_2)$ sampled from rectangles to points in $m=2$ with _embedding coordinates_ denoted $(v_0,v_1)$. In other words, we aren't even trying to "reduce dimension", as the data is already "embedded" in 2D. But the algorithms do not know it, and we will have the opportunity to observe their behavior.

The $v$ notation for embedding coordinates is motivated by the fact that most embedding algorithms use the eigenvectors of a matrix as embedding coordinates (Isomap, SpectralEmbedding, LLE). The UMAP algorithm starts with coordinates obtained by eigenvectors, which are then post-processed; t-SNE is the only method that does not use eigendecomposition. 

**Uniform Density**

| ML algo | 1.33         | 2.5       | 3.16 | 4.21 | 5.26 | 8.42 | 10.53 | 15.79 |
| :---                        |    :----:   |   :---: |   :----:    |   :----:    |    :----:    |    :----:    |    :----:    |    :----:    | 
| Isomap |<img src = aspect-ratio-plots/Isomap/Rectangle/Rectangle_a4b3_Isomap_x.jpg width="111" height="168">|<img src = aspect-ratio-plots/Isomap/Rectangle/Rectangle_a5b2_Isomap_x.jpg width="111" height="168">|<img src = aspect-ratio-plots/Isomap/Rectangle/Rectangle_a6b1_9_Isomap_x.jpg width="111" height="168">|<img src = aspect-ratio-plots/Isomap/Rectangle/Rectangle_a8b1_9_Isomap_x.jpg width="111" height="168">|<img src = aspect-ratio-plots/Isomap/Rectangle/Rectangle_a10b1_9_Isomap_x.jpg width="111" height="168">|<img src = aspect-ratio-plots/Isomap/Rectangle/Rectangle_a16b1_9_Isomap_x.jpg width="111" height="168">|<img src = aspect-ratio-plots/Isomap/Rectangle/Rectangle_a20b1_9_Isomap_x.jpg width="111" height="168">|<img src = aspect-ratio-plots/Isomap/Rectangle/Rectangle_a30b1_9_Isomap_x.jpg width="111" height="168">|
| Spectral |<img src = aspect-ratio-plots/Spectral-megaman/Rectangle/Rectangle_a4b3_Spectral_x.jpg width="111" height="168">|<img src = aspect-ratio-plots/Spectral-megaman/Rectangle/Rectangle_a5b2_Spectral_x.jpg width="111" height="168">|<img src = aspect-ratio-plots/Spectral-megaman/Rectangle/Rectangle_a6b1_9_Spectral_x.jpg width="111" height="168">|<img src = aspect-ratio-plots/Spectral-megaman/Rectangle/Rectangle_a8b1_9_Spectral_x.jpg width="111" height="168">|<img src = aspect-ratio-plots/Spectral-megaman/Rectangle/Rectangle_a10b1_9_Spectral_x.jpg width="111" height="168">|<img src = aspect-ratio-plots/Spectral-megaman/Rectangle/Rectangle_a16b1_9_Spectral_x.jpg width="111" height="168">|<img src = aspect-ratio-plots/Spectral-megaman/Rectangle/Rectangle_a20b1_9_Spectral_x.jpg width="111" height="168">|<img src = aspect-ratio-plots/Spectral-megaman/Rectangle/Rectangle_a30b1_9_Spectral_x.jpg width="111" height="168">|
| LLE     |<img src = https://user-images.githubusercontent.com/91905313/214987749-5c8d2ae3-c255-4b19-9020-983f29b49986.jpg width="111" height="168"> | <img src = https://user-images.githubusercontent.com/91905313/214988271-6b486775-f0d1-4b06-89e0-9c265967c5c1.jpg width="111" height="168"> | <img src = https://user-images.githubusercontent.com/91905313/214988435-b627ee46-35ba-408d-a95e-21c2e4dcbf26.jpg width="111" height="168"> | <img src = https://user-images.githubusercontent.com/91905313/214988702-cf765b9e-5f0b-4c4c-a126-0423f9cf21b0.jpg width="111" height="168"> | <img src = https://user-images.githubusercontent.com/91905313/214988823-56491b8c-142d-4577-894b-b8a17737a88c.jpg width="111" height="168"> | <img src = https://user-images.githubusercontent.com/91905313/214988924-47737a22-958b-4b3a-9729-f2ab04579a53.jpg width="111" height="168"> | <img src = https://user-images.githubusercontent.com/91905313/214989047-e891d22d-2607-4db3-bb1c-f7be25e68355.jpg width="111" height="168"> | <img src = https://user-images.githubusercontent.com/91905313/214989154-b31395b1-ada0-4ca5-8b00-d9e0fa65ce7f.jpg width="111" height="168"> |
| UMAP    | <img src = https://user-images.githubusercontent.com/81238710/187545635-a57c1574-24b4-42b1-9358-16e1f22a7862.jpeg width="111" height="168"> | <img src = https://user-images.githubusercontent.com/81238710/187545732-4950349b-9ca5-4620-83dc-7003d9862efb.jpeg width="111" height="168"> | <img src = https://user-images.githubusercontent.com/81238710/187545792-af037ace-e64c-4372-a30b-0c59a8b5f933.jpeg width="111" height="168"> | <img src = https://user-images.githubusercontent.com/81238710/187545824-4a6271db-73b4-4f5c-9a79-140b4887bb91.jpeg width="111" height="168"> | <img src = https://user-images.githubusercontent.com/81238710/187545910-91cb2a0b-a135-4cce-8078-3145881d6919.jpeg width="111" height="168"> | <img src = https://user-images.githubusercontent.com/81238710/187545953-b5945b47-414f-40aa-b8c1-e2b1af156908.jpeg width="111" height="168"> | <img src = https://user-images.githubusercontent.com/81238710/187545999-2680c19c-8a0b-445b-8b16-8a37a87f09a6.jpeg width="111" height="168"> | <img src = https://user-images.githubusercontent.com/81238710/187546037-0c5cb4f7-a95c-4810-91a1-a65e21df696d.jpeg width="111" height="168"> |

*The best single plot for different aspect ratio* **TODO: add a second row with the eigenvectors chosen in each case**

| ML algo | 1.33         | 2.5       | 3.16 | 4.21 | 5.26 | 8.42 | 10.53 | 15.79 |
| :---                        |    :----:   |   :---: |   :----:    |   :----:    |    :----:    |    :----:    |    :----:    |    :----:    | 
| UMAP    | <img src = https://user-images.githubusercontent.com/81238710/190961595-41515ac0-3437-4c6d-b70f-56f964cfb086.jpeg width="111" height="111"> | <img src = https://user-images.githubusercontent.com/81238710/190961596-5bb5a029-5743-4b7e-9b19-defbded719a7.jpeg width="111" height="111"> | <img src = https://user-images.githubusercontent.com/81238710/190961597-dabfe06d-232b-4c8e-a4b8-fb3956a8b3d3.jpeg width="111" height="111"> | <img src = https://user-images.githubusercontent.com/81238710/190961600-de79c4df-037f-4ba4-b8c0-1880f4ef09e6.jpeg width="111" height="111"> | <img src = https://user-images.githubusercontent.com/81238710/190961601-d6a0e72b-b835-4ad5-8be8-8752c61022d8.jpeg width="111" height="111"> | <img src = https://user-images.githubusercontent.com/81238710/190961602-653e8a59-05d9-4b6a-b26b-ebf6e8443736.jpeg width="111" height="111"> | <img src = https://user-images.githubusercontent.com/81238710/190961603-81266b80-536d-4fa3-bfbb-4d89ed1d34c4.jpeg width="111" height="111"> | <img src = https://user-images.githubusercontent.com/81238710/190961604-d1b06b31-ce45-4ec2-abd2-b242a7c4efd2.jpeg width="111" height="111"> |

Swiss roll
----------
A swiss roll is just a rectangle rolled up. So, the embedding algorithms should output the same results as before, since they are getting the essentially same data, right? This pretty much what we observe. (At a more careful examination, we see that one end of the swiss roll is sometimes more stretched than the other. This is an effect of the sampling density, which is *not exaclty uniform*. When we generate our swiss rolls, the dark (blue) points get denser, because they are in the inner part of the spiral, while the light (yellow) points become sparser. As we will discuss in more detail [here --to be written shortly --](variable-density.md), some ML algorithms can be sensitive to the non-uniformity of the samples.]

**Uniform Density**

| ML algo | 1.33         | 2.5       | 3.16 | 4.21 | 5.26 | 8.42 | 10.53 |
| :---                        |    :----:   |   :---: |   :----:    |   :----:    |    :----:    |    :----:    |    :----:    |
| Isomap     | <img src =aspect-ratio-plots/Isomap/SwissRoll/Swiss_Roll_a8b6_Isomap_phi.jpg width="125" height="189"> | <img src =aspect-ratio-plots/Isomap/SwissRoll/Swiss_Roll_a10b4_Isomap_phi.jpg width="125" height="189"> | <img src =aspect-ratio-plots/Isomap/SwissRoll/Swiss_Roll_a12b3_8_Isomap_phi.jpg width="125" height="189"> | <img src =aspect-ratio-plots/Isomap/SwissRoll/Swiss_Roll_a8b1_9_Isomap_phi.jpg width="125" height="189"> | <img src =aspect-ratio-plots/Isomap/SwissRoll/Swiss_Roll_a10b1_9_Isomap_phi.jpg width="125" height="189"> | <img src =aspect-ratio-plots/Isomap/SwissRoll/Swiss_Roll_a16b1_9_Isomap_phi.jpg width="125" height="189"> | <img src =aspect-ratio-plots/Isomap/SwissRoll/Swiss_Roll_a20b1_9_Isomap_phi.jpg width="125" height="189"> |
| Spectral    | <img src =aspect-ratio-plots/Spectral-megaman/SwissRoll/Swiss_Roll_a8b6_Spectral_phi.jpg width="125" height="189"> | <img src =aspect-ratio-plots/Spectral-megaman/SwissRoll/Swiss_Roll_a10b4_Spectral_phi.jpg width="125" height="189"> | <img src =aspect-ratio-plots/Spectral-megaman/SwissRoll/Swiss_Roll_a12b3_8_Spectral_phi.jpg width="125" height="189"> | <img src =aspect-ratio-plots/Spectral-megaman/SwissRoll/Swiss_Roll_a8b1_9_Spectral_phi.jpg width="125" height="189"> | <img src =aspect-ratio-plots/Spectral-megaman/SwissRoll/Swiss_Roll_a10b1_9_Spectral_phi.jpg width="125" height="189"> | <img src =aspect-ratio-plots/Spectral-megaman/SwissRoll/Swiss_Roll_a16b1_9_Spectral_phi.jpg width="125" height="189"> | <img src =aspect-ratio-plots/Spectral-megaman/SwissRoll/Swiss_Roll_a20b1_9_Spectral_phi.jpg width="125" height="189"> |
| LLE     | <img src =https://user-images.githubusercontent.com/91905313/214991475-43cf3b4f-41ba-4f75-90bf-c1bd58e3c8c6.jpg width="125" height="189"> | <img src =https://user-images.githubusercontent.com/91905313/214991539-db158a12-28c2-4b98-9a6b-b0c5cb7b18e1.jpg width="125" height="189"> | <img src =https://user-images.githubusercontent.com/91905313/214991577-3e92f51f-5b62-44bb-b812-f40af32261e9.jpg width="125" height="189"> | <img src =https://user-images.githubusercontent.com/91905313/214991612-85aaa503-1ad4-4c24-b5d8-00862048ab74.jpg width="125" height="189"> | <img src =https://user-images.githubusercontent.com/91905313/214991644-b86dca34-bd89-41d0-9949-2fc4435ff91a.jpg width="125" height="189"> | <img src =https://user-images.githubusercontent.com/91905313/214991665-3c949ca5-a2af-45a1-a7b8-de101ddfdd27.jpg width="125" height="189"> | <img src =https://user-images.githubusercontent.com/91905313/214991692-385324ed-880d-4ef6-87dd-bdd59d7f5966.jpg width="125" height="189"> |
| UMAP    | <img src =https://user-images.githubusercontent.com/81238710/187552599-7a458012-099d-414c-9705-6bbfa97bbfd6.jpeg width="125" height="189"> | <img src =https://user-images.githubusercontent.com/81238710/187552649-757fc126-a931-4d85-aa68-5b85891a47dc.jpeg width="125" height="189"> | <img src =https://user-images.githubusercontent.com/81238710/187552670-cd369134-2530-41ca-b6ec-cc73eaa6550b.jpeg width="125" height="189"> | <img src =https://user-images.githubusercontent.com/81238710/187552560-61f85e78-c0d6-4644-88ac-1b94b55e6e0c.jpeg width="125" height="189"> | <img src =https://user-images.githubusercontent.com/81238710/187552718-1f48c64b-b812-4cd0-9d52-bd6a67a80d76.jpeg width="125" height="189"> | <img src =https://user-images.githubusercontent.com/81238710/187552747-7886c7da-0aa2-489a-8632-92cdfba6d7df.jpeg width="125" height="189"> | <img src =https://user-images.githubusercontent.com/81238710/187552757-9628d143-1ecf-4587-86e7-74cf97355032.jpeg width="125" height="189"> |

*The best single plot for different aspect ratios*

| ML algo | 1.33         | 2.5       | 3.16 | 4.21 | 5.26 | 8.42 | 10.53 |
| :---                        |    :----:   |   :---: |   :----:    |   :----:    |    :----:    |    :----:    |    :----:    |
| UMAP    | <img src =https://user-images.githubusercontent.com/81238710/190962239-ba4b96ec-5b65-4a84-a8f3-f70b3d46bde5.jpeg width="125" height="189"> | <img src =https://user-images.githubusercontent.com/81238710/190962241-9b9ee4ce-ba3a-4327-8d0c-1f4099e9de89.jpeg width="125" height="189"> | <img src =https://user-images.githubusercontent.com/81238710/190962244-b710a3aa-053f-4af2-8d58-f2256d54100d.jpeg width="125" height="189"> | <img src =https://user-images.githubusercontent.com/81238710/190962238-03541129-ef57-4fab-944e-b8c14b988e90.jpeg width="125" height="189"> | <img src =https://user-images.githubusercontent.com/81238710/190962240-619ccf87-f876-414f-9af2-4d81f600c4f5.jpeg width="125" height="189"> |  |  |

**Variable Density**

| ML algo | 1.33         | 2.5       | 3.16 | 4.21 | 5.26 | 8.42 | 10.53 |
| :---                        |    :----:   |   :---: |   :----:    |   :----:    |    :----:    |    :----:    |    :----:    |
| UMAP    | <img src =https://user-images.githubusercontent.com/81238710/190932516-a07d940d-90bb-4a37-bc8c-39c4fa318eb5.jpeg width="125" height="189"> | <img src =https://user-images.githubusercontent.com/81238710/190932523-c81f77bf-15c1-4996-b354-0f9c9d8e3d49.jpeg width="125" height="189"> | <img src =https://user-images.githubusercontent.com/81238710/190932526-1d658138-d178-466b-b678-7b04aa244222.jpeg width="125" height="189"> | <img src =https://user-images.githubusercontent.com/81238710/190932506-7a37bd1d-27c8-4700-ab6b-0df0b6b6936e.jpeg width="125" height="189"> | <img src =https://user-images.githubusercontent.com/81238710/190932519-0984ba8e-3e37-49fc-8da0-aa0d0be19c23.jpeg width="125" height="189"> | <img src =https://user-images.githubusercontent.com/81238710/190932528-8d56799a-bbd4-4bd2-8323-f852403ae94c.jpeg width="125" height="189"> | <img src =https://user-images.githubusercontent.com/81238710/190932539-cd005b07-7b2a-4ce4-a52b-c86a6bc1f0a5.jpeg width="125" height="189"> |

Rectangle with hole
-------------------
Because ML algorithms are "myopic", and only see small neighborhoods around each point, creating a hole in the data complicates their work. Some of the challenges are minor; for example, there are multiple ways to map the data that are approximately the same -- this is what causes Isomap to "round the hole". This effect will disappear gradually with more densely sampled data. Other challenges are more serious: a long rectangle with a hole is in fact *the union of 4 long rectangles*! 

**Uniform Density**

| ML algo | 1.33         | 2.5       | 3.16 | 4.21 | 5.26 | 8.42 | 10.53 | 15.79 |
| :---                        |    :----:   |   :---: |   :----:    |   :----:    |    :----:    |    :----:    |    :----:    |    :----:    | 
| Isomap     | <img src = aspect-ratio-plots/Isomap/RectangleHole/Rectangle_hole_a4b3_Isomap_x.jpg width="111" height="168"> | <img src = aspect-ratio-plots/Isomap/RectangleHole/Rectangle_hole_a5b2_Isomap_x.jpg width="111" height="168"> | <img src = aspect-ratio-plots/Isomap/RectangleHole/Rectangle_hole_a6b1_9_Isomap_x.jpg width="111" height="168"> | <img src = aspect-ratio-plots/Isomap/RectangleHole/Rectangle_hole_a8b1_9_Isomap_x.jpg width="111" height="168"> | <img src = aspect-ratio-plots/Isomap/RectangleHole/Rectangle_hole_a10b1_9_Isomap_x.jpg width="111" height="168"> | <img src = aspect-ratio-plots/Isomap/RectangleHole/Rectangle_hole_a16b1_9_Isomap_x.jpg width="111" height="168"> | <img src = aspect-ratio-plots/Isomap/RectangleHole/Rectangle_hole_a20b1_9_Isomap_x.jpg width="111" height="168"> | <img src = aspect-ratio-plots/Isomap/RectangleHole/Rectangle_hole_a30b1_9_Isomap_x.jpg width="111" height="168"> |
| Spectral     | <img src = aspect-ratio-plots/Spectral-megaman/RectangleHole/Rectangle_hole_a4b3_Spectral_x.jpg width="111" height="168"> | <img src = aspect-ratio-plots/Spectral-megaman/RectangleHole/Rectangle_hole_a5b2_Spectral_x.jpg width="111" height="168"> | <img src = aspect-ratio-plots/Spectral-megaman/RectangleHole/Rectangle_hole_a6b1_9_Spectral_x.jpg width="111" height="168"> | <img src = aspect-ratio-plots/Spectral-megaman/RectangleHole/Rectangle_hole_a8b1_9_Spectral_x.jpg width="111" height="168"> | <img src = aspect-ratio-plots/Spectral-megaman/RectangleHole/Rectangle_hole_a10b1_9_Spectral_x.jpg width="111" height="168"> | <img src = aspect-ratio-plots/Spectral-megaman/RectangleHole/Rectangle_hole_a16b1_9_Spectral_x.jpg width="111" height="168"> | <img src = aspect-ratio-plots/Spectral-megaman/RectangleHole/Rectangle_hole_a20b1_9_Spectral_x.jpg width="111" height="168"> | <img src = aspect-ratio-plots/Spectral-megaman/RectangleHole/Rectangle_hole_a30b1_9_Spectral_x.jpg width="111" height="168"> |
| LLE     | <img src = https://user-images.githubusercontent.com/91905313/214993944-ba493936-9879-4d54-a496-7529fe8f84f6.jpg width="111" height="168"> | <img src = https://user-images.githubusercontent.com/91905313/214993989-2a3d327f-4e27-4c39-ab22-6e5c80ec3ba7.jpg width="111" height="168"> | <img src = https://user-images.githubusercontent.com/91905313/214994023-4dfd7615-1dd8-4042-af0d-6dbe481ae723.jpg width="111" height="168"> | <img src = https://user-images.githubusercontent.com/91905313/214994065-864950b2-57a5-43e3-8b50-6d4b7dfb632a.jpg width="111" height="168"> | <img src = https://user-images.githubusercontent.com/91905313/214994092-f0f82b07-4d48-4361-bbb6-da1286f0530d.jpg width="111" height="168"> | <img src = https://user-images.githubusercontent.com/91905313/214994121-f00cf572-7671-453c-a1b3-91bf34d210af.jpg width="111" height="168"> | <img src = https://user-images.githubusercontent.com/91905313/214994152-dd50ef16-3c7a-4eee-9fa4-ca047fd4550f.jpg width="111" height="168"> | <img src = https://user-images.githubusercontent.com/91905313/214994162-faf95e1a-198c-4abe-9b68-fe0af25b4a91.jpg width="111" height="168"> | 
| UMAP    | <img src = https://user-images.githubusercontent.com/81238710/187547422-fc55c21a-5e2a-44e4-a1a3-9206bb326786.jpeg width="111" height="168"> | <img src = https://user-images.githubusercontent.com/81238710/187547455-2186efe7-6a8a-4502-ba8d-a42ee9884538.jpeg width="111" height="168"> | <img src = https://user-images.githubusercontent.com/81238710/187547489-e8a71bc2-7731-426b-b500-ffc66d6391d6.jpeg width="111" height="168"> | <img src = https://user-images.githubusercontent.com/81238710/187547539-4952fef8-61bb-4f20-a786-9388168b2612.jpeg width="111" height="168"> | <img src = https://user-images.githubusercontent.com/81238710/187547591-b0461342-c5b1-40b3-8ad4-2189c637a602.jpeg width="111" height="168"> | <img src = https://user-images.githubusercontent.com/81238710/187547621-bbdce286-2da6-4741-b137-5142c7415720.jpeg width="111" height="168"> | <img src = https://user-images.githubusercontent.com/81238710/187547671-25ba99fb-3e85-486d-a4cc-ff10db7630f0.jpeg width="111" height="168"> | <img src = https://user-images.githubusercontent.com/81238710/187547799-368e24c9-c819-4082-a6cf-8f0e6279d52a.jpeg width="111" height="168"> | 

*The best single plot for different aspect ratio*

| ML algo | 1.33         | 2.5       | 3.16 | 4.21 | 5.26 | 8.42 | 10.53 | 15.79 |
| :---                        |    :----:   |   :---: |   :----:    |   :----:    |    :----:    |    :----:    |    :----:    |    :----:    | 
| UMAP    | <img src = https://user-images.githubusercontent.com/81238710/190962576-5093604c-3e4c-4ad5-a78e-59d1bd10b0ba.jpeg width="111" height="168"> | <img src = https://user-images.githubusercontent.com/81238710/190962577-24613454-b43d-489a-b8bd-85d779bfe297.jpeg width="111" height="168"> | <img src = https://user-images.githubusercontent.com/81238710/190962578-8dba2f01-3077-4e2b-b0e8-78f192dde5a6.jpeg width="111" height="168"> | <img src = https://user-images.githubusercontent.com/81238710/190962579-43019d04-e61a-4027-961d-a69d7bf9c138.jpeg width="111" height="168"> | <img src = https://user-images.githubusercontent.com/81238710/190962580-f4000ab3-7f66-4974-8343-8e86405b7347.jpeg width="111" height="168"> | <img src = https://user-images.githubusercontent.com/81238710/190962582-d49c09be-abed-43ab-93c1-076e17d818fb.jpeg width="111" height="168"> | <img src = https://user-images.githubusercontent.com/81238710/190962586-157a127b-d72e-46bf-b3a1-251c7c844e0e.jpeg width="111" height="168"> | <img src = https://user-images.githubusercontent.com/81238710/190962587-19b65f01-aef4-4186-af6a-6483e03ddc3b.jpeg width="111" height="168"> |


Torus
-----

| ML algo | 1.33         | 2.5       | 3.16 | 4.21 | 5.26 | 8.42 |
| :---                        |    :----:   |   :---: |   :----:    |   :----:    |    :----:    |    :----:    |
| Isomap     | <img src = aspect-ratio-plots/Isomap/Torus/Torus_a4b3_Isomap_z.jpg width="142" height="346"> | <img src = aspect-ratio-plots/Isomap/Torus/Torus_a5b2_Isomap_z.jpg width="142" height="346"> | <img src = aspect-ratio-plots/Isomap/Torus/Torus_a6b1_9_Isomap_z.jpg width="142" height="346"> | <img src = aspect-ratio-plots/Isomap/Torus/Torus_a8b1_9_Isomap_z.jpg width="142" height="346"> | <img src = aspect-ratio-plots/Isomap/Torus/Torus_a10b1_9_Isomap_z.jpg width="142" height="346"> | <img src = aspect-ratio-plots/Isomap/Torus/Torus_a16b1_9_Isomap_z.jpg width="142" height="346"> | 
| Spectral     | <img src = aspect-ratio-plots/Spectral-megaman/Torus/Torus_a4b3_Spectral_z.jpg width="142" height="346"> | <img src = aspect-ratio-plots/Spectral-megaman/Torus/Torus_a5b2_Spectral_z.jpg width="142" height="346"> | <img src = aspect-ratio-plots/Spectral-megaman/Torus/Torus_a6b1_9_Spectral_z.jpg width="142" height="346"> | <img src = aspect-ratio-plots/Spectral-megaman/Torus/Torus_a8b1_9_Spectral_z.jpg width="142" height="346"> | <img src = aspect-ratio-plots/Spectral-megaman/Torus/Torus_a10b1_9_Spectral_z.jpg width="142" height="346"> | <img src = aspect-ratio-plots/Spectral-megaman/Torus/Torus_a16b1_9_Spectral_z.jpg width="142" height="346"> | 
| LLE     | <img src = https://user-images.githubusercontent.com/91905313/187164202-be80d354-54e7-46b4-8729-edebf1f7632e.jpg width="142" height="346"> | <img src = https://user-images.githubusercontent.com/91905313/187164220-7fda116a-8d3a-47e2-af95-46284467f4e1.jpg width="142" height="346"> | <img src = https://user-images.githubusercontent.com/91905313/187164236-cd5da8dc-c537-44d4-8180-049c62f52ce3.jpg width="142" height="346"> | <img src = https://user-images.githubusercontent.com/91905313/187164753-0a59f9ed-8d33-49b7-ac8b-f0c2fe84b0be.jpg width="142" height="346"> | <img src = https://user-images.githubusercontent.com/91905313/187164761-db0019de-175c-4f67-bf39-a60bbfc793be.jpg width="142" height="346"> | <img src = https://user-images.githubusercontent.com/91905313/187164770-c311b4c7-a624-4282-91c5-4316ac323f28.jpg width="142" height="346"> | 
| UMAP    | <img src = https://user-images.githubusercontent.com/81238710/187553518-82f92e8f-ddac-4a01-a6d9-026d3ac8c886.jpeg width="142" height="150"> | <img src = https://user-images.githubusercontent.com/81238710/187553524-c44b6716-a36d-43be-b947-3611a23acf2a.jpeg width="142" height="150"> | <img src = https://user-images.githubusercontent.com/81238710/187553532-d7134782-a5bf-4846-aeca-b6972fd82ce7.jpeg width="142" height="150"> | <img src = https://user-images.githubusercontent.com/81238710/187553542-1bcb3ba3-35a6-4980-a36c-4c185875d1dc.jpeg width="142" height="150"> | <img src = https://user-images.githubusercontent.com/81238710/187553552-a961540d-8f80-4713-a05d-b7a13fa0d997.jpeg width="142" height="150"> | <img src = https://user-images.githubusercontent.com/81238710/187553562-60920c61-1d2b-43c6-bb23-bbf822e153ac.jpeg width="142" height="150"> |

*The best single plot for different aspect ratios*

| ML algo | 1.33         | 2.5       | 3.16 | 4.21 | 5.26 | 8.42 |
| :---                        |    :----:   |   :---: |   :----:    |   :----:    |    :----:    |    :----:    |
| UMAP    | <img src = https://user-images.githubusercontent.com/81238710/190962979-c6568816-e574-42ad-b8eb-9564c66afad3.jpeg width="142" height="150"> | <img src = https://user-images.githubusercontent.com/81238710/190962983-37b2e8ef-dc1b-4bb6-b5f8-2218c6769e66.jpeg width="142" height="150"> | <img src = https://user-images.githubusercontent.com/81238710/190962985-39688127-a1fa-45fa-bd8c-fb8343d4f8bb.jpeg width="142" height="150"> | <img src = https://user-images.githubusercontent.com/81238710/190962986-f4e05eb9-b00e-4e55-b065-561680dd0a2d.jpeg width="142" height="150"> | <img src = https://user-images.githubusercontent.com/81238710/190962989-d1f6081f-98ff-4064-881b-360bebcb8ba5.jpeg width="142" height="150"> | <img src = https://user-images.githubusercontent.com/81238710/190962990-b72fb3ae-a058-4e87-bae1-78f650581d58.jpeg width="142" height="150"> |

+ single plot of best embedding (aspect ratio x alg )
+ 1-2 complete examples

**Variable Density**

| ML algo | 1.33         | 2.5       | 3.16 | 4.21 | 5.26 | 8.42 |
| :---                        |    :----:   |   :---: |   :----:    |   :----:    |    :----:    |    :----:    |
| UMAP    | <img src = https://user-images.githubusercontent.com/81238710/190932642-a5d50246-10a8-4843-8faa-524f2015c18d.jpeg width="142" height="150"> | <img src = https://user-images.githubusercontent.com/81238710/190932643-8c622a2c-f80b-41b2-a052-f704ec550d09.jpeg width="142" height="150"> | <img src = https://user-images.githubusercontent.com/81238710/190932644-b6ade052-e47c-4ddd-b2ab-ad7f6ddb2956.jpeg width="142" height="150"> | <img src = https://user-images.githubusercontent.com/81238710/190932645-b2acf0a9-86ee-4cb9-96e2-e672a4f299d7.jpeg width="142" height="150"> | <img src = https://user-images.githubusercontent.com/81238710/190932646-e09da5dd-a387-4a05-8bc1-3bd1f6d3b35a.jpeg width="142" height="150"> | <img src = https://user-images.githubusercontent.com/81238710/190932647-3c2d1f16-35d4-4a24-a1d3-6ce8e03d4326.jpeg width="142" height="150"> |


A manifold with $d=3$ 
---------------------
(brick?, ellipsoid? swiss roll?)

A "cute" manifold
------------------

Explanation, diagnosis, and what to do
---------------------------------------

For all ML algorithms presented here, the $m$ embedding coordinates are eigenvectors of a matrix. We would like each of them to represent an independent coordinate, but, in reality, the picture is more complex. If we compute many more than $m$ eigenvectors, we see that some or the higher order eigenvectors are harmonics of the preceding ones.

[Here, v1, v2 and v5 are harmonics of v0, and v4 is a harmonic of v3](https://github.com/mk322/manifold-learning-examples/blob/main/aspect-ratio-plots/Spectral-megaman/SwissRoll/Swiss_Roll_a10b4_Spectral_phi.jpg)

The larger the aspect ratio, the more harmonics of v0, the first eigenvector, will be found immediately following v0.

If we select harmonics among our embedding coordinate, the observed dimension of the embedding is *smaller than $d$, the intrinsic dimension. This is the main diagnostic that the **Independent Eigenvector Selection** (this is how we call our goal in technical terms) has not succeeded. In fact, if the dimension observed is not equal to $d$ everywhere, the embedding *has failed*. For simple cases, the drop in dimension happens everywhere (see above), for more complicated manifolds, it can happen only on parts of the data.

![A rectangle with hole is a union of long rectangles. Some are embedded correctly and some not. For this rectangle, we need $m>2$ eigenvectors to obtain an embedding]()

###What to do?

We must search among the eigenvectors, from lower orders to higher, for a set of $m$ that preserve $d$ everywhere. When the manifold becomes more difficult (thinner, closer to itself) we may *need to increase $m$, the number of embedding coordinates* -- as shown by Johanthan Bates here [The embedding dimension of Laplacian eigenfunction maps](https://arxiv.org/abs/1605.01643).


Further reading and examples with real data 
--------------------------------------------

<a href="https://proceedings.neurips.cc/paper/2019/hash/6a10bbd480e4c5573d8f3af73ae0454b-Abstract.html">Selecting the independent coordinates of manifolds with large aspect ratios </a> discusses the problems in the case of Spectral Embedding (the authors have experimented with other algorithms such as LTSA and UMAP as well, observing similar behaviors) and proposes a solution, while <a href="https://projecteuclid.org/journals/annals-of-applied-statistics/volume-2/issue-3/Horseshoes-in-multidimensional-scaling-and-local-kernel-methods/10.1214/08-AOAS165.full">Horeshoes in multidimensional scaling and local kernel methods</a> does the same for MDS. In [Parsimonious representation of nonlinear dynamical systems through manifold learning: A chemotaxis case study](https://www.sciencedirect.com/science/article/pii/S1063520315000949) describe the aspect ratio problem for ML algorithm, and introduce the name **Independent Eigenvector Selection** and a first algorithm to correct it. 

Contributions
--------------
*MK* ;*MM* concept, main text, references; *HR*; *QW*; *YW* .





