class Solution(object):
    def stoneGameII(self, piles):
        """
        :type piles: List[int]
        :rtype: int
        """
        n = len(piles)
        
        # Suffix sums array to get total remaining stones from index i in O(1) time
        suffix_sum = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            suffix_sum[i] = suffix_sum[i + 1] + piles[i]
            
        memo = {}
        
        def dp(i, M):
            # Base case: if remaining piles can all be taken, take all of them
            if i + 2 * M >= n:
                return suffix_sum[i]
            
            if (i, M) in memo:
                return memo[(i, M)]
            
            max_stones = 0
            
            # The player can take X piles where 1 <= X <= 2 * M
            for X in range(1, 2 * M + 1):
                # Total remaining stones minus the opponent's best possible score from the next state
                opponent_score = dp(i + X, max(M, X))
                current_score = suffix_sum[i] - opponent_score
                max_stones = max(max_stones, current_score)
                
            memo[(i, M)] = max_stones
            return max_stones

        # Alice starts at index 0 with M = 1
        return dp(0, 1)