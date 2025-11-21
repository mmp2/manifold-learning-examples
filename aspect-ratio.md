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
| UMAP    | <img src = https://user-images.githubusercontent.com/81238710/217629208-ba33d513-11ae-4ef9-a059-cdf3ff14d323.jpeg width="111" height="168"> | <img src = https://user-images.githubusercontent.com/81238710/217629255-5068adfe-384a-4908-8e31-0f249d0d50de.jpeg width="111" height="168"> | <img src = https://user-images.githubusercontent.com/81238710/217629272-582ce8da-5e66-4dae-b639-8e3486eb8060.jpeg width="111" height="168"> | <img src = https://user-images.githubusercontent.com/81238710/217629291-db79837e-7439-46c7-98ec-e5d7876ae60e.jpeg width="111" height="168"> | <img src = https://user-images.githubusercontent.com/81238710/217629311-8a1f0f08-3790-469d-8dc1-46f1a50db2ce.jpeg width="111" height="168"> | <img src = https://user-images.githubusercontent.com/81238710/217629325-0f893e5e-ed21-499f-bb2b-4cd220b4c2e9.jpeg width="111" height="168"> | <img src = https://user-images.githubusercontent.com/81238710/217629341-29982e3f-e6c5-4889-ab37-e7a7a2d2d942.jpeg width="111" height="168"> | <img src = https://user-images.githubusercontent.com/81238710/217629357-54cce79e-63d3-4cf8-af01-a6f8dfb7cb98.jpeg width="111" height="168"> |

*The best single plot for different aspect ratio* 

| ML algo | 1.33         | 2.5       | 3.16 | 4.21 | 5.26 | 8.42 | 10.53 | 15.79 |
| :---                        |    :----:   |   :---: |   :----:    |   :----:    |    :----:    |    :----:    |    :----:    |    :----:    | 
| UMAP    | <img src = https://user-images.githubusercontent.com/81238710/190961595-41515ac0-3437-4c6d-b70f-56f964cfb086.jpeg width="111" height="111"> | <img src = https://user-images.githubusercontent.com/81238710/190961596-5bb5a029-5743-4b7e-9b19-defbded719a7.jpeg width="111" height="111"> | <img src = https://user-images.githubusercontent.com/81238710/190961597-dabfe06d-232b-4c8e-a4b8-fb3956a8b3d3.jpeg width="111" height="111"> | <img src = https://user-images.githubusercontent.com/81238710/190961600-de79c4df-037f-4ba4-b8c0-1880f4ef09e6.jpeg width="111" height="111"> | <img src = https://user-images.githubusercontent.com/81238710/190961601-d6a0e72b-b835-4ad5-8be8-8752c61022d8.jpeg width="111" height="111"> | <img src = https://user-images.githubusercontent.com/81238710/190961602-653e8a59-05d9-4b6a-b26b-ebf6e8443736.jpeg width="111" height="111"> | <img src = https://user-images.githubusercontent.com/81238710/190961603-81266b80-536d-4fa3-bfbb-4d89ed1d34c4.jpeg width="111" height="111"> | <img src = https://user-images.githubusercontent.com/81238710/190961604-d1b06b31-ce45-4ec2-abd2-b242a7c4efd2.jpeg width="111" height="111"> |
| Eigenvectors ($v_1$ denotes first eigenvector, $v_2$ denotes second eigenvector, and so on) | $\{v_1, v_2\}$ |  $\{v_1, v_3\}$ |  $\{v_1, v_4\}$ |  $\{v_1, v_5\}$ |  $\{v_1, v_6\}$ |  $\{v_1, v_8\}$ |  $\{v_1, v_8\}$ |  $\{v_1, v_{10}\}$ | 

Swiss roll
----------
A swiss roll is just a rectangle rolled up. So, the embedding algorithms should output the same results as before, since they are getting the essentially same data, right? This pretty much what we observe. (At a more careful examination, we see that one end of the swiss roll is sometimes more stretched than the other. This is an effect of the sampling density, which is *not exactly uniform*). When we generate our swiss rolls, the dark (blue) points get denser, because they are in the inner part of the spiral, while the light (yellow) points become sparser. As we will discuss in more detail [here](variable_density.md), some ML algorithms can be sensitive to the non-uniformity of the samples.

