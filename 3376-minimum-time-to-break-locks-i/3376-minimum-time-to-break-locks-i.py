import math
from typing import List


class Solution:

  def findMinimumTime(self, strength: List[int], k: int) -> int:
    n = len(strength)

    # memo[mask] stores the minimum time to break the subset of locks represented by mask
    memo = {}

    def dp(mask: int) -> int:
      if mask == (1 << n) - 1:
        return 0
      if mask in memo:
        return memo[mask]

      # Number of locks broken so far is the number of set bits in mask
      locks_broken = bin(mask).count("1")
      x = 1 + locks_broken * k

      res = float("inf")
      for i in range(n):
        if not (mask & (1 << i)):
          # Time to break lock i with current rate x
          time_needed = (strength[i] + x - 1) // x
          res = min(res, time_needed + dp(mask | (1 << i)))

      memo[mask] = res
      return res

    return dp(0)