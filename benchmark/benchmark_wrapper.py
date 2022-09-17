import numpy as np
import datetime

import distm

points = 750
dimension = 2

print('Benchmarking various calculations for {} {}D points'.format(points, dimension))
print('Testing the difference between the wrapped and unwrapped functions.')

points = np.random.rand(points, dimension).astype(np.float32)

a = datetime.datetime.now()

matrix = distm.calcm(points)

b = datetime.datetime.now()

matrix2 = distm.distm(points)

c = datetime.datetime.now()

print('Time to complete calculations:')
print('\t\tfull time\tseconds\tmicroseconds')
unwrapped = b - a
print('Unwrapped: \t', unwrapped, ' ', unwrapped.seconds, '\t ', unwrapped.microseconds)
wrapped = c - b
print('Wrapped: \t', wrapped, ' ', wrapped.seconds, '\t ', wrapped.microseconds)

print('\nMax difference between matrix entries:')
print('unwrapped/wrapped max difference: ', np.max(np.abs(matrix - matrix2)))
print('self              max difference: ', np.max(np.abs(matrix - matrix)))
