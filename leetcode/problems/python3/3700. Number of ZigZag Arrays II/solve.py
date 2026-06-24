class Solution:
    def zigZagArrays(self, n: int, l: int, r: int) -> int:
        MOD = 10**9 + 7

        matrix_size = r - l

        if matrix_size == 1:
            return 2

        trans_matrix = [[0] * matrix_size for _ in range(matrix_size)]

        for row in range(matrix_size):
            for col in range(matrix_size - row - 1, matrix_size):
                trans_matrix[row][col] = 1

        init_vector = [i + 1 for i in range(matrix_size)]

        def mat_mul(mat_a, mat_b):
            size = len(mat_a)
            res = [[0] * size for _ in range(size)]
            for i in range(size):
                r_i = res[i]
                a_i = mat_a[i]
                for k in range(size):
                    a_ik = a_i[k]
                    if a_ik:
                        b_k = mat_b[k]
                        for j in range(size):
                            r_i[j] = (r_i[j] + a_ik * b_k[j]) % MOD
            return res

        def mat_vec_mul(mat, vector):
            size = len(mat)
            res = [0] * size
            for i in range(size):
                a_i = mat[i]
                val = 0
                for j in range(size):
                    val = (val + a_i[j] * vector[j]) % MOD
                res[i] = val
            return res

        def mat_pow(mat, power):
            size = len(mat)
            res = [[0] * size for _ in range(size)]
            for i in range(size):
                res[i][i] = 1
            base = mat
            while power > 0:
                if power % 2 == 1:
                    res = mat_mul(res, base)
                base = mat_mul(base, base)
                power //= 2
            return res

        exp_times = n - 2

        trans_matrix = mat_pow(trans_matrix, exp_times)

        result_vector = mat_vec_mul(trans_matrix, init_vector)

        return ((sum(result_vector) % MOD) * 2) % MOD
