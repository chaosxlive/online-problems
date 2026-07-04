from math import inf
from typing import List


class Solution:

    def minScore(self, n: int, roads: List[List[int]]) -> int:

        uf = [i for i in range(n + 1)]
        min_score = [inf] * (n + 1)

        def find(i):
            if i != uf[i]:
                uf[i] = find(uf[i])
            return uf[i]

        def union(i, j, s):
            root_i = find(i)
            root_j = find(j)

            if root_i != root_j:
                uf[root_i] = root_j

            min_score[root_i] = min_score[root_j] = min(min_score[root_i], min_score[root_j], s)

        for u, v, s in roads:
            union(u, v, s)

        return min_score[find(1)]
