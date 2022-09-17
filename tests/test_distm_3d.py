import distm
import numpy as np
import pytest


def test_low_dim_calc_3d():
    points = np.asarray([[0, 1, 2], [2, 3, 4], [4, 5, 6]])
    matrix = distm.calcm3d(points)
    py_matrix = distm.python_calcm(points)
    assert matrix.shape == (3, 3)
    assert py_matrix.shape == (3, 3)
    assert (matrix == py_matrix).all()


def test_mid_dim_calc_3d():
    points = np.random.rand(100, 3)
    matrix = distm.calcm3d(points)
    py_matrix = distm.python_calcm(points)
    assert matrix.shape == (100, 100)
    assert py_matrix.shape == (100, 100)
    assert matrix == pytest.approx(py_matrix)


def test_large_dim_calc_3d():
    points = np.random.rand(1000, 3)
    matrix = distm.calcm3d(points)
    py_matrix = distm.python_calcm(points)
    assert matrix.shape == (1000, 1000)
    assert py_matrix.shape == (1000, 1000)
    assert matrix == pytest.approx(py_matrix)


def test_parallel_calc_3d():
    points = np.random.rand(1000, 3)
    matrix = distm.calcm3d_parallel(points)
    py_matrix = distm.python_calcm(points)
    assert matrix.shape == (1000, 1000)
    assert py_matrix.shape == (1000, 1000)
    assert matrix == pytest.approx(py_matrix)
