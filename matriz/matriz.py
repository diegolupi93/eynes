
import random
def isSequence(sequence):
    """Check if it is sequence of consecutive numbers or not
    :param sequence: The size of the sample
    :type description: List
    :returns: True if is a consecutive numbers sequence or False if it is not
    :rtype: Bool
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
    """
    result = [[random.randint(*rang) for _ in range(shape[0])] for _ in range(shape[1])]
    return result

def getSequences(shape, rang, l_sequence):
    """Return the points that start the sequence and end the sequence
    :param shape: The shape of the matriz
    :type description: tuple
    :param rang: the range of random int.
    :type rang: tuple
    :param l_sequence: length of sequence
    :type l_sequence: int
    :returns: a list of tuples with sample data.
    :rtype: list
    """
    result = []
    matriz = generateMatriz(shape, rang)
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
    sample = getSequences((5,4), (1,5), 4)
    import doctest
    doctest.testmod()