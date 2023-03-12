class Solution:
    """
    https://leetcode.com/problems/longest-substring-without-repeating-characters/

    >>> solution = Solution()
    >>> solution.lengthOfLongestSubstring("abcabcbb")
    3
    """
    def lengthOfLongestSubstring(self, s: str) -> int:
        L = 0
        length = 0
        char_set = set()

        for R in range(len(s)):
            while s[R] in char_set:
                char_set.remove(s[L])
                L += 1
            char_set.add(s[R])
            length = max(length, R - L + 1)

        return length


if __name__ == "__main__":
    import doctest
    doctest.testmod()
