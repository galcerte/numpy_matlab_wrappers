import numpy as np

def any(array: np.ndarray):
    '''
    Partial implementation of the any() function from MATLAB. It is partial in
    the sense that additional parameters aside from the target array have not
    been considered.

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
        raise TypeError('array parameter is not of type ndarray.')

    # If we have a one-dimensional array, we merely return True if any of its
    # elements are True
    if len(array.shape) == 1:
        any = np.any(array)
    # If we have a two-dimensional array which has a size of 1 in either axis,
    # we consider that as an equivalent of a MATLAB vector so we reshape the
    # resulting array such that we preserve the shape of the original.
    # This is because NumPy functions get rid of the axis that is equal to 1 in
    # the output
    elif len(array.shape) == 2 and (1 in array.shape):
        any = np.any(array)
        any = any.reshape(array.shape)
    # If it is a two-dimensional array with no axis with size 1, we check for
    # True values over columns
    elif (len(array.shape) == 2) and (1 not in array.shape):
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
    Partial implementation of the behaviour of the cumsum() function from
    MATLAB. It is partial in the sense that additional parameters aside from
    the target array have not been considered.

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
        raise TypeError('array parameter is not of type ndarray.')
    
    # If we have a one-dimensional array, we merely do the cumulative sum
    if len(array.shape) == 1:
        cumsum = np.cumsum(array)
    # If we have a two-dimensional array which has a size of 1 in either axis,
    # we consider that as an equivalent of a MATLAB vector so we reshape the
    # resulting array such that we preserve the shape of the original.
    # This is because NumPy functions get rid of the axis that is equal to 1 in
    # the output
    elif (len(array.shape) == 2) and (1 in array.shape):
        cumsum = np.cumsum(array)
        cumsum = cumsum.reshape(array.shape)
    # If it is a two-dimensional array with no axis with size 1, we do the
    # cumulative sum over its columns
    elif (len(array.shape) == 2) and (1 not in array.shape):
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
        raise TypeError('array parameter is not of type ndarray.')
    
    # If it's a vector, we merely calculate the cumulative product over all of
    # its elements
    if len(array.shape) == 1:
        cumprod = np.cumprod(array)
    # Preserving the original shape if array is two-dimensional
    elif (len(array.shape) == 2) and (1 in array.shape):
        cumprod = np.cumprod(array)
        cumprod = cumprod.reshape(array.shape)
    # If it's a matrix, we calculate the cumulative product over its columns
    elif (len(array.shape) == 2) and (1 not in array.shape):
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
        raise TypeError('array parameter is not of type ndarray.')
    
    # If it's an array with one dimension, we calculate the difference over all
    # of its elements. A vector may have one or two dimensions in NumPy; row
    # vectors have one element in their shape
    if len(array.shape) == 1:
        diff = np.diff(array)
    # If we have an array with two dimensions, we need to specify the right
    # axis when having a column vector to get a proper vector of differences
    elif len(array.shape) == 2:
        if array.shape[0] == 1:
            diff = np.diff(array)
        elif array.shape[1] == 1:
            diff = np.diff(array, axis=0)
        if (len(array.shape) == 2) and (1 in array.shape):
            # If we're dealing with a row or column vector, we reshape the
            # resulting array such that we preserve the shape of the original
            diff = diff.reshape(array.shape)
    # If it's an array with two dimensions and one of those has size different
    # than zero, we calculate the difference between its rows
    elif (len(array.shape) == 2) and (array.shape[0] != 1) and (array.shape[1] != 1):
        diff = np.diff(array, axis=0)
    # If it's an array with n > 2 axis, we do the difference over the first
    # axis we find that has more than one element
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
        raise TypeError('array parameter is not of type ndarray.')

    # If we have a one-dimensional array, we flip left to right with np.flip()
    if (len(array.shape) == 1):
        fliplr = np.flip(array)
    # If we have a two-dimensional array with the first axis having size 1,
    # that could be considered the equivalent of a MATLAB row vector, so
    # we flip as before
    elif (len(array.shape) == 2):
        if array.shape[0] == 1:
            fliplr = np.flip(array)
        # If we have a column vector, we flip left to right with np.fliplr()
        if array.shape[1] == 1:
            fliplr = np.fliplr(array)
        # Preserving the shape of the input
        fliplr = fliplr.reshape(array.shape)
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
        raise TypeError('array parameter is not of type ndarray.')
    
    # If it's a one-dimensional array, we merely calculate the mean over all of
    # its elements
    if len(array.shape) == 1:
        mean = np.mean(array)
    # If it's a two-dimensional array with size of any axis equal to 1, we're
    # dealing with the equivalent of a row or column vector, so we reshape the
    # resulting array such that we preserve the shape of the original
    if (len(array.shape) == 2) and ((array.shape[0] == 1) or (array.shape[1] == 1)):
        mean = np.mean(array)
        mean = mean.reshape(array.shape)
    # If it's a two dimensional array with no axis with size equal to 1, we
    # calculate the mean over the columns
    elif (len(array.shape) == 2) and (1 not in array.shape):
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
        raise TypeError('array parameter is not of type ndarray.')
    
    # If it's a one-dimensional, we merely calculate the sum over all of its elements
    if len(array.shape) == 1:
        sum = np.sum(array)
    # If it's a two-dimensional array with size of any axis equal to 1, we're
    # dealing with the equivalent of a row or column vector, so we reshape the
    # resulting array such that we preserve the shape of the original
    elif (len(array.shape) == 2) and ((array.shape[0] == 1) or (array.shape[1] == 1)):
        sum = np.sum(array)
        sum = sum.reshape(array.shape)
    # If it's a two-dimensional array with no size of any axis equal to 1, we
    # calculate the mean over its columns
    elif (len(array.shape) == 2) and (1 not in array.shape):
        sum = np.sum(array, axis=1)
    # If it's an array with n axis where n > 2, we calculate the mean
    # over the first axis we find that contains more than one element
    elif len(array.shape) > 2:
        for idx, i in enumerate(array.shape):
            if i > 1:
                sum = np.sum(array, axis=idx)
                break
    
    return sum
