from collections import Counter
from fractions import gcd

class Solution(object):
    def countPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        gcd_counts = Counter(gcd(num, k) for num in nums)
        unique_gcds = list(gcd_counts.keys())
        
        total_pairs = 0
        m = len(unique_gcds)
        
        for i in range(m):
            g1 = unique_gcds[i]
            # Pairs with the same GCD value
            if (g1 * g1) % k == 0:
                total_pairs += gcd_counts[g1] * (gcd_counts[g1] - 1) // 2
                
            # Pairs with different GCD values
            for j in range(i + 1, m):
                g2 = unique_gcds[j]
                if (g1 * g2) % k == 0:
                    total_pairs += gcd_counts[g1] * gcd_counts[g2]
                    
        return total_pairs