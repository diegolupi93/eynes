import random

def generateSample(N, rang):
    """Exercise one, generate the Sample

    :param N: The size of the sample
    :type description: Int
    :param rang: the range of random int.
    :type rang: tuple
    :returns: a list of dict with sample data.
    :rtype: List

    Test of generateSample
    Length of Sample
    >>> len(generateSample(10,(1,100)))
    10
    
    All numbers are in the range
    >>> all([100 > e['age'] > 0 for e in generateSample(10,(1,100))])
    True

    There is no duplicate id
    >>> len(set([e['id'] for e in generateSample(10,(1,100))]))
    10
    """ 
    sample = []
    for i in range(N):
        sample.append({'id':i,
                       'age': random.randint(*rang)
                     })

    return sample

def sortSample(sample):
    """Ordenate the sample

    :param N: List of dictionary with the sample
    :type description: List
    :returns: Ordered list
    :rtype: List

    Test of sortSample
    Length of Sample and de result are the same
    >>> len(sortSample(sample)) == len(sample) # doctest: +NORMALIZE_WHITESPACE, +ELLIPSIS
    <BLANKLINE>
    ...True

    Its Ordered
    >>> result = sortSample(sample) # doctest: +NORMALIZE_WHITESPACE, +ELLIPSIS
    <BLANKLINE>
    ...
    >>> all([result[i]['age'] >= result[i+1]['age']  for i in range(len(result)-1)]) # doctest: +NORMALIZE_WHITESPACE, +ELLIPSIS
    <BLANKLINE>
    ...True
    
    The dictionaries do not change
    >>> all([e == sample[e['id']] for e in sortSample(sample)]) # doctest: +NORMALIZE_WHITESPACE, +ELLIPSIS
    <BLANKLINE>
    ...True
    """
    sorted_sample = sorted(sample, key=lambda x: x['age'], reverse=True)
    print(f'The youngest is {sorted_sample[-1]["id"]}')
    print(f'The oldest is {sorted_sample[0]["id"]}')
    return sorted_sample

if __name__ == "__main__":
    sample = generateSample(10, (1,100))
    sorted_sample = sortSample(sample)
    import doctest
    doctest.testmod()