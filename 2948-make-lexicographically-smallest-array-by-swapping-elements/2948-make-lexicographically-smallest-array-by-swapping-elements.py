from collections import deque
from typing import List


class Solution:

  def lexicographicallySmallestArray(
      self, nums: List[int], limit: int
  ) -> List[int]:
    # Sort a copy of the array to find connected components based on the limit
    sorted_nums = sorted(nums)

    groups = []  # List of deques, where each deque holds sorted elements of a group
    num_to_group = {}  # Maps each number to its group index

    for num in sorted_nums:
      # If this is the first element or the difference with the previous group's
      # largest element exceeds limit, start a new group
      if not groups or num - groups[-1][-1] > limit:
        groups.append(deque())

      # Add the number to the current group
      groups[-1].append(num)
      num_to_group[num] = len(groups) - 1

    # Reconstruct the answer by taking the smallest available element from each number's group
    result = []
    for num in nums:
      group_idx = num_to_group[num]
      result.append(groups[group_idx].popleft())

    return result