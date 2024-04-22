## Welcome to the Manifold Learning Examples project! 

**Manifold Learning (ML) algorithms** -- also called **Embedding algorithms** -- can help us interpret data with many dimensions (such as a cloud of word embeddings or of configurations of a molecule) by mapping it to 2D or to 3D where **we can see** it. But is what we are seeing the **real shape** of the data? Almost always, ML algorithms *distort the shape*. Sometimes the distortions are unimportant, but sometimes they can make us see *clusters, "arms", holes, and "horseshoes"* (what we will call **artefacts**) that are not properties of the data, but just effects of the algorithm and parameter choices. 

This project illustrates some of the most common effects and artefacts you will encounter, as you start using Embedding algorithms for your  real data. The artefacts are *not* symptoms of "too little data" -- most of them persist even when the data size _n_ goes to infinity! We chose simple artificial examples as the most common effects are present even with the simplest data. 

The good news is that once you are aware of their presence, the artefacts and distorions can be recognized and methods exist to circumvent or to correct them. 

## What you will find on this site
* a recent talk hosted by the ACMS social [Unsupervised Learning in the age of Big Data](research-overview-ACMS23.pdf)
* a recent talk hosted by [IMSI](https://www.imsi.institute/activities/data-driven-materials-informatics/learning-collective-variables-and-coarse-grained-models/): [Dimension reduction from a user's perspective. Understanding the configuration spaces of molecules with Manifold Learning](Talks/mani-w3imsi24.pdf)

* **short tutorial introductions** to manifold learning
     -  [Manifolds explained](manifolds-explained.md)
     -  Manifold Learning explained (in progress) [](manifold-learning-explained.md)
* **links to longer tutorials** on manifold learning
    -- Video lectures on Manifold Learning by Marina Meila [Video Lecture 1](http://www.fields.utoronto.ca/talks/tutorial-Manifold-Learning-real-data-0), [Video Lecture 2](http://www.fields.utoronto.ca/talks/tutorial-Manifold-Learning-real-data-1), [Video Lecture 3](http://www.fields.utoronto.ca/talks/tutorial-Manifold-Learning-real-data-2), annotated slides from Lecture 1 and from Lectures 2-3 [here](https://sites.stat.washington.edu/mmp/classes.html), and unannotated [Lecture slides](https://sites.stat.washington.edu/mmp/Talks/mani-fields22-notes.pdf) with additional definitions and notes
    -- [Manifold learning: what, how and why](https://www.annualreviews.org/content/journals/10.1146/annurev-statistics-040522-115238) by Marina Meila and Hanyu Zhang. Review article in *Annual Reviews of Statistics and Its Applications*, Volume 11, 2024. 

* **links to software**
     * [scikit-learn](https://scikit-learn.org) simple Manifold Learning software package
     * [megaman](mmp2.github.io/megaman/) performance optimized Manifold Learning software package, with API compatible with `sk-learn`; `megaman` implements state of the art theoretical results. Updated instructions for installing and using `megaman` on your computer are in [install_use_megaman.ipynb](install_use_megaman.ipynb), [install_env.sh](install_env.sh).
* **a series of short articles** illustrating significant but less widely known counterintuitive behaviors of manifold learning algorithms. Most of these effects are predictable or documented theoretically, and we include (light) references to the main sources. 
  * [aspect-ratio.md](aspect-ratio.md)  Most real (manifold) data  extends more in one direction than in others, that is, it looks more like elongated strips than as discs or blobs. This can have unexpected drastic consequences on some ML algorithms, when they are used naively. We demonstrate both what can happen, how the problem is detected by simple inspecttion and a simple way to fix it.
  * TBW For most ML algorithms, the way we sample the data affects the algorithm's output. In other words, what we see is not just _the shape_ of the manifold, but a combination of the shape and the _density_ of the data on the manifold, that can vary by algorithm and by the parameters used. 
  * [tsne.md (under construction)](tsne.md) t-SNE is a very popular algorithm for visualizing high-dimensional data in 2D and 3D. However, care must be taken, as sometimes the features we see do not exist in the original data. 

* **the python code** used to generate the examples. Most of the examples are based on sk-learn; for spectral_embedding (aka the DiffusionMaps / LaplacianEigenmaps algorithm) the megaman code is used; for UMAP and t-SNE we used the code provided by the authors. Additionally, we occasionally share our experience in installing/running these codes. 
  * generating samples from simple synthetic manifolds (rectangle, rectangle with a hole, swiss roll=rolled up rectangle, 3D rectangle, circle, torus); in these examples, the samples are distributed nearly uniformly [more details TBW] 
  * generating samples from the same manifolds as above, but in a highly non-uniform manner (that can be controlled). 
  * generating informative plots of the algorithms' output
  * instructions on how to install megaman on windows [install_use_megaman.ipynb](install_use_megaman.ipynb), [install_env.sh](install_env.sh).

* **the plots** used in the articles and many more

## How to use this site 
Feel free to use the code, articles and graphics, citing this repository (_please see sidebar_ **About** to obtain citation). Currently, this is a working repository; changes to the code or files are possible.

## Contributors (in alphabetical order)
* [Haoqiang (Murray) Kang](https://github.com/mk322), non-uniform density, aspect ratio, t-SNE
* Marina Meila, Professor, concept and scientific leadership
* [Hangliang Ren (Harry)](https://github.com/Harryahh), spectral embedding, non-uniform density, plotting, aspect ratio
* [Qirui Wang](https://github.com/Typhoeus-Wang), UMAP, aspect ratio
* [Yujia Wu](https://github.com/yujiaw3-1933467), data generation, plotting, Local Linear Embedding, aspect ratio



