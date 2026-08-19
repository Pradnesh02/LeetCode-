class Solution(object):
    def countKeyChanges(self, s):
        """
        :type s: str
        :rtype: int
        """
        s_lower = s.lower()
        changes = 0
        
        for i in range(1, len(s_lower)):
            if s_lower[i] != s_lower[i - 1]:
                changes += 1
                
        return changes