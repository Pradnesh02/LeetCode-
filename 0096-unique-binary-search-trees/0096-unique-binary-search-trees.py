class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        # dp[i] stores the number of unique BSTs with i nodes
        dp = [0] * (n + 1)
        
        # Base cases
        dp[0] = 1
        dp[1] = 1
        
        # Compute dp values from 2 to n
        for length in range(2, n + 1):
            for root in range(1, length + 1):
                left_nodes = root - 1
                right_nodes = length - root
                dp[length] += dp[left_nodes] * dp[right_nodes]
                
        return dp[n]