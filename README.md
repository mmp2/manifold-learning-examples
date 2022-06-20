# manifold-learning-examples
### This repo is a group project regarding the examples of different implementations of manifold learning and the study of the dependence of manifold learning algorithms on parameters

Next meeting: Monday 6/20 2:30pm

List of Problems
* the Aspect Ratio Problem: choosing independent eigenvectors
* the Variable Density Problem: distortions due to variable density of data on manifold
* the Neighborhood Graph Problem: distortions due to the choice of neighborhood graph (in variable density)
* Artefacts due to method inconsistency and other artefacts

The first 3 problems are typical of convergent algorithms with poor choices of parameters. The last illustrates mainly the problems of non-convergent algorithms. 

Plan for week 1

* learn scikit-learn manifold learning functions, specifically isomap, spectral_embedding, lle, [t-sne], [ltsa if available]
* learn megaman package by MMP
* learn t-sne (this is part of scikit-learn)
* learn UMAP
* write code that generates synthetic examples

Plan for week 2
 1.t-SNE on a disk and 2D Gaussian (Daniel)
 2. aspect ratio examples: script rectangle, torus, rectangle with hole, ...
-- algorithms: isomap, spectral embedding, LLE, t-SNE, UMAP
- make param files for each data set (Hangliang, Yujia, Qirui)
3. generate data with variable density (Murray)
