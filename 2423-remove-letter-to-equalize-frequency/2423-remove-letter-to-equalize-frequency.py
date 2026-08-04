from collections import Counter

class Solution(object):
    def equalFrequency(self, word):
        """
        :type word: str
        :rtype: bool
        """
        for i in range(len(word)):
            # Remove character at index i
            modified_word = word[:i] + word[i+1:]
            
            # Get frequency counts of remaining characters
            counts = Counter(modified_word).values()
            
            # Check if all remaining characters have the exact same frequency
            if len(set(counts)) == 1:
                return True
                
        return False