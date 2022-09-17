import ctypes
import numpy
import os

basedir = os.path.abspath(os.path.dirname(__file__))
clibfile = os.path.join(basedir, 'libdistm.so')

# open shared library
clib = ctypes.CDLL(clibfile)

# make Python aware of the the arguments and result types of the c++
# functions

# Two dimensional functions


clib.distm.restype = ctypes.c_void_p
clib.distm.argtypes = [
    numpy.ctypeslib.ndpointer(
        dtype=numpy.float32),
    ctypes.c_int,
    ctypes.c_int,
    numpy.ctypeslib.ndpointer(
        dtype=numpy.float32)]


def calcm(points):
    internal_points = points.astype(numpy.float32)
    dist_matrix = numpy.zeros(
        (internal_points.shape[0],
         internal_points.shape[0]),
        dtype=numpy.float32)
    clib.distm(
        internal_points,
        internal_points.shape[0],
        internal_points.shape[1],
        dist_matrix)
    return dist_matrix


# Parallel version


clib.distm_parallel.restype = ctypes.c_void_p
clib.distm_parallel.argtypes = [
    numpy.ctypeslib.ndpointer(
        dtype=numpy.float32),
    ctypes.c_int,
    ctypes.c_int,
    numpy.ctypeslib.ndpointer(
        dtype=numpy.float32)]


def calcm_parallel(points):
    internal_points = points.astype(numpy.float32)
    dist_matrix = numpy.zeros(
        (internal_points.shape[0],
         internal_points.shape[0]),
        dtype=numpy.float32)
    clib.distm_parallel(
        internal_points,
        internal_points.shape[0],
        internal_points.shape[1],
        dist_matrix)
    return dist_matrix


# Three dimensional functions


clib.distm3d.restype = ctypes.c_void_p
clib.distm3d.argtypes = [
    numpy.ctypeslib.ndpointer(
        dtype=numpy.float32),
    ctypes.c_int,
    ctypes.c_int,
    numpy.ctypeslib.ndpointer(
        dtype=numpy.float32)]


def calcm3d(points):
    internal_points = points.astype(numpy.float32)
    dist_matrix = numpy.zeros(
        (internal_points.shape[0],
         internal_points.shape[0]),
        dtype=numpy.float32)
    clib.distm3d(
        internal_points,
        internal_points.shape[0],
        internal_points.shape[1],
        dist_matrix)
    return dist_matrix


# Parallel version


clib.distm3d_parallel.restype = ctypes.c_void_p
clib.distm3d_parallel.argtypes = [
    numpy.ctypeslib.ndpointer(
        dtype=numpy.float32),
    ctypes.c_int,
    ctypes.c_int,
    numpy.ctypeslib.ndpointer(
        dtype=numpy.float32)]


def calcm3d_parallel(points):
    internal_points = points.astype(numpy.float32)
    dist_matrix = numpy.zeros(
        (internal_points.shape[0],
         internal_points.shape[0]),
        dtype=numpy.float32)
    clib.distm3d_parallel(
        internal_points,
        internal_points.shape[0],
        internal_points.shape[1],
        dist_matrix)
    return dist_matrix


# Wrapper functions for easy use of bothe 2d and 3d sequential and
# parallel functions


def distm(points):
    if points.shape[1] == 2:
        return calcm(points)
    elif points.shape[1] == 3:
        return calcm3d(points)
    else:
        raise ValueError(
            "Dimension of points not supported. Point dimension: {}".format(
                points.shape[1]))


def distm_parallel(points):
    if points.shape[1] == 2:
        return calcm_parallel(points)
    elif points.shape[1] == 3:
        return calcm3d_parallel(points)
    else:
        raise ValueError(
            "Dimension of points not supported. Point dimension: {}".format(
                points.shape[1]))


# Naive function for testing


def python_calcm(points):
    points = points.astype(numpy.float32)
    num_points = points.shape[0]
    dist_matrix = numpy.zeros((num_points, num_points),
                              dtype=numpy.float32)
    for i in range(num_points):
        for j in range(i, num_points):
            dist_matrix[i][j] = \
                dist_matrix[j][i] = numpy.linalg.norm(points[i] - points[j])
    return dist_matrix
