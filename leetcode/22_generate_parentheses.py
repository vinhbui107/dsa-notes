class Solution:
    """
    https://leetcode.com/problems/generate-parentheses/

    >>> solution = Solution()
    >>> solution.generateParenthesis(n=3)
    ['((()))', '(()())', '(())()', '()(())', '()()()']
    """

    def generateParenthesis(self, n: int) -> list[str]:
        def backtrack(open_n, closed_n, path):
            if open_n == closed_n == n:
                result.append(path)
                return

            if open_n < n:
                backtrack(open_n + 1, closed_n, path + "(")

            if closed_n < open_n:
                backtrack(open_n, closed_n + 1, path + ")")

        result = []
        backtrack(0, 0, "")
        return result


if __name__ == "__main__":
    import doctest

    doctest.testmod()
