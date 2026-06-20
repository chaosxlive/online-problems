from typing import List


class Solution:
    def maxBuilding(self, n: int, restrictions: List[List[int]]) -> int:
        restrictions.append([1, 0])
        restrictions.sort()

        if restrictions[-1][0] < n:
            restrictions.append([n, n - 1])

        L = len(restrictions)

        for i in range(1, L):
            left_id, left_height = restrictions[i - 1]
            right_id, right_height = restrictions[i]
            restrictions[i][1] = min(right_height, left_height + right_id - left_id)

        for i in range(L - 2, -1, -1):
            right_id, right_height = restrictions[i + 1]
            left_id, left_height = restrictions[i]
            restrictions[i][1] = min(left_height, right_height + right_id - left_id)

        max_height = 0
        for i in range(1, L):
            left_id, left_height = restrictions[i - 1]
            right_id, right_height = restrictions[i]
            max_height = max((left_height + right_height + right_id - left_id) // 2, max_height)

        return max_height
