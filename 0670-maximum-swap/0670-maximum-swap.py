class Solution:

  def maximumSwap(self, num: int) -> int:
    digits = list(str(num))

    # Store the last seen index for each digit (0-9)
    last = {int(d): i for i, d in enumerate(digits)}

    # Traverse digits from left to right
    for i, d in enumerate(digits):
      # Look for a larger digit (from 9 down to current digit + 1) that appears after index i
      for larger_d in range(9, int(d), -1):
        if larger_d in last and last[larger_d] > i:
          # Swap and return immediately
          j = last[larger_d]
          digits[i], digits[j] = digits[j], digits[i]
          return int("".join(digits))

    return num