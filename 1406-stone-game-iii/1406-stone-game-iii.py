class Solution(object):
    def stoneGameIII(self, stoneValue):
        """
        :type stoneValue: List[int]
        :rtype: str
        """
        n = len(stoneValue)
        # dp[i] represents the maximum score difference (current_player - opponent) 
        # starting from index i to the end of the array.
        dp = [0] * (n + 1)

        # Iterate backwards from the end of the array
        for i in range(n - 1, -1, -1):
            dp[i] = float('-inf')
            take = 0
            
            # The current player can take 1, 2, or 3 stones
            for k in range(1, 4):
                if i + k <= n:
                    take += stoneValue[i + k - 1]
                    # Score gained by taking k stones minus the opponent's max relative score
                    dp[i] = max(dp[i], take - dp[i + k])

        # Evaluate the result based on Alice's score relative to Bob's from index 0
        if dp[0] > 0:
            return "Alice"
        elif dp[0] < 0:
            return "Bob"
        else:
            return "Tie"