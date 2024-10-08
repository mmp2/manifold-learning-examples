## Manifold Learning (ML) / Embedding explained  (in progress)

We all know and love *Principal Components Analysis (PCA)* the workhorse of *linear* dimension reduction. It's universally accepted, understood, reproducible. But when they turn to *non-linear dimension reduction*, the newcomers' first impression is one of chaos: so many choices of algorithms, of parameters, and each output different results for the same data!

Here we what we can expect and ask of an embedding algorithm (and what we should not), what is a "good embedding" (and how to diagnose a failed one), why the variations one sees are unavoidable, being baked into the ML paradigm (at least apparently), and how to still make sense of the valuable tools ML offers. 

(from smooth_embedding.md)

When is an embedding "good"? How to evaluate the output of a manifold learning (embedding) algorithm?

Unrolling the Swissroll
=======================

*Figures: Swissroll 8/1.9 | rectangle 8/1.9 |
A swissroll and the original data before rolling. Ideally, the ML algorithm should recover the original data, or a good approximation of it. Consider the embeddings below. Which ones look "correct" to you and which ones don't? Try to explain to yourself why.

<p align="center">
  <img src="aspect-ratio-plots/Swissroll_representatives/SwissRoll_curve.png" width="19%" />
  <img src="aspect-ratio-plots/Swissroll_representatives/SwissRoll_rectangle.png" width="19%" />
  <img src="aspect-ratio-plots/Swissroll_representatives/SwissRoll_rotate_curve.png" width="19%" />
  <img src="aspect-ratio-plots/Swissroll_representatives/SwissRoll_rotation.png" width="19%" />
  <img src="aspect-ratio-plots/Swissroll_representatives/SwissRoll_symmetric.png" width="19%" />
</p>



Local deformations
==================
Now, what should we mean by a _good approximation_? (For a more 
formal mathematical definition of _embedding_ see these videolectures).

Clearly, a rigid translation or rotation of the original data sh
ould be acceptable. We may also find acceptable some _small defo
rmations_ of the data. This last concept needs refinement.

*examples needed here -- to take from one of the non-embeddings 
above*

### No metric:

| ![Isomap](graphs-from-ARSIA-figs/inward_ct_Isomap_no_metric_horiz_largedot.png) | ![LE](graphs-from-ARSIA-figs/inward_ct_LE_no_metric_horiz_largedot.png) | ![LLE](graphs-from-ARSIA-figs/inward_ct_LLE_no_metric_horiz_largedot.png) | ![LTSA](graphs-from-ARSIA-figs/inward_ct_LTSA_no_metric_horiz_largedot.png) | ![UMAP](graphs-from-ARSIA-figs/inward_ct_Umap_no_metric_horiz_largedot.png) | ![t-SNE](graphs-from-ARSIA-figs/inward_ct_t-SNE_no_metric_horiz_largedot.png) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| Isomap | LE | LLE | LTSA | UMAP | t-SNE |

### With metric:

| ![Isomap](graphs-from-ARSIA-figs/inward_ct_Isomap_with_metric_horiz_largedot.png) | ![LE](graphs-from-ARSIA-figs/inward_ct_LE_with_metric_horiz_largedot.png) | ![LLE](graphs-from-ARSIA-figs/inward_ct_LLE_with_metric_horiz_largedot.png) | ![LTSA](graphs-from-ARSIA-figs/inward_ct_LTSA_with_metric_horiz_largedot.png) | ![UMAP](graphs-from-ARSIA-figs/inward_ct_Umap_with_metric_horiz_largedot.png) | ![t-SNE](graphs-from-ARSIA-figs/inward_ct_t-SNE_with_metric_horiz_largedot.png) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| Isomap | LE | LLE | LTSA | UMAP | t-SNE |

### Radius cut:

