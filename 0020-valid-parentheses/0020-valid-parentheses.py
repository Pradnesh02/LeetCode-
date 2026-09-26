class Solution:

  def isValid(self, s: str) -> bool:
    stack = []
    mapping = {")": "(", "}": "{", "]": "["}

    for char in s:
      if char in mapping:
        # Pop the topmost element if stack is non-empty, otherwise assign a dummy value
        top_element = stack.pop() if stack else "#"
        if mapping[char] != top_element:
          return False
      else:
        # It's an opening bracket, push onto the stack
        stack.append(char)

    # If the stack is empty, all opening brackets were properly closed
    return not stack