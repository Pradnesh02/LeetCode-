from collections import Counter

class Solution(object):
    def minimumPushes(self, word):
        """
        :type word: str
        :rtype: int
        """
        # Count frequency of each character in word
        counts = Counter(word)
        
        # Sort frequencies in descending order
        freqs = sorted(counts.values(), reverse=True)
        
        ans = 0
        
        # Assign the most frequent characters to key presses first
        for i, count in enumerate(freqs):
            ans += count * ((i // 8) + 1)
            
        return ans