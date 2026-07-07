from math import inf
from typing import List


class Solution:

    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: (x[0], -x[1]))

        prev_end = -inf
        count = 0
        for start, end in intervals:
            if start <= prev_end and end <= prev_end:
                continue
            prev_end = end
            count += 1

        return count
