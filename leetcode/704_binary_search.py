class Solution:
    """
    https://leetcode.com/problems/binary-search/

    >>> solution = Solution()
    >>> solution.search(nums=[-1,0,3,5,9,12], target=9)
    4
    >>> solution.search(nums=[1,2,3], target=1)
    0
    >>> solution.search(nums=[1,2,3], target=4)
    -1
    """

    def search(self, nums: list[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] > target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                return mid

        return -1


if __name__ == "__main__":
    import doctest
    doctest.testmod()
