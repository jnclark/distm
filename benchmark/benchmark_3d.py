import numpy as np
from sklearn.metrics import pairwise_distances
import datetime

import distm

points = 300

print('Benchmarking various calculations for {} 3D points'.format(points))

points = np.random.rand(points, 3).astype(np.float32)

a = datetime.datetime.now()

matrix = distm.calcm3d(points)

b = datetime.datetime.now()

py_matrix = distm.python_calcm(points)

c = datetime.datetime.now()

paired_dist = pairwise_distances(points, points, metric='euclidean')

d = datetime.datetime.now()

matrix2 = distm.calcm3d_parallel(points)

e = datetime.datetime.now()

print('Time to complete calculations:')
print('\tfull time\tseconds\tmicroseconds')
pytho = c - b
print('python\t', pytho, ' ', pytho.seconds, '\t ', pytho.microseconds)
skl = d - c
print('sklearn\t', skl, ' ', skl.seconds, '\t ', skl.microseconds)
cpp = b - a
print('cpp\t', cpp, ' ', cpp.seconds, '\t ', cpp.microseconds)
cppp = e - d
print('cpp/par\t', cppp, ' ', cppp.seconds, '\t ', cppp.microseconds)

print('\nMax difference between matrix entries:')
print('cpp/py  max difference: ', np.max(np.abs(matrix - py_matrix)))
print('cpp/skl max difference: ', np.max(np.abs(matrix - paired_dist)))
print('skl/py  max difference: ', np.max(np.abs(py_matrix - paired_dist)))
print('cpp/par max difference: ', np.max(np.abs(matrix - matrix2)))
print('self    max difference: ', np.max(np.abs(matrix - matrix)))
