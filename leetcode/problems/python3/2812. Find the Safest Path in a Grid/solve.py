from collections import deque
import heapq
from math import inf
from typing import List


class Solution:

    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        R, C = len(grid), len(grid[0])
        dist = [[inf] * C for _ in range(R)]

        q = deque()
        for r in range(R):
            for c in range(C):
                if grid[r][c] == 1:
                    q.append((r, c))
                    dist[r][c] = 0

        while q:
            r, c = q.popleft()
            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < R and 0 <= nc < C and dist[nr][nc] == inf:
                    dist[nr][nc] = dist[r][c] + 1
                    q.append((nr, nc))

        min_dist = inf
        heap = [(dist[0][0], 0, 0)]
        visited = set()

        while heap:
            d, r, c = heapq.heappop_max(heap)
            if (r, c) in visited:
                continue

            visited.add((r, c))
            min_dist = min(min_dist, d)

            if r == R - 1 and c == C - 1:
                break

            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < R and 0 <= nc < C and (nr, nc) not in visited:
                    heapq.heappush_max(heap, (dist[nr][nc], nr, nc))

        return min_dist
