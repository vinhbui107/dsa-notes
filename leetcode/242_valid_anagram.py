class Solution:
    """
    https://leetcode.com/problems/valid-anagram/

    >>> solution = Solution()
    >>> solution.isAnagram(s="anagram", t="nagaram")
    True
    >>> solution.isAnagram(s="tar", t="car")
    False
    """
    def isAnagram(self, s: str, t: str) -> bool:
        if len(set(s)) != len(set(t)):
            return False

        for letter in s:
            if letter not in t:
                return False

            if letter in t and t.count(letter) != s.count(letter):
                return False

        return True


if __name__ == "__main__":
    import doctest
    doctest.testmod()
