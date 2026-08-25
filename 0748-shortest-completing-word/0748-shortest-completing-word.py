from collections import Counter

class Solution(object):
    def shortestCompletingWord(self, licensePlate, words):
        """
        :type licensePlate: str
        :type words: List[str]
        :rtype: str
        """
        # Count only alphabetic characters, converted to lowercase
        target_counts = Counter(ch.lower() for ch in licensePlate if ch.isalpha())
        
        best_word = None
        
        for word in words:
            word_counts = Counter(word)
            
            # Check if current word contains at least the required count of each letter
            if all(word_counts[ch] >= count for ch, count in target_counts.items()):
                if best_word is None or len(word) < len(best_word):
                    best_word = word
                    
        return best_word