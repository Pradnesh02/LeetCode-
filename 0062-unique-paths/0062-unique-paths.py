import math

class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        # C(m + n - 2, m - 1) using factorial
        N = m + n - 2
        k = m - 1
        return math.factorial(N) // (math.factorial(k) * math.factorial(N - k))