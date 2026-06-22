package main

import "math"

func maxNumberOfBalloons(text string) int {
	counts := make(map[rune]int)
	for _, r := range text {
		counts[r]++
	}
	result := math.MaxInt32
	result = min(result, counts['b'])
	result = min(result, counts['a'])
	result = min(result, counts['l']/2)
	result = min(result, counts['o']/2)
	result = min(result, counts['n'])
	return result
}
