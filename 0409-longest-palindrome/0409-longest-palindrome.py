from collections import Counter


class Solution:

  def longestPalindrome(self, s: str) -> int:
    counts = Counter(s)
    length = 0
    has_odd = False

    for freq in counts.values():
      if freq % 2 == 0:
        length += freq
      else:
        length += freq - 1
        has_odd = True

    # If any character has an odd frequency, one can sit in the center
    return length + 1 if has_odd else length