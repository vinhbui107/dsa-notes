def counting_sort(nums: list[int]) -> list[int]:
    """
    >>> counting_sort(nums=[3, 4, 5, 2, 1, 100, 7])
    [1, 2, 3, 4, 5, 7, 100]
    """
    if len(nums) <= 1:
        return nums

    max_value = max(nums)
    count = [0] * (max_value + 1)

    for num in nums:
        count[num] += 1

    sorted_arr = []
    for i in range(len(count)):
        sorted_arr.extend([i] * count[i])

    return sorted_arr


if __name__ == "__main__":
    import doctest
    doctest.testmod()
