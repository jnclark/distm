# distm [![build](https://github.com/jnclark/distm/actions/workflows/build.yml/badge.svg)](https://github.com/jnclark/distm/actions/workflows/build.yml)

A `python` package for quick distance matrix calculation for two
dimensional points.

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
| naive python | 0:00:00.000164 | 0:00:00.012227 | 0:00:00.110480 | 0:00:01.179250  | 0:02:00.645777   | untested         |
| scikit-learn | 0:00:00.000307 | 0:00:00.000389 | 0:00:00.000897 | 0:00:00.013485  | 0:00:00.840474   | 0:00:17.072966   |
| C++          | 0:00:00.000033 | 0:00:00.000098 | 0:00:00.000550 | 0:00:00.005955  | 0:00:00.545406   | 0:00:11.098653   |
| C++/Parallel | 0:00:00.000238 | 0:00:00.000306 | 0:00:00.000341 | 0:00:00.012431  | 0:00:00.437423   | 0:00:08.450542   |

Note: 45000 two dimensonal points is approximately the limit of my
offline hardware. That produces a distance matrix with 2,025,000,000
entries, after all.

### Features

- Distance matrix calculation for a list of two dimensional points
  both sequentially and in parallel.

## Using `distm`

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
`.whl`

### Usage

To call upon the functions in this library, simply 

```python 
import numpy
import distm
```

and you may call the functions `distm.calcm` and
`distm.calcm_parallel`, et al. For some examples of use, you can look
under `examples/`

### Testing

You may use `pytest` to test some of the functionality of the
package. To do so, run `pytest` in the repository root.

### License

This project is licensed under the [MIT License](LICENSE).

## Note

If this code helps you in your academic work let me know by sending me
a message. If you wish to cite this repository, see [citing
info](CITATION.cff).
