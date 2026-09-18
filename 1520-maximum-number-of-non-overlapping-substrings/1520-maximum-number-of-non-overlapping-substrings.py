class Solution:
    def maxNumOfSubstrings(self, s: str) -> list[str]:
        # 1. Record the first and last occurrence of each character
        first = {}
        last = {}
        for i, ch in enumerate(s):
            if ch not in first:
                first[ch] = i
            last[ch] = i

        # 2. Find valid minimal intervals starting at each character's first index
        intervals = []
        for ch in first:
            l = first[ch]
            r = last[ch]
            valid = True

            k = l
            while k <= r:
                c = s[k]
                if first[c] < l:
                    valid = False
                    break
                r = max(r, last[c])
                k += 1

            if valid:
                intervals.append((l, r))

        # 3. Sort intervals by end index (greedy interval scheduling)
        intervals.sort(key=lambda x: x[1])

        # 4. Greedily pick non-overlapping intervals
        res = []
        prev_end = -1
        for l, r in intervals:
            if l > prev_end:
                res.append(s[l : r + 1])
                prev_end = r

        return res