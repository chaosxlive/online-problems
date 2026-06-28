from typing import List


class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        arr.sort()
        curr = 0
        for num in arr:
            if num - curr > 1:
                curr += 1
            elif num - curr == 1:
                curr += 1

        return curr
