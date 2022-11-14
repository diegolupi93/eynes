
import random

def isSequence(sequence):
    """Check if it is sequence of consecutive numbers or not
    :param sequence: The size of the sample
    :type description: List
    :returns: True if is a consecutive numbers sequence or False if it is not
    :rtype: Bool
    
    Test of isSequence
    True case in normal way
    >>> isSequence([1,2,3,4])
    True
    
    True case in reverse
    >>> isSequence([4,3,2,1])
    True
    
    False case
    >>> isSequence([2,3,2,1])
    False
    """
    sec1 = all([sequence[i] == sequence[i+1] + 1  for i in range(len(sequence)-1)])
    sequence.reverse()
    sec2 = all([sequence[i] == sequence[i+1] + 1  for i in range(len(sequence)-1)])
    return sec1 or sec2

def generateMatriz(shape, rang):
    """Generate Matriz with integers
    :param shape: The shape of the matriz
    :type description: tuple
    :param rang: the range of random int.
    :type rang: tuple
    :returns: a list of list with sample data.
    :rtype: list

    Test of generateMatriz
    Shape of matriz
    >>> result = generateMatriz((5,4), (1,10))
    >>> len(result)==4 and len(result[0])==5
    True

    Shape of matriz
    >>> result = generateMatriz((5,4), (1,10))
    >>> len(result)==4 and len(result[0])==4
    False

    All numbers in the range
    >>> result = generateMatriz((5,4), (1,10))
    >>> all([all([1 <= e <=10 for e in elem]) for elem in result])
    True

    All numbers in the range
    >>> result = generateMatriz((5,4), (1,10))
    >>> all([all([1 > e  for e in elem]) for elem in result])
    False

    All numbers in the range
    >>> result = generateMatriz((5,4), (1,10))
    >>> all([all([10 < e  for e in elem]) for elem in result])
    False
    """
    result = [[random.randint(*rang) for _ in range(shape[0])] for _ in range(shape[1])]
    return result

def getSequences(matriz, l_sequence):
    """Return the points that start the sequence and end the sequence
    :param shape: The shape of the matriz
    :type description: tuple
    :param rang: the range of random int.
    :type rang: tuple
    :param l_sequence: length of sequence
    :type l_sequence: int
    :returns: a list of tuples with sample data.
    :rtype: list

    Test of getSequences
    Get a sequence vertical
    >>> getSequences([[2, 1, 5, 5, 3], [2, 2, 5, 5, 3], [3, 3, 1, 2, 2], [5, 4, 4, 1, 2], [1, 1, 1, 1, 1]], 4) # doctest: +NORMALIZE_WHITESPACE, +ELLIPSIS
    <BLANKLINE>
    ...[((0, 1), (4, 1))]

    Get a sequence vertical in reverse
    >>> getSequences([[2, 4, 5, 5, 3], [2, 3, 5, 5, 3], [3, 2, 1, 2, 2], [5, 1, 4, 1, 2], [1, 1, 1, 1, 1]], 4) # doctest: +NORMALIZE_WHITESPACE, +ELLIPSIS
    <BLANKLINE>
    ...[((0, 1), (4, 1))]

    Get a sequence horizontal
    >>> getSequences([[1, 2, 3, 4, 3], [2, 3, 5, 5, 3], [3, 2, 1, 2, 2], [5, 1, 4, 1, 2], [1, 1, 1, 1, 1]], 4) # doctest: +NORMALIZE_WHITESPACE, +ELLIPSIS
    <BLANKLINE>
    ...[((0, 0), (0, 4))]

    Get a sequence horizontal in reverse
    >>> getSequences([[4, 3, 2, 1, 3], [2, 3, 5, 5, 3], [3, 2, 1, 2, 2], [5, 1, 4, 1, 2], [1, 1, 1, 1, 1]], 4) # doctest: +NORMALIZE_WHITESPACE, +ELLIPSIS
    <BLANKLINE>
    ...[((0, 0), (0, 4))]


    Do not get a sequence
    >>> getSequences([[2, 2, 5, 5, 3], [2, 2, 5, 5, 3], [3, 3, 1, 2, 2], [5, 4, 4, 1, 2], [1, 1, 1, 1, 1]], 4) # doctest: +NORMALIZE_WHITESPACE, +ELLIPSIS
    <BLANKLINE>
    ...[]
    """
    result = []
    shape = (len(matriz[1]), len(matriz))
    # Horizontal
    for i in range(shape[1]):
        for j in range(shape[0]-l_sequence+1):
            sequence = matriz[i][j:j+l_sequence]
            if isSequence(sequence):
                result.append(((i,j), (i,j+l_sequence)))
    # Vertical
    for i in range(shape[1]-l_sequence+1):
        for j in range(shape[0]):
            sequence = [matriz[i+k][j] for k in range(l_sequence)]
            if isSequence(sequence):
                result.append(((i,j), (i+l_sequence,j)))
    if result:
        print(matriz)
        print(result)
    return result
if __name__ == "__main__":
    matriz = generateMatriz((5,4), (1,5))
    sample = getSequences(matriz, 4)
    import doctest
    doctest.testmod()