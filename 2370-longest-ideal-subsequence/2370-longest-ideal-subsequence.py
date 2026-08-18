class Solution(object):
    def longestIdealString(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        dp = [0] * 26
        
        for ch in s:
            idx = ord(ch) - ord('a')
            
            left = max(0, idx - k)
            right = min(25, idx + k)
            
            best_prev = max(dp[left:right + 1])
            dp[idx] = best_prev + 1
            
        return max(dp)