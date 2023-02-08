class Solution:
    """
    https://leetcode.com/problems/top-k-frequent-elements/

    >>> solution = Solution()
    >>> solution.topKFrequent(nums=[1,1,1,2,2,3], k=2)
    [1, 2]
    """
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        freq = {}
        sorted_nums = [[] for i in range(len(nums) + 1)]
        result = []

        # loop through nums to find the freq of each value
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        # loop through the freq to insert to sorted array (bucket sort)
        for num in freq.keys():
            sorted_nums[freq[num]].append(num)
        # loop through the sorted array from the end and get k
        for i in sorted_nums[::-1]:
            if sorted_nums and len(result) < k:
                result.extend(i)

        return result


if __name__ == "__main__":
    import doctest
    doctest.testmod()
