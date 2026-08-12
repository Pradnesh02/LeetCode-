from collections import Counter
import bisect

class Solution(object):
    def maximumTotalDamage(self, power):
        """
        :type power: List[int]
        :rtype: int
        """
        counts = Counter(power)
        unique_powers = sorted(counts.keys())
        n = len(unique_powers)
        
        dp = [0] * n
        
        for i in range(n):
            v = unique_powers[i]
            current_damage = v * counts[v]
            
            # Find the rightmost unique power that is strictly less than (v - 2)
            j = bisect.bisect_right(unique_powers, v - 3) - 1
            
            if j >= 0:
                current_damage += dp[j]
                
            # Option 1: Don't take unique_powers[i] -> dp[i-1]
            # Option 2: Take unique_powers[i] -> current_damage
            prev_max = dp[i - 1] if i > 0 else 0
            dp[i] = max(prev_max, current_damage)
            
        return dp[-1]