class Solution:
    """
    https://leetcode.com/problems/daily-temperatures/

    >>> solution = Solution()
    >>> solution.dailyTemperatures([73,74,75,71,69,72,76,73])
    [1, 1, 4, 2, 1, 1, 0, 0]
    """

    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        result = [0] * len(temperatures)
        stack = []

        for i in range(len(temperatures)):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                prev_index = stack.pop()
                result[prev_index] = i - prev_index
            stack.append(i)

        return result


if __name__ == "__main__":
    import doctest

    doctest.testmod()
