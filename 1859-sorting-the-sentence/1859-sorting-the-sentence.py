class Solution(object):
    def sortSentence(self, s):
        words = s.split()
        # Sort based on the last character (the digit)
        words.sort(key=lambda w: int(w[-1]))
        
        # Remove the digit from each word and join with spaces
        return " ".join(w[:-1] for w in words)