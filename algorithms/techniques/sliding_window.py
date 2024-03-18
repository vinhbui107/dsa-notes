def sliding_window_fixed(nums: list[int], k: int) -> bool:
    """
    Given a array return true if there are two total values of tow element within a window equal k

    >>> sliding_window_fixed([1, 6, 2, 7, 4], 8)
    True

    >>> sliding_window_fixed([1, 6, 2, 7, 4], 100)
    False

    >>> sliding_window_fixed([], 100)
    False
    """
    L = 0

    for R in range(1, len(nums)):
        if nums[L] + nums[R] == k:
            return True
        else:
            L += 1
    return False


def sliding_window_variable(nums: list[int]) -> int:
    """
    Find length of longest subarray, with the same value of each position

    >>> sliding_window_variable([1, 2, 2, 3, 3, 3])
    3

    >>> sliding_window_variable([1, 2, 3, 4, 5])
    1

    >>> sliding_window_variable([1, 2, 2, 4, 4, 4, 4, 3, 4, 3])
    3
    """
    length = 0
    L = 0

    for R in range(len(nums)):
        if nums[L] != nums[R]:
            L = R
        else:
            length = max(length, R - L + 1)
    return length


if __name__ == "__main__":
    import doctest

    doctest.testmod()
