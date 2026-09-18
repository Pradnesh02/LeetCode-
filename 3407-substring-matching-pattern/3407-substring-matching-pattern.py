class Solution:
    def hasMatch(self, s: str, p: str) -> bool:
        prefix, suffix = p.split('*')
        
        # Find the earliest occurrence of prefix
        idx = s.find(prefix)
        if idx == -1:
            return False
        
        # Look for suffix in the remaining substring
        return suffix in s[idx + len(prefix):]