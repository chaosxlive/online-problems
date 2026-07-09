from typing import List


class Solution:

    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[bool]:
        group = [0] * n
        for i in range(1, n):
            if nums[i] - nums[i - 1] <= maxDiff:
                group[i] = group[i - 1]
            else:
                group[i] = group[i - 1] + 1
        return list(group[a] == group[b] for a, b in queries)
