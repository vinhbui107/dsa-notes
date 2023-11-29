class Solution:
    """
    https://leetcode.com/problems/longest-consecutive-sequence

    >>> solution = Solution()
    >>> solution.longestConsecutive(nums=[100,4,200,1,3,2])
    4
    """
    def longestConsecutive(self, nums: list[int]) -> int:
        if not nums:
            return 0

        nums = set(nums)
        max_length = 0

        for num in nums:
            # check start of sequence
            if num - 1 not in nums:
                current_num = num
                length = 1

                while current_num + 1 in nums:
                    current_num += 1
                    length += 1

                max_length = max(max_length, length)

        return max_length


if __name__ == "__main__":
    import doctest
    doctest.testmod()
