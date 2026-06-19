package main

func jump(nums []int) int {
	L := len(nums)
	if L == 1 {
		return 0
	}
	steps := 1
	farthest := 0
	checkEnd := 0
	for i, n := range nums {
		farthest = max(i+n, farthest)
		if farthest >= L-1 {
			break
		}
		if i == checkEnd {
			steps += 1
			checkEnd = farthest
		}
	}
	return steps
}
