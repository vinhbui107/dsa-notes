class Solution:
    """
    https://leetcode.com/problems/valid-parentheses/

    >>> solution = Solution()
    >>> solution.isValid(s="[()]")
    True
    >>> solution.isValid(s="[](){}")
    True
    >>> solution.isValid(s="[}")
    False
    """
    def isValid(self, s: str) -> bool:
        stack = []
        close_bracket_mappings = {
            ")": "(",
            "}": "{",
            "]": "["
        }

        for c in s:
            if stack and c in close_bracket_mappings:
                current_open_bracket = stack.pop()
                if close_bracket_mappings[c] == current_open_bracket:
                    continue
                else:
                    return False
            else:
                stack.append(c)

        return not stack


if __name__ == "__main__":
    import doctest
    doctest.testmod()
