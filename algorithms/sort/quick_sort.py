def quick_sort(nums: list[int]) -> list[int]:
    """
    Examples:
    >>> quick_sort([0, 5, 3, 2, 2])
    [0, 2, 2, 3, 5]
    >>> quick_sort([])
    []
    >>> quick_sort([-2, 5, 0, -45])
    [-45, -2, 0, 5]
    """

    if len(nums) <= 1:
        return nums

    pivot = nums.pop(0)
    left = [num for num in nums if num <= pivot]
    right = [num for num in nums if num > pivot]

    return [*quick_sort(left), pivot, *quick_sort(right)]


if __name__ == "__main__":
    import doctest
    doctest.testmod()
