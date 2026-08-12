class Solution(object):
    def partitionString(self, s):
        """
        :type s: str
        :rtype: int
        """
        seen = set()
        count = 1  # At least 1 substring is needed
        
        for char in s:
            if char in seen:
                count += 1
                seen = set()  # Reset set for the new substring
            seen.add(char)
            
        return count