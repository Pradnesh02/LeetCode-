class Solution(object):
    def smallestNumber(self, pattern):
        res = []
        stack = []
        
        for i in range(len(pattern) + 1):
            stack.append(str(i + 1))
            
            # Pop everything when reaching 'I' or the end of the pattern
            if i == len(pattern) or pattern[i] == 'I':
                while stack:
                    res.append(stack.pop())
                    
        return "".join(res)