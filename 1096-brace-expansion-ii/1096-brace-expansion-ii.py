class Solution:

  def braceExpansionII(self, expression: str) -> list[str]:
    stack = []
    # Current group of elements being combined via union
    # In each scope, elements are maintained as a list of sets where:
    # - comma (',') starts a new term in the union
    # - concatenation ('') does Cartesian product with the preceding term
    curr_group = [set()]

    for char in expression:
      if char == '{':
        stack.append(curr_group)
        curr_group = [set()]
      elif char == '}':
        # Union all terms accumulated in the current scope
        resolved = set.union(*curr_group)
        curr_group = stack.pop()
        # Concatenate resolved group with the last term in the parent scope
        if not curr_group[-1]:
          curr_group[-1] = resolved
        else:
          curr_group[-1] = {
              a + b for a in curr_group[-1] for b in resolved
          }
      elif char == ',':
        # Start a new union branch in the current scope
        curr_group.append(set())
      else:
        # Lowercase character
        if not curr_group[-1]:
          curr_group[-1] = {char}
        else:
          curr_group[-1] = {a + char for a in curr_group[-1]}

    # Union all branches in the outer group and return in sorted order
    return sorted(list(set.union(*curr_group)))