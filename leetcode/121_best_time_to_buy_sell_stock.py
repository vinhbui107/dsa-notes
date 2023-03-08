class Solution:
    """
    >>> solution = Solution()
    >>> solution.maxProfit(prices=[7, 1, 5, 3, 6, 4])
    5
    """
    def maxProfit(self, prices: list[int]) -> int:
        buy_price = prices[0]
        profit = 0

        for price in prices:
            if price < buy_price:
                buy_price = price
            profit = max(price - buy_price, profit)

        return profit


if __name__ == "__main__":
    import doctest
    doctest.testmod()