**Uniform Density**

| ML algo | 1.33         | 2.5       | 3.16 | 4.21 | 5.26 | 8.42 | 10.53 |
| :---                        |    :----:   |   :---: |   :----:    |   :----:    |    :----:    |    :----:    |    :----:    |
| Isomap     | <img src =aspect-ratio-plots/Isomap/SwissRoll/Swiss_Roll_a8b6_Isomap_phi.jpg width="125" height="189"> | <img src =aspect-ratio-plots/Isomap/SwissRoll/Swiss_Roll_a10b4_Isomap_phi.jpg width="125" height="189"> | <img src =aspect-ratio-plots/Isomap/SwissRoll/Swiss_Roll_a12b3_8_Isomap_phi.jpg width="125" height="189"> | <img src =aspect-ratio-plots/Isomap/SwissRoll/Swiss_Roll_a8b1_9_Isomap_phi.jpg width="125" height="189"> | <img src =aspect-ratio-plots/Isomap/SwissRoll/Swiss_Roll_a10b1_9_Isomap_phi.jpg width="125" height="189"> | <img src =aspect-ratio-plots/Isomap/SwissRoll/Swiss_Roll_a16b1_9_Isomap_phi.jpg width="125" height="189"> | <img src =aspect-ratio-plots/Isomap/SwissRoll/Swiss_Roll_a20b1_9_Isomap_phi.jpg width="125" height="189"> |
| Spectral    | <img src =aspect-ratio-plots/Spectral-megaman/SwissRoll/Swiss_Roll_a8b6_Spectral_phi.jpg width="125" height="189"> | <img src =aspect-ratio-plots/Spectral-megaman/SwissRoll/Swiss_Roll_a10b4_Spectral_phi.jpg width="125" height="189"> | <img src =aspect-ratio-plots/Spectral-megaman/SwissRoll/Swiss_Roll_a12b3_8_Spectral_phi.jpg width="125" height="189"> | <img src =aspect-ratio-plots/Spectral-megaman/SwissRoll/Swiss_Roll_a8b1_9_Spectral_phi.jpg width="125" height="189"> | <img src =aspect-ratio-plots/Spectral-megaman/SwissRoll/Swiss_Roll_a10b1_9_Spectral_phi.jpg width="125" height="189"> | <img src =aspect-ratio-plots/Spectral-megaman/SwissRoll/Swiss_Roll_a16b1_9_Spectral_phi.jpg width="125" height="189"> | <img src =aspect-ratio-plots/Spectral-megaman/SwissRoll/Swiss_Roll_a20b1_9_Spectral_phi.jpg width="125" height="189"> |
| LLE     | <img src =https://user-images.githubusercontent.com/91905313/214991475-43cf3b4f-41ba-4f75-90bf-c1bd58e3c8c6.jpg width="125" height="189"> | <img src =https://user-images.githubusercontent.com/91905313/214991539-db158a12-28c2-4b98-9a6b-b0c5cb7b18e1.jpg width="125" height="189"> | <img src =https://user-images.githubusercontent.com/91905313/214991577-3e92f51f-5b62-44bb-b812-f40af32261e9.jpg width="125" height="189"> | <img src =https://user-images.githubusercontent.com/91905313/214991612-85aaa503-1ad4-4c24-b5d8-00862048ab74.jpg width="125" height="189"> | <img src =https://user-images.githubusercontent.com/91905313/214991644-b86dca34-bd89-41d0-9949-2fc4435ff91a.jpg width="125" height="189"> | <img src =https://user-images.githubusercontent.com/91905313/214991665-3c949ca5-a2af-45a1-a7b8-de101ddfdd27.jpg width="125" height="189"> | <img src =https://user-images.githubusercontent.com/91905313/214991692-385324ed-880d-4ef6-87dd-bdd59d7f5966.jpg width="125" height="189"> |
| UMAP    | <img src =https://user-images.githubusercontent.com/81238710/217629593-31434d8a-a5fc-408a-8b0c-74c1f40d2a2a.jpeg width="125" height="189"> | <img src =https://user-images.githubusercontent.com/81238710/217629616-3b55814b-503b-4e23-940b-762e74b5c090.jpeg width="125" height="189"> | <img src =https://user-images.githubusercontent.com/81238710/217629624-1843cefd-823b-4ba5-9e3f-631b2259f6d1.jpeg width="125" height="189"> | <img src =https://user-images.githubusercontent.com/81238710/217629577-519b82a5-e456-4d59-a3ea-7f7e835e4486.jpeg width="125" height="189"> | <img src =https://user-images.githubusercontent.com/81238710/217629607-0f218c87-44c2-4f3f-9fb5-98eda2293b1c.jpeg width="125" height="189"> | <img src =https://user-images.githubusercontent.com/81238710/217629633-0942ed4e-38fe-4a80-be43-3d3954ddc140.jpeg width="125" height="189"> | <img src =https://user-images.githubusercontent.com/81238710/217629645-b1bb367f-30d8-4483-a289-d1f63823ea61.jpeg width="125" height="189"> |

