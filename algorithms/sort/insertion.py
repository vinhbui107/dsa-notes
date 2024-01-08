def insertion_sort(nums: list[int]) -> list[int]:
    """
    >>> insertion_sort(nums=[2, 4, 1, 6, 8])
    [1, 2, 4, 6, 8]
    """
    if not nums:
        return []

    for i in range(1, len(nums)):
        key = nums[i]

        j = i - 1
        while j >= 0 and nums[j] > key:
            nums[j + 1] = nums[j]
            j -= 1

        nums[j + 1] = key

    return nums
