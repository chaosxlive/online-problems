from typing import List


class Solution:
    def maxBuilding(self, n: int, restrictions: List[List[int]]) -> int:
        restrictions.append([1, 0])
        restrictions.sort()

        if restrictions[-1][0] < n:
            restrictions.append([n, n - 1])

        L = len(restrictions)

        def cap_height(left_index: int, right_index: int, target: str) -> None:
            left = restrictions[left_index]
            left_id, left_height = left

            right = restrictions[right_index]
            right_id, right_height = right

            id_diff = abs(left_id - right_id)

            if target == "left":
                restrictions[left_index][1] = min(right_height + id_diff, left_height)
            else:
                restrictions[right_index][1] = min(left_height + id_diff, right_height)

        for i in range(1, L):
            cap_height(i - 1, i, "right")

        for i in range(L - 2, -1, -1):
            cap_height(i, i + 1, "left")

        def find_peak(left_index: int, right_index: int) -> int:
            left = restrictions[left_index]
            left_id, left_height = left

            right = restrictions[right_index]
            right_id, right_height = right

            id_diff = right_id - left_id
            higher = max(left_height, right_height)
            lower = min(left_height, right_height)

            return lower + (higher - lower + id_diff) // 2

        max_height = 0

        for i in range(1, L):
            max_height = max(find_peak(i - 1, i), max_height)

        return max_height
