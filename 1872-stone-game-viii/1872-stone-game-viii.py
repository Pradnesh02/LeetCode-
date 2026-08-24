class Solution(object):
    def stoneGameVIII(self, stones):
        # Compute prefix sums
        pref = [0] * len(stones)
        pref[0] = stones[0]
        for i in range(1, len(stones)):
            pref[i] = pref[i - 1] + stones[i]
        
        # Base case
        dp = pref[-1]
        
        # Iterate backward from n - 2 down to 1
        for i in range(len(stones) - 2, 0, -1):
            dp = max(dp, pref[i] - dp)
            
        return dp