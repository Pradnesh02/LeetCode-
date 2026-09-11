from collections import Counter
from typing import List


class Solution:

  def findEvenNumbers(self, digits: List[int]) -> List[int]:
    count = Counter(digits)
    result = []

    # Iterate through all 3-digit even numbers in ascending order
    for num in range(100, 1000, 2):
      d1 = num // 100
      d2 = (num // 10) % 10
      d3 = num % 10

      needed = Counter([d1, d2, d3])

      # Verify if digits has enough copies of each required digit
      if all(count[d] >= needed[d] for d in needed):
        result.append(num)

    return result