# Aspect Ratio Plots

This folder contains plots generated from aspect ratio analysis, showcasing various algorithms applied to different data sources.

## Files for More Information

- [Aspect Ratio Documentation](../aspect_ratio.md): A detailed explanation of the aspect ratio calculations, methodology, and analysis process.
- [Code](../aspect_ratio_code): The script used to generate the plots.
- [Parameters](../aspect_ratio): The parameters used for the plots.

## Sub-Folders

This folder contains multiple sub-folders, each representing different algorithms used or different special target for the analysis.

### File Naming Criteria

The files are named according to the following format: (which_data) _ (algorithms) _ (special_feature)


#### Examples:

- **(Circle) _ (Spectral_embedding) _ (v0_v6)**: Refers to Circle data using Spectral Embedding, where the plot shows the 0th and 6th eigenvectors.
  
- **(ct) _ (Isomap) _ (radial)**: Refers to Chopped Torus data using Isomap embedding, chopped again by the radial direction.

> **Notes: (SwissRoll) _ (rectangle)**: Refers to SwissRoll data, deformed by the algorithm into a rectangular shape. Algorithms not included

These conventions help identify the dataset, algorithm, and specific features used in each plot.