*The best single plot for different aspect ratios*

| ML algo | 1.33         | 2.5       | 3.16 | 4.21 | 5.26 | 8.42 | 10.53 |
| :---                        |    :----:   |   :---: |   :----:    |   :----:    |    :----:    |    :----:    |    :----:    |
| UMAP    | <img src =https://user-images.githubusercontent.com/81238710/190962239-ba4b96ec-5b65-4a84-a8f3-f70b3d46bde5.jpeg width="125" height="189"> | <img src =https://user-images.githubusercontent.com/81238710/190962241-9b9ee4ce-ba3a-4327-8d0c-1f4099e9de89.jpeg width="125" height="189"> | <img src =https://user-images.githubusercontent.com/81238710/190962244-b710a3aa-053f-4af2-8d58-f2256d54100d.jpeg width="125" height="189"> | <img src =https://user-images.githubusercontent.com/81238710/190962238-03541129-ef57-4fab-944e-b8c14b988e90.jpeg width="125" height="189"> | <img src =https://user-images.githubusercontent.com/81238710/190962240-619ccf87-f876-414f-9af2-4d81f600c4f5.jpeg width="125" height="189"> |  |  |
|Eigenvectors| $\{v_1, v_3\}$ |  $\{v_1, v_4\}$ |  $\{v_1, v_4\}$ | $\{v_1, v_4\}$ |  $\{v_1, v_7\}$ |  | | 



Rectangle with hole
-------------------
Because ML algorithms are "myopic", and only see small neighborhoods around each point, creating a hole in the data complicates their work. Some of the challenges are minor; for example, there are multiple ways to map the data that are approximately the same -- this is what causes Isomap to "round the hole". This effect will disappear gradually with more densely sampled data. Other challenges are more serious: a long rectangle with a hole is in fact *the union of 4 long rectangles*! 

**Uniform Density**

