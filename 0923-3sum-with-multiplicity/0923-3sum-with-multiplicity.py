from collections import Counter
from typing import List


class Solution:

  def threeSumMulti(self, arr: List[int], target: int) -> int:
    MOD = 10**9 + 7
    count = Counter(arr)
    keys = sorted(count.keys())
    ans = 0

    for i, x in enumerate(keys):
      # Case 3: All three values are the same (x == y == z)
      if 3 * x == target:
        ans += count[x] * (count[x] - 1) * (count[x] - 2) // 6

      for j in range(i, len(keys)):
        y = keys[j]
        z = target - x - y

        if z < y:
          break

        if z not in count:
          continue

        if x == y and y < z:
          # Case 2a: Two values are equal (x == y < z)
          ans += (count[x] * (count[x] - 1) // 2) * count[z]
        elif x < y and y == z:
          # Case 2b: Two values are equal (x < y == z)
          ans += count[x] * (count[y] * (count[y] - 1) // 2)
        elif x < y and y < z:
          # Case 1: All three values are distinct (x < y < z)
          ans += count[x] * count[y] * count[z]

    return ans % MOD