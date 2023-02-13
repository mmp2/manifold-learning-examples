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

These are the embeddings obtained.
<img width="900" src="T-SNE/k_vs_R of T-SNE-1row.png">

From left to right, we see:  a circular blob with higher density in the center, clusters of various granularities, or a disk with a hole (that is, a ring). If these data were cells, we could hypothesise that they all behave the same way (the blob), that there are multiple groups with different behaviors (clusters), or that that the behavior varies continuously and cyclically (the ring).  How to figure out how the original data looked like? 

Based on generic results on manifold learning from non-parameteric statistics, to consistently represent a manifold from samples, $n$ must grow to infinity, and the neighborhood radius must shrink towards 0, at a rate much slower than $n$. Hence, by this reasoning the "true structure" of the data must be that on the left hand side. 

On the other hand, by the recommendation of the algorithm authors and implementers, larger perplexity is better, hence we should believe the plots on the extreme right (the ring). Which is the correct answer in this case. 

[plot of true ring data]

A featureless low dimensional data set
---------------------------------------
We now embed a disk of radius 1 using various $k$ and $n$ values. As before, when $k$ changes, features appear and disappear in the data. The most remarkable fact is that t-SNE displays not just clusters, but also 1-dimensional *filaments* that do not exist in the data. 

![T-SNE for Uniform Disks](https://user-images.githubusercontent.com/77368272/215301106-6425a699-a6ea-4f52-8f39-abec86754b72.png)

Note that here the number of neighbors $k$ varies from low values, lower or similar to other embedding algorithms, to high values, that is, larger neighborhoods, as recommended for t-SNE. 

It appears that more neighbors work better for t-SNE. However, requiring more neighbors can get an algorithm into problems, when the manifold is non-trivially curved. When the previous disk is deformed, neighborhoods become curved, and  their shape in 2D cannot be accurately reproduced. Thus t-SNE has a much harder time finding a good local minimum.

<img width="300" src="T_SNE/3d_disk_original_notitle.png">

![3d_disk_tsne_original](https://user-images.githubusercontent.com/77368272/215299264-118ede45-5ca4-4934-89ca-16d8ecf5a18d.png)

3d disk:
![k_vs_n of_T-SNE_3D](https://user-images.githubusercontent.com/77368272/215299118-345a6dc7-da36-46fb-af3d-b3aa59764072.png)

A featureless graph
--------------------
This paper https://arxiv.org/abs/2102.13009 offers an analysis of t-SNE on structureless graphs, such as the random $k$-*regular* graph, and the *Erdos-Renyi*$(p)$ graph. 

A *$k$-regular graph* is a graph where each node has exactly $k$ neighbors. This is exactly the situation of a t-SNE neighborhood graphs. However, in the *geometric* neighborhoods graphs above, there is high correlation between the neighbors of nearby nodes. In other words, if 2 points are near each other, they have more neighbors in common. In a *random* $k$-regular graph, 2 nodes that are neighbors are not more likely to have other neighbors in common. 

An *Erdos-Renyi* ER$(p)$ graph is a random graph in which each possible edge $(i,j)$ is present with probability $p\in (0,1)$. Hence the expected number of neighbors of an ER$(p)$ graph with $n$ nodes is $np=\bar{k}$.  Below we see how close the ER($p$) graph is to having exactly $\bar{k}$ neighbors pers node. 
[plots: histograms of k for each p, fixed n]

These simple to construct graphs are examples of "high-dimensional" data, i.e. of data that cannot be embedded in low dimensions without distortion. They are also featureless with very high probability, hence if their embedding shows anything different from a blob, that would be an artefact. Our experiments show that t-SNE does find blobs, but it still adds some features like *filaments* and even faint *clusters*.  

Indeed, for the $k$-regular graphs, the results are featureless. When the number of neighbors $k$ increases, the embedding collapses in what is essentially a single point. 

The results are more variable for the ER$(p)$ graph, and in fact in some cases we observe artefacts such as thin rings. 

![T-SNE for Erdos Renyi_vs p_large](https://user-images.githubusercontent.com/77368272/215298860-94954d01-181f-4790-a17c-27b86f80a6b3.png)

vs k:
![T-SNE for Erdos Renyi_vs k](https://user-images.githubusercontent.com/77368272/215300127-ae822723-680c-4c2c-aa90-6fdc8f5829b0.png)

For very large $n$, on these simple graphs, it is known what t-SNE will do. ![t-SNE, forceful colorings and Mean-Field limits](https://arxiv.org/abs/2102.13009) shows that t-SNE outputs a *ring*, and moreover that the ring becomes thinner when $n$ and $k$ increase.  Their figures display rings appearing for $n\geq 40,000$ (while the present simulations stop at $n=10,000)$. More precisely, for the rings to appear, $k\propto n$ and the ring width is $\propto (kn)^{-1/4}$. For smaller $k$,the embedding is featureless (as we can observe too). 

The reason for this (now with actual proofs) is the same as the more intuitive explanation in [this FAQ](https://lvdmaaten.github.io/tsne/#faq): t-SNE "solves a problem known as the crowding problem", in other words, it works by trying to push points away from each other, against the "neighborhood ties". In a data set with clusters, the weaker ties between clusters will give. However, when there are no clusters, t-SNE will still be happier if it can break some ties. Note that the number of ties in a random graph grows like $pn^2$, but to break away a cluster you only need to break $\propto n$ ties. Hence, the larger $n$, the more neglijible will look the (wrongly) broken ties compared to all the (correctly) unbroken ties. 

The run time
-------------
In most embedding algorithms, the number of neighbors $k$ is a vanishingly small fraction of $n$. Not so in t-SNE, where the author's recommendation as well as the analysis above suggest that $k/n$ should be approximately constant (in other words, $k$ needs to grow proportionally with $n$). Let's see what this means for the algorithm's run time, by looking at the dependence of the run time on $k$.

For this, we use the ring data.
![k_vs_R of T-SNE](https://user-images.githubusercontent.com/5679461/215303791-e77e189a-0b5d-439a-9a34-49bb73b02384.png)

-- to make a table with 2 columns. these figures need axes and labels!-- 
| Runtime | Algorithm Cost   |
| :----:   | :----: |
 |![image](https://user-images.githubusercontent.com/77368272/215253970-e7a6d369-43be-46d1-9dd6-e6cd9ef1279b.png) |
 |![image](https://user-images.githubusercontent.com/77368272/215254017-b374577c-5a72-4471-acc7-ad61733f7381.png) |

Perplexity and neighborhoods radius
------------------------------------
t-SNE takes a "statistical" or shall we say "geometric" parameter, the perplexity, and a number of other parameters that control the iterative descent algorithm that estimates the embedding. In our experiments, we focus solely on perplexity, and we run the algorithm with the default parameters in sk-learn and a sufficient number of iterations. 

But what is the perplexity? It turn out that the t-SNE algorithm chooses for each point $k$ nearest neighbors (including the point itself), with 
$k=3\times perplexity+1$. Hence, the perplexity is proportional to the number of neighbors (other than the point itself). Indirectly, the number of neighbors affects the neighborhood *scale*. For any additional neighbor, the radius of the ball that contains all neighbors grows. If the data was sampled uniformly, this radius would be approximately the same for every data point. When the samples are not uniform, then the neighborhood radius is smaller where the points are dense, and larger where the points are sparse, if $k$ is held the same. [merge these paragraphs]

But the t-sne authors recommend a parameter called *perplexity*, which is $90\times k$. Moreover, papers like [] suggest $k\propto n$. [Something about run time in this case] Here are the experiments with the author's recommendation. [We believe that choosing larger $k$ indeed forces the algorithm to behave better for smaller sample sizes, but delaying the appearace of problems until $n$ is much larger]

[ Figure with k larger ]
![k_vs_R of T-SNE](https://user-images.githubusercontent.com/77368272/215299027-4ccb8466-a48e-450e-8cb4-6fff8e4c0c8e.png)


 
So can we find any intuition on the choice of the perplexity (or equivalently of the $k$) parameter?
-----------------------------------------------------------------------------------------------------
We look again at the embedding of the disk. Maybe $k/n$ should be kept constant, following the intuition from the featurelss graphs? In the plot below, each row has the same $k/n$. We see that having $k$ strictly proportional to $n$ does not give similar results. 

Rather, from Figure ... reference the fig above... suggests that the neighborhood radius is a parameter that influences the topology of the embedding. 



 
Many other artefact producing behavior was exemplified at 
https://distill.pub/2016/misread-tsne/

t-sne stability and distortions
--------------------------------
![Tracking on Disks after TSNE](https://user-images.githubusercontent.com/77368272/218435215-a1b8dbf1-4b12-453e-89bb-974918d52980.png)

 
