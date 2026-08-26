from collections import Counter

class Solution:
    def findValidPair(self, s: str) -> str:
        freq = Counter(s)
        
        # Traverse adjacent pairs from left to right
        for i in range(len(s) - 1):
            a, b = s[i], s[i + 1]
            
            # Check distinct digits and exact frequency matches
            if a != b and freq[a] == int(a) and freq[b] == int(b):
                return s[i:i + 2]
                
        return ""