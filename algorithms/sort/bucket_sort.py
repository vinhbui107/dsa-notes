def bucket_sort(nums: list[int], bucket_size: int = 5) -> list[int]:
    """
    >>> bucket_sort(nums=[3, 4, 5, 2, 1, 100, 7])
    [1, 2, 3, 4, 5, 7, 100]
    """
    max_val, min_val = max(nums), min(nums)
    span = (max_val - min_val + 1) // bucket_size
    buckets = [[] for _ in range(bucket_size)]

    for num in nums:
        index = (num - min_val) // span

        if index == bucket_size:
            index -= 1

        buckets[index].append(num)

    sorted_arr = []
    for bucket in buckets:
        sorted_arr.extend(sorted(bucket))

    return sorted_arr


if __name__ == "__main__":
    import doctest
    doctest.testmod()
