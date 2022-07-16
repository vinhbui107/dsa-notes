class Solution:
    def containsDuplicate(self, nums) -> bool:
        seen = {}

        for num in nums:
            if num in seen:
                return True
            else:
                seen[num] = 1

        return False


given_array = 1, 2, 3, 1
expected = True
actual = Solution().containsDuplicate(nums=given_array)

print(expected == actual)
