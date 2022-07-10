class Solution:
    def maxProfit(self, prices) -> int:
        buy_price = float('inf')
        profit = 0

        for price in prices:
            if price < buy_price:
                buy_price = price
            elif (price - buy_price) > profit:
                profit = price - buy_price

        return profit


given_array = [7, 1, 5, 3, 6, 4]
expected = 5
actual = Solution().maxProfit(prices=given_array)

print(actual == expected)
