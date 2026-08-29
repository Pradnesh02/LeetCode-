from typing import List


class Solution:

  def partitionDisjoint(self, nums: List[int]) -> int:
    # left_max tracks the maximum value in the current left partition
    left_max = nums[0]
    # max_so_far tracks the maximum value seen in the array up to the current index
    max_so_far = nums[0]
    # partition_idx marks the ending index of the left partition
    partition_idx = 0

    for i in range(1, len(nums)):
      max_so_far = max(max_so_far, nums[i])

      # If an element is strictly smaller than left_max, it must be included in the left partition
      if nums[i] < left_max:
        left_max = max_so_far
        partition_idx = i

    # The length of the left partition is the last index + 1
    return partition_idx + 1