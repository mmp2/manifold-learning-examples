# University of Waterloo Map 

In this project, we explore how well various manifold learning algorithms compute "trivial" embeddings, which we define to be the embedding from an $n$-dimensional input to an $n$-dimensional output. This is "trivial" since the input and output dimensions are the same, so there is no need to compress data or project data to lower dimensions. Ideally, a good manifold learning algorithm should replicate the input graph as the output, possibly with minor distortions. The goal of this demonstration is to illustrate that even trivial embeddings rarely yield the same graph, and different embedding algorithms distort data in unique ways. 

Isomap, Laplacian Eigenmaps (LE), Locally Linear Embeddings (LLE), Local Tangent Space Alignment (LTSA), t-SNE, and UMAP are popular embedding algorithms that we use in this project. We perform an embedding of our input using each of these ML algorithms and compare the output graphs. 

### Data 
The data we use comes from University of Waterloo's campus map. 
- Data for the University of Waterloo buildings is retrieved from an Arcgis dataset: [https://www.arcgis.com/home/item.html?id=a3c568e6630e47b7841ccf6ea73108dd][https://www.arcgis.com/home/item.html?id=a3c568e6630e47b7841ccf6ea73108dd]. To reproduce it, follow these steps: 
1. Select the layer "City of Waterloo Buildings"
2. Copy the URL of the layer (the one with the domain "services1.arcgis.com")
3. Paste into the following website: [https://geodatadownloader.com/maps/create][https://geodatadownloader.com/maps/create]
4. Download data as GeoJSON
- Data for the University of Waterloo road is extracted from an image of the campus map. The original image is photoshopped to make the road more visible, and then OpenCV’s image recognition library is used to extract the roads. We then project the roads into our UW model. 

### Sampling 
For the buildings, we perform a mixture sampling where the sampling density is proportional to the height of buildings. This gives us a set of 2-dimensional points for which there are more points centered around taller buildings. We sample a total of $10,000$ points from buildings. 

For the roads, we perform a uniform sampling. We sample a total of $1,000$ points from roads. 

As a remark, the number of points for buildings and roads are chosen arbitrarily. 

![Isomap](/uw-map/Color/UW_Sampling_Color.png)


### Embeddings 
We run the ML algorithms described before to create multiple "trivial" embeddings of the UW campus map, from $2$-dimensional input to $2$-dimensional output. The graphs are embedded below. 
| ![Isomap](/uw-map/Color/UW_Isomap_Color.png) | ![LE](/uw-map/Color/UW_LE_Color.png) | ![LLE](/uw-map/Color/UW_LLE_Color.png) | ![LTSA](/uw-map/Color/UW_LTSA_Color.png) | ![t-SNE](/uw-map/Color/UW_tSNE_Color.png) | ![UMAP](/uw-map/Color/UW_UMAP_Color.png) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| **Isomap** | **LE** | **LLE** | **LTSA** | **t-SNE** | **UMAP** |



