class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = [-1]
        max_len = 0

        for i, char in enumerate(s):
            if char == '(':
                stack.append(i)
            else:
                stack.pop()
                if not stack:
                    # If stack becomes empty, record current index as new boundary
                    stack.append(i)
                else:
                    # Current valid substring length is current index minus last unmatched index
                    max_len = max(max_len, i - stack[-1])

        return max_len