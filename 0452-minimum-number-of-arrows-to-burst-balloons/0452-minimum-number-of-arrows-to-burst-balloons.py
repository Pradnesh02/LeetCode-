from typing import List


class Solution:

  def findMinArrowShots(self, points: List[List[int]]) -> int:
    if not points:
      return 0

    # Sort balloons by their ending coordinates
    points.sort(key=lambda x: x[1])

    arrows = 1
    arrow_pos = points[0][1]

    # Greedily shoot arrows at the earliest finishing balloon's end point
    for start, end in points[1:]:
      if start > arrow_pos:
        # A new arrow is required because the current balloon starts after the last arrow position
        arrows += 1
        arrow_pos = end

    return arrows