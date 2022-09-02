# manifold-learning-examples
### This repo is a group project regarding the examples of different implementations of manifold learning and the study of the dependence of manifold learning algorithms on parameters

Next meeting: Tuesday 9/13 3:30pm (maybe also 9/6 ?)

List of Problems
* the Aspect Ratio Problem: choosing independent eigenvectors
* the Variable Density Problem: distortions due to variable density of data on manifold
* the Neighborhood Graph Problem: distortions due to the choice of neighborhood graph (in variable density)
* Artefacts due to method inconsistency and other artefacts

The first 3 problems are typical of convergent algorithms with poor choices of parameters. The last illustrates mainly the problems of non-convergent algorithms. 

Plan for Weeks of **September 5-19** _(Priority lowest = LP < nothing < HP=highest )_

* Effect of aspect ratio on output of **Spectral embedding** -- to use the same data and plotting style as LLE. A radius must be selected. [**HP**]  ** in progress, Hangliang**
* Effect of aspect ratio on output of **t-SNE** -- to use the same data and plotting style as LLE. [**HP**]
* UMAP -- first set of tasks-- for increasing m, can we recover the embedding for m=3 among the dimensions $v_0, v_1, ... v_{m-1}$ ? **Qirui**
* Effect of aspect ratio on output of UMAP (m=3 or 2 by case) to use the same data and plotting style as LLE [**LP**] done Qirui
* t-SNE for data sampled uniformly on disk **Murray, almost done**
* Polish figures and text in aspect_ratio.md **MMP & al**
* First draft of tsne.md **MMP**
* First draft of variable density effects and neighborhood graph effects [**LP, MMP**]
* computing and displaying distortions 
* a cool manifold [**LP**]  Find a HUSKY 3D model. Number of points must be high enough for the display to look good. For example, this site https://www.turbosquid.com/3d-models/dog-haskey-statue-max/952051 has a model for sale that is only $14, has 1.2M points. It also has a husky model, but a bit more expensive. However, there are free data sets elsewhere that are just as good (or better, as they have fewer  points)

Done tasks
* Generate rectangles with a fixed set of aspect ratios, uniformly sampled (code and 1 data set of each) -- pretty much done by Yujia
* same as above, with holes -- done by Yujia
* Generate swissroll, torus from rectangles: in fact, take points *sampled* from rectangles, with coordinates $x_1,x_2$ and map them to points on swiss roll and torus, with coordinates (x,y,z)  -- done Yujia, Hangliang
* Generate rectangles with a fixed set of aspect ratios, **non-uniformly** sampled (code and 1 data set of each) --  done by Murray
* for all the above, let's unify the code and  data [**LP**] 
* Effect of aspect ratio on output of LLE embedding - done Yujia
* Effect of aspect ratio on output of Isomap embedding -- to use the same data and plotting style as LLE - done Hangliang
* Write first draft of white paper, describing effects of aspect ratio on embeddings -- **MMP**


Displaying the distortion
=========================
To be "correct" an embedding algorithm must output a *diffeomorphic* mapping (that is, a function which is differentiable, and has a differentiable inverse) between the input $X_{1:n}$ and its output $Y_{1:n}$. However, the embedding algorithm is not required to preserve *geometric* properties of $X$, such as distances, or areas. Embedding algorithms usually *distort* the data. 

_Figures here_

We can measure the distortion by calculating something called the *push-forward Riemannian Metric* $G$ and its pseudo-inverse $H$. _more about this later_ The distortion changes from point to point, so $H$, which is a $m\times m$ *positive semi-definite matrix* which represents the distortion, must also be calculated at each point. 

Here is how to do it.  megaman has a function that can do this, geometry/rmetric.py.  An ellipse at a point shows the deformation around that point. You will take embeddings obtained already and display the deformation. 

1. install megaman by Hangliang's script in colab.
2. in examples/ find a tutorial that shows how to display the Riemannian metric by ellipses, i.e. $H$. 
3. learn what the function geometry/rmetric.py does -- this calculates $G$ and $H$
4. plotter/covariance_plotter.py plots ellipses. Note that you have to manually rescale the ellipses sizes; otherwise they can be << or >> to be seen.
5. upload the embedding of a rectangle with hole and display the deformation with ellipses -- for practice
6. refine the algorithm and write a streamlined function that takes any embedding (and other parameters) and plots the data with $H$ displayed


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


