from typing import List


class Solution:

  def haveConflict(self, event1: List[str], event2: List[str]) -> bool:
    # Since the strings are in "HH:MM" 24-hour format, lexicographical comparison matches chronological order.
    # Two inclusive intervals [start1, end1] and [start2, end2] overlap if:
    # max(start1, start2) <= min(end1, end2)
    return max(event1[0], event2[0]) <= min(event1[1], event2[1])