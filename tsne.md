DRAFT Title: a beloved algorithm's artefacts
==============================================

An intro on t-sne with links
------------------------------
The t-SNE algorithm takes a "statistical" or shall we say "geometric" parameter, the perplexity, and a number of other parameters that control the iterative descent algorithm that estimates the embedding. In our experiments, we focus solely on perplexity, and we run the algorithm with the default parameters in sk-learn and a sufficient number of iterations. 

But what is the perplexity? It turn out that the t-SNE algorithm chooses for each point $k$ nearest neighbors (including the point itself), with 
$k=3\times perplexity+1$. Hence, the perplexity is proportional to the number of neighbors (other than the point itself). Indirectly, the number of neighbors affects the neighborhood *scale*. For any additional neighbor, the radius of the ball that contains all neighbors grows. If the data was sampled uniformly, this radius would be approximately the same for every data point. When the samples are not uniform, then the neighborhood radius is smaller where the points are dense, and larger where the points are sparse, if $k$ is held the same. 



t-sne likes blah blah
-------------------------------------

We know from many examples and from [this paper] that t-SNE separates data into clusters, when *there are clusters*.

--a figure of e.g. digits data from sk-learn

But what if t-SNE just *likes* to create clusters, whether the data is clustered or not? More generally, an *artefact* a feature that we observe in the embedding of the data by  t-SNE, but which does not exist in the data. Such features can be clusters, holes, "arms" and anything else that we may find relevant for our problem, when they are *not* in the data but appear to us in the embedding by t-SNE. (Of course, the question of artefacts applies to any other embedding algorithm). 

Note that here we do not give a formal definition of "feature", just like researchers to may observe these features in data do not use formal definitions.  

So, we will give t-SNE very simple artificial data that has no features, and if we observe clusters or other structure, we will learn what artefacts t-SNE likes to create. Since the output of the embedding algorithms also depends on the input parameters, we shall also look briefly into the effect of parameter choices. 

Here is a first example to illustrate the issues a practitioner may face with t-SNE. A cell biologist has painstakingly obtained multi-dimensional measurements from thousands of cells. They use t-SNE to represent the data in 2D. Unbeknownst to them, the data is in fact precisely 2-dimensional, and it can be represented in 2D by a simple rotation in the original space. Hence from the point of an embedding algorithm, this should be an easy problem with a stable solution (up to rigid translations and rotations).

The research group is aware that the parameter choices may affect the algorithm, so they try many possible choices of perplexity. Perplexity is proportional to the number of neighbors $k$ of a data point, and the number of neigbors implicitly defines a radius of the neighborhood (more neighbors implies larger radius); note that the radius does not grow proportionally with $k$, but slower, e.g., approximately as $\sqrt{k}$ when for 2-dimensional data. 

These are the embedding they obtain. Can you figure out how the original data looked like? The answer is [here] or scroll below. 

[figure of d1=5, d2=2 data with no original data, no axes]

From left to right, we see:  a circular blob with higher density in the center, clusters of various granularities, or a disk with a hole (that is, a ring). If these data were cells, we could hypothesise that they all behave the same way (the blob), that there are multiple groups with different behaviors (clusters), or that that the behavior varies continuously and cyclically (the ring). 

Based on generic results on manifold learning from non-parameteric statistics, to consistently represent a manifold from samples, $n$ must grow to infinity, and the neighborhood radius must shrink towards 0, at a rate much slower than $n$. Hence, by this reasoning the "true structure" of the data must be that on the left hand side. 

On the other hand, by the recommendation of the algorithm authors and implementers, larger perplexity is better, hence we should believe the plots on the extreme right (the ring). Which is the correct answer in this case. 

[plot of true data]

A featureless low dimensional data set
---------------------------------------
We now embed a disk of radius 1 using various $k$ and $n$ values. As before, when $k$ changes, features appear and disappear in the data. The most remarkable fact is that t-SNE displays not just clusters, but also 1-dimensional *filaments* that do not exist in the data. 

Note that here the number of neighbors $k$ is similar to other embedding algorithms.

But the t-sne authors recommend a parameter called *perplexity*, which is $90\times k$. Moreover, papers like [] suggest $k\propto n$. [Something about run time in this case] Here are the experiments with the author's recommendation. [We believe that choosing larger $k$ indeed forces the algorithm to behave better for smaller sample sizes, but delaying the appearace of problems until $n$ is much larger]

[ Figure with k larger ]

A featureless graph
--------------------

This paper https://arxiv.org/abs/2102.13009 offers an analysis of t-sne on structureless graphs, such as the random $k$-*regular* graph, and the *Erdos-Renyi*$(p)$ graph. 

A $k$-regular graph is a graph where each node has exactly $k$ neighbors. This is exactly the situation of t-SNE neighborhood graphs. However, in the neighborhoods graphs above, there is high correlation between the neighbors of nearby nodes. In other words, if 2 points are near each other, they have more neighbors in common. In a random $k$-regular graph, 2 nodes that are neighbors are not more likely to have other neighbors in common. An ER$(p)$ graph  is a random graph in which each possible edge $(i,j)$ is present with probability $p\in (0,1)$. Hence the expected number of neighbors of an ER$(p)$ graph with $n$ nodes is $np=\bar{k}$.

These simple to construct graphs are examples of "high-dimensional" data, i.e. of data that cannot be embedded in low dimensions without distortion. They are also featureless with very high probability, hence if their embedding shows anything different from a blob, that would be an artefact. As it turns out, for this examples, it can be proved that t-SNE outputs a *ring*, and moreover that the ring becomes thinner when $n$ and $k$ increase. (More precisely, $k\propto n$ and the righ width $\propto (kn)^{-1/4}$. But the embedding is featureless for small $k$ *to check this*

[ figure with ER graph ]


So can we find any intuition on the choice of the perplexity (or equivalently of the $k$) parameter?
-------------------------------------------------------------------------------------------------------
We look again at the embedding of the disk. Maybe $k/n$ should be kept constant, following the intuition from the featurelss graphs? In the plot below, each row has the same $k/n$. We see that having $k$ strictly proportional to $n$ does not give similar results. 

Rather, from Figure ... reference the fig above... suggests that the neighborhood radius is a parameter that influences the topology of the embedding. 



run time w.r.t k,n
-------------------

a k-regular graph (can we build it? -- yes, approximately]

an Erdos-Renyi graph 

rectangle with hole and our other manifolds -- large $k$

Many other artefact producing behavior was exemplified at 
https://distill.pub/2016/misread-tsne/

t-sne stability and distortions
----------------------

real data examples revisited -- e.g. digits and initialization

limits of t-sne
----------------
what can we say/show about this?
to design an algorithm with a reasonable growth rate

more from steinerberger
