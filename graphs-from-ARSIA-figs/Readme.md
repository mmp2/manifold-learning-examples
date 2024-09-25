# README: Graph Generation from Manifold Algorithms

This folder contains a collection of graphs generated using various manifold learning algorithms. Each graph represents different datasets and configurations, capturing the results of different approaches and visual styles.

### Naming Convention for Files:
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
