Manifolds explained
====================
Think of the surface of the Earth (pretend it has no oceans and life, and it's smoothed out by e.g. Google Earth). This is a *manifold*.

Dimensions:  intrinsic ($d$), embedding ($m$), and ambient ($D$)
----------------------------------------------------------------
If you live somewhere on it, the Earth from your perspective will look flat. You can make and use topographic maps, with rectangular grids, if you draw geometric figures, like the plan of your yard, or of a city, all the laws of planar geometry apply. This is true anywhere on Earth. We say that the manifold Earth has **intrinsic dimension** $d=2$. 

But if you now wanted to map the *whole Earth* you would find that the laws of planar geometry *do not apply*. For example, following a straight line will bring you back to where you started. However, you (and others before) can make maps of the entire Earth by (a) making cuts into the surface to "open it up", then (b) stretching out the surface on a plane (imagine doing this with a balloon). [illustration] To reconstruct Earth from such a map you reverse the process (b') curve and deform the map back into a spherical shape, then glue it back together along the cuts. Note that to be able to do this, *you have to leave the plane*, *expand into 3 or more dimensions*, just like the real Earth lives compfortably in 3D space. 

Because Earth can be reconstructed in $m=3$ dimensions, we say that $m$ is its **embedding dimension**, and that the manifold Earth is **embedded* into ${\mathbb R}^m$.

If a manifold $\mathcal M$ has $m=d$, we call it a **flat** manifold. It means that we can embed it into $d$ dimensions without cutting or stretching. The *Swiss roll* is a flat manifold; a *half sphere* is not (we don't have to cut it, but we have to stretch it). 

Of course, we can embed a manifold in any number of dimensions $D$, as long as $D\geq m$, the minimum necessary. For instance, a piece of string has $d=1$ and is flat, but we can deform it into an S-curve ($D=2$) or into a spiral in space ($D=3$). If somebody gave us points on this spiral, they would have coordinates $(x,y,z)\in\mathbb R^3$. We say that $D$ is the **ambient dimension** of the data. The part of machine learning called *Manifold Learning* develops algorithms to discover that these points are a string and to "line them up" properly in 1D. 

Charts and atlases
-------------------
With a lot of topo maps, so that every patch of earth is covered by a map, one can also reconstruct the whole Earth. For this, you must first deform each topo map just a bit give it the shape of a *spherical shell*. Then you put the maps *in correspondence* (this is also called *registration*). We must overlap the maps so that every point that appears on multiple maps (for example University of Washington) overlaps exactly with its copies from other maps.

You can do it by putting 2 maps in correspondence, then adding a third that overlaps with one of the previous two, and so on. Finally, when this is done, the overlapping maps can be glued together like papier mache and we will have a globe.

This is how mathematicians think of manifolds. They call a topo map a **chart**, and the entire set of maps an **atlas**.

Coordinates
------------
On Earth, geographers have a rather smart way to describe every point on earth by its latitude and longitude, the geographic coordinates. 
bla bla bla

Computers every point is represented in coordinates.
A person in Seattle and a person in the Netherlands (where Descartes published his work on analytic geometry and "Cartesian" coordinates) ...
