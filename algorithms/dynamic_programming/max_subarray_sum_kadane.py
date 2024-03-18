"""
Kadane's algorithm is a simple dynamic programming algorithm that solves the maximum
subarray sum problem in O(n) time and O(1) space.
"""


def max_subarray_sum(nums: list[int]) -> int:
    """
    >>> max_subarray_sum([2, 3, -9, 8, -2])
    8
    >>> max_subarray_sum([-2, -3, -1, -4, -6])
    -1
    """
    max_sum = nums[0]
    current_sum = 0

    for num in nums:
        current_sum = max(current_sum, 0)
        current_sum += num
        max_sum = max(max_sum, current_sum)

    return max_sum


if __name__ == "__main__":
    import doctest

    doctest.testmod()
