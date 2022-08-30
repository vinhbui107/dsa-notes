def bubble_sort(collection: list[int]) -> list[int]:
    if not collection:
        return []

    loop_count = 0
    for i in range(len(collection)):
        for j in range(0, len(collection) - i - 1):
            loop_count += 1

            if collection[j] > collection[j + 1]:
                collection[j], collection[j + 1] = collection[j + 1], collection[j]

    print(f"Number of loop: {loop_count}")
    return collection


items = [10, 24, 32, 21, 1, 8, 9, 345]
print(f"List a: {items}")
print(f"List a after sort: {bubble_sort(items)}")


def bubble_sort_optimized(collection: list[int]) -> list[int]:
    if not collection:
        return []

    loop_count = 0
    for i in range(len(collection)):
        # keep track of swapping
        swapped = False

        for j in range(0, len(collection) - i - 1):
            loop_count += 1

            if collection[j] > collection[j + 1]:
                collection[j], collection[j + 1] = collection[j + 1], collection[j]
                swapped = True

        if not swapped:
            break

    print(f"Number of loop: {loop_count}")
    return collection


items = [24, 14, 32, 21, 1, 8, 9, 345]
print(f"\nList a: {items}")
print(f"List a after sort: {bubble_sort_optimized(items)}")
