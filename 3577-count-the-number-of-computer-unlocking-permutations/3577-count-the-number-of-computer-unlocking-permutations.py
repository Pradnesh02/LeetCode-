import math

class Solution(object):
    def countPermutations(self, complexity):
        """
        :type complexity: List[int]
        :rtype: int
        """
        MOD = 10**9 + 7
        n = len(complexity)
        
        # Check if all other computers have strictly greater complexity than computer 0
        root_complexity = complexity[0]
        for i in range(1, n):
            if complexity[i] <= root_complexity:
                return 0
                
        # If all can be unlocked directly by 0, the remaining (n - 1) computers can be in any order
        return math.factorial(n - 1) % MOD