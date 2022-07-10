from typing import List


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        left_sum = 0
        right_sum = sum(nums)

        for i in range(len(nums)):
            right_sum = right_sum - nums[i]

            if right_sum == left_sum:
                return i

            left_sum = left_sum + nums[i]

        return -1


given_array = [1, 7, 3, 6, 5, 6]
expected = 3
actual = Solution().pivotIndex(nums=given_array)

print(actual == expected)
