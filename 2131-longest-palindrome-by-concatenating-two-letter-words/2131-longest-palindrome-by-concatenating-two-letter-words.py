from collections import Counter


class Solution:

  def longestPalindrome(self, words: list[str]) -> int:
    count = Counter(words)
    length = 0
    has_central = False

    for word, freq in count.items():
      # Case 1: Word consists of two identical letters (e.g., 'aa', 'gg')
      if word[0] == word[1]:
        if freq % 2 == 0:
          length += freq * 2
        else:
          length += (freq - 1) * 2
          has_central = True
      # Case 2: Word consists of different letters (e.g., 'lc' and 'cl')
      elif word < word[::-1]:  # Ensure each pair is processed once
        rev = word[::-1]
        if rev in count:
          length += min(freq, count[rev]) * 4

    # If any symmetric word had an odd count, one instance can sit at the center
    if has_central:
      length += 2

    return length