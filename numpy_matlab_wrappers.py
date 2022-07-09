import numpy as np

def any(array: np.ndarray):
    '''
    Partial implementation of the any() function from MATLAB.
    It is partial in the sense that additional parameters aside from the
    target array have not been considered.

    The following is pulled from https://mathworks.com/help/matlab/ref/any.html

    any(A) tests along the first array dimension of A whose size does not equal
    1, and determines if any element is a nonzero number or logical 1 (true). In
    practice, any() is a natural extension of the logical OR operator.

    If A is a vector, then B = any(A) returns logical 1 (True in Python) if any
    of the elements of A is a nonzero number (not implemented) or is logical 1
    (True in Python), and returns logical 0 (False in Python) if all the
    elements are zero.

    If A is a nonempty, nonvector matrix, then any(A) treats the columns of
    A as vectors, returning a row vector of logical 1s (True) and 0s (False).

    If A is an empty 0-by-0 matrix, any(A) returns logical 0 (False) (not implemented).

    If A is a multidimensional array, any(A) acts along the first array
    dimension whose size does not equal 1 and returns an array of logical
    values. The size of this dimension becomes 1, while the sizes of all other
    dimensions remain the same.

    Parameters
    ----------
    array : ndarray
        Array of boolean values upon which we carry out checks

    Returns
    -------
    any : bool or ndarray
        True if there is any element of the array which is True,
        False otherwise.
    '''

    # We check that the parameter is of the right type
    if not isinstance(array, np.ndarray):
        raise TypeError('array variable is not of type ndarray.')

    # If it's a vector, we merely return True if any of its elements are True.
    # A vector may have one or two dimensions in NumPy; we also check that the
    # shape, if it has two elements, has one of them equal to 1, before
    # treating it like a vector as in MATLAB.
    if (len(array.shape) == 1) or ((len(array.shape) == 2) and ((array.shape[0] == 1) or (array.shape[1] == 1))):
        any = np.any(array)
    # If it is a 2-dimensional array, we check for True values over columns
    # As NumPy can spit out an array which is a row (so technically has
    # two dimensions) we also have to check whether or not the shape
    # of any of those two dimensions is equal to 1, given that in this case,
    # MATLAB treats them as in the previous case.
    elif (len(array.shape) == 2) and ((array.shape[0] != 1) and (array.shape[1] != 1)):
        any = np.any(array, axis=1)
    # If it is an n-dimensional array with n > 2, we check for True
    # values in the first axis we find that has size > 1
    elif len(array.shape) > 2:
        for idx, i in enumerate(array.shape):
            if i > 1:
                any = np.any(array, axis=idx)
                break
    
    return any

def cumsum(array: np.ndarray):
    '''
    Partial implementation of the behaviour of the cumsum() function from MATLAB.
    It is partial in the sense that additional parameters aside from the
    target array have not been considered.

    The following is pulled from https://mathworks.com/help/matlab/ref/cumsum.html
    
    cumsum(A) returns the cumulative sum of A starting at the beginning of the
    first array dimension in A whose size does not equal 1.

    If A is a vector, then cumsum(A) returns a vector containing the cumulative
    sum of the elements of A.

    If A is a matrix, then cumsum(A) returns a matrix containing the cumulative
    sums for each column of A.

    If A is a multidimensional array, then cumsum(A) acts along the first
    nonsingleton dimension.

    Parameters
    ----------
    array : ndarray
        Array upon which we compute its cumulative sum

    Returns
    -------
    cumsum  : ndarray
        Cumulative sum of the array along a certain axis
    '''

    # We check that the parameter is of the right type
    if not isinstance(array, np.ndarray):
        raise TypeError('array variable is not of type ndarray.')
    
    # If it's a vector, we merely calculate the cumulative sum over all of its elements
    # A vector may have one or two dimensions in NumPy; we also check that the
    # shape, if it has two elements, has one of them equal to 1, before
    # treating it like a vector as in MATLAB
    if (len(array.shape) == 1) or ((len(array.shape) == 2) and ((array.shape[0] == 1) or (array.shape[1] == 1))):
        cumsum = np.cumsum(array)
    # If it's an array with two axis, we do the cumulative sum over its columns.
    # As NumPy can spit out an array which is a row (so technically has
    # two dimensions) we also have to check whether or not the shape
    # of any of those two dimensions is equal to 1, given that in this case,
    # MATLAB treats them as in the previous case
    elif (len(array.shape) == 2) and ((array.shape[0] != 1) and (array.shape[1] != 1)):
        cumsum = np.cumsum(array, axis=0)
    # If it's a matrix with n axis, where n > 2, we do the cumulative sum
    # over the first axis we find that contains more than one element
    elif len(array.shape) > 2:
        for idx, i in enumerate(array.shape):
            if i > 1:
                cumsum = np.cumsum(array, axis=idx)
                break
    
    return cumsum

