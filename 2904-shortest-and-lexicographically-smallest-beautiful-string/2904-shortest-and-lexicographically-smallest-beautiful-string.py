class Solution(object):

  def shortestBeautifulSubstring(self, s, k):
    """
    :type s: str
    :type k: int
    :rtype: str
    """
    # Collect indices of all '1's
    ones = [i for i, ch in enumerate(s) if ch == "1"]

    # If there are fewer than k '1's, no beautiful substring exists
    if len(ones) < k:
      return ""

    min_len = float("inf")
    result = ""

    # Check every window of k consecutive '1's
    for i in range(len(ones) - k + 1):
      start = ones[i]
      end = ones[i + k - 1]
      sub = s[start : end + 1]
      curr_len = len(sub)

      if curr_len < min_len:
        min_len = curr_len
        result = sub
      elif curr_len == min_len:
        result = min(result, sub)

    return result