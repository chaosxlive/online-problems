from typing import List, Tuple


class Solution:

    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        R = len(grid)
        C = len(grid[0])
        TOTAL = R * C
        k %= TOTAL

        def get_row_and_col(index: int) -> Tuple[int, int]:
            return (index // C, index % C)

        new_grid = [[0] * C for _ in range(R)]

        for i in range(R):
            for j in range(C):
                new_index = (i * C + j + k) % TOTAL
                new_i, new_j = get_row_and_col(new_index)
                new_grid[new_i][new_j] = grid[i][j]

        return new_grid
