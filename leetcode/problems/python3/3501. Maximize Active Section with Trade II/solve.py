from bisect import bisect_left, bisect_right
from typing import List


class Solution:

    def maxActiveSectionsAfterTrade(self, s: str, queries: List[List[int]]) -> List[int]:
        L = len(s)
        ONE_COUNT = s.count('1')

        if ONE_COUNT == 0:
            return [0] * len(queries)

        ones = []
        i = 0
        while i < L:
            if s[i] == '1':
                start = i
                while i < L and s[i] == '1':
                    i += 1
                ones.append((start, i - 1, i - start))
            else:
                i += 1

        K = len(ones)
        if K == 0:
            return [0] * len(queries)

        L1 = [0] * (K + 1)
        R1 = [0] * (K + 1)
        a = [0] * (K + 1)
        for idx in range(1, K + 1):
            L1[idx], R1[idx], a[idx] = ones[idx - 1]

        L0 = [0] * (K + 1)
        R0 = [0] * (K + 1)
        len0 = [0] * (K + 1)

        L0[0] = 0
        R0[0] = L1[1] - 1
        len0[0] = max(0, R0[0] - L0[0] + 1)

        for idx in range(1, K):
            L0[idx] = R1[idx] + 1
            R0[idx] = L1[idx + 1] - 1
            len0[idx] = R0[idx] - L0[idx] + 1

        L0[K] = R1[K] + 1
        R0[K] = L - 1
        len0[K] = max(0, R0[K] - L0[K] + 1)

        S = [0] * (K + 1)
        for idx in range(1, K + 1):
            S[idx] = len0[idx - 1] + len0[idx]

        sz_S = 1
        while sz_S < K:
            sz_S *= 2
        tree_S = [0] * (2 * sz_S)
        for idx in range(1, K + 1):
            tree_S[sz_S + idx - 1] = S[idx]
        for p in range(sz_S - 1, 0, -1):
            tree_S[p] = max(tree_S[2 * p], tree_S[2 * p + 1])

        def merge_min3(l1, l2):
            res = []
            p1 = p2 = 0
            n1, n2 = len(l1), len(l2)
            while len(res) < 3 and (p1 < n1 or p2 < n2):
                if p1 < n1 and (p2 >= n2 or l1[p1][0] <= l2[p2][0]):
                    res.append(l1[p1])
                    p1 += 1
                else:
                    res.append(l2[p2])
                    p2 += 1
            return res

        def merge_max3(l1, l2):
            res = []
            p1 = p2 = 0
            n1, n2 = len(l1), len(l2)
            while len(res) < 3 and (p1 < n1 or p2 < n2):
                if p1 < n1 and (p2 >= n2 or l1[p1][0] >= l2[p2][0]):
                    res.append(l1[p1])
                    p1 += 1
                else:
                    res.append(l2[p2])
                    p2 += 1
            return res

        sz_a = 1
        while sz_a < K:
            sz_a *= 2
        tree_a = [[] for _ in range(2 * sz_a)]
        for idx in range(1, K + 1):
            tree_a[sz_a + idx - 1] = [(a[idx], idx)]
        for p in range(sz_a - 1, 0, -1):
            tree_a[p] = merge_min3(tree_a[2 * p], tree_a[2 * p + 1])

        sz_0 = 1
        while sz_0 < K + 1:
            sz_0 *= 2
        tree_0 = [[] for _ in range(2 * sz_0)]
        for idx in range(0, K + 1):
            tree_0[sz_0 + idx] = [(len0[idx], idx)]
        for p in range(sz_0 - 1, 0, -1):
            tree_0[p] = merge_max3(tree_0[2 * p], tree_0[2 * p + 1])

        L1_starts = [L1[i] for i in range(1, K + 1)]
        R1_ends = [R1[i] for i in range(1, K + 1)]
        L0_starts = L0
        R0_ends = R0

        ans = [0] * len(queries)

        for q_idx, (l, r) in enumerate(queries):
            idx_start = bisect_left(L1_starts, l + 1)
            idx_end = bisect_right(R1_ends, r - 1) - 1
            if idx_start > idx_end:
                ans[q_idx] = ONE_COUNT
                continue

            i_first = idx_start + 1
            i_last = idx_end + 1

            j_first = bisect_left(R0_ends, l)
            j_last = bisect_right(L0_starts, r) - 1

            if j_first > j_last:
                ans[q_idx] = ONE_COUNT
                continue

            b_left_first = max(0, min(R0[i_first - 1], r) - max(L0[i_first - 1], l) + 1)
            b_right_first = max(0, min(R0[i_first], r) - max(L0[i_first], l) + 1)
            max_gain = b_left_first + b_right_first

            if i_last != i_first:
                b_left_last = max(0, min(R0[i_last - 1], r) - max(L0[i_last - 1], l) + 1)
                b_right_last = max(0, min(R0[i_last], r) - max(L0[i_last], l) + 1)
                if b_left_last + b_right_last > max_gain:
                    max_gain = b_left_last + b_right_last

            if i_first + 1 <= i_last - 1:
                L_p = sz_S + i_first
                R_p = sz_S + i_last - 2
                while L_p <= R_p:
                    if L_p % 2 == 1:
                        if tree_S[L_p] > max_gain:
                            max_gain = tree_S[L_p]
                        L_p += 1
                    if R_p % 2 == 0:
                        if tree_S[R_p] > max_gain:
                            max_gain = tree_S[R_p]
                        R_p -= 1
                    L_p //= 2
                    R_p //= 2

            b_j_first = max(0, min(R0[j_first], r) - max(L0[j_first], l) + 1)
            b_j_last = max(0, min(R0[j_last], r) - max(L0[j_last], l) + 1)

            top3_zeros = [(b_j_first, j_first)]
            if j_last != j_first:
                top3_zeros.append((b_j_last, j_last))

            if j_first + 1 <= j_last - 1:
                L_p = sz_0 + j_first + 1
                R_p = sz_0 + j_last - 1
                while L_p <= R_p:
                    if L_p % 2 == 1:
                        top3_zeros.extend(tree_0[L_p])
                        L_p += 1
                    if R_p % 2 == 0:
                        top3_zeros.extend(tree_0[R_p])
                        R_p -= 1
                    L_p //= 2
                    R_p //= 2

            top3_zeros.sort(key=lambda x: x[0], reverse=True)
            sorted_zeros = []
            seen_j = set()
            for b_len, j_idx in top3_zeros:
                if j_idx not in seen_j:
                    seen_j.add(j_idx)
                    sorted_zeros.append((b_len, j_idx))
                    if len(sorted_zeros) == 3:
                        break

            cand_a = []
            L_p = sz_a + i_first - 1
            R_p = sz_a + i_last - 1
            while L_p <= R_p:
                if L_p % 2 == 1:
                    cand_a.extend(tree_a[L_p])
                    L_p += 1
                if R_p % 2 == 0:
                    cand_a.extend(tree_a[R_p])
                    R_p -= 1
                L_p //= 2
                R_p //= 2

            candidate_i = {i_first, i_last}
            for a_val, i_idx in cand_a:
                candidate_i.add(i_idx)

            for b_len, j_idx in sorted_zeros:
                if i_first <= j_idx <= i_last:
                    candidate_i.add(j_idx)
                if i_first <= j_idx + 1 <= i_last:
                    candidate_i.add(j_idx + 1)

            for i_cand in candidate_i:
                for b_len, j_idx in sorted_zeros:
                    if j_idx != i_cand - 1 and j_idx != i_cand:
                        gain = b_len - a[i_cand]
                        if gain > max_gain:
                            max_gain = gain
                        break

            ans[q_idx] = ONE_COUNT + max_gain

        return ans
