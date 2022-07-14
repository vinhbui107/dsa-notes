class Solution:
    def dominantIndex(self, nums):

        if len(nums) == 1:
            return -1

        max_num = -1
        second_num = -1
        highest_index = 0

        for i, n in enumerate(nums):
            if n > max_num:
                second_num = max_num
                max_num = n
                highest_index = i
            else:
                if n > second_num:
                    second_num = n

        return -1 if max_num < second_num * 2 else highest_index


given_array = [1, 2, 3, 4]
expected = -1
actual = Solution().dominantIndex(nums=given_array)

print(actual == expected)
