class Solution:
    def maximumWealth(self, accounts) -> int:
        return max([sum(account) for account in accounts])


given_array = [[1, 2, 3], [3, 2, 1]]
expected = 6
actual = Solution().maximumWealth(accounts=given_array)

print(actual == expected)
