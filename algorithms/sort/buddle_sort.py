def bubble_sort(items: list[int]) -> list[int]:
    if not items:
        return []

    loop_count = 0
    for i in range(len(items)):
        for j in range(0, len(items) - i - 1):
            loop_count += 1

            if items[j] > items[j + 1]:
                items[j], items[j + 1] = items[j + 1], items[j]

    print(f"Number of loop: {loop_count}")
    return items


a = [10, 24, 32, 21, 1, 8, 9, 345]
print(f"List a: {a}")
print(f"List a after sort: {bubble_sort(a)}")


def bubble_sort_optimized(items: list[int]) -> list[int]:
    if not items:
        return []

    loop_count = 0
    for i in range(len(items)):
        # keep track of swapping
        swapped = False

        for j in range(0, len(items) - i - 1):
            loop_count += 1

            if items[j] > items[j + 1]:
                items[j], items[j + 1] = items[j + 1], items[j]
                swapped = True

        if not swapped:
            break

    print(f"Number of loop: {loop_count}")
    return items


a = [24, 14, 32, 21, 1, 8, 9, 345]
print(f"\nList a: {a}")
print(f"List a after sort: {bubble_sort_optimized(a)}")
