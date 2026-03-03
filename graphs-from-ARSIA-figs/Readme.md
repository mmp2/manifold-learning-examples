# README: Graph Generation from Manifold Algorithms

This folder contains a collection of graphs generated using various manifold learning algorithms. Each graph represents different datasets and configurations, capturing the results of different approaches and visual styles. All figures here were created by running: [Review-figures.ipynb](../Review-figures.ipynb) 

## Explanation of workflow:
We start from a dataset, choose a manifold method to map it into **2D**, optionally add a **local-metric overlay**, then save the figure using a consistent filename.

### 1) Data
- `sr_` comes from a Swiss roll dataset (generated in the notebook and cached as a `.pickle`).
- `inward_ct_` comes from an inward chopped torus dataset (generated in the notebook and cached as a `.pickle`).
- `mnist_` comes from `sklearn.datasets.load_digits(n_class=6)`.

### 2) Method 
For each dataset, the notebook:
- computes a **2D embedding** with a chosen manifold algorithm,
- colors points using a chosen **direction** (`horiz` vs `vert`),
- optionally computes a **local metric** and draws **ellipses** (`with_metric`) to visualize local distortion,
- optionally increases point size (`largedot`),
- exports the plot into this folder.

### 3) Algorithm
Algorithms used:
- `Isomap`, `LE` (Spectral Embedding), `LTSA`, `LLE` (via `megaman`)
- `t-SNE` (via `sklearn`)
- `Umap` (via `umap`)

## Naming Convention for Files:
Each graph's filename consists of 5 components, with the following format:

`(dataset)_(algorithm)_(metric)_(coloring_direction)_(point_size)`

### Explanation of Components:
1. **Dataset Name**: The name of the dataset used to generate the graph (e.g., `inward_ct` for inward chopped torus).
2. **Algorithm**: The manifold learning algorithm applied (e.g., `Isomap`).
3. **Metric**: Indicates whether a metric is included:
   - `metric`: A metric is used.
   - `no_metric`: No metric is used.
4. **Coloring Direction**: Specifies the direction used for coloring the data points:
   - `horiz`: Coloring based on the x or y direction (for 2D maps).
   - `vert`: Coloring based on the z direction (for 3D maps).
5. **Point Size**: Indicates the size of the points in the graph:
   - `largedot`: Larger point sizes for better visibility.
   - If absent, default point size is used.

### Example:
`inward_ct_Isomap_no_metric_horiz_largedot`

This filename means the graph is generated using:
- The **inward chopped torus** dataset (`inward_ct`)
- **Isomap** algorithm (`Isomap`)
- **No metric** is applied (`no_metric`)
- Colored based on the **x or y direction** (`horiz`)
- Using **larger point sizes** (`largedot`)
