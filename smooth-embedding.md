What is an embedding? A touch of topology on the torus
======================================================

The torus is a manifold with intrinsic dimension $d=2$, but which cannot be *embedded* into 2D. This is similar to the sphere which cannot be mapped entirely on a sheet of paper without first cutting it, then deforming it. A good illustration of this is [here](https://www.axismaps.com/guide/map-projections). 


Of course we can always *map* a torus in 2D, by flattening it or cutting it, but we would not call these **embeddings** because they destroy the **topology** of the original torus shape, while an **embedding** (sometimes we like to call it a *smooth embedding*) must **preserve the topology**.

The neighborhood view of topology
=================================
Topology can be described as who is near whom among the points of a shape (topology applies to many other things than manifolds). For example, A and B are neighbors on the torus, but C is not a neighbor of A (or B).  If we deform the torus so that all these relations still hold, we *preserve the topology*. But if we violate some of the relations, even for a single pair of points, we break the (torus) topology.

When the torus is flattened, A and B remain neighbors, but A and C **become neighbors**, or quite possibly, A and C become the same point. Note that many other pairs of points suffer the same fate, along with A and C. Topology was not preserved. 

When the torus is cut, A and C continue to not be neighbors, but A and B now become separated as well. Topology is not preserved.

You can also notice than in the first example, no neighborhoods are broken, but many new neighbor pairs are created. In the second example, no new neighbor pairs appear, but some neighbor pairs are broken.

There are many other ways to break the topology of a shape. Here is an example for the circle, where new neighbors are created in a very very small region. Still, this breaks the topology and we can't call this mapping an embedding.

The loops and hollows view of topology
======================================
We can check if a mapping of the torus is an embedding with  *global* criteria, by checking that all the loops and hollows of the shape are preserved. For example, the torus has 2 **loops** and 1 **hollow**. When we flatten it, only 1 loop remains. When we cut it, the hollow and both loops are destroyed.


 * Torus 2 loops + 1 hollow
 * Circle 1 loop
 * Double torus 4 loops + 1 hollow
 * Sphere 1 hollow
 * Cut torus 0 loops, 0 hollows

The numbers of loops and hollows are called the [Beti numbers](https://en.wikipedia.org/wiki/Betti_number) of the shape.
