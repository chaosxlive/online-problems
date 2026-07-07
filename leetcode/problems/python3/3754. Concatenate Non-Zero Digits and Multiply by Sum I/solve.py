class Solution:

    def sumAndMultiply(self, n: int) -> int:
        if n == 0:
            return 0
        total = 0
        chs = []
        while n:
            d = n % 10
            if d != 0:
                chs.append(str(d))
                total += d
            n //= 10
        return int(''.join(chs[::-1])) * total