| ML algo | 1.33         | 2.5       | 3.16 | 4.21 | 5.26 | 8.42 | 10.53 | 15.79 |
| :---                        |    :----:   |   :---: |   :----:    |   :----:    |    :----:    |    :----:    |    :----:    |    :----:    | 
| Isomap     | <img src = aspect-ratio-plots/Isomap/RectangleHole/Rectangle_hole_a4b3_Isomap_x.jpg width="111" height="168"> | <img src = aspect-ratio-plots/Isomap/RectangleHole/Rectangle_hole_a5b2_Isomap_x.jpg width="111" height="168"> | <img src = aspect-ratio-plots/Isomap/RectangleHole/Rectangle_hole_a6b1_9_Isomap_x.jpg width="111" height="168"> | <img src = aspect-ratio-plots/Isomap/RectangleHole/Rectangle_hole_a8b1_9_Isomap_x.jpg width="111" height="168"> | <img src = aspect-ratio-plots/Isomap/RectangleHole/Rectangle_hole_a10b1_9_Isomap_x.jpg width="111" height="168"> | <img src = aspect-ratio-plots/Isomap/RectangleHole/Rectangle_hole_a16b1_9_Isomap_x.jpg width="111" height="168"> | <img src = aspect-ratio-plots/Isomap/RectangleHole/Rectangle_hole_a20b1_9_Isomap_x.jpg width="111" height="168"> | <img src = aspect-ratio-plots/Isomap/RectangleHole/Rectangle_hole_a30b1_9_Isomap_x.jpg width="111" height="168"> |
| Spectral     | <img src = aspect-ratio-plots/Spectral-megaman/RectangleHole/Rectangle_hole_a4b3_Spectral_x.jpg width="111" height="168"> | <img src = aspect-ratio-plots/Spectral-megaman/RectangleHole/Rectangle_hole_a5b2_Spectral_x.jpg width="111" height="168"> | <img src = aspect-ratio-plots/Spectral-megaman/RectangleHole/Rectangle_hole_a6b1_9_Spectral_x.jpg width="111" height="168"> | <img src = aspect-ratio-plots/Spectral-megaman/RectangleHole/Rectangle_hole_a8b1_9_Spectral_x.jpg width="111" height="168"> | <img src = aspect-ratio-plots/Spectral-megaman/RectangleHole/Rectangle_hole_a10b1_9_Spectral_x.jpg width="111" height="168"> | <img src = aspect-ratio-plots/Spectral-megaman/RectangleHole/Rectangle_hole_a16b1_9_Spectral_x.jpg width="111" height="168"> | <img src = aspect-ratio-plots/Spectral-megaman/RectangleHole/Rectangle_hole_a20b1_9_Spectral_x.jpg width="111" height="168"> | <img src = aspect-ratio-plots/Spectral-megaman/RectangleHole/Rectangle_hole_a30b1_9_Spectral_x.jpg width="111" height="168"> |
| LLE     | <img src = https://user-images.githubusercontent.com/91905313/214993944-ba493936-9879-4d54-a496-7529fe8f84f6.jpg width="111" height="168"> | <img src = https://user-images.githubusercontent.com/91905313/214993989-2a3d327f-4e27-4c39-ab22-6e5c80ec3ba7.jpg width="111" height="168"> | <img src = https://user-images.githubusercontent.com/91905313/214994023-4dfd7615-1dd8-4042-af0d-6dbe481ae723.jpg width="111" height="168"> | <img src = https://user-images.githubusercontent.com/91905313/214994065-864950b2-57a5-43e3-8b50-6d4b7dfb632a.jpg width="111" height="168"> | <img src = https://user-images.githubusercontent.com/91905313/214994092-f0f82b07-4d48-4361-bbb6-da1286f0530d.jpg width="111" height="168"> | <img src = https://user-images.githubusercontent.com/91905313/214994121-f00cf572-7671-453c-a1b3-91bf34d210af.jpg width="111" height="168"> | <img src = https://user-images.githubusercontent.com/91905313/214994152-dd50ef16-3c7a-4eee-9fa4-ca047fd4550f.jpg width="111" height="168"> | <img src = https://user-images.githubusercontent.com/91905313/214994162-faf95e1a-198c-4abe-9b68-fe0af25b4a91.jpg width="111" height="168"> | 
| UMAP    | <img src = https://user-images.githubusercontent.com/81238710/217629416-ca795bfa-9ba6-4d06-9f56-8af59275fefa.jpeg width="111" height="168"> | <img src = https://user-images.githubusercontent.com/81238710/217629428-f85f7f37-3f17-49c4-aa2d-80926a4cfb07.jpeg width="111" height="168"> | <img src = https://user-images.githubusercontent.com/81238710/217629444-f5157f48-f087-4a9c-9fb6-b68926bba135.jpeg width="111" height="168"> | <img src = https://user-images.githubusercontent.com/81238710/217629457-97e1ac91-bcf0-4cdd-8060-13f054725ef8.jpeg width="111" height="168"> | <img src = https://user-images.githubusercontent.com/81238710/217629478-5de78697-e7a4-4a24-aceb-d0a86174f3f2.jpeg width="111" height="168"> | <img src = https://user-images.githubusercontent.com/81238710/217629500-3c2bc35f-30e7-429e-a114-927bb2cb64df.jpeg width="111" height="168"> | <img src = https://user-images.githubusercontent.com/81238710/217629515-021731a6-1936-4f97-ab47-6bfaaa8bf612.jpeg width="111" height="168"> | <img src = https://user-images.githubusercontent.com/81238710/217629523-30adfd59-7bf1-41f5-93b4-e32dba1952a0.jpeg width="111" height="168"> | 

