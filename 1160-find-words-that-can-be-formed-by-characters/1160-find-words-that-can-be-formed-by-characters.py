from collections import Counter

class Solution(object):
    def countCharacters(self, words, chars):
        """
        :type words: List[str]
        :type chars: str
        :rtype: int
        """
        chars_count = Counter(chars)
        total_length = 0
        
        for word in words:
            word_count = Counter(word)
            # Check if all characters in the word are covered by chars
            if all(word_count[ch] <= chars_count[ch] for ch in word_count):
                total_length += len(word)
                
        return total_length