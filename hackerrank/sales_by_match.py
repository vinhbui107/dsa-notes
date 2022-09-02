# https://www.hackerrank.com/challenges/sock-merchant


def sockMerchant(n, socks):
    """
    >>> sockMerchant(n=9, socks=[10, 20, 20, 10, 10, 30, 50, 10, 20])
    3
    """
    number_of_pairs = 0
    seen = {}
    for sock in socks:
        if sock in seen and seen[sock] == 1:
            seen[sock] = 0
            number_of_pairs += 1
        else:
            seen[sock] = 1

    return number_of_pairs
