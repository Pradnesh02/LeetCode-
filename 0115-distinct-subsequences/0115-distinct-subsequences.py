class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m, n = len(s), len(t)
        
        # dp[j] stores the number of subsequences of s that form t[:j]
        dp = [0] * (n + 1)
        dp[0] = 1  # Base case: empty t can always be formed once
        
        for char_s in s:
            # Traverse backwards to use values from the previous state
            for j in range(n, 0, -1):
                if char_s == t[j - 1]:
                    dp[j] += dp[j - 1]
                    
        return dp[n]