# Aspect Ratio Plots

This folder contains plots generated from aspect ratio analysis, showcasing various algorithms applied to different data sources.

## Files for More Information

- [Aspect Ratio Documentation](../aspect_ratio.md): A detailed explanation of the aspect ratio calculations, methodology, and analysis process.
- [Code](../aspect_ratio_code): The script used to generate the plots.
- [Parameters](../aspect_ratio): The parameters used for the plots.

## Naming Convention

### Manifold Explanation

This folder contains multiple sub-folders, each representing different algorithms used for the analysis. The six algorithm-specific folders are:

- Isomap
- LE 
- LLE 
- LTSA 
- t-SNE
- UMAP

Within each algorithm's folder, sub-folders correspond to the data types on which the algorithms are run.

### File Naming Criteria

The files are named according to the following format:


#### Examples:

- **Circle_Spectral_embedding_v0_v6**: Refers to Circle data using Spectral Embedding, where the plot shows the 0th and 6th eigenvectors.
  
- **ct_Isomap_radial**: Refers to Chopped Torus data using Isomap embedding, chopped again by the radial direction.
  
- **SwissRoll_rectangle**: Refers to SwissRoll data, deformed by the algorithm into a rectangular shape.

These conventions help identify the dataset, algorithm, and specific features used in each plot.
