# manifold-learning-examples
### This repo is a group project regarding the examples of different implementations of manifold learning and the study of the dependence of manifold learning algorithms on parameters

Next meeting: Tuesday 8/30 2:30pm

List of Problems
* the Aspect Ratio Problem: choosing independent eigenvectors
* the Variable Density Problem: distortions due to variable density of data on manifold
* the Neighborhood Graph Problem: distortions due to the choice of neighborhood graph (in variable density)
* Artefacts due to method inconsistency and other artefacts

The first 3 problems are typical of convergent algorithms with poor choices of parameters. The last illustrates mainly the problems of non-convergent algorithms. 

Plan for Weeks of **August 2-15** _(Priority lowest = LP < nothing < HP=highest )_
* Generate rectangles with a fixed set of aspect ratios, uniformly sampled (code and 1 data set of each) -- pretty much done by Yujia
* same as above, with holes -- done by Yujia
* Generate swissroll, torus from rectangles: in fact, take points *sampled* from rectangles, with coordinates $x_1,x_2$ and map them to points on swiss roll and torus, with coordinates (x,y,z)  -- done Yujia, Hangliang
* Generate rectangles with a fixed set of aspect ratios, **non-uniformly** sampled (code and 1 data set of each) --  done by Murray
* for all the above, let's unify the code and  data [**LP**] 
* Effect of aspect ratio on output of LLE embedding - done Yujia
* Effect of aspect ratio on output of Isomap embedding -- to use the same data and plotting style as LLE - done Hangliang
* Effect of aspect ratio on output of **Spectral embedding** -- to use the same data and plotting style as LLE. Note that for Spectral Embedding, one must use the radius_neighbors method. Ask me if not sure what this means. A radius must be selected. [**HP**]
* Effect of aspect ratio on output of **t-SNE** -- to use the same data and plotting style as LLE. [**HP**]
* UMAP -- first set of tasks-- for increasing m, can we recover the embedding for m=3 among the dimensions $v_0, v_1, ... v_{m-1}$ ? **Qirui**
* Effect of aspect ratio on output of UMAP (m=3 or 2 by case) to use the same data and plotting style as LLE [**LP**] done Qirui
* Effect of aspect ratio on output of t-SNE (m=3 or 2 by case) to use the same data and plotting style as LLE [**HP**]
* Write first draft of white paper, describing effects of aspect ratio on embeddings -- **MMP**
* t-SNE for data sampled uniformly on disk 


Plan for week 2
* share with others what you have learned/done
* learn basics of manifold learning -- short tutorial by MMP
* plan and run first set of experiments 

Plan for week 1
* learn scikit-learn manifold learning functions, specifically isomap, spectral_embedding, lle, [t-sne], [ltsa if available]
* learn megaman package by MMP
* learn t-sne (this is part of scikit-learn)
* learn UMAP
* write code that generates synthetic examples


