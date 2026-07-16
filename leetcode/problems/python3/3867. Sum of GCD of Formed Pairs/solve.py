import math
from typing import List


class Solution:

    def gcdSum(self, nums: List[int]) -> int:
        L = len(nums)
        prefix_gcd = [0] * L
        prefix_gcd[0] = nums[0]
        curr_max = nums[0]
        for i in range(1, L):
            curr = nums[i]
            curr_max = max(curr_max, curr)
            prefix_gcd[i] = math.gcd(curr, curr_max)
        prefix_gcd.sort()
        result = 0
        for i in range(L // 2):
            left = prefix_gcd[i]
            right = prefix_gcd[-i - 1]
            result += math.gcd(left, right)
        return result
