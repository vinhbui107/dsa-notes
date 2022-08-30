def binary_search(collection: list[int], key: int) -> bool:
    if not collection:
        return False

    left = 0
    right = len(collection) - 1

    while left < right:
        mid_point = left + (right - left)
        current_item = collection[mid_point]
        if current_item == key:
            return True
        elif current_item < key:
            left = mid_point + 1
        else:
            right = mid_point - 1

    return False


key_search = 2
items_a = [1, 2, 3, 4, 5, 6, 8]
print(f"List a: {items_a}")
print(f"Is key {key_search} in items: {binary_search(collection=items_a, key=key_search)}")

key_search = 10
print(f"List a: {items_a}")
print(f"Is key {key_search} in items: {binary_search(collection=items_a, key=key_search)}")
