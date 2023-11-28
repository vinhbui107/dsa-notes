def selection_sort(collection: list[int]) -> list[int]:
    length = len(collection)

    for i in range(length - 1):
        least = i
        for k in range(i + 1, length):
            if collection[k] < collection[least]:
                least = k

        if least != i:
            collection[least], collection[i] = collection[i], collection[least]

    return collection


items = [10, 24, 32, 21, 1, 8, 9, 345]
print(f"List a: {items}")
print(f"List a after sort: {selection_sort(items)}")
