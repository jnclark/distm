import numpy as np
import distm

# 2D points

points = np.asarray([[0, 1],
                     [2, 3],
                     [4, 5],
                     [6, 7],
                     [8, 9]])
matrix = distm.calcm(points)
matrix_parallel = distm.calcm_parallel(points)

print('\n2D points: ')
print(points)

print('\n2D point distance matrix: ')
print(matrix)

print('\n2D point distance matrix (computed in parallel):')
print(matrix_parallel)

# 3D points

points_3d = np.asarray([[0, 1, 2],
                        [2, 3, 4],
                        [4, 5, 6],
                        [6, 7, 8],
                        [8, 9, 10]])
matrix_3d = distm.calcm3d(points_3d)
matrix_3d_parallel = distm.calcm3d_parallel(points_3d)

print('\n3D points: ')
print(points_3d)

print('\n3D point distance matrix: ')
print(matrix_3d)

print('\n3D point distance matrix (computed in parallel):')
print(matrix_3d_parallel)

# Wrapped functions

# sequential computation demo
wrapped_matrix = distm.distm(points)

# parallel computation demo
wrapped_matrix_3d = distm.distm_parallel(points_3d)
