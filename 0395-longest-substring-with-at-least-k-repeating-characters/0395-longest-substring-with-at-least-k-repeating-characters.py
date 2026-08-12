from collections import Counter

class Solution(object):
    def longestSubstring(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        if len(s) < k:
            return 0
            
        counts = Counter(s)
        
        for char, count in counts.items():
            if count < k:
                # Split s on the invalid character and recurse on all parts
                return max(self.longestSubstring(sub, k) for sub in s.split(char))
                
        # If no character has a frequency less than k, the entire string is valid
        return len(s)