from collections import Counter

class Solution(object):
    def similarPairs(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        # Convert each word to a frozenset of its unique characters to group identical sets
        counts = Counter(frozenset(w) for w in words)
        
        # For each unique set with count c, number of pairs is c * (c - 1) // 2
        return sum(c * (c - 1) // 2 for c in counts.values())