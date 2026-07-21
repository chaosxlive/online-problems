class Solution:

    def maxActiveSectionsAfterTrade(self, s: str) -> int:
        counts = []
        curr_ch = '0'
        curr_count = 0
        for i in range(len(s)):
            if s[i] == curr_ch:
                curr_count += 1
            else:
                counts.append(curr_count)
                curr_ch = s[i]
                curr_count = 1
        counts.append(curr_count)

        max_flip = 0
        len_of_counts = len(counts)
        active_count = 0
        for i in range(1, len_of_counts, 2):
            active_count += counts[i]
            if counts[i - 1] == 0 or i + 1 >= len_of_counts:
                continue
            max_flip = max(max_flip, counts[i - 1] + counts[i + 1])
        return active_count + max_flip
