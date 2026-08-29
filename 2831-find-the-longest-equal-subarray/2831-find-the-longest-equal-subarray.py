from collections import defaultdict
from typing import List


class Solution:

  def longestEqualSubarray(self, nums: List[int], k: int) -> int:
    # Group indices by their values
    pos_map = defaultdict(list)
    for idx, num in enumerate(nums):
      pos_map[num].append(idx)

    max_len = 0

    # For each number, use a sliding window over its list of original indices
    for positions in pos_map.values():
      left = 0
      for right in range(len(positions)):
        # Number of deletions needed between positions[left] and positions[right]:
        # (total elements in between) - (count of target element)
        while (
            positions[right] - positions[left] + 1 - (right - left + 1)
        ) > k:
          left += 1

        max_len = max(max_len, right - left + 1)

    return max_len