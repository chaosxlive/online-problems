package main

import "math"

func angleClock(hour int, minutes int) float64 {
	minute_angle := float64(minutes) * 6
	hour_angle := (float64(hour%12) + float64(minutes)/60) * 30
	diff := math.Abs(hour_angle - minute_angle)
	if diff > 180 {
		return 360 - diff
	}
	return diff
}
