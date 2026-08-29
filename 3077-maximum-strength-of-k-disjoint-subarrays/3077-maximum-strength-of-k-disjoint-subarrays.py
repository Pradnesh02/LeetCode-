from typing import List


class Solution:

  def maximumStrength(self, nums: List[int], k: int) -> int:
    # dp[j][0]: max strength using j subarrays formed from previous elements (currently closed)
    # dp[j][1]: max strength using j subarrays where the j-th subarray ends at the current element (open)
    NEG_INF = -float("inf")
    dp = [[NEG_INF, NEG_INF] for _ in range(k + 1)]
    dp[0][0] = 0

    for x in nums:
      # Iterate backwards to use dp values from the previous index
      for j in range(k, 0, -1):
        weight = (k - j + 1) if (j % 2 == 1) else -(k - j + 1)

        # Either continue the j-th subarray, or start a new j-th subarray from a previous disjoint state
        prev_best = max(dp[j - 1][0], dp[j - 1][1])
        dp[j][1] = max(dp[j][1], prev_best) + weight * x

        # Update the closed state for j subarrays
        dp[j][0] = max(dp[j][0], dp[j][1])

    return dp[k][0]