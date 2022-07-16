class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)


expected = True
actual = Solution().isAnagram(s="anagram", t="nagaram")
print(expected == actual)


expected = False
actual = Solution().isAnagram(s="tar", t="car")
print(expected == actual)
