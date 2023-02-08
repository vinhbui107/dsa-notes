class Solution:
    """
    https://leetcode.com/problems/3sum/

    >>> solution = Solution()
    >>> solution.threeSum(nums=[-1,0,1,2,-1,-4])
    [[-1, -1, 2], [-1, 0, 1]]
    """
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        result = []
        nums.sort()

        for index, num in enumerate(nums):
            if num > 0:
                break

            if index > 0 and num == nums[index - 1]:
                continue

            left, right = index + 1, len(nums) - 1
            while right > left:
                three_sum = num + nums[right] + nums[left]

                if three_sum < 0:
                    left += 1
                elif three_sum > 0:
                    right -= 1
                else:
                    result.append([num, nums[left], nums[right]])
                    left += 1
                    right -= 1

                    # avoid duplicate number
                    while right > left and nums[left] == nums[left - 1]:
                        left += 1

        return result


if __name__ == "__main__":
    import doctest
    doctest.testmod()
