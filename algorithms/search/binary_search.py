from __future__ import annotations


def binary_search(items: list[int], key: int) -> bool:
    if not items:
        return False

    left = 0
    right = len(items) - 1

    while left < right:
        mid_point = left + (right - left)
        current_item = items[mid_point]
        if current_item == key:
            return True
        elif current_item < key:
            left = mid_point + 1
        else:
            right = mid_point - 1

    return False


key_search = 2
list_a = [1, 2, 3, 4, 5, 6, 8]
print(f"List a: {list_a}")
print(f"Is key {key_search} in items: {binary_search(items=list_a, key=key_search)}")

key_search = 10
list_a = [1, 2, 3, 4, 5, 6, 8]
print(f"List a: {list_a}")
print(f"Is key {key_search} in items: {binary_search(items=list_a, key=key_search)}")
