from typing import List

from sortedcontainers import SortedList


class Solution:
    def maxBuilding(self, n: int, restrictions: List[List[int]]) -> int:
        if len(restrictions) == 0:
            return n - 1

        result_max_height = 0

        restrictions.append([1, 0])

        id_queue = SortedList()
        heights = {}
        ids = []
        id_to_ids_index = {}

        sorted_by_id = sorted(restrictions)
        if sorted_by_id[-1][0] < n:
            sorted_by_id.append([n, n - 1])

        for [id, height] in sorted_by_id:
            ids.append(id)
            height = min(height, id - 1)
            heights[id] = height
            id_queue.add((height, id))
            id_to_ids_index[id] = len(ids) - 1

        while len(id_queue) > 0:
            current_height, current_id = id_queue.pop(0)

            result_max_height = max(current_height, result_max_height)
            current_index = id_to_ids_index[current_id]

            if current_index > 0:
                left_index = current_index - 1
                left_id = ids[left_index]
                left_height = heights[left_id]

                is_left_in_queue = False
                try:
                    id_queue.remove((left_height, left_id))
                    is_left_in_queue = True
                except ValueError:
                    pass

                id_diff = current_id - left_id

                if left_height <= current_height:
                    result_max_height = max((current_height - left_height + id_diff) // 2 + left_height, result_max_height)
                else:
                    left_predicted_height = current_height + id_diff
                    if left_height >= left_predicted_height:
                        left_height = left_predicted_height
                        heights[left_id] = left_height

                if is_left_in_queue:
                    id_queue.add((left_height, left_id))

            if current_index < len(ids) - 1:
                right_index = current_index + 1
                right_id = ids[right_index]
                right_height = heights[right_id]

                is_right_in_queue = False
                try:
                    id_queue.remove((right_height, right_id))
                    is_right_in_queue = True
                except ValueError:
                    pass

                id_diff = right_id - current_id

                if right_height < current_height:
                    result_max_height = max((right_height - current_height + id_diff) // 2 + current_height, result_max_height)
                elif right_height > current_height:
                    right_predicted_height = current_height + id_diff
                    if right_height >= right_predicted_height:
                        right_height = right_predicted_height
                        heights[right_id] = right_height

                if is_right_in_queue:
                    id_queue.add((right_height, right_id))

        return result_max_height