def cumprod(array: np.ndarray):
    '''
    Partial implementation of the behaviour of the cumprod() function from MATLAB.
    It is partial in the sense that additional parameters aside from the
    target array have not been considered.
    
    The following is pulled from https://mathworks.com/help/matlab/ref/cumprod.html
    
    cumprod(A) returns the cumulative product of A starting at the beginning of
    the first array dimension in A whose size does not equal 1.

    If A is a vector, then cumprod(A) returns a vector containing the cumulative
    product of the elements of A.

    If A is a matrix, then cumprod(A) returns a matrix containing the cumulative
    products for each column of A.

    If A is a multidimensional array, then cumprod(A) acts along the first
    nonsingleton dimension.

    Parameters
    ----------
    array : ndarray
        Array upon which we compute its cumulative product

    Returns
    -------
    cumprod  : ndarray
        Cumulative product of the array along a certain axis
    '''

    # We check that the parameter is of the right type
    if not isinstance(array, np.ndarray):
        raise TypeError('array variable is not of type ndarray.')
    
    # If it's a vector, we merely calculate the cumulative product over all of
    # its elements. A vector may have one or two dimensions in NumPy; we also
    # check that the shape, if it has two elements, has one of them equal to 1,
    # before treating it like a vector as in MATLAB
    if (len(array.shape) == 1) or ((len(array.shape) == 2) and ((array.shape[0] == 1) or (array.shape[1] == 1))):
        cumprod = np.cumprod(array)
    # If it's a matrix, we calculate the cumulative product over its columns.
    # As NumPy can spit out an array which is a row (so technically has
    # two dimensions) we also have to check whether or not the shape
    # of any of those two dimensions is equal to 1, given that in this case,
    # MATLAB treats them as in the previous case
    elif (len(array.shape) == 2) and ((array.shape[0] != 1) and (array.shape[1] != 1)):
        cumprod = np.cumprod(array, axis=0)
    # If it's a matrix with n > 2 dimensions, we do the cumulative product
    # over the first axis we find which contains more than one element
    elif len(array.shape) > 2:
        for idx, i in enumerate(array.shape):
            if i > 1:
                cumprod = np.cumprod(array, axis=idx)
                break
    
    return cumprod

