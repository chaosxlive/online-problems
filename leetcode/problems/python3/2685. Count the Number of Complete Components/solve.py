from collections import defaultdict
from typing import List


class Solution:

    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        uf = [i for i in range(n)]

        def find(i):
            if i != uf[i]:
                uf[i] = find(uf[i])
            return uf[i]

        def union(i, j):
            root_i = find(i)
            root_j = find(j)

            if root_i != root_j:
                uf[root_i] = root_j

        neighbors = defaultdict(set)

        for u, v in edges:
            neighbors[u].add(v)
            neighbors[v].add(u)
            union(u, v)

        groups = defaultdict(list)

        for i in range(n):
            groups[find(i)].append(i)

        complete_component_count = 0

        for root in groups.keys():
            group = groups[root]
            expected_neighbor_count = len(group) - 1

            is_complete = True
            for member in group:
                if len(neighbors[member]) != expected_neighbor_count:
                    is_complete = False
                    break

            if is_complete:
                complete_component_count += 1

        return complete_component_count
