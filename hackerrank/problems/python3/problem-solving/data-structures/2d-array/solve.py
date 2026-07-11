#!/bin/python3

from math import inf
import os
from typing import List

#
# Complete the 'hourglassSum' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#


def hourglassSum(arr: List[List[int]]) -> int:
    hourglass_shape = [(0, 0), (0, 1), (0, 2), (1, 1), (2, 0), (2, 1), (2, 2)]

    H = len(arr)
    W = len(arr[0])

    max_sum = -inf

    for i in range(H - 2):
        for j in range(W - 2):
            curr_sum = sum(arr[i + di][j + dj] for di, dj in hourglass_shape)
            max_sum = max(max_sum, curr_sum)

    return max_sum


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
