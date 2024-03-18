def is_palindrome_array(nums: list[int]) -> bool:
    """
    >>> is_palindrome_array([1, 2, 3, 3, 2, 1])
    True

    >>> is_palindrome_array([1, 2, 3, 3, 2])
    False

    >>> is_palindrome_array([1])
    True
    """
    L, R = 0, len(nums) - 1

    while R >= L:
        if nums[L] != nums[R]:
            return False

        L += 1
        R -= 1

    return True


def target_sum(nums: list[int], target: int) -> [int, int]:
    """
    Give sorted array nums and target, find the sum of 2 elements (diff position) that sum to the target

    >>> target_sum([1, 5, 2, 7, 2], 7)
    [1, 2]

    >>> target_sum([1, 5, 2, 7, 2], 10)
    []

    >>> target_sum([1, 5, 2, 7, 3], 10)
    [3, 4]
    """
    if len(nums) < 2:
        return []

    L, R = 0, 1

    while R < len(nums):
        if nums[L] + nums[R] == target:
            return [L, R]
        else:
            L += 1
            R += 1

    return []


if __name__ == "__main__":
    import doctest

    doctest.testmod()
