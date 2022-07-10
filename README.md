# NumPy-MATLAB Wrappers
This repo holds two files meant to be used in conjunction:

- `numpy_matlab_wrappers.py`, a module meant to reproduce the behaviour of
  various MATLAB functions in Python using NumPy.

- This `README.md` (the "Translation notes" section specifically), which has
  a table holding comparisons between MATLAB functions which I deemed not worth
  imitating and their NumPy/SciPy counterparts, given how little code they
  need. 

## Why?
On my day job, I'm working on translating a MATLAB codebase to Python and
NumPy. The way that MATLAB handles arrays makes it a bit hard to tell what
dimension they have, since scalars are handled as 1x1 arrays, for instance.
Since executing all bits of code to see what dimension their arrays have is
time consuming, I decided I would instead make wrappers around NumPy functions
to imitate the behaviour of their MATLAB counterparts, and merely plug those
in.

Of course, perfectly imitating MATLAB code is not a good idea (error
handling and for loops come to mind) but for the sake of adapting isolated
functions rather than small clumps of logic, this ought to do somewhat well.

## Usage
Just drop `numpy_matlab_wrappers.py` onto the root of your codebase and do
`import numpy_matlab_wrappers as mat`. Not sure if I'll ever get this onto
PyPI, I don't think it's worth it. There must be a million tools like this.
But this one is mine.

## Dependencies
NumPy.

## Translation notes
Not all functions behave wildly differently on NumPy/SciPy with respect to
MATLAB. Some are completely equivalent. This repo also contains comparisons
that are relevant to my job, not sure if I'll add many which are not. If in the
table below you find stuff you might've found in the NumPy documentation,
that's because it's from there. 

|              | MATLAB                      | Python                                        |
|--------------|-----------------------------|-----------------------------------------------|
| Requirements | (Nothing)                   | `import numpy as np` and `import scipy as sp` |
| Functions    | `cumsum(X)`                 | `np.cumsum(X, axis=0)`                        |
|              | `size(X)`                   | `X.shape`                                     |
|              | `zeros(size(X))`            | `np.zeros(X.shape)`                           |
|              | `zeros(size(X)(1), ass)`    | `np.zeros((X.shape[0], ass))`                 |
|              | `length(X)`                 | `np.max(X.shape)`                             |
|              | `1:N`                       | `np.arange(1., N + 1)`                        |
|              | `ones(3, 4)`                | `np.ones((3, 4))`                             |
|              | `round(X)`                  | `np.around(X)`                                |
|              | `ceil(X)`                   | `np.ceil(X)`                                  |
|              | `floor(X)`                  | `np.floor(X)`                                 | 
|              | `find(X)`                   | `np.nonzero(X)`                               |
|              | `find(X <= 0)`              | `np.nonzero(X <= 0)`                          |
|              | `randn(3, 4)`               | `np.random.randn(3, 4)`                       |
|              | `randn(size(X))`            | `np.random.standard_normal(X.shape)`          |
|              | `erfinv(X)`                 | `sp.special.erfinv(X)`                        |
|              | `rem(a, b)`                 | `np.fmod(a, b)`                               |
|              | `max(X)`                    | `X.max(0)`                                    |
|              | `max(X, Y)`                 | `np.maximum(X, Y)`                            |
|              | `min(X)`                    | `X.min(0)`                                    |
|              | `min(X, Y)`                 | `np.minimum(X, Y)`                            |
|              | `sort(X)`                   | `np.sort(X)`                                  |

- Most, if not all functions in MATLAB which act on arrays and which *could*
  return arrays, (like `mean()`, `cumsum()`, `cumprod()`, `sum()`, `any()`
  among others), by default, return the result of the computation over the
  column vectors of an array (if it's two-dimensional), but in NumPy it returns
  the computation done over all elements. These sorts of functions are the ones
  which are implemented the most in this module.

  So a vector may have one or two dimensions in NumPy, actually; we need to check
  for that. The way we do that is checking whether or not we have one dimension.
  If we do, it's a vector. If we have two, then we also need to check if one of
  those dimensions has size 1, in that case, it should also be treated as a
  vector. These if statements currently make up most of the functions in this
  module, actually.

  If we have two dimensional arrays and none of these have a size equal to 1,
  then we do make the selected calculation over the columns, as MATLAB would.

- With NumPy, as several functions and classes are often used from there at once,
  it is preferred to import the entire library as `import numpy as np`, but in
  SciPy, what is used are functions of specific modules, so it is preferred to
  import the functions individually, for example: `from scipy.special import erfinv`.

- Although there are many functions which are more or less equivalent, there are
  considerable differences. `find()` in MATLAB, for example, returns indices of a
  flattened array, while the NumPy equivalent returns a tuple with an array of
  NumPy per axis, containing the position of each element that fits on that axis.

- In MATLAB, the output from functions like `round()`, `floor()` and `ceil()` is
  seemingly usable as indices in arrays straight away, however in NumPy, what is
  returned is almost always a float, so a manual cast from `np.float64` to
  `np.int32` or similar is needed when using `np.round()` and others.

## Is it NumPy-to-MATLAB or MATLAB-to-NumPy?
At the time of naming this module I had to work, so I didn't have much time
to think of a name. Now that I think this through, it's probably the latter.
I purposefully left out the "to" such that the name would not imply any
directionality.

## Legal
Code I've written myself is licensed under BSD-3-Clause. This module
requires NumPy, also licensed under BSD-3-Clause. Furthermore, this README.md
contains portions of
<https://numpy.org/doc/stable/user/numpy-for-matlab-users.html> © Copyright
2008-2022, NumPy Developers. MATLAB® is a registered trademark of The MathWorks, Inc.
