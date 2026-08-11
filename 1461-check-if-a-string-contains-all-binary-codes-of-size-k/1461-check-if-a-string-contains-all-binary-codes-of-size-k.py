class Solution(object):
    def hasAllCodes(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: bool
        """
        target = 1 << k  # Total unique codes of length k (2^k)
        seen = set()
        
        for i in range(len(s) - k + 1):
            seen.add(s[i:i + k])
            if len(seen) == target:
                return True
                
        return len(seen) == target