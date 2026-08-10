class Solution(object):
    def minSideJumps(self, obstacles):
        """
        :type obstacles: List[int]
        :rtype: int
        """
        # dp[i] represents the min jumps to be on lane (i + 1)
        # Starting at lane 2 (index 1), so lane 1 and 3 cost 1 side jump initially.
        dp = [1, 0, 1]
        
        for obs in obstacles:
            # If an obstacle is present in a lane, mark it unreachable at this point
            if obs > 0:
                dp[obs - 1] = float('inf')
                
            # Find the minimum side jumps among all valid lanes at the current point
            min_jumps = min(dp)
            
            # Update all open lanes: side jump from the current best lane if it's better
            for lane in range(3):
                if obs != lane + 1:
                    dp[lane] = min(dp[lane], min_jumps + 1)
                    
        return min(dp)