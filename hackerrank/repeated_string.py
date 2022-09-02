# https://www.hackerrank.com/challenges/repeated-string


def repeatedString(s, n):
    """
    >>> repeatedString(s="aba", n=10)
    7
    """
    total_repeat = n // len(s)
    remain_string = n % len(s)
    count = 0

    for letter in s:
        if letter == "a":
            count += 1

    count = count * total_repeat

    for letter in s[:remain_string]:
        if letter == "a":
            count += 1

    return count
