class Solution:
    def processStr(self, s: str, k: int) -> str:
        L = 0
        for c in s:
            if c == "*":
                L = max(L - 1, 0)
            elif c == "#":
                L *= 2
            elif c == "%":
                pass
            else:
                L += 1

        if k > L - 1:
            return "."

        for c in reversed(s):
            if c == "*":
                L += 1
            elif c == "#":
                L //= 2
                if k >= L:
                    k -= L
            elif c == "%":
                k = L - 1 - k
            else:
                if k == L - 1:
                    return c
                else:
                    L -= 1

        return "."
