class Solution:
    """
    https://leetcode.com/problems/longest-repeating-character-replacement/description/

    >>> solution = Solution()
    >>> solution.characterReplacement("ABBBAB", 1)
    5
    """
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        count = {}
        L = 0
        max_f = 0

        for R in range(len(s)):
            current_char = s[R]

            # calculate the frequent for current char
            count[current_char] = 1 + count.get(current_char, 0)

            # we need to find current max_f to compare with the current window size
            max_f = max(max_f, count[current_char])

            # window_size - max_f is more then k, this is invalid so we need to move L
            window_size = R - L + 1
            if window_size - max_f > k:
                count[s[L]] -= 1
                L += 1

            res = max(res, R - L + 1)

        return res


if __name__ == "__main__":
    import doctest
    doctest.testmod()
