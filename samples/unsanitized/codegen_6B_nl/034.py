

def unique(l: list):
    """
    Ek list mein sorted unique elements return karo
    >>> unique([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [0, 2, 3, 5, 9, 123]
    """
    result = []
    seen = set()
    for element in l:
        if element not in seen:
             result.append(element)
             seen.add(element)
    return result

a = [5, 3,5, 2, 3, 3, 9, 0,123]

unique(a)
>>> [0, 2, 3, 5, 9, 123]
