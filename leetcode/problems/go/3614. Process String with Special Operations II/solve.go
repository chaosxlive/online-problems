package main

func processStr(s string, k int64) byte {
	var L int64
	for _, c := range s {
		switch c {
		case '*':
			L = max(L-1, 0)
		case '#':
			L *= 2
		case '%':
			// do nothing
		default:
			L++
		}
	}

	if k > L-1 {
		return '.'
	}
	for i := len(s) - 1; i >= 0; i-- {
		c := s[i]
		switch c {
		case '*':
			L++
		case '#':
			L /= 2
			if k > L-1 {
				k -= L
			}
		case '%':
			k = L - 1 - k
		default:
			if k == L-1 {
				return byte(c)
			} else {
				L--
			}
		}
	}

	return '.'
}
