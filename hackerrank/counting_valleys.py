# https://www.hackerrank.com/challenges/counting-valleys


def countingValleys(steps, path):
    """
    >>> countingValleys(steps=8, path="UDDDUDUU")
    1
    """
    count_valleys = 0
    balance = 0

    for step in range(steps):
        if path[step] == "D":
            balance -= 1
        else:
            balance += 1

        if path[step] == "U" and balance == 0:
            count_valleys += 1

    return count_valleys
