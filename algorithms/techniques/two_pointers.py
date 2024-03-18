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


if __name__ == "__main__":
    import doctest

    doctest.testmod()
