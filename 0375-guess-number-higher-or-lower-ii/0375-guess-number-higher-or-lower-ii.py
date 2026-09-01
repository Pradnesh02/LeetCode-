from functools import lru_cache

class Solution:
    def getMoneyAmount(self, n: int) -> int:
        @lru_cache(None)
        def dp(i: int, j: int) -> int:
            if i >= j:
                return 0
            if i + 1 == j:
                return i
            
            min_cost = float('inf')
            # Optimization: The best guess k is usually in the upper half of [i, j]
            for k in range(i + (j - i) // 2, j):
                cost = k + max(dp(i, k - 1), dp(k + 1, j))
                min_cost = min(min_cost, cost)
                
            return min_cost

        return dp(1, n)