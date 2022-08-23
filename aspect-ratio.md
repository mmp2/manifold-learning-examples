The effect of manifold aspect ratio
=====================================

What is aspect ratio? 
---------------------
Below we see two examples of rectangles with different aspect ratios. 

*figures here, just rectangles 4/3 and ~ 4 *

Below we see data sampled uniformly from these 2 rectangles.

*figures* here

Aspect ratio can be defined for other simple manifolds, that can be obtained by "rolling up" these rectangles. 

*figures here: 2 swiss rolls, then 2 tori*

These manifolds all have *intrinsic dimension* $d=2$, because they are obtained by a transformation of a rectangle. Later we will discuss examples of manifolds with $d=3$, such as the sphere. Note however that the torus and swiss roll live in $m=3$ coordinates, and we call $m$ the *embedding dimension*. Of course not all manifolds are obtained from rectangles. Qualitatively, we think of the aspect ratio of a manifold as the aspect ratio of the data, after the manifold is "unfolded" in $d$ dimensions. *a figure here*

Most real data is not generated form rectangles, but most real data, when unfolded, has aspect ratio $>2$, in other words, not close to 1. The following examples illustrate how this affects the embeddings produced by different embedding algorithms. 

*todo: a section on what is a good embedding. continuous map with continuous inverse, smooth map with smooth inverse. with examples*.

*?? a table with links to subsets of results*

Rectangle
---------

The rectangle is the simplest possible manifold. The embedding algorithm will map data sampled from rectangles $(x_1,x_2)$ to points in $m=2$ with coordinates $v_1,v_2$ **MMP decision point: use 0-indexed coordinates? I think YES**

*figure -- see handwritten notes *

Swiss roll
----------
A swiss roll is just a rectangle rolled up. So, the embedding algorithms should output the same results as before, since they are getting the essentially same data, right? transformed by XXX. *explain the stretching*

Rectangle with hole
-------------------

Torus
-----

A manifold with $d=3$ 
---------------------
(brick?, ellipsoid? swiss roll?)

A "cute" manifold
------------------

An example with real data (maybe)
---------------------------------

This paper https://arxiv.org/pdf/1907.01651.pdf discusses the problems in the case of Spectral Embedding and proposes a solution. 




