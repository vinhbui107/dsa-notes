def merge(left: list, right: list) -> list:
    result = []

    while left and right:
        result.append(left.pop(0) if left[0] <= right[0] else right.pop(0))

    result.extend(left)
    result.extend(right)
    return result


def merge_sort(nums: list) -> list:
    """
    Examples:
    >>> merge_sort([0, 5, 3, 2, 2])
    [0, 2, 2, 3, 5]
    >>> merge_sort([])
    []
    >>> merge_sort([-2, -5, -45])
    [-45, -5, -2]
    """

    if len(nums) <= 1:
        return nums

    mid_index = len(nums) // 2
    return merge(merge_sort(nums[:mid_index]), merge_sort(nums[mid_index:]))


if __name__ == "__main__":
    import doctest
    doctest.testmod()
