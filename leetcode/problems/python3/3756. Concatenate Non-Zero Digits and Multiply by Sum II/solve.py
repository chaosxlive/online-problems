from typing import List


class Solution:

    def sumAndMultiply(self, s: str, queries: List[List[int]]) -> List[int]:
        N = len(s)
        MOD = 10**9 + 7

        pow10 = [1] * (N + 1)
        for i in range(1, N + 1):
            pow10[i] = (pow10[i - 1] * 10) % MOD

        cnt = [0] * (N + 1)
        P = [0] * (N + 1)
        S = [0] * (N + 1)

        for i in range(N):
            n = int(s[i])
            if n == 0:
                cnt[i + 1] = cnt[i]
                P[i + 1] = P[i]
                S[i + 1] = S[i]
            else:
                cnt[i + 1] = cnt[i] + 1
                P[i + 1] = (P[i] * 10 + n) % MOD
                S[i + 1] = S[i] + n

        result = []
        for start, end in queries:
            c = cnt[end + 1] - cnt[start]
            x = (P[end + 1] - P[start] * pow10[c]) % MOD
            sum_val = S[end + 1] - S[start]
            result.append((x * sum_val) % MOD)

        return result
