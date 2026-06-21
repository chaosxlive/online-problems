package main

func maxIceCream(costs []int, coins int) int {
	maxCost := 0
	for _, cost := range costs {
		if cost > maxCost {
			maxCost = cost
		}
	}

	counts := make([]int, maxCost+1)
	for _, cost := range costs {
		counts[cost]++
	}

	amount := 0
	for cost, count := range counts {
		if coins < cost {
			break
		} else if count == 0 {
			continue
		}
		buyCount := min(coins/cost, count)
		amount += buyCount
		coins -= cost * buyCount
	}

	return amount
}
