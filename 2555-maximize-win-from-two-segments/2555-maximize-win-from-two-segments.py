from typing import List

class Solution:
    def maximizeWin(self, prizePositions: List[int], k: int) -> int:
        n = len(prizePositions)
        
        # If two segments of length k can cover the entire range, return n
        if 2 * k + 1 >= prizePositions[-1] - prizePositions[0]:
            return n

        # dp[i] represents the maximum prizes covered by 1 segment using prizePositions[:i]
        dp = [0] * (n + 1)
        max_prizes = 0
        left = 0

        for right in range(n):
            # Maintain sliding window where the segment length is at most k
            while prizePositions[right] - prizePositions[left] > k:
                left += 1

            # Number of prizes covered by a segment ending at prizePositions[right]
            current_count = right - left + 1

            # Combine current segment with the best non-overlapping previous segment
            max_prizes = max(max_prizes, current_count + dp[left])

            # Update dp[right + 1] for future lookups
            dp[right + 1] = max(dp[right], current_count)

        return max_prizes