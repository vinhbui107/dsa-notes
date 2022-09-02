def checkMagazine(magazine, note):
    """
    >>> m = "give me one grand today night".split()
    >>> n = "give one grand today".split()
    >>> checkMagazine(magazine=m, note=n)
    Yes
    """

    mapping = {}
    for word in magazine:
        mapping[word] = mapping.get(word, 0) + 1

    for word in note:
        if mapping.get(word, 0) == 0:
            print('No')
            return
        else:
            mapping[word] -= 1

    print('Yes')
