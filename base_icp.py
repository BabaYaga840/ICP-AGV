import open3d as o3d
import numpy as np
import copy

ply = o3d.data.PLYPointCloud()
source = o3d.io.read_point_cloud(ply.path)
print(source[0:96133])
target = copy.deepcopy(source).translate((0.085, 0.08, -0.12))
target.rotate(target.get_rotation_matrix_from_xyz((0,np.pi/48,0)))