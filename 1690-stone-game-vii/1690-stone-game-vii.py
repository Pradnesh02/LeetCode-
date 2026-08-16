class Solution(object):
    def stoneGameVII(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        n = len(stones)
        
        # Prefix sum array to compute subarray sums in O(1)
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + stones[i]
            
        def get_sum(i, j):
            return prefix[j + 1] - prefix[i]

        # dp[i] will represent dp[i][j] for the current length
        dp = [0] * n

        # Iterate over length of subarray from 2 to n
        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                
                # Option 1: remove stones[i] -> gain sum(i+1, j) - dp[i+1][j]
                take_left = get_sum(i + 1, j) - dp[i + 1]
                # Option 2: remove stones[j] -> gain sum(i, j-1) - dp[i][j-1]
                take_right = get_sum(i, j - 1) - dp[i]
                
                dp[i] = max(take_left, take_right)

        return dp[0]