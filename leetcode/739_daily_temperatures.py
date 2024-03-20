class Solution:
    """
    https://leetcode.com/problems/two-sum/

    >>> solution = Solution()
    >>> solution.dailyTemperatures([73,74,75,71,69,72,76,73])
    [1,1,4,2,1,1,0,0]
    """
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        daily = [0] * len(temperatures)
        stack = []  # pair [index, value]

        for index, value in enumerate(temperatures):
            while stack and stack[-1][0] > value:
                stack_index, stack_value = stack.pop()

            stack.append([index, value])
        return daily


if __name__ == "__main__":
    import doctest
    doctest.testmod()
