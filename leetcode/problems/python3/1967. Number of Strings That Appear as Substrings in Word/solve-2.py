from collections import deque
from typing import Deque, List, Optional


class ACNode:

    def __init__(self):
        self.children: List[Optional["ACNode"]] = [None] * 26
        self.fail_pointer: Optional["ACNode"] = None
        self.matched_indexes: List[int] = []
        self.visited: bool = False


class Solution:

    def numOfStrings(self, patterns: List[str], word: str) -> int:

        def get_ch_num(ch: str) -> int:
            return ord(ch) - ord("a")

        root = ACNode()

        # Build Trie
        for pattern_index, pattern in enumerate(patterns):
            current = root
            for ch in pattern:
                ch_num = get_ch_num(ch)
                if not current.children[ch_num]:
                    current.children[ch_num] = ACNode()
                current = current.children[ch_num]
            current.matched_indexes.append(pattern_index)

        # Build Failed Pointers
        queue: Deque[ACNode] = deque()
        for i in range(26):
            if root.children[i]:
                root.children[i].fail_pointer = root
                queue.append(root.children[i])
            else:
                root.children[i] = root

        while queue:
            current = queue.popleft()
            for i in range(26):
                if current.children[i]:
                    current.children[i].fail_pointer = current.fail_pointer.children[i]
                    queue.append(current.children[i])
                else:
                    current.children[i] = current.fail_pointer.children[i]

        # Matching Pattern
        matched = [False] * len(patterns)
        current = root
        for ch in word:
            ch_num = get_ch_num(ch)
            current = current.children[ch_num]
            temp = current
            while temp != root:
                if temp.visited:
                    break
                temp.visited = True
                for idx in temp.matched_indexes:
                    matched[idx] = True
                temp = temp.fail_pointer

        return matched.count(True)
