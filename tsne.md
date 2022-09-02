DRAFT Title: a beloved algorithm's artefacts
==============================================

An intro on t-sne with links
------------------------------
TBW
t-sne likes to create 1-D structures
-------------------------------------
disk of radius 1 embedded by t-sne

Note that here the number of neighbors $k$ is similar to other embedding algorithms.

But the t-sne authors recommend a parameter called *perplexity*, which is $90\times k$. Moreover, papers like [] suggest $k\propto n$. [Something about run time in this case] Here are the experiments with the author's recommendation. [We believe that choosing larger $k$ indeed forces the algorithm to behave better for smaller sample sizes, but delaying the appearace of problems until $n$ is much larger]

This paper https://arxiv.org/abs/2102.13009 demonstrates t-sne on structureless high dimensional point clouds

a k-regular graph (can we build it? -- yes, approximately]

an Erdos-Renyi graph 

rectangle with hole and our other manifolds -- large $k$

t-sne stability and distortions
----------------------

real data examples revisited -- e.g. digits and initialization

limits of t-sne
----------------
what can we say/show about this?
to design an algorithm with a reasonable growth rate

more from steinerberger
