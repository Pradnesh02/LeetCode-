class Solution:

  def generateParenthesis(self, n: int) -> list[str]:
    result = []

    def backtrack(current: list[str], open_count: int, close_count: int):
      # Base case: valid string of length 2 * n formed
      if len(current) == 2 * n:
        result.append("".join(current))
        return

      # Can add an opening parenthesis if we haven't used all n
      if open_count < n:
        current.append("(")
        backtrack(current, open_count + 1, close_count)
        current.pop()

      # Can add a closing parenthesis only if it doesn't exceed open parentheses
      if close_count < open_count:
        current.append(")")
        backtrack(current, open_count, close_count + 1)
        current.pop()

    backtrack([], 0, 0)
    return result