from typing import List


class Solution:

  def maxStrength(self, nums: List[int]) -> int:
    if len(nums) == 1:
      return nums[0]

    positives = [x for x in nums if x > 0]
    negatives = [x for x in nums if x < 0]
    zeros = [x for x in nums if x == 0]

    # Sort negatives so the smallest magnitude negative is at the end
    negatives.sort()

    # If the number of negatives is odd, drop the one with the smallest absolute value (largest negative)
    if len(negatives) % 2 != 0:
      negatives.pop()

    # If no positive numbers and no paired negatives exist:
    # 1. If there's at least one zero, max product possible is 0.
    # 2. Otherwise (e.g., a single negative number), return that negative number.
    if not positives and not negatives:
      return 0 if zeros else max(nums)

    product = 1
    for x in positives + negatives:
      product *= x

    return product