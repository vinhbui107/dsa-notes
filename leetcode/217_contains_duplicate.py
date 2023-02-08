class Solution:
    """
    >>> solution = Solution()
    >>> solution.containsDuplicate(nums=[2, 7, 2, 15])
    True
    """
    def containsDuplicate(self, nums) -> bool:
        seen = {}

        for num in nums:
            if num in seen:
                return True
            else:
                seen[num] = 1

        return False


if __name__ == "__main__":
    import doctest
    doctest.testmod()
