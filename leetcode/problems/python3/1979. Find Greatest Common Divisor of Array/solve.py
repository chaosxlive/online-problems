import math
from typing import List


class Solution:

    def findGCD(self, nums: List[int]) -> int:
        max_num = max(nums)
        min_num = min(nums)
        return math.gcd(max_num, min_num)
