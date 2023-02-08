class Solution:
    """
    https://leetcode.com/problems/product-of-array-except-self/

    >>> solution = Solution()
    >>> solution.productExceptSelf(nums=[1,2,3,4])
    [24, 12, 8, 6]
    """
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        # nums: [1, 2, 3, 4]
        # loop forward: [1, 1, 2, 6]
        # loop backward: [24, 12, 4, 1]
        n = len(nums)
        left_products = [1] * n
        right_products = [1] * n
        solution = [1] * n

        for i in range(1, n):
            left_products[i] = left_products[i - 1] * nums[i - 1]
        for i in range(n - 2, -1, -1):
            right_products[i] = right_products[i + 1] * nums[i + 1]
        for i in range(n):
            solution[i] = left_products[i] * right_products[i]

        return solution


if __name__ == "__main__":
    import doctest
    doctest.testmod()