*The best single plot for different aspect ratio*

| ML algo | 1.33         | 2.5       | 3.16 | 4.21 | 5.26 | 8.42 | 10.53 | 15.79 |
| :---                        |    :----:   |   :---: |   :----:    |   :----:    |    :----:    |    :----:    |    :----:    |    :----:    | 
| UMAP    | <img src = https://user-images.githubusercontent.com/81238710/190962576-5093604c-3e4c-4ad5-a78e-59d1bd10b0ba.jpeg width="111" height="168"> | <img src = https://user-images.githubusercontent.com/81238710/190962577-24613454-b43d-489a-b8bd-85d779bfe297.jpeg width="111" height="168"> | <img src = https://user-images.githubusercontent.com/81238710/190962578-8dba2f01-3077-4e2b-b0e8-78f192dde5a6.jpeg width="111" height="168"> | <img src = https://user-images.githubusercontent.com/81238710/190962579-43019d04-e61a-4027-961d-a69d7bf9c138.jpeg width="111" height="168"> | <img src = https://user-images.githubusercontent.com/81238710/190962580-f4000ab3-7f66-4974-8343-8e86405b7347.jpeg width="111" height="168"> | <img src = https://user-images.githubusercontent.com/81238710/190962582-d49c09be-abed-43ab-93c1-076e17d818fb.jpeg width="111" height="168"> | <img src = https://user-images.githubusercontent.com/81238710/190962586-157a127b-d72e-46bf-b3a1-251c7c844e0e.jpeg width="111" height="168"> | <img src = https://user-images.githubusercontent.com/81238710/190962587-19b65f01-aef4-4186-af6a-6483e03ddc3b.jpeg width="111" height="168"> |
| Eigenvectors | $\{v_1, v_2\}$ | $\{v_1, v_2\}$ | $\{v_1, v_2\}$ | $\{v_1, v_8\}$ | $\{v_1, v_7\}$ | $\{v_1, v_8\}$ | $\{v_1, v_3\}$ | $\{v_1, v_6\}$ | 

Torus
-----