def diff(array: np.ndarray):
    '''
    Partial implementation of the behaviour of the diff() function from MATLAB.
    It is partial in the sense that additional parameters aside from the
    target array have not been considered.
    
    The following is pulled from https://mathworks.com/help/matlab/ref/diff.html
    
    diff(X) calculates differences between adjacent elements of X along the
    first array dimension whose size does not equal 1:

    If X is a vector of length m, then Y = diff(X) returns a vector of length
    m-1. The elements of Y are the differences between adjacent elements of X.

    Y = [X(2)-X(1) X(3)-X(2) ... X(m)-X(m-1)]

    If X is a nonempty, nonvector p-by-m matrix, then Y = diff(X) returns a
    matrix of size (p-1)-by-m, whose elements are the differences between the
    rows of X.

    Y = [X(2,:)-X(1,:); X(3,:)-X(2,:); ... X(p,:)-X(p-1,:)]

    If X is a 0-by-0 empty matrix, then Y = diff(X) returns a 0-by-0 empty
    matrix.

    Parameters
    ----------
    array : ndarray
        Array upon which we compute its differences

    Returns
    -------
    diff  : ndarray
        Difference of the array's elements along a certain axis
    '''

    # We check that the parameter is of the right type
    if not isinstance(array, np.ndarray):
        raise TypeError('array variable is not of type ndarray.')
    
    # If it's a row vector, we calculate the difference over all of
    # its elements. A vector may have one or two dimensions in NumPy; row
    # vectors have one element in their shape
    if len(array.shape) == 1:
        diff = np.diff(array)
    # However column vectors have two; also, we need to specify the right
    # axis when having a column vector to get a proper vector of
    # differences
    elif len(array.shape) == 2:
        if array.shape[0] == 1:
            diff = np.diff(array)
        elif array.shape[1] == 1:
            diff = np.diff(array, axis=0)
    # If it's a matrix, we calculate the difference between its rows.
    # As NumPy can spit out an array which is a row (so technically has
    # two dimensions) we also have to check whether or not the shape
    # of any of those two dimensions is equal to 1, given that in this case,
    # MATLAB treats them as in the previous case
    elif (len(array.shape) == 2) and (array.shape[0] != 1) and (array.shape[1] != 1):
        diff = np.diff(array, axis=0)
    # If it's an array with n > 2 axis, we do the difference over
    # the first axis we find that has more than one element
    elif len(array.shape) > 2:
        for idx, i in enumerate(array.shape):
            if i > 1:
                diff = np.diff(array, axis=idx)
                break
    
    return diff

def fliplr(array: np.ndarray):
    '''
    Partial implementation of the fliplr() function from MATLAB.
    It is partial in the sense that additional parameters aside from the
    target array have not been considered.

    The following is pulled from https://mathworks.com/help/matlab/ref/fliplr.html)

    fliplr(A) returns A with its columns flipped in the left-right direction
    (that is, about a vertical axis).

    If A is a row vector, then fliplr(A) returns a vector of the same length with
    the order of its elements reversed. If A is a column vector, then fliplr(A)
    simply returns A. For multidimensional arrays, fliplr operates on the planes
    formed by the first and second dimensions.

    Parameters
    ----------
    array : ndarray
        Array that will be flipped

    Returns
    -------
    fliplr : ndarray
        Flipped array
    '''

    # We check that the parameter is of the right type
    if not isinstance(array, np.ndarray):
        raise TypeError('array variable is not of type ndarray.')

    # If we have a row vector, we flip left to right normally, with flip()
    if (len(array.shape) == 1) or ((len(array.shape) == 2) and ((array.shape[0] == 1) or (array.shape[1] == 1))):
        fliplr = np.flip(array)

    # If we have a column vector, we flip left to right normally, with fliplr()
    elif (len(array.shape) == 2) and ((array.shape[0] != 1) and (array.shape[1] != 1)):
        fliplr = np.fliplr(array)

    # Proper implementation of multidimensional array flipping not complete
    elif len(array.shape) > 2:
        for idx, i in enumerate(array.shape):
            if i > 1:
                fliplr = np.fliplr(array, axis=idx)
                break

    return fliplr

