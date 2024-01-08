def selection_sort(nums: list[int]) -> list[int]:
    """
    >>> selection_sort(nums=[2, 4, 1, 6, 8])
    [1, 2, 4, 6, 8]
    """
    length = len(nums)

    for i in range(length - 1):
        least = i
        for k in range(i + 1, length):
            if nums[k] < nums[least]:
                least = k

        if least != i:
            nums[least], nums[i] = nums[i], nums[least]

    return nums