| ML algo | 1.33         | 2.5       | 3.16 | 4.21 | 5.26 | 8.42 |
| :---                        |    :----:   |   :---: |   :----:    |   :----:    |    :----:    |    :----:    |
| Isomap     | <img src = aspect-ratio-plots/Isomap/Torus/Torus_a4b3_Isomap_z.jpg width="142" height="346"> | <img src = aspect-ratio-plots/Isomap/Torus/Torus_a5b2_Isomap_z.jpg width="142" height="346"> | <img src = aspect-ratio-plots/Isomap/Torus/Torus_a6b1_9_Isomap_z.jpg width="142" height="346"> | <img src = aspect-ratio-plots/Isomap/Torus/Torus_a8b1_9_Isomap_z.jpg width="142" height="346"> | <img src = aspect-ratio-plots/Isomap/Torus/Torus_a10b1_9_Isomap_z.jpg width="142" height="346"> | <img src = aspect-ratio-plots/Isomap/Torus/Torus_a16b1_9_Isomap_z.jpg width="142" height="346"> | 
| Spectral     | <img src = aspect-ratio-plots/Spectral-megaman/Torus/Torus_a4b3_Spectral_z.jpg width="142" height="346"> | <img src = aspect-ratio-plots/Spectral-megaman/Torus/Torus_a5b2_Spectral_z.jpg width="142" height="346"> | <img src = aspect-ratio-plots/Spectral-megaman/Torus/Torus_a6b1_9_Spectral_z.jpg width="142" height="346"> | <img src = aspect-ratio-plots/Spectral-megaman/Torus/Torus_a8b1_9_Spectral_z.jpg width="142" height="346"> | <img src = aspect-ratio-plots/Spectral-megaman/Torus/Torus_a10b1_9_Spectral_z.jpg width="142" height="346"> | <img src = aspect-ratio-plots/Spectral-megaman/Torus/Torus_a16b1_9_Spectral_z.jpg width="142" height="346"> | 
| LLE     | <img src = https://user-images.githubusercontent.com/91905313/214996964-db4d0b39-40fa-4b4d-bb87-e58a5391c46d.jpg width="142" height="346"> | <img src = https://user-images.githubusercontent.com/91905313/214997000-8a053167-768e-49a8-89ea-0e078e131000.jpg width="142" height="346"> | <img src = https://user-images.githubusercontent.com/91905313/214997020-be854c5a-93ae-4608-bf9f-36f011254e56.jpg width="142" height="346"> | <img src = https://user-images.githubusercontent.com/91905313/214997086-a332ec90-fba4-4577-a6c7-a57eb0242a62.jpg width="142" height="346"> | <img src = https://user-images.githubusercontent.com/91905313/214997169-ffbd4a4e-2bf8-43f2-b161-f1cc6332faf9.jpg width="142" height="346"> | <img src = https://user-images.githubusercontent.com/91905313/214997150-1bad168e-fabe-4302-b695-4eb67a51dbb3.jpg width="142" height="346"> | 
| UMAP    | <img src = https://user-images.githubusercontent.com/81238710/217629665-bcc89f08-ed7b-4cef-9404-8044b10a4421.jpeg width="142" height="346"> | <img src = https://user-images.githubusercontent.com/81238710/217629692-66c0d0c7-ed2d-41b7-8e0f-209ab139840e.jpeg width="142" height="346"> | <img src = https://user-images.githubusercontent.com/81238710/217629706-0b6a0869-7e74-44c7-a32b-859e8fb0f119.jpeg width="142" height="346"> | <img src = https://user-images.githubusercontent.com/81238710/217629719-8e5899d2-50ef-40e1-8abe-767e56046e1e.jpeg width="142" height="346"> | <img src = https://user-images.githubusercontent.com/81238710/217629730-88740164-f02c-4a84-aa83-057f0a22f8d7.jpeg width="142" height="346"> | <img src = https://user-images.githubusercontent.com/81238710/217629747-690ee0fe-3fb8-4ee0-827b-f7a98993d515.jpeg width="142" height="346"> |

*The best single plot for different aspect ratios*

| ML algo | 1.33         | 2.5       | 3.16 | 4.21 | 5.26 | 8.42 |
| :---                        |    :----:   |   :---: |   :----:    |   :----:    |    :----:    |    :----:    |
| UMAP    | <img src = https://user-images.githubusercontent.com/81238710/190962979-c6568816-e574-42ad-b8eb-9564c66afad3.jpeg width="142" height="150"> | <img src = https://user-images.githubusercontent.com/81238710/190962983-37b2e8ef-dc1b-4bb6-b5f8-2218c6769e66.jpeg width="142" height="150"> | <img src = https://user-images.githubusercontent.com/81238710/190962985-39688127-a1fa-45fa-bd8c-fb8343d4f8bb.jpeg width="142" height="150"> | <img src = https://user-images.githubusercontent.com/81238710/190962986-f4e05eb9-b00e-4e55-b065-561680dd0a2d.jpeg width="142" height="150"> | <img src = https://user-images.githubusercontent.com/81238710/190962989-d1f6081f-98ff-4064-881b-360bebcb8ba5.jpeg width="142" height="150"> | <img src = https://user-images.githubusercontent.com/81238710/190962990-b72fb3ae-a058-4e87-bae1-78f650581d58.jpeg width="142" height="150"> |
| Eigenvectors | The first eigenvector, the second eigenvector, and the third eigenvector | The first eigenvector, the second eigenvector, and the sixth eigenvector | The first eigenvector, the second eigenvector, and the eighth eigenvector | The first eigenvector, the second eigenvector, and the tenth eigenvector | The first eigenvector, the second eigenvector, and the tenth eigenvector | The first eigenvector, the second eigenvector, and the nineth eigenvector |

+ One good exanple here is that for aspect ratio 1.33, the single best plot generated by UMAP is using the first eigenvector, the second eigenvector, and the third eigenvector. The plot is colored by z-axis based on the original dataset. From the plot, we notice that the plot result does not have any significant parts where points with different color intersects together. 



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
*MK* ;*MM* concept, main text, references; *HR*; *QW*; *YW*, *KK* .