| ![Isomap](aspect-ratio-plots/Chopped_Torus/ct_Isomap_radial.png) | ![LE](aspect-ratio-plots/Chopped_Torus/ct_LE_radial.png) | ![LLE](aspect-ratio-plots/Chopped_Torus/ct_LLE_radial.png) | ![LTSA](aspect-ratio-plots/Chopped_Torus/ct_LTSA_radial.png) | ![UMAP](aspect-ratio-plots/Chopped_Torus/ct_Umap_radial.png) | ![t-SNE](aspect-ratio-plots/Chopped_Torus/ct_t-SNE_radial.png) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| Isomap | LE | LLE | LTSA | UMAP | t-SNE |

### China map example:

| ![Isomap](aspect-ratio-plots/China_map/ChinaMap_Isomap_no_metric_0.5.png) | ![LE](aspect-ratio-plots/China_map/ChinaMap_LE_no_metric_0.5.png) | ![LLE](aspect-ratio-plots/China_map/ChinaMap_LLE_no_metric_0.5.png) | ![LTSA](aspect-ratio-plots/China_map/ChinaMap_LTSA_no_metric_0.5.png) | ![UMAP](aspect-ratio-plots/China_map/ChinaMap_Umap_no_metric_0.5.png) | ![t-SNE](aspect-ratio-plots/China_map/ChinaMap_t-sne_no_metric_0.5.png) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| Isomap | LE | LLE | LTSA | UMAP | t-SNE |

| ![Isomap](aspect-ratio-plots/China_map/ChinaMap_Isomap_with_metric_0.5.png) | ![LE](aspect-ratio-plots/China_map/ChinaMap_LE_with_metric_0.5.png) | ![LLE](aspect-ratio-plots/China_map/ChinaMap_LLE_with_metric_0.5.png) | ![LTSA](aspect-ratio-plots/China_map/ChinaMap_LTSA_with_metric_0.5.png) | ![UMAP](aspect-ratio-plots/China_map/ChinaMap_Umap_with_metric_0.5.png) | ![t-SNE](aspect-ratio-plots/China_map/ChinaMap_t-sne_with_metric_0.5.png) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| Isomap | LE | LLE | LTSA | UMAP | t-SNE |

### Torus examples:

| ![Isomap](aspect-ratio-plots/Torus/Torus_Isomap_no_metric_vert.png) | ![LE](aspect-ratio-plots/Torus/Torus_LE_no_metric_vert.png) | ![LLE](aspect-ratio-plots/Torus/Torus_LLE_no_metric_vert.png) | ![LTSA](aspect-ratio-plots/Torus/Torus_LTSA_no_metric_vert.png) | ![UMAP](aspect-ratio-plots/Torus/Torus_Umap_no_metric_vert.png) | ![t-SNE](aspect-ratio-plots/Torus/Torus_t-sne_no_metric_vert.png) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| Isomap | LE | LLE | LTSA | UMAP | t-SNE |

| ![Isomap](aspect-ratio-plots/Torus/Torus_Isomap_with_metric_vert.png) | ![LE](aspect-ratio-plots/Torus/Torus_LE_with_metric_vert.png) | ![LLE](aspect-ratio-plots/Torus/Torus_LLE_with_metric_vert.png) | ![LTSA](aspect-ratio-plots/Torus/Torus_LTSA_with_metric_vert.png) | ![UMAP](aspect-ratio-plots/Torus/Torus_Umap_with_metric_vert.png) | ![t-SNE](aspect-ratio-plots/Torus/Torus_t-sne_with_metric_vert.png) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| Isomap | LE | LLE | LTSA | UMAP | t-SNE |


### Jupyter Nodebook for previous examples:
[Open the Jupyter Notebook](Review-figures.ipynb)


No matter how a ML algorithm works, its input is always a description of the _local neighborhoods_ of the data points. Typically, for each data point $i$, the distances to $i$'s neighbors are 
the input. The _neighbors_ are either the $k$-nearest neighbors 
in the data, or all the points with distance $\leq r$ from $i$.

Since the local information is all that the ML algorithm has access to, it is natural that it preserves the _intrinsic_ structure/shape of the data (the rectangle, in the case of the Swissroll) but not the _ambient_ strucuture and shape (e.g. how the rectangle was rolled and in how many dimensions).  

So, when we talk about dis
