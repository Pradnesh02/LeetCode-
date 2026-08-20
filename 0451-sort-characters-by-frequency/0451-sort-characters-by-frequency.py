from collections import Counter

class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        counts = Counter(s)
        # Sort characters by frequency descending and reconstruct the string
        return "".join(char * count for char, count in counts.most_common())