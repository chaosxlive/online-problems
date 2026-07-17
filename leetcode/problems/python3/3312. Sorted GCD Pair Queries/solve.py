from bisect import bisect_right
from collections import Counter
from itertools import accumulate
from typing import List


class Solution:

    def gcdValues(self, nums: List[int], queries: List[int]) -> List[int]:
        MAX_NUM = max(nums)

        num_counts = Counter(nums)
        num_prods = [0] * (MAX_NUM + 1)
        for i in range(1, MAX_NUM + 1):
            for j in range(i, MAX_NUM + 1, i):
                num_prods[i] += num_counts[j]

        gcd_counts = [0] * (MAX_NUM + 1)
        for i in range(MAX_NUM, 0, -1):
            gcd_counts[i] = num_prods[i] * (num_prods[i] - 1) // 2
            for j in range(i * 2, MAX_NUM + 1, i):
                gcd_counts[i] -= gcd_counts[j]

        gcd_counts_prefix = list(accumulate(gcd_counts))

        result = [1 for _ in range(len(queries))]
        for i, query in enumerate(queries):
            result[i] = bisect_right(gcd_counts_prefix, query)

        return result
