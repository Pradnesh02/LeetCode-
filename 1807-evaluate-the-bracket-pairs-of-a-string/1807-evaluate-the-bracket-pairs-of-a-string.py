class Solution:

  def evaluate(self, s: str, knowledge: list[list[str]]) -> str:
    # Convert knowledge into a hash map for O(1) key lookups
    know_dict = {k: v for k, v in knowledge}

    result = []
    curr_key = []
    in_bracket = False

    for char in s:
      if char == "(":
        in_bracket = True
      elif char == ")":
        in_bracket = False
        key = "".join(curr_key)
        # Substitute key with knowledge value if present, else '?'
        result.append(know_dict.get(key, "?"))
        curr_key = []
      elif in_bracket:
        curr_key.append(char)
      else:
        result.append(char)

    return "".join(result)