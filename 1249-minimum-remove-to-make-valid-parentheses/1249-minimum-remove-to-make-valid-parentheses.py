class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        # Indices of parentheses that need to be removed
        to_remove = set()
        stack = []  # Stores indices of unmatched '('

        for i, char in enumerate(s):
            if char == '(':
                stack.append(i)
            elif char == ')':
                if stack:
                    stack.pop()
                else:
                    # Unmatched ')'
                    to_remove.add(i)

        # Any remaining '(' in the stack are unmatched
        to_remove.update(stack)

        # Reconstruct the string omitting the marked indices
        return "".join(char for i, char in enumerate(s) if i not in to_remove)