class Solution(object):
    def canCross(self, stones):
        """
        :type stones: List[int]
        :rtype: bool
        """
        # First jump must be 1 unit from stones[0] (0) to stones[1] (1)
        if len(stones) < 2 or stones[1] != 1:
            return False
        
        # Map each stone position to a set of jump sizes that reached it
        dp = {stone: set() for stone in stones}
        dp[0].add(0)
        
        for stone in stones:
            for k in dp[stone]:
                for step in (k - 1, k, k + 1):
                    if step > 0 and (stone + step) in dp:
                        dp[stone + step].add(step)
                        
        return len(dp[stones[-1]]) > 0