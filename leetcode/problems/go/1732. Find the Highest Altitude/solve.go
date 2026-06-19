package main

func largestAltitude(gain []int) int {
	altitude := 0
	maxAlutitude := 0
	for _, g := range gain {
		altitude += g
		maxAlutitude = max(altitude, maxAlutitude)
	}
	return maxAlutitude
}
