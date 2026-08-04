from collections import Counter

class Solution(object):
    def minDeletions(self, s):
        """
        :type s: str
        :rtype: int
        """
        freq_map = Counter(s)
        seen_freq = set()
        deletions = 0
        
        for freq in freq_map.values():
            # Decrement frequency until it becomes unique or reaches 0
            while freq > 0 and freq in seen_freq:
                freq -= 1
                deletions += 1
            
            if freq > 0:
                seen_freq.add(freq)
                
        return deletions