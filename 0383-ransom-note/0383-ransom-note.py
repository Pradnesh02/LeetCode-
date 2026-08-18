from collections import Counter

class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        # If magazine has fewer characters, it's impossible
        if len(ransomNote) > len(magazine):
            return False
            
        mag_counts = Counter(magazine)
        
        for ch in ransomNote:
            if mag_counts[ch] <= 0:
                return False
            mag_counts[ch] -= 1
            
        return True