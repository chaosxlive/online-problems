from collections import Counter
from typing import List


class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        counts = Counter()
        counts[0] = 1
        result = 0
        curr = 0
        less_than_curr = 0
        for num in nums:
            if num == target:
                curr += 1
                less_than_curr += counts[curr - 1]
            else:
                curr -= 1
                less_than_curr -= counts[curr]
            result += less_than_curr
            counts[curr] += 1
        return result
