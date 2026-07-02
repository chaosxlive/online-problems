import heapq
from typing import List


class Solution:

    def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:
        R = len(grid)
        C = len(grid[0])

        visited = set()
        heap = [(health, 0, 0)]
        while heap:
            h, r, c = heapq.heappop_max(heap)
            if (r, c) in visited:
                continue
            visited.add((r, c))

            h -= grid[r][c]
            if h <= 0:
                continue

            if (r, c) == (R - 1, C - 1):
                return True

            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < R and 0 <= nc < C and (nr, nc) not in visited:
                    heapq.heappush_max(heap, (h, nr, nc))

        return False
