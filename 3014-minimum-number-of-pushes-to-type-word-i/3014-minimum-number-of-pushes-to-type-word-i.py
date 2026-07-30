class Solution(object):
    def minimumPushes(self, word):
        """
        :type word: str
        :rtype: int
        """
        n = len(word)
        ans = 0
        
        # We have 8 available keys (2 through 9).
        # The first 8 distinct letters require 1 push each.
        # The next 8 distinct letters require 2 pushes each.
        # The next 8 require 3 pushes each, and so on.
        
        for i in range(n):
            ans += (i // 8) + 1
            
        return ans