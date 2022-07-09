|--------------|-----------------------------|------------------------------------|
|              | MATLAB                      | Python                             |
|--------------|-----------------------------|------------------------------------|
| Requirements | (Nothing)                   | import numpy as np                 |
|              |                             | import scipy as sp                 |
|------------- |-----------------------------|------------------------------------|
| Functions    | cumsum(X)                   | np.cumsum(X, axis=0)               |
|              | size(X)                     | X.shape                            |
|              | zeros(size(toa))            | np.zeros(toa.shape)                |
|              | zeros(size(toa)(1), ass)    | np.zeros((toa.shape[0], ass))      |
|              | length(X)                   | np.max(X.shape)                    |
|              | 1:N                         | np.arange(1., N + 1)               |
|              | ones(3, 4)                  | np.ones((3, 4))                    |
|              | round(X)                    | np.around(X)                       |
|              | ceil(X)                     | np.ceil(X)                         |
|              | floor(X)                    | np.floor(X)                        |
|              | find(X)                     | np.nonzero(X)                      |
|              | find(X <= 0)                | np.nonzero(X <= 0)                 |
|              | randn(3, 4)                 | np.random.randn(3, 4)              |
|              | randn(size(X))              | np.random.standard_normal(X.shape) |
|              | erfinv(X)                   | sp.special.erfinv(X)               |
|              | rem(a, b)                   | np.fmod(a, b)                      |
|              | max(X)                      | X.max(0)                           |
|              | max(X, Y)                   | np.maximum(X, Y)                   |
|              | min(X)                      | X.min(0)                           |
|              | min(X, Y)                   | np.minimum(X, Y)                   |
|              | sort(X)                     | np.sort(X)                         |
|--------------|-----------------------------|------------------------------------|

With NumPy, as several functions and classes are often used from there at once,
it is preferred to import the entire library as `import numpy as np`, but in
SciPy, as what is used are functions of specific SciPy, as what is used are
functions of specific modules, it is preferred to import the functions
individually, e.g. from functions are imported individually, for example: `from
scipy.special import erfinv`.

Although there are many functions which are more or less equivalent, there are
considerable differences. `find()` in MATLAB, for example, returns indexes of a
flattened array, while the NumPy equivalent returns a tuple with an array of
NumPy per axis, containing the position of each element that fits on that axis.

`mean()` in MATLAB, by default, returns the averages of the column vectors of an
array, but in NumPy an array, but in NumPy it returns the mean of all elements.
This behavior also occurs in `cumsum()`, `cumprod()`, `sum()` and `any()`.

`round()`, `floor()` and `ceil()` in MATLAB return `int` or `float`
variables that are converted to `float` type in MATLAB. `float` variables that
are converted to integers once they are evaluated. In NumPy, you need to a
manual cast from float to int when using `np.round()`, `np.floor()`,
`np.ceil()`.
