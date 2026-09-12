from bisect import bisect_left
from typing import List

class Solution:
    def maximumWeight(self, intervals: List[List[int]]) -> List[int]:
        # Store intervals with original index: (l, r, weight, original_index)
        events = sorted([(l, r, w, i) for i, (l, r, w) in enumerate(intervals)], key=lambda x: x[1])
        n = len(events)
        
        # r-values list for binary search
        rights = [ev[1] for ev in events]
        
        # dp[i][k] = (weight, indices_tuple)
        # Using 1-indexed DP for convenience where index 0 means 0 intervals considered
        dp = [[(0, ()) for _ in range(5)] for _ in range(n + 1)]
        
        def is_better(cand, curr):
            # cand and curr are (weight, indices)
            # We want greater weight; on tie, lexicographically smaller indices
            if cand[0] != curr[0]:
                return cand[0] > curr[0]
            return cand[1] < curr[1]

        for i in range(1, n + 1):
            l, r, w, orig_idx = events[i - 1]
            
            # Find rightmost interval j (1-indexed) such that events[j-1].r < l
            # rights is 0-indexed, so bisect_left(rights, l) gives the count of intervals with r < l
            p = bisect_left(rights, l)
            
            for k in range(5):
                # Option 1: Do not include interval i
                best = dp[i - 1][k]
                
                # Option 2: Include interval i (if k > 0)
                if k > 0:
                    prev_w, prev_indices = dp[p][k - 1]
                    new_indices = tuple(sorted(prev_indices + (orig_idx,)))
                    cand = (prev_w + w, new_indices)
                    if is_better(cand, best):
                        best = cand
                
                dp[i][k] = best

        # Find the overall best among choices of 1, 2, 3, or 4 intervals
        ans = (0, ())
        for k in range(1, 5):
            if is_better(dp[n][k], ans):
                ans = dp[n][k]
                
        return list(ans[1])