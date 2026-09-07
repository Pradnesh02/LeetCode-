import math
from typing import List


class Solution:

  def minOperations(self, nums: List[int]) -> int:
    n = len(nums)
    count_ones = nums.count(1)

    # Case 1: If there are already 1s in the array
    if count_ones > 0:
      return n - count_ones

    # Case 2: Find the shortest subarray with gcd == 1
    min_len = float("inf")

    for i in range(n):
      current_gcd = nums[i]
      for j in range(i, n):
        current_gcd = math.gcd(current_gcd, nums[j])
        if current_gcd == 1:
          min_len = min(min_len, j - i + 1)
          break  # Subarrays starting at i won't get any shorter

    if min_len == float("inf"):
      return -1

    return (min_len - 1) + (n - 1)