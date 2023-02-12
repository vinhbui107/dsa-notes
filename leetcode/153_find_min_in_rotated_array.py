class Solution:
    """
    https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/description/

    >>> solution = Solution()
    >>> solution.findMin(nums=[3,4,5,1,2])
    1
    >>> solution.findMin(nums=[1,2,3])
    1
    """

    def findMin(self, nums: list[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        if nums[0] < nums[n - 1]:
            return nums[0]

        left, right = 0, n - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[mid + 1]:
                return nums[mid + 1]
            if nums[mid] < nums[mid - 1]:
                return nums[mid]
            if nums[mid] < nums[left]:
                right = mid + 1
            elif nums[mid] > nums[left]:
                left = mid + 1

        return -1


if __name__ == "__main__":
    import doctest
    doctest.testmod()
