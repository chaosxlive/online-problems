package main

import "slices"

func maximumLength(nums []int) int {
	if len(nums) == 0 {
		return 0
	}

	counts := make(map[int]int)
	for _, num := range nums {
		counts[num]++
	}
	checked := make(map[int]bool)
	slices.Sort(nums)
	maxLen := 1
	for _, num := range nums {
		if checked[num] {
			continue
		}
		checked[num] = true

		if num == 1 {
			if counts[num]%2 == 1 {
				maxLen = max(maxLen, counts[num])
			} else {
				maxLen = max(maxLen, counts[num]-1)
			}
			continue
		}

		curr := num
		currLen := 1
		for {
			if counts[curr] < 2 {
				break
			}
			next := curr * curr
			checked[next] = true
			if counts[next] == 0 {
				break
			}
			curr = next
			currLen += 2
			maxLen = max(maxLen, currLen)
		}
	}
	return maxLen
}
