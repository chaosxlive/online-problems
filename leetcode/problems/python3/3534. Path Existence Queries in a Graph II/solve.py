from typing import List
from bisect import bisect_left, bisect_right


class Solution:

    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[int]:
        vals = sorted(list(set(nums)))
        val_to_idx = {val: i for i, val in enumerate(vals)}
        M = len(vals)

        LEVELS = 18  # 2^17 = 131072 > 10^5
        up = [[0] * LEVELS for _ in range(M)]

        for i in range(M):
            up[i][0] = bisect_left(vals, vals[i] - maxDiff)

        for j in range(1, LEVELS):
            for i in range(M):
                up[i][j] = up[up[i][j - 1]][j - 1]

        result = []

        for u, v in queries:
            if u == v:
                result.append(0)
                continue
            u_val, v_val = nums[u], nums[v]
            if u_val == v_val:
                result.append(1)
                continue

            u_idx = val_to_idx[u_val]
            v_idx = val_to_idx[v_val]

            if u_idx < v_idx:
                u_idx, v_idx = v_idx, u_idx

            curr = u_idx
            steps = 0
            for j in range(LEVELS - 1, -1, -1):
                nxt = up[curr][j]
                if nxt > v_idx and nxt < curr:
                    curr = nxt
                    steps += (1 << j)
            next_pos = up[curr][0]
            if next_pos <= v_idx:
                result.append(steps + 1)
            else:
                result.append(-1)

        return result
