from collections import Counter


class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        counts = Counter(text)
        return min(counts["b"] // 1, counts["a"] // 1, counts["l"] // 2, counts["o"] // 2, counts["n"] // 1)
