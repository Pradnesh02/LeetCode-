class Solution:

  def reverseParentheses(self, s: str) -> str:
    n = len(s)
    pair = {}
    stack = []

    # Precompute matching bracket pairs (wormhole teleportation)
    for i, char in enumerate(s):
      if char == '(':
        stack.append(i)
      elif char == ')':
        j = stack.pop()
        pair[i] = j
        pair[j] = i

    result = []
    curr = 0
    step = 1  # 1 for forward, -1 for backward

    # Traverse characters by jumping through matching brackets
    while curr < n:
      if s[curr] in ('(', ')'):
        curr = pair[curr]
        step = -step
      else:
        result.append(s[curr])
      curr += step

    return ''.join(result)