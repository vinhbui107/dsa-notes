RADIX = 10


def radix_sort(nums: list[int]) -> list[int]:
    """
    >>> radix_sort(nums=[2, 4, 1, 6, 8])
    [1, 2, 4, 6, 8]

    >>> radix_sort(nums=[123, 4624, 75764, 2312, 53452]) == sorted([123, 4624, 75764, 2312, 53452])
    True
    """
    placement = 1
    max_digit = max(nums)

    while placement <= max_digit:
        # declare and initialize empty buckets
        buckets: list[list] = [[] for _ in range(RADIX)]

        # split list_of_ints between the buckets
        for num in nums:
            index = int((num / placement) % RADIX)
            buckets[index].append(num)

        # put each buckets' contents into list_of_ints
        a = 0
        for b in range(RADIX):
            for num in buckets[b]:
                nums[a] = num
                a += 1

        # move to next
        placement *= RADIX

    return nums


if __name__ == "__main__":
    import doctest
    doctest.testmod()
