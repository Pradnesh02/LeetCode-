class Solution:
    def canPartition(self, nums: list[int]) -> bool:
        total_sum = sum(nums)
        
        # An odd total sum cannot be split into two equal integer halves
        if total_sum % 2 != 0:
            return False
        
        target = total_sum // 2
        
        # dp[i] will be True if a subset with sum i can be formed
        dp = [False] * (target + 1)
        dp[0] = True
        
        for num in nums:
            # Iterate backwards to ensure each number is used at most once
            for i in range(target, num - 1, -1):
                dp[i] = dp[i] or dp[i - num]
            
            # Early exit if target sum is already reached
            if dp[target]:
                return True
                
        return dp[target]