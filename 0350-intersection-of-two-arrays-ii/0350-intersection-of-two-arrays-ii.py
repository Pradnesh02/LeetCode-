from collections import Counter


class Solution:

  def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
    # Count frequencies of the smaller array to optimize auxiliary space
    if len(nums1) > len(nums2):
      nums1, nums2 = nums2, nums1

    counts = Counter(nums1)
    result = []

    for num in nums2:
      if counts[num] > 0:
        result.append(num)
        counts[num] -= 1

    return result