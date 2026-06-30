class Solution:

    def numberOfSubstrings(self, s: str) -> int:
        last_a_index = -1
        last_b_index = -1
        last_c_index = -1

        count = 0

        for i, c in enumerate(s):
            if c == 'a':
                last_a_index = i
            elif c == 'b':
                last_b_index = i
            else:
                last_c_index = i

            if last_a_index != -1 and last_b_index != -1 and last_c_index != -1:
                count += min(last_a_index, last_b_index, last_c_index) + 1

        return count
