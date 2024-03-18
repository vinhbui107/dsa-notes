def has_two_elements_sum_in_window(nums: list[int], k: int) -> bool:
    """
    Given an array, return True if there are two elements within a window whose sum equals k.

    >>> has_two_elements_sum_in_window([1, 6, 2, 7, 4], 8)
    True

    >>> has_two_elements_sum_in_window([1, 6, 2, 7, 4], 100)
    False

    >>> has_two_elements_sum_in_window([], 100)
    False
    """
    L = 0

    for R in range(1, len(nums)):
        if nums[L] + nums[R] == k:
            return True
        else:
            L += 1
    return False


def longest_uniform_subarray(nums: list[int]) -> int:
    """
    Find the length of the longest subarray with the same value at each position.

    >>> longest_uniform_subarray([1, 2, 2, 3, 3, 3])
    3

    >>> longest_uniform_subarray([1, 2, 3, 4, 5])
    1

    >>> longest_uniform_subarray([1, 2, 2, 4, 4, 4, 4, 3, 4, 3])
    4
    """
    length = 0
    L = 0

    for R in range(len(nums)):
        if nums[L] != nums[R]:
            L = R
        else:
            length = max(length, R - L + 1)
    return length


def min_subarray_sum_ge_k(nums: list[int], k: int) -> int:
    """
    Find the minimum length subarray, where the sum is equal or greater than k.

    >>> min_subarray_sum_ge_k([2, 3, 1, 2, 4, 3], 7)
    2

    >>> min_subarray_sum_ge_k([1, 4, 4], 4)
    1

    >>> min_subarray_sum_ge_k([5, 1, 1, 1, 1, 1, 1, 1], 7)
    3
    """
    L, total = 0, 0
    length = float("inf")

    for R in range(len(nums)):
        total += nums[R]

        while total >= k:
            length = min(length, R - L + 1)
            total -= nums[L]
            L += 1

    return 0 if length == float("inf") else length


if __name__ == "__main__":
    import doctest

    doctest.testmod()
