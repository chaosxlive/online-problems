from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        L = len(nums)
        if L == 1:
            return 0
        steps = 1
        farthest = 0
        check_end = 0
        for i, n in enumerate(nums):
            farthest = max(i + n, farthest)
            if farthest >= L - 1:
                break
            if i == check_end:
                steps += 1
                check_end = farthest
        return steps
