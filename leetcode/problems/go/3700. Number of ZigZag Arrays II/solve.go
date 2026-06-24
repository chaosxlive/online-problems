package main

const MOD = 1_000_000_007

func matMul(matA, matB [][]int) [][]int {
	size := len(matA)
	res := make([][]int, size)
	for i := range res {
		res[i] = make([]int, size)
	}

	for i := range size {
		aI := matA[i]
		for k := range size {
			aIK := aI[k]
			if aIK == 0 {
				continue
			}
			bK := matB[k]
			rI := res[i]
			for j := range size {
				rI[j] = (rI[j] + aIK*bK[j]) % MOD
			}
		}
	}
	return res
}

func matPow(mat [][]int, exp int) [][]int {
	size := len(mat)
	res := make([][]int, size)
	for i := range res {
		res[i] = make([]int, size)
		res[i][i] = 1
	}

	base := mat
	for exp > 0 {
		if exp%2 == 1 {
			res = matMul(res, base)
		}
		base = matMul(base, base)
		exp /= 2
	}
	return res
}

func matVecMul(mat [][]int, vec []int) []int {
	size := len(mat)
	res := make([]int, size)
	for i := range size {
		aI := mat[i]
		sum := 0
		for j := range size {
			sum = (sum + aI[j]*vec[j]) % MOD
		}
		res[i] = sum
	}
	return res
}

func zigZagArrays(n int, l int, r int) int {
	K := r - l

	if K == 1 {
		return 2
	}

	transMatrix := make([][]int, K)
	for i := range transMatrix {
		transMatrix[i] = make([]int, K)
	}

	for row := range K {
		for col := K - row - 1; col < K; col++ {
			transMatrix[row][col] = 1
		}
	}

	initVec := make([]int, K)
	for i := range K {
		initVec[i] = i + 1
	}

	expTimes := n - 2
	finalTransMatrix := matPow(transMatrix, expTimes)
	resultVec := matVecMul(finalTransMatrix, initVec)
	totalSum := 0
	for _, v := range resultVec {
		totalSum = (totalSum + v) % MOD
	}

	return (totalSum * 2) % MOD
}
