class Solution:
    def zigZagArrays(self, n: int, l: int, r: int) -> int:
        L = r - l + 1
        MOD = 10**9 + 7

        dp = [1] * L
        for i in range(2, n + 1):
            dp.reverse()

            pre = 0
            for j in range(L):
                temp = dp[j]
                dp[j] = pre
                pre = (pre + temp) % MOD

        return (sum(dp) * 2) % MOD
