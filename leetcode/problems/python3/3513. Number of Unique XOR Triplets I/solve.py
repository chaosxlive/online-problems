from typing import List


class Solution:

    def uniqueXorTriplets(self, nums: List[int]) -> int:
        N = len(nums)
        if N <= 2:
            return N
        result = 1
        while result <= N:
            result <<= 1
        return result
