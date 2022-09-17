import numpy as np
import distm

points = np.asarray([[0, 1],
                     [2, 3],
                     [4, 5],
                     [6, 7],
                     [8, 9]])
matrix = distm.calcm(points)
matrix_parallel = distm.calcm_parallel(points)

print('Distance matrix: ')
print(matrix)

print('\nDistance matrix (computed in parallel):')
print(matrix_parallel)
