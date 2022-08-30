def intersection_sort(collection: list[int]) -> list[int]:
    if not collection:
        return []

    for i in range(1, len(collection)):
        current_item = collection[i]

        j = i - 1
        while j >= 0 and collection[j] > current_item:
            collection[j + 1] = collection[j]
            j -= 1

        collection[j + 1] = current_item

    return collection


items = [10, 24, 32, 21, 1, 8, 9, 345]
print(f"List a: {items}")
print(f"List a after sort: {intersection_sort(items)}")
