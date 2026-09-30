class Solution:

  def palindromePairs(self, words: list[str]) -> list[list[int]]:
    word_map = {word: i for i, word in enumerate(words)}
    pairs = []

    def is_palindrome(s: str) -> bool:
      return s == s[::-1]

    for i, word in enumerate(words):
      n = len(word)
      for j in range(n + 1):
        prefix = word[:j]
        suffix = word[j:]

        # Case 1: If prefix is a palindrome, reversed suffix + word forms a palindrome
        if is_palindrome(prefix):
          rev_suffix = suffix[::-1]
          if rev_suffix in word_map and word_map[rev_suffix] != i:
            pairs.append([word_map[rev_suffix], i])

        # Case 2: If suffix is a palindrome, word + reversed prefix forms a palindrome
        # j != n prevents duplicate entries when prefix == word (already checked when j == 0)
        if j != n and is_palindrome(suffix):
          rev_prefix = prefix[::-1]
          if rev_prefix in word_map and word_map[rev_prefix] != i:
            pairs.append([i, word_map[rev_prefix]])

    return pairs