def mean(array: np.ndarray):
    '''
    Partial implementation of the behaviour of the mean() function from MATLAB.
    It is partial in the sense that additional parameters aside from the
    target array have not been considered.

    The following is pulled from https://mathworks.com/help/matlab/ref/mean.html

    mean(A) returns the mean of the elements of A along the first array
    dimension whose size does not equal 1.

    If A is a vector, then mean(A) returns the mean of the elements.

    If A is a matrix, then mean(A) returns a row vector containing the mean of
    each column.

    If A is a multidimensional array, then mean(A) operates along the first
    array dimension whose size does not equal 1, treating the elements as
    vectors. This size of this dimension becomes 1 while the sizes of all other
    dimensions remain the same as A. 
    
    Parameters
    ----------
    array : ndarray
        Array upon which we compute its mean

    Returns
    -------
    mean  : float64 or ndarray
        Mean of the array along a certain axis
    '''

    # We check that the parameter is of the right type
    if not isinstance(array, np.ndarray):
        raise TypeError('array variable is not of type ndarray.')
    
    # If it's a vector, we merely calculate the mean over all of its elements
    # A vector may have one or two dimensions in NumPy; we also check that the
    # shape, if it has two elements, has one of them equal to 1, before
    # treating it like a vector as in MATLAB
    if (len(array.shape) == 1) or ((len(array.shape) == 2) and ((array.shape[0] == 1) or (array.shape[1] == 1))):
        mean = np.mean(array)
    # If it's a two dimensional array, we calculate the mean over the columns.
    # As NumPy can spit out an array which is a row (so technically has
    # two dimensions) we also have to check whether or not the shape
    # of any of those two dimensions is equal to 1, given that in this case,
    # MATLAB treats them as in the previous case.
    elif (len(array.shape) == 2) and ((array.shape[0] != 1) and (array.shape[1] != 1)):
        mean = np.mean(array, axis=1)
    # If it's a matrix with more than n axis, we calculate the mean over
    # the first axis we find containing more than one element
    elif len(array.shape) > 2:
        for idx, i in enumerate(array.shape):
            if i > 1:
                mean = np.mean(array, axis=idx)
                break
    
    return mean

def sum(array: np.ndarray):
    '''
    Partial implementation of the behaviour of the sum() function from MATLAB.
    It is partial in the sense that additional parameters aside from the
    target array have not been considered.

    The following is pulled from https://mathworks.com/help/matlab/ref/sum.html

    sum(A) returns the sum of the elements of A along the first array dimension
    whose size does not equal 1.

    If A is a vector, then sum(A) returns the sum of the elements.

    If A is a matrix, then sum(A) returns a row vector containing the sum of
    each column.

    If A is a multidimensional array, then sum(A) operates along the first array
    dimension whose size does not equal 1, treating the elements as vectors.
    This dimension becomes 1 while the sizes of all other dimensions remain the
    same.

    Parameters
    ----------
    array : ndarray
        Array upon which we compute its sum

    Returns
    -------
    sum  : float64 o ndarray
        Sum of the array along a certain axis
    '''

    # We check that the parameter is of the right type
    if not isinstance(array, np.ndarray):
        raise TypeError('array variable is not of type ndarray.')
    
    # If it's a vector, we merely calculate the sum over all of its elements. A
    # vector may have one or two dimensions in NumPy; we also check that the
    # shape, if it has two elements, has one of them equal to 1, before treating
    # it like a vector as in MATLAB.
    if (len(array.shape) == 1) or ((len(array.shape) == 2) and ((array.shape[0] == 1) or (array.shape[1] == 1))):
        sum = np.sum(array)
    # If it's a matrix, we calculate the mean over its columns
    # As NumPy can spit out an array which is a row (so technically has
    # two dimensions) we also have to check whether or not the shape
    # of any of those two dimensions is equal to 1, given that in this case,
    # MATLAB treats them as in the previous case.
    elif (len(array.shape) == 2) and ((array.shape[0] != 1) and (array.shape[1] != 1)):
        sum = np.sum(array, axis=1)
    # If it's an array with n axis where n > 2, we calculate the mean
    # over the first axis we find that contains more than one element
    elif len(array.shape) > 2:
        for idx, i in enumerate(array.shape):
            if i > 1:
                sum = np.sum(array, axis=idx)
                break
    
    return sum
