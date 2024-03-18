def subarray_sum(nums: list[int], i: int, j: int) -> int:
    """
    Calculate the sum of elements in the subarray [i, j] of the given array.

    >>> subarray_sum([1, 4, 2, 3, 5], 1, 3)
    9
    >>> subarray_sum([1, 4, 2, 3, 5], 0, 2)
    7
    >>> subarray_sum([1, 4, 2, 3, 5], 2, 4)
    10
    """
    prefix_sum = []
    total = 0

    for num in nums:
        total += num
        prefix_sum.append(total)

    range_sum = prefix_sum[j] - prefix_sum[i - 1] if i > 0 else prefix_sum[j]
    return range_sum


if __name__ == "__main__":
    import doctest

    doctest.testmod()
