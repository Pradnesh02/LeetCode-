class Solution(object):
    def countPalindromicSubsequences(self, s):
        """
        :type s: str
        :rtype: int
        """
        MOD = 10**9 + 7
        n = len(s)
        dp = [[0] * n for _ in range(n)]
        
        for i in range(n):
            dp[i][i] = 1
            
        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                
                if s[i] != s[j]:
                    dp[i][j] = (dp[i + 1][j] + dp[i][j - 1] - dp[i + 1][j - 1]) % MOD
                else:
                    low = i + 1
                    high = j - 1
                    
                    while low <= high and s[low] != s[i]:
                        low += 1
                    while low <= high and s[high] != s[i]:
                        high -= 1
                        
                    if low > high:
                        # No identical character in s[i+1...j-1]
                        dp[i][j] = (2 * dp[i + 1][j - 1] + 2) % MOD
                    elif low == high:
                        # Exactly one identical character in s[i+1...j-1]
                        dp[i][j] = (2 * dp[i + 1][j - 1] + 1) % MOD
                    else:
                        # Two or more identical characters in s[i+1...j-1]
                        dp[i][j] = (2 * dp[i + 1][j - 1] - dp[low + 1][high - 1]) % MOD
                        
        return (dp[0][n - 1] + MOD) % MOD