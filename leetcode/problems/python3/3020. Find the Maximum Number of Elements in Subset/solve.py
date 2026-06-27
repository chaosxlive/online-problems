from collections import Counter
from typing import List


class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        counts = Counter(nums)
        checked = set()
        nums = sorted(counts.keys())
        max_len = 1

        for num in nums:
            if num in checked:
                continue
            checked.add(num)

            if num == 1:
                max_len = max(max_len, counts[num] if counts[num] % 2 == 1 else counts[num] - 1)
                continue

            curr = num
            curr_len = 1
            while True:
                if counts[curr] < 2:
                    break
                next = curr**2
                checked.add(next)
                if not counts[next]:
                    break
                curr = curr**2
                curr_len += 2
                max_len = max(max_len, curr_len)

        return max_len
