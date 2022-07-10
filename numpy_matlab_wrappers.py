import numpy as np

def any(array: np.ndarray):
    '''
    Partial implementation of the any() function from MATLAB.
    It is partial in the sense that additional parameters aside from the
    target array have not been considered.

    More information about this function can be found in
    https://mathworks.com/help/matlab/ref/any.html

    Parameters
    ----------
    array : ndarray
        Array of boolean values upon which we carry out checks

    Returns
    -------
    any : bool or ndarray of bools
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

    More information about this function can be found in
    https://mathworks.com/help/matlab/ref/cumsum.html

    Parameters
    ----------
    array  : ndarray
        Array upon which we compute its cumulative sum

    Returns
    -------
    cumsum : ndarray
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
    
    More information about this function can be found in
    https://mathworks.com/help/matlab/ref/cumprod.html
    
    Parameters
    ----------
    array   : ndarray
        Array upon which we compute its cumulative product

    Returns
    -------
    cumprod : ndarray
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
    
    More information about this function can be found in
    https://mathworks.com/help/matlab/ref/diff.html
    
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

    More information about this function can be found in
    https://mathworks.com/help/matlab/ref/fliplr.html)

    Parameters
    ----------
    array  : ndarray
        Array to be flipped

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

    More information about this function can be found in
    https://mathworks.com/help/matlab/ref/mean.html

    Parameters
    ----------
    array : ndarray
        Array upon which we compute its mean

    Returns
    -------
    mean  : float or ndarray
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

    More information about this function can be found in
    https://mathworks.com/help/matlab/ref/sum.html

    Parameters
    ----------
    array : ndarray
        Array upon which we compute its sum

    Returns
    -------
    sum  : float or ndarray
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
