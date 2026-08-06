class Solution(object):
    def longestPalindromeSubseq(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        # dp[i][j] stores the length of LPS for substring s[i..j]
        dp = [[0] * n for _ in range(n)]
        
        # Base case: single character palindromes
        for i in range(n):
            dp[i][i] = 1
            
        # Traverse backwards for 'i' and forwards for 'j'
        for i in range(n - 1, -1, -1):
            for j in range(i + 1, n):
                if s[i] == s[j]:
                    dp[i][j] = dp[i + 1][j - 1] + 2
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])
                    
        return dp[0][n - 1]