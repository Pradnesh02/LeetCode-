import heapq
from typing import List


class Solution:

  def minGroups(self, intervals: List[List[int]]) -> int:
    # Sort intervals primarily by start time
    intervals.sort(key=lambda x: x[0])

    # Min-heap to store the end times of each group
    pq = []

    for left, right in intervals:
      # If the earliest ending group ends before current start, reuse it
      if pq and pq[0] < left:
        heapq.heappop(pq)
      # Push the current interval's end time
      heapq.heappush(pq, right)

    # The size of the heap is the minimum number of groups required
    return len(pq)