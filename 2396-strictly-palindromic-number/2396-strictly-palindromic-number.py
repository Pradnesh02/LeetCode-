class Solution(object):
    def isStrictlyPalindromic(self, n):
        """
        :type n: int
        :rtype: bool
        """
        # It is mathematically impossible for any integer n >= 4 
        # to be strictly palindromic.
        return False