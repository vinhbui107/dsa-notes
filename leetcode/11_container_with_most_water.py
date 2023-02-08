class Solution:
    """
    https://leetcode.com/problems/container-with-most-water/

    >>> solution = Solution()
    >>> solution.maxArea([1,8,6,2,5,4,8,3,7])
    49
    >>> solution.maxArea([4,3,2,1,4])
    16
    >>> solution.maxArea([2, 1])
    1
    """
    def maxArea(self, height: list[int]) -> int:
        left_index, right_index = 0, len(height) - 1
        max_values = []

        while left_index < right_index:
            left_value = height[left_index]
            right_value = height[right_index]

            if left_value > right_value:
                max_values.append(right_value * (right_index - left_index))
                right_index -= 1
                continue

            if left_value < right_value:
                max_values.append(left_value * (right_index - left_index))
                left_index += 1
                continue

            if left_index != right_index and left_value == right_value:
                max_values.append(left_value * (right_index - left_index))
                right_index -= 1
                left_index += 1
                continue

            if left_index == right_index:
                max_values.append(left_value)
                right_index -= 1
                left_index += 1
                continue

        return max(max_values)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
