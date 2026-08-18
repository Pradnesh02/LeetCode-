from collections import Counter

class Solution(object):
    def rearrangeCharacters(self, s, target):
        """
        :type s: str
        :type target: str
        :rtype: int
        """
        count_s = Counter(s)
        count_target = Counter(target)
        
        return min(count_s[c] // count_target[c] for c in count_target)