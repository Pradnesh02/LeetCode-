class Solution(object):
    def clumsy(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1
        if n == 2:
            return 2
        if n == 3:
            return 6
        if n == 4:
            return 7
            
        rem = n % 4
        if rem == 0:
            return n + 1
        elif rem == 1:
            return n + 2
        elif rem == 2:
            return n + 2
        else: # rem == 3
            return n - 1