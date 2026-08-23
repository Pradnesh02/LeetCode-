class Solution(object):
    def minZeroArray(self, nums, queries):
        """
        :type nums: List[int]
        :type queries: List[List[int]]
        :rtype: int
        """
        n = len(nums)
        ans = 0
        
        for i in range(n):
            target = nums[i]
            if target == 0:
                continue
                
            # Collect all queries covering index i along with their 1-based index (k)
            # dp[s] stores the minimum k needed to achieve a subset sum of s
            dp = {0: 0}
            
            for k, (l, r, val) in enumerate(queries, 1):
                if l <= i <= r:
                    # Update DP in reverse order to avoid using the same query multiple times
                    new_dp = dict(dp)
                    for s, min_k in dp.items():
                        new_s = s + val
                        if new_s <= target:
                            if new_s not in new_dp or k < new_dp[new_s]:
                                new_dp[new_s] = k
                    dp = new_dp
            
            if target not in dp:
                return -1
                
            ans = max(ans, dp[target])
            
        return ans