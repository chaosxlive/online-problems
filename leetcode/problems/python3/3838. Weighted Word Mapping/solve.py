from typing import List


class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        chars = []
        for word in words:
            w = sum(weights[ord(c) - ord("a")] for c in word)
            chars.append(chr(26 - (w % 26) - 1 + ord("a")))
        return "".join(chars)
