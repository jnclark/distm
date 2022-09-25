# distm [![build](https://github.com/jnclark/distm/actions/workflows/build.yml/badge.svg)](https://github.com/jnclark/distm/actions/workflows/build.yml)

A `python` package for quick distance matrix calculation for both two
and three dimensional points.

## Description

`distm` was created to answer a question, namely, is it possible to
improve the time needed to compute distance matrices in Python, the
current platform for many of my academic projects, without adding too
much complexity to the workflow.

The hope is that I accomplished this. Build the project and see if it
might help you. (I find `benchmark/benchmark.py` helpful for this
purpose.) 

On available hardware, for various numbers of two dimensional points,
the following performance comparison is obtained:

| Algorithm    | 10 point time  | 100 point time | 300 point time | 1000 point time | 10000 point time | 45000 point time |
|--------------|----------------|----------------|----------------|-----------------|------------------|------------------|
| naive python | 0:00:00.000165 | 0:00:00.012241 | 0:00:00.103896 | 0:00:01.124534  | 0:01:58.250470   | untested         |
| scikit-learn | 0:00:00.000305 | 0:00:00.000364 | 0:00:00.000878 | 0:00:00.011287  | 0:00:00.814089   | 0:00:17.175534   |
| C++          | 0:00:00.000031 | 0:00:00.000079 | 0:00:00.000446 | 0:00:00.004367  | 0:00:00.437151   | 0:00:09.178394   |
| C++/Parallel | 0:00:00.000244 | 0:00:00.000748 | 0:00:00.000326 | 0:00:00.011626  | 0:00:00.386297   | 0:00:07.315356   |

Note: 45000 two dimensonal points is approximately the limit of my
offline hardware. That produces a distance matrix with 2,025,000,000
entries, after all.

And a similar set for three dimensional points:

| Algorithm    | 10 point time  | 100 point time | 300 point time | 1000 point time | 10000 point time |
|--------------|----------------|----------------|----------------|-----------------|------------------|
| naive python | 0:00:00.000160 | 0:00:00.011874 | 0:00:00.108764 | 0:00:01.191408  | 0:01:55.601313   |
| scikit-learn | 0:00:00.000178 | 0:00:00.000372 | 0:00:00.004161 | 0:00:00.014556  | 0:00:00.851405   |
| C++          | 0:00:00.000031 | 0:00:00.000085 | 0:00:00.000511 | 0:00:00.005072  | 0:00:00.490086   |
| C++/Parallel | 0:00:00.000248 | 0:00:00.000263 | 0:00:00.036277 | 0:00:00.011716  | 0:00:00.450051   |

### Features

- Distance matrix calculation for a list of two dimensional points
  both sequentially and in parallel.
- Distance matrix calculation for a list of three dimensional points
  both sequentially and in parallel.
- Distance matrix calcualtion for a list of points that is two or
  three dimenstions, but you do not neccesarily know beforehand.

## Using `distm`

Precompiled point version releases of a `pip install`-able package
and shared library are available under
[releases](https://github.com/jnclark/distm/releases).

To use this, simply download the wheel and install it in the python
environment of your choice with

```python 
pip install distm-[version information].whl
```

If you wish to build the package for yourself, read on.

### Prerequisites

The following assumes that you are on a GNU\Linux machine with

- `CMake`
- `gcc`
- `python` (of course)

### Install

To build the package, simply clone the repository, `cd` into the
directory and run 

```shell
make
```

Assuming the correct dependencies are present, this should build the
shared `c++` library alongside a python package in `dist/`.

Once this build is complete, you may use `pip install` on the created
`.whl`.

For development-style use, one may `pip install -e .` from the
repository root for an editable install.

### Usage

To call upon the functions in this library, simply 

```python 
import numpy
import distm
```

and you may call the wrapped functions `distm.distm` and
`distm.distm_parallel`, et al. For some examples of use, you can look
under `examples/`. If you wish to use the optimized 2D or 3D specific
functions, they are available under the names `distm.calcm`,
`distm.calcm3d`, with the parallel versions denoted with an appended
`_parallel`.

### Testing

You may use `pytest` to test some of the functionality of the
package. To do so, run `pytest` in the repository root.

### License

This project is licensed under the [MIT License](LICENSE).

## Note

If this code helps you in your academic work let me know by sending me
a message. If you wish to cite this repository, see [citing
info](CITATION.cff).
