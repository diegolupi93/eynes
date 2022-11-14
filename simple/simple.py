import random

def generateSample(N, rang):
    """Exercise one, generate the Sample

    :param N: The size of the sample
    :type description: Int
    :param rang: the range of random int.
    :type rang: tuple
    :returns: a list of dict with sample data.
    :rtype: List
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
    """
    sorted_sample = sorted(sample, key=lambda x: x['age'], reverse=True)
    print(f'The youngest is {sorted_sample[-1]["id"]}')
    print(f'The oldest is {sorted_sample[0]["id"]}')
    return sorted_sample

if __name__ == "__main__":
    sample = generateSample(10, (1,100))
    sorted_sample = sortSample(sample)
