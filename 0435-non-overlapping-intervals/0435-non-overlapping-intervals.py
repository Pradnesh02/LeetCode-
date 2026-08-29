from typing import List


class Solution:

  def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
    if not intervals:
      return 0

    # Sort intervals primarily by their end time
    intervals.sort(key=lambda x: x[1])

    removals = 0
    last_end = intervals[0][1]

    # Greedily keep the interval that finishes earliest
    for i in range(1, len(intervals)):
      start, end = intervals[i]
      if start < last_end:
        # Overlap detected, remove the current interval
        removals += 1
      else:
        # No overlap, update the boundary of the last accepted interval
        last_end = end

    return removals