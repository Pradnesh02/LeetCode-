class Solution(object):
    def countOfPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        MOD = 10**9 + 7
        n = len(nums)
        max_val = max(nums)
        
        # dp[v] = count of valid monotonic pairs ending at arr1[0] = v
        dp = [1] * (nums[0] + 1) + [0] * (max_val - nums[0])
        
        for i in range(1, n):
            new_dp = [0] * (max_val + 1)
            diff = max(0, nums[i] - nums[i - 1])
            
            # Compute prefix sums of previous DP state
            prefix = [0] * (max_val + 2)
            for v in range(max_val + 1):
                prefix[v + 1] = (prefix[v] + dp[v]) % MOD
                
            for v2 in range(diff, nums[i] + 1):
                # Valid previous values v1 must satisfy: v1 <= v2 - diff
                max_v1 = v2 - diff
                new_dp[v2] = prefix[max_v1 + 1]
                
            dp = new_dp
            
        return sum(dp) % MOD