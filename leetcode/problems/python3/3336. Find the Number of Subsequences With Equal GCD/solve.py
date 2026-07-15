from typing import List
import math


class Solution:

    def subsequencePairCount(self, nums: List[int]) -> int:
        MOD = 10**9 + 7

        dp = {(0, 0): 1}

        for x in nums:
            next_dp = dp.copy()

            unique_g = set()
            for g1, g2 in dp:
                unique_g.add(g1)
                unique_g.add(g2)

            gcd_cache = {g: math.gcd(g, x) if g > 0 else x for g in unique_g}

            for (g1, g2), count in dp.items():
                ng1 = gcd_cache[g1]
                next_dp[(ng1, g2)] = (next_dp.get((ng1, g2), 0) + count) % MOD

                ng2 = gcd_cache[g2]
                next_dp[(g1, ng2)] = (next_dp.get((g1, ng2), 0) + count) % MOD

            dp = next_dp

        ans = 0
        for (g1, g2), count in dp.items():
            if g1 == g2 and g1 > 0:
                ans = (ans + count) % MOD

        return ans
