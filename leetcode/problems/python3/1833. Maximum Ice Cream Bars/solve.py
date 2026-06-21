from typing import List


class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        counts = [0] * (max(costs) + 1)
        for cost in costs:
            counts[cost] += 1

        amount = 0
        for cost, count in enumerate(counts):
            if coins < cost:
                break
            elif count == 0:
                continue
            buy_count = min(coins // cost, count)
            amount += buy_count
            coins -= cost * buy_count

        return amount
