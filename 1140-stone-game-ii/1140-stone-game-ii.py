from functools import lru_cache
from typing import List

class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        n = len(piles)
        
        # Precompute suffix sums
        suffix_sum = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            suffix_sum[i] = suffix_sum[i + 1] + piles[i]
            
        @lru_cache(None)
        def dp(i: int, m: int) -> int:
            # If all remaining piles can be taken in one turn
            if i + 2 * m >= n:
                return suffix_sum[i]
            
            max_stones = 0
            for x in range(1, 2 * m + 1):
                # Total remaining stones minus what the next player gets optimally
                current_take = suffix_sum[i] - dp(i + x, max(m, x))
                max_stones = max(max_stones, current_take)
                
            return max_stones
        
        return dp(0, 1)