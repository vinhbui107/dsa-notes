class Solution:
    def runningSum(self, nums):
        for i in range(1, len(nums)):
            nums[i] += nums[i - 1]

        return nums


given_array = [1, 2, 3, 4]
expected = [1, 3, 6, 10]
actual = Solution().runningSum(nums=given_array)

print(actual == expected)
