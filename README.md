SLAM-TASKS
TASK-1
Went through videos on ICP posted by Cyrill Stachniss to understand ICP and its working
TASK-2
A Vanilla ICP:
the Iterative Corresponding Point, one point cloud (vertex cloud), the reference, or target, is kept fixed, while the other one, the source, is transformed to best match the reference. The algorithm iteratively revises the transformation (combination of translation and rotation) needed to minimize an error metric, usually a distance from the source to the reference point cloud, such as the sum of squared differences between the coordinates of the matched pairs. ICP is one of the widely used algorithms in aligning three dimensional models given an initial guess of the rigid transformation required

Solving the local minima problem:
Using global registration. 
We first downsample the point clouds using voxel downsampling to decrease computation time. We then extract the fpfh(Fast Point Feature Histograms descriptors). Fpfh used instead of pfh as pfh is very very slow.

FPFH
The default FPFH implementation uses 11 binning subdivisions (e.g., each of the four feature values will use this many bins from its value interval), and a decorrelated scheme which results in a 33-byte array of float values.
It uses the neighbors of each point to form descriptors of that point.

Then points with similar features are matched. Outliers to the matched points are removed using ransac and then using remaining points the point cloud is transformed.

Finally ICP is applied as a local registration method to match the point clouds

Finally ICP is applied as a local registration method to match the point clouds


Point clouds are moved drastically to induce the local minima problem if ICP is applied to the point clouds.
TASK-3




