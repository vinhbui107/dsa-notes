def insertion_sort(items: list[int]) -> list[int]:
    if not items:
        return []

    for i in range(1, len(items)):
        key = items[i]

        j = i - 1
        while j >= 0 and items[j] > key:
            items[j + 1] = items[j]
            j -= 1

        items[j + 1] = key

    return items


items_a = [10, 24, 32, 21, 1, 8, 9, 345]
print(f"List a: {items_a}")
print(f"List a after sort: {insertion_sort(items_a)}")
