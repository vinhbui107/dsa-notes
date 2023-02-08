class Solution:
    """
    https://leetcode.com/problems/valid-palindrome/

    >>> solution = Solution()
    >>> solution.isPalindrome("A man, a plan, a canal: Panama")
    True
    """
    def isPalindrome(self, s: str) -> bool:
        new_s = ""

        for c in s:
            if c.isalnum():
                new_s += c.lower()

        return new_s == new_s[::-1]


if __name__ == "__main__":
    import doctest
    doctest.testmod()
