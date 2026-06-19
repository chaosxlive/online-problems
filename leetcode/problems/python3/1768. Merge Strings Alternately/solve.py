class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        DL = min(len(word1), len(word2))
        return (
            "".join(map(lambda x: x[0] + x[1], zip(word1, word2)))
            + word1[DL:]
            + word2[DL:]
        )
