from collections import Counter
from typing import List


class Solution:

  def minimumIndex(self, nums: List[int]) -> int:
    n = len(nums)

    # Step 1: Find the dominant element of the entire array
    counts = Counter(nums)
    dominant_elem = -1
    total_dom_count = 0

    for elem, count in counts.items():
      if count * 2 > n:
        dominant_elem = elem
        total_dom_count = count
        break

    # Step 2: Iterate to find the smallest valid split index
    left_dom_count = 0
    for i in range(n - 1):
      if nums[i] == dominant_elem:
        left_dom_count += 1

      left_len = i + 1
      right_len = n - left_len
      right_dom_count = total_dom_count - left_dom_count

      # Check dominance condition for both subarrays
      if left_dom_count * 2 > left_len and right_dom_count * 2 > right_len:
        return i

    return -1