class Solution:
    def reverseParentheses(self, s: str) -> str:
        n = len(s)
        stack = []
        pair = [0] * n
        
        # Step 1: Precompute paired brackets
        for i, char in enumerate(s):
            if char == '(':
                stack.append(i)
            elif char == ')':
                j = stack.pop()
                pair[i] = j
                pair[j] = i
                
        # Step 2: Traverse with direction switches
        res = []
        i = 0
        direction = 1
        
        while i < n:
            if s[i] in '()':
                i = pair[i]
                direction = -direction
            else:
                res.append(s[i])
            i += direction
            
        return "".join(res)