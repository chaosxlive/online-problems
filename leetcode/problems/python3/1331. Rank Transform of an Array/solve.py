from typing import List


class Solution:

    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        rank_map = {}
        for r, v in enumerate(sorted(set(arr)), start=1):
            rank_map[v] = r
        return list(map(lambda x: rank_map[x], arr))
