class Solution:
    """
    https://leetcode.com/problems/trapping-rain-water/

    >>> solution = Solution()
    >>> solution.trap(height=[0,1,0,2,1,0,1,3,2,1,2,1])
    6
    """

    def trap(self, height: list[int]) -> int:
        water_trapped = 0
        L, R = 0, len(height) - 1
        max_left, max_right = 0, 0

        while R > L:
            if height[L] <= height[R]:
                max_left = max(max_left, height[L])
                water_trapped += max_left - height[L]
                L += 1
            else:
                max_right = max(max_right, height[R])
                water_trapped += max_right - height[R]
                R -= 1

        return water_trapped


if __name__ == "__main__":
    import doctest

    doctest.testmod()
