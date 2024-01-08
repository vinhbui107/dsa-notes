def bubble_sort(nums: list[int]) -> list[int]:
    """
    >>> bubble_sort(nums=[2, 4, 1, 5, 6, 8])
    Number of loop: 15
    [1, 2, 4, 5, 6, 8]
    """
    if not nums:
        return []

    loop_count = 0
    for i in range(len(nums)):
        for j in range(0, len(nums) - i - 1):
            loop_count += 1

            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]

    print(f"Number of loop: {loop_count}")
    return nums


def bubble_sort_optimized(nums: list[int]) -> list[int]:
    """
    >>> bubble_sort_optimized(nums=[2, 4, 1, 5, 6, 8])
    Number of loop: 12
    [1, 2, 4, 5, 6, 8]
    """
    if not nums:
        return []

    loop_count = 0
    for i in range(len(nums)):
        # keep track of swapping
        swapped = False

        for j in range(0, len(nums) - i - 1):
            loop_count += 1

            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
                swapped = True

        if not swapped:
            break

    print(f"Number of loop: {loop_count}")
    return nums
