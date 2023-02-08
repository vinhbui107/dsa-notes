class Solution:
    """
    https://leetcode.com/problems/group-anagrams/

    >>> solution = Solution()
    >>> solution.groupAnagrams(["eat","tea","tan","ate","nat","bat"])
    [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]
    """
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        if not strs:
            return [['']]

        result = {}

        for word in strs:
            word_sorted = ''.join(sorted(word))
            if word_sorted in result:
                result[word_sorted].append(word)
            else:
                result[word_sorted] = [word]

        return list(result.values())


if __name__ == "__main__":
    import doctest
    doctest.testmod()
