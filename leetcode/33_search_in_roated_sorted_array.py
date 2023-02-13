class Solution:
    """
    https://leetcode.com/problems/search-in-rotated-sorted-array/

    >>> solution = Solution()
    >>> solution.search(nums=[4,5,6,7,0,1,2], target=0)
    4
    >>> solution.search(nums=[4,5,6,7,0,1,2], target=3)
    -1
    >>> solution.search(nums=[1], target=0)
    -1
    """
    def search(self, nums: list[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            mid_value = nums[mid]

            if mid_value == target:
                return mid

            if mid_value >= nums[left]:
                if target < nums[left]:
                    left = mid + 1
                elif target > mid_value:
                    left = mid + 1
                else:
                    right = mid - 1

            # right
            else:
                if target > nums[right]:
                    right = mid - 1
                elif target < mid_value:
                    right = mid - 1
                else:
                    left = mid + 1

        return -1


if __name__ == "__main__":
    import doctest
    doctest.testmod()
