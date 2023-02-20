class Solution:
    """
    https://leetcode.com/problems/maximum-subarray/

    >>> solution = Solution()
    >>> solution.maxSubArray(nums=[-2, 1, -3, 4, -1, 2, 1, -5, 4])
    6
    """
    def maxSubArray(self, nums: list[int]) -> int:
        max_sum = nums[0]
        curr_sum = 0

        for n in nums:
            curr_sum = max(curr_sum, 0)
            curr_sum += n
            max_sum = max(max_sum, curr_sum)

        return max_sum


if __name__ == "__main__":
    import doctest
    doctest.testmod()
