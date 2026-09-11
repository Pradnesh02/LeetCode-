from collections import Counter
from typing import List


class Solution:

  def totalNumbers(self, digits: List[int]) -> int:
    digit_counts = Counter(digits)
    ans = 0

    # Iterate over all possible 3-digit even numbers (100 to 998)
    for num in range(100, 1000, 2):
      d1 = num // 100
      d2 = (num // 10) % 10
      d3 = num % 10

      needed = Counter([d1, d2, d3])

      # Check if available digits satisfy the required count
      if all(digit_counts[d] >= needed[d] for d in needed):
        ans += 1

    return ans