from typing import List


class Solution:

    def pathsWithMaxScore(self, board: List[str]) -> List[int]:
        SIZE = len(board)
        MOD = 10**9 + 7

        dp = [[(0, 0) for c in range(SIZE)] for r in range(SIZE)]
        dp[-1][-1] = (0, 1)
        for r in range(SIZE - 1, -1, -1):
            for c in range(SIZE - 1, -1, -1):
                ch = board[r][c]

                if ch == 'X' or ch == 'S':
                    continue

                val = int(ch) if ch != 'E' else 0
                has_right = c + 1 < SIZE
                has_down = r + 1 < SIZE

                max_val = 0
                max_val_count = 0

                if has_right:
                    right_max_val, right_max_val_count = dp[r][c + 1]
                    if right_max_val > max_val:
                        max_val = right_max_val
                        max_val_count = right_max_val_count
                    elif right_max_val == max_val:
                        max_val_count += right_max_val_count
                if has_down:
                    down_max_val, down_max_val_count = dp[r + 1][c]
                    if down_max_val > max_val:
                        max_val = down_max_val
                        max_val_count = down_max_val_count
                    elif down_max_val == max_val:
                        max_val_count += down_max_val_count
                if has_right and has_down:
                    diag_max_val, diag_max_val_count = dp[r + 1][c + 1]
                    if diag_max_val > max_val:
                        max_val = diag_max_val
                        max_val_count = diag_max_val_count
                    elif diag_max_val == max_val:
                        max_val_count += diag_max_val_count

                if max_val_count > 0:
                    dp[r][c] = (max_val + val, max_val_count % MOD)
                else:
                    dp[r][c] = (0, 0)

                if ch == 'E':
                    return list(dp[r][c])
