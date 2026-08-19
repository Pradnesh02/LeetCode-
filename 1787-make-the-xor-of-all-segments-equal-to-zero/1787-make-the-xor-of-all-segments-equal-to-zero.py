from collections import Counter

class Solution(object):
    def minChanges(self, nums, k):
        MAX_VAL = 1024
        n = len(nums)
        
        # Count frequencies of each value at each index modulo k
        groups = [Counter() for _ in range(k)]
        size = [0] * k
        for i, val in enumerate(nums):
            groups[i % k][val] += 1
            size[i % k] += 1
            
        # dp[mask] = min changes to make prefix XOR equal to mask
        dp = [float('inf')] * MAX_VAL
        dp[0] = 0
        
        for i in range(k):
            min_prev = min(dp)
            # Default transition: change all elements in this group to an arbitrary value
            new_dp = [min_prev + size[i]] * MAX_VAL
            
            # Optimized transition: choose a value that already exists in this group
            for prev_mask in range(MAX_VAL):
                if dp[prev_mask] == float('inf'):
                    continue
                for val, count in groups[i].items():
                    new_mask = prev_mask ^ val
                    cost = dp[prev_mask] + size[i] - count
                    if cost < new_dp[new_mask]:
                        new_dp[new_mask] = cost
                        
            dp = new_dp
            
        return dp[0]