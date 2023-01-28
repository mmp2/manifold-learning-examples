t-SNE: a beloved algorithm's artefacts
======================================
The t-SNE algorithm is immesely popular for data visualization. But is t-SNE sometimes showing us features -- in other words creating *artefacts* -- that do not exist in the data? Does it "halucinate" clusters, and shapes that do not exist? does it miss other structures that do?

For example, we know from, e.g., [this paper](https://scikit-learn.org/stable/modules/generated/sklearn.manifold.TSNE.html) that t-SNE separates data into clusters, when *there are clusters*.

--a figure of e.g. digits data from sk-learn

But what if t-SNE just *likes* to create clusters, whether the data is clustered or not? More generally, an *artefact* a feature that we observe in the embedding of the data by  t-SNE, but which does not exist in the data. Such features can be clusters, holes, "arms" and anything else that we may find interesting, when they are *not* in the data but appear to us in the embedding by t-SNE. (Of course, the question of artefacts applies to any other embedding algorithm). 

Note that here we do not give a formal definition of "feature", just like researchers to may observe these features in data do not use formal definitions.  

So, we will give t-SNE very simple artificial data that has no features, and if we observe clusters or other structure, we will learn what artefacts t-SNE likes to create. Since the output of the embedding algorithms also depends on the input parameters, we shall also look briefly into the effect of parameter choices. Here we use the [sk-learn implementation of t-SNE](https://scikit-learn.org/stable/modules/generated/sklearn.manifold.TSNE.html). The reader unfamiliar with the algorithm can consult the original paper [van der Maaten and Hinton 2008](https://scikit-learn.org/stable/modules/generated/sklearn.manifold.TSNE.html), and find a variety of implementations [here](https://lvdmaaten.github.io/tsne/)

[How to use t-SNE effectively](https://scikit-learn.org/stable/modules/generated/sklearn.manifold.TSNE.html) describes some unexpected behaviours of t-SNE, that are mostly specific to data with clusters. While their experiments illustrate small data sets, here we consider larger data, up to $n=20,000$ points, based on the common wisdom that with more data, the "correct" structure is easiear to find.  We also focus on the simplest possible data sets, such as disks or rings in 2D and 3D. A researcher would expect from a visualization algorithm to recover such simple structures reliably, before trying it out on more complex data, or data with unknown structure. 

A first example
----------------
Here is a first example to illustrate the issues a practitioner may face with t-SNE. A scientist has painstakingly obtained multi-dimensional measurements from thousands of objects (they can be cells, patients, users of a web site, stars or galaxies). They use t-SNE to represent the data in 2D. Unbeknownst to them, the data is in fact precisely 2-dimensional, and it can be represented in 2D by a simple rotation in the original space. Hence from the point of view of an embedding algorithm, this should be an easy problem with a stable solution (up to rigid translations and rotations).

The research group is aware that the parameter choices may affect the algorithm, so they try many possible choices of perplexity. Perplexity is proportional to the number of neighbors $k$ of a data point, and the number of neigbors implicitly defines a radius of the neighborhood (more neighbors implies larger radius); note that the radius does not grow proportionally with $k$, but slower, e.g., approximately as $\sqrt{k}$ when for 2-dimensional data. 

These are the embedding they obtain. Can you figure out how the original data looked like? The answer is [here] or scroll below. 

[figure of d1=5, d2=2 data with no original data, no axes]

From left to right, we see:  a circular blob with higher density in the center, clusters of various granularities, or a disk with a hole (that is, a ring). If these data were cells, we could hypothesise that they all behave the same way (the blob), that there are multiple groups with different behaviors (clusters), or that that the behavior varies continuously and cyclically (the ring). 

Based on generic results on manifold learning from non-parameteric statistics, to consistently represent a manifold from samples, $n$ must grow to infinity, and the neighborhood radius must shrink towards 0, at a rate much slower than $n$. Hence, by this reasoning the "true structure" of the data must be that on the left hand side. 

On the other hand, by the recommendation of the algorithm authors and implementers, larger perplexity is better, hence we should believe the plots on the extreme right (the ring). Which is the correct answer in this case. 

[plot of true ring data]

A featureless low dimensional data set
---------------------------------------
We now embed a disk of radius 1 using various $k$ and $n$ values. As before, when $k$ changes, features appear and disappear in the data. The most remarkable fact is that t-SNE displays not just clusters, but also 1-dimensional *filaments* that do not exist in the data. 

Note that here the number of neighbors $k$ is similar to other embedding algorithms.

A featureless graph
--------------------

This paper https://arxiv.org/abs/2102.13009 offers an analysis of t-sne on structureless graphs, such as the random $k$-*regular* graph, and the *Erdos-Renyi*$(p)$ graph. 

A *$k$-regular graph* is a graph where each node has exactly $k$ neighbors. This is exactly the situation of a t-SNE neighborhood graphs. However, in the *geometric* neighborhoods graphs above, there is high correlation between the neighbors of nearby nodes. In other words, if 2 points are near each other, they have more neighbors in common. In a *random* $k$-regular graph, 2 nodes that are neighbors are not more likely to have other neighbors in common. An ER$(p)$ graph is a random graph in which each possible edge $(i,j)$ is present with probability $p\in (0,1)$. Hence the expected number of neighbors of an ER$(p)$ graph with $n$ nodes is $np=\bar{k}$.  Below we see how close the ER($p$) graph is to having exactly $\bar{k}$ neighbors pers node. 
[plots: histograms of k for each p, fixed n]

These simple to construct graphs are examples of "high-dimensional" data, i.e. of data that cannot be embedded in low dimensions without distortion. They are also featureless with very high probability, hence if their embedding shows anything different from a blob, that would be an artefact. Our experiments show that t-SNE does find blobs, but it still adds some features like *filaments* and even faint *clusters*.  

[MK's figures of ER]

As it turns out, for the ER graph and it's relative the $k$-regular graph, it is known what t-SNE will do for $n$ very large. This paper shows that t-SNE outputs a *ring*, and moreover that the ring becomes thinner when $n$ and $k$ increase, and their figures display rings appearing for $n\geq 40,000$. More precisely, for the rings to appear, $k\propto n$ and the ring width is $\propto (kn)^{-1/4}$. For smaller $k$,the embedding is featureless (as we can observe too). 

The reason for this (now with actual proofs) is the same as the more intuitive explanation in [this FAQ](https://lvdmaaten.github.io/tsne/#faq): t-SNE "solves a problem known as the crowding problem", in other words, it works by trying to push points away from each other, against the "neighborhood ties". In a data set with clusters, the weaker ties between clusters will give. However, when there are no clusters, t-SNE will still be happier if it can break some ties. Note that the number of ties in a random graph grows like $pn^2$, but to break away a cluster you only need to break $\propto n$ ties. Hence, the larger $n$, the more neglijible will look the (wrongly) broken ties compared to all the (correctly) unbroken ties. 

The run time
-------------
In most embedding algorithms, the number of neighbors $k$ is a vanishingly small fraction of $n$. Not so in t-SNE, where the author's recommendation as well as the analysis in [...] is to have $k/n$ approximately constant. Let's see what this means for the algorithm's run time, by looking at the dependence of the run time on $k$.

 [MK: to rerun k vs n columns k/n = 0.2 or 0.1 and k/n = 0.01 --because it shows features. save results. save run time:). plot run time vs n, 2 curves for the 2 k/n values, on the same plot. may need to make y axis logarithmic]
 
 Plots:
 
 ![image](https://user-images.githubusercontent.com/77368272/215254028-b75423a9-8e62-4e21-af30-d0ea21164d1c.png)
 
Runtime:
 ![image](https://user-images.githubusercontent.com/77368272/215253970-e7a6d369-43be-46d1-9dd6-e6cd9ef1279b.png)
 
 Algorithm Cost:
 ![image](https://user-images.githubusercontent.com/77368272/215254017-b374577c-5a72-4471-acc7-ad61733f7381.png)


Perplexity and neighborhoods radius
------------------------------------
t-SNE takes a "statistical" or shall we say "geometric" parameter, the perplexity, and a number of other parameters that control the iterative descent algorithm that estimates the embedding. In our experiments, we focus solely on perplexity, and we run the algorithm with the default parameters in sk-learn and a sufficient number of iterations. 

But what is the perplexity? It turn out that the t-SNE algorithm chooses for each point $k$ nearest neighbors (including the point itself), with 
$k=3\times perplexity+1$. Hence, the perplexity is proportional to the number of neighbors (other than the point itself). Indirectly, the number of neighbors affects the neighborhood *scale*. For any additional neighbor, the radius of the ball that contains all neighbors grows. If the data was sampled uniformly, this radius would be approximately the same for every data point. When the samples are not uniform, then the neighborhood radius is smaller where the points are dense, and larger where the points are sparse, if $k$ is held the same. [merge these paragraphs]

But the t-sne authors recommend a parameter called *perplexity*, which is $90\times k$. Moreover, papers like [] suggest $k\propto n$. [Something about run time in this case] Here are the experiments with the author's recommendation. [We believe that choosing larger $k$ indeed forces the algorithm to behave better for smaller sample sizes, but delaying the appearace of problems until $n$ is much larger]

[ Figure with k larger ]

 
So can we find any intuition on the choice of the perplexity (or equivalently of the $k$) parameter?
-----------------------------------------------------------------------------------------------------
We look again at the embedding of the disk. Maybe $k/n$ should be kept constant, following the intuition from the featurelss graphs? In the plot below, each row has the same $k/n$. We see that having $k$ strictly proportional to $n$ does not give similar results. 

Rather, from Figure ... reference the fig above... suggests that the neighborhood radius is a parameter that influences the topology of the embedding. 



 
Many other artefact producing behavior was exemplified at 
https://distill.pub/2016/misread-tsne/

t-sne stability and distortions
--------------------------------

 
