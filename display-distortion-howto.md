Displaying the distortion
=========================
To be "correct" an embedding algorithm must output a *diffeomorphic* mapping (that is, a function which is differentiable, and has a differentiable inverse) between the input $X_{1:n}$ and its output $Y_{1:n}$. However, the embedding algorithm is not required to preserve *geometric* properties of $X$, such as distances, or areas. Embedding algorithms usually *distort* the data. 

_Figures here_

We can measure the distortion by calculating something called the *push-forward Riemannian Metric* $G$ and its pseudo-inverse $H$ (details [here (_Non-linear dimensionality reduction: Riemannian metric estimation and the problem of geometric discovery_)](https://arxiv.org/abs/1305.7255)) The distortion changes from point to point, so $H$, which is a $m\times m$ *positive semi-definite matrix* which represents the distortion, must also be calculated at each point. 

Here is how to do it.  megaman has a function that can do this, geometry/rmetric.py.  An ellipse at a point shows the deformation around that point. You will take embeddings obtained already and display the deformation. 

1. install `megaman` by [this script](install_env.sh) and [this notebook](install_use_megaman.ipynb)
2. in `examples/` find a tutorial that shows how to display the Riemannian metric by ellipses, i.e. $H$. 
3. learn what the function `geometry/rmetric.py` does -- this calculates $G$ and $H$
4. `plotter/covariance_plotter.py` plots ellipses. Note that you have to manually rescale the ellipses sizes; otherwise they can be << or >> to be seen.
5. upload the embedding of a rectangle with hole and display the deformation with ellipses -- for practice
6. refine the algorithm and write a streamlined function that takes any embedding (and other parameters) and plots the data with $H$ displayed
