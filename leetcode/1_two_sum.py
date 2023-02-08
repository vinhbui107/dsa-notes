class Solution:
    """
    >>> solution = Solution()
    >>> solution.twoSum(nums=[2, 7, 11, 15], target=9)
    [0, 1]
    """
    def twoSum(self, nums, target: int):
        visited_nums = {}

        for index in range(len(nums)):
            needed_num = target - nums[index]
            needed_index = visited_nums.get(needed_num, -1)

            if needed_index >= 0:
                return [needed_index, index]

            visited_nums[nums[index]] = index

        return visited_nums


if __name__ == "__main__":
    import doctest
    doctest.testmod()
