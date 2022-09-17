import distm
import numpy as np
import pytest


def test_sequential_calc_2d():
    points = np.random.rand(5, 2)
    matrix = distm.distm(points)
    py_matrix = distm.python_calcm(points)
    assert matrix.shape == (5, 5)
    assert py_matrix.shape == (5, 5)
    assert matrix == pytest.approx(py_matrix)


def test_parallel_calc_2d():
    points = np.random.rand(5, 2)
    matrix = distm.distm_parallel(points)
    py_matrix = distm.python_calcm(points)
    assert matrix.shape == (5, 5)
    assert py_matrix.shape == (5, 5)
    assert matrix == pytest.approx(py_matrix)


def test_sequential_calc_3d():
    points = np.random.rand(5, 3)
    matrix = distm.distm(points)
    py_matrix = distm.python_calcm(points)
    assert matrix.shape == (5, 5)
    assert py_matrix.shape == (5, 5)
    assert matrix == pytest.approx(py_matrix)


def test_parallel_calc_3d():
    points = np.random.rand(5, 3)
    matrix = distm.distm_parallel(points)
    py_matrix = distm.python_calcm(points)
    assert matrix.shape == (5, 5)
    assert py_matrix.shape == (5, 5)
    assert matrix == pytest.approx(py_matrix)


def test_exception():
    points = np.random.rand(5, 4)
    with pytest.raises(ValueError, match='Dimension of points not supported.'):
        matrix = distm.distm(points)
