package main

import "sort"

func maxBuilding(n int, restrictions [][]int) int {
	restrictions = append(restrictions, []int{1, 0})
	sort.Slice(restrictions, func(i, j int) bool {
		return restrictions[i][0] < restrictions[j][0]
	})

	if restrictions[len(restrictions)-1][0] < n {
		restrictions = append(restrictions, []int{n, n - 1})
	}

	L := len(restrictions)

	for i := 1; i < L; i++ {
		left_id := restrictions[i-1][0]
		left_height := restrictions[i-1][1]
		right_id := restrictions[i][0]
		right_height := restrictions[i][1]
		restrictions[i][1] = min(right_height, left_height+right_id-left_id)
	}

	for i := L - 2; i >= 0; i-- {
		right_id := restrictions[i+1][0]
		right_height := restrictions[i+1][1]
		left_id := restrictions[i][0]
		left_height := restrictions[i][1]
		restrictions[i][1] = min(left_height, right_height+right_id-left_id)
	}

	max_height := 0
	for i := 1; i < L; i++ {
		left_id := restrictions[i-1][0]
		left_height := restrictions[i-1][1]
		right_id := restrictions[i][0]
		right_height := restrictions[i][1]
		peak := (left_height + right_height + right_id - left_id) / 2
		if peak > max_height {
			max_height = peak
		}
	}

	return max_height
}
