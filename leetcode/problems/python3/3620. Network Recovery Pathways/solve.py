from collections import defaultdict
import heapq
from math import inf
from typing import List


class Solution:

    def findMaxPathScore(self, edges: List[List[int]], online: List[bool], k: int) -> int:
        N = len(online)

        neighbors = defaultdict(list)
        lowest_cost = inf
        highest_cost = 0

        for u, v, cost in edges:
            if not online[u] or not online[v]:
                continue
            neighbors[u].append((v, cost))
            lowest_cost = min(lowest_cost, cost)
            highest_cost = max(highest_cost, cost)

        def check_valid(limit):
            dist = [inf] * N
            dist[0] = 0

            heap = [(0, 0)]

            while heap:
                curr_cost, node = heapq.heappop(heap)

                if curr_cost > dist[node]:
                    continue

                for next_node, cost in neighbors[node]:
                    if cost < limit:
                        continue

                    if next_node != N - 1 and not online[next_node]:
                        continue

                    new_cost = curr_cost + cost

                    if new_cost < dist[next_node]:
                        dist[next_node] = new_cost
                        heapq.heappush(heap, (new_cost, next_node))

            return dist[N - 1] <= k

        result = -1
        while lowest_cost <= highest_cost:
            mid = lowest_cost + (highest_cost - lowest_cost) // 2

            if check_valid(mid):
                result = mid
                lowest_cost = mid + 1
            else:
                highest_cost = mid - 1

        return result
