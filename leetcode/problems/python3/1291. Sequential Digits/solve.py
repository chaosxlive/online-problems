from typing import List


class Solution:

    def sequentialDigits(self, low: int, high: int) -> List[int]:
        ORDER = '123456789'

        result = []

        for l in range(1, 10):
            for i in range(10 - l):
                num = int(ORDER[i:i + l])
                if low <= num <= high:
                    result.append(num)

        return result
