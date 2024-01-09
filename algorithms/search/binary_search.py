def binary_search(nums: list[int], key: int) -> bool:
    """
    Examples:
    >>> binary_search([1, 2, 3, 4, 5, 6, 8], 1)
    True
    >>> binary_search([1, 2, 3, 4, 5, 6, 8], 10)
    False
    >>> binary_search([])
    False
    """
    if not nums:
        return False

    left = 0
    right = len(nums) - 1

    while left < right:
        mid_point = left + (right - left)
        current_item = nums[mid_point]

        if current_item == key:
            return True
        elif current_item < key:
            left = mid_point + 1
        else:
            right = mid_point - 1

    return False


if __name__ == "__main__":
    import doctest
    doctest.testmod()
