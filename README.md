## Welcome to the Manifold Learning Examples project! 

**Manifold Learning (ML) algorithms** -- also called **Embedding algorithms** -- can help us interpret data with many dimensions (such as a cloud of word embeddings or of configurations of a molecule) by mapping it to 2D or to 3D where **we can see** it. But is what we are seeing the **real shape** of the data? Almost always, ML algorithms *distort the shape*. Sometimes the distortions are unimportant, but sometimes they can make us see *clusters, "arms", holes, and "horseshoes"* (what we will call **artefacts**) that are not properties of the data, but just effects of the algorithm and of how we used it. 

This project illustrates some of the most common effects and artefacts you will encounter, as you start using Embedding algorithms for your  real data. The artefacts are *not* symptoms of "too little data" -- most of them persist even when the data size _n_ goes to infinity! We chose simple artificial examples as the most common effects are present even with the simplest data. 

The good news is that once you are aware of their presence, the artefacts and distorions can be recognized and methods exist to circumvent or to correct them. 

## What you will find on this site
* **a recent talk hosted by the ACMS social [Unsupervised Learning in the age of Big Data](research-overview-ACMS23.pdf)

* **a series of short articles** illustrating significant but less widely known counterintuitive behaviors of manifold learning algorithms. Most of these effects are predictable or documented theoretically, and we include (light) references to the main sources. 
  * [aspect-ratio.md](aspect-ratio.md)  Most real (manifold) data  extends more in one direction than in others, that is, it looks more like elongated strips than as discs or blobs. This can have unexpected drastic consequences on some ML algorithms, when they are used naively. We demonstrate both what can happen, how the problem is detected by simple inspecttion and a simple way to fix it.
  * TBW For most ML algorithms, the way we sample the data affects the algorithm's output. In other words, what we see is not just _the shape_ of the manifold, but a combination of the shape and the _density_ of the data on the manifold, that can vary by algorithm and by the parameters used. 
  * [tsne.md (under construction)](tsne.md) t-SNE is a very popular algorithm for visualizing high-dimensional data in 2D and 3D. However, care must be taken, as sometimes the features we see do not exist in the original data. 

* **the python code** used to generate the examples. Most of the examples are based on sk-learn; for spectral_embedding (aka the DiffusionMaps / LaplacianEigenmaps algorithm) the megaman code is used; for UMAP and t-SNE we used the code provided by the authors. Additionally, we occasionally share our experience in installing/running these codes. 
  * generating samples from simple synthetic manifolds (rectangle, rectangle with a hole, swiss roll=rolled up rectangle, 3D rectangle, circle, torus); in these examples, the samples are distributed nearly uniformly [more details TBW] 
  * generating samples from the same manifolds as above, but in a highly non-uniform manner (that can be controlled). 
  * generating informative plots of the algorithms' output
  * instructions on how to install megaman on windows

* **the plots** used in the articles and many more

## How to use this site 
[gnu licence] Feel free to use the code, plots, and to cite the articles on this site. Currently, this is a working repository; some changes to the code or files are possible. For the articles, please use this citation format [TBW].

For figures and code, please credit [TBW] and cite [TBW]

## Contributors (in alphabetical order)
* Haoqi Murray Kang, non-uniform density, aspect ratio, t-SNE
* Marina Meila, Professor, concept and scientific leadership
* Hangliang Harry Ren, spectral embedding, non-uniform density, plotting, aspect ratio
* [Qirui Wang](https://github.com/Typhoeus-Wang), UMAP, aspect ratio
* Yujia Wu, data generation, plotting, Local Linear Embedding, aspect ratio

**TODO:** add links to contributors, megaman, sk-learn, images of word2vec, molecule (one distorted and one not), how to give credit/cite


