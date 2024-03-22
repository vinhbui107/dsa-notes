class Solution:
    """
    https://leetcode.com/problems/longest-substring-without-repeating-characters/

    >>> solution = Solution()
    >>> solution.characterReplacement("ABAB", 2)
    4
    """

    def characterReplacement(self, s: str, k: int) -> int:
        frequent = {}
        max_frequent = 0
        L, R = 0, 0

        while R < len(s):
            current_char = s[R]
            frequent[current_char] = 1 + frequent.get(current_char, 0)
            max_frequent = max(max_frequent, s[L:R].count(current_char))

            if len(s[L:R]) - max_frequent > k:
                frequent[s[L]] -= 1
                L += 1

            R += 1

        return R - L


if __name__ == "__main__":
    import doctest

    doctest.testmod()
