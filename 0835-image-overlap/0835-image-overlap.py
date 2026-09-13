from collections import defaultdict
from typing import List


class Solution:

  def largestOverlap(
      self, img1: List[List[int]], img2: List[List[int]]
  ) -> int:
    n = len(img1)

    # Collect coordinates where value is 1
    ones1 = [
        (r, c) for r in range(n) for c in range(n) if img1[r][c] == 1
    ]
    ones2 = [
        (r, c) for r in range(n) for c in range(n) if img2[r][c] == 1
    ]

    # Count how many pairs share the same translation vector (dr, dc)
    count = defaultdict(int)
    for r1, c1 in ones1:
      for r2, c2 in ones2:
        vector = (r2 - r1, c2 - c1)
        count[vector] += 1

    return max(count.values(), default=0)