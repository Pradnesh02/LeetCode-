from typing import List

class Solution:
    def resultArray(self, nums: List[int], k: int) -> List[int]:
        ans = [0] * k
        # dp[r] stores the number of subarrays ending at the previous position with product % k == r
        dp = [0] * k
        
        for num in nums:
            next_dp = [0] * k
            val = num % k
            
            # Single-element subarray [num]
            next_dp[val] += 1
            
            # Extend existing subarrays ending at the previous element
            for r in range(k):
                if dp[r]:
                    next_dp[(r * val) % k] += dp[r]
            
            # Accumulate into the total result
            for r in range(k):
                ans[r] += next_dp[r]
                
            dp = next_dp
            
        return ans