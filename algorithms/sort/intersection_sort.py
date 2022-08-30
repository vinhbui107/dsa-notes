def intersection_sort(items: list[int]) -> list[int]:
    if not items:
        return []

    items_sorted = []
    for item in items:
        for item_sorted in items_sorted:
            if item_sorted > item:
                pass
            elif item_sorted < item:
                pass
            else:
                pass


a = [10, 24, 32, 21, 1, 8, 9, 345]
print(f"List a: {a}")
print(f"List a after sort: {intersection_sort(a)}")
