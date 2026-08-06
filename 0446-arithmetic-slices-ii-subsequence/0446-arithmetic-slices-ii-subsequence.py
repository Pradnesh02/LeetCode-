from collections import defaultdict

class Solution(object):
    def numberOfArithmeticSlices(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        total_slices = 0
        
        # dp[i][diff] stores count of arithmetic subsequences ending at index i with difference diff
        dp = [defaultdict(int) for _ in range(n)]
        
        for i in range(n):
            for j in range(i):
                diff = nums[i] - nums[j]
                
                # Count of subsequences ending at j with difference 'diff'
                count = dp[j][diff]
                
                # Appending nums[i] to these forms valid subsequences of length >= 3
                total_slices += count
                
                # Update dp[i][diff] with existing subsequences + new 2-element pair [nums[j], nums[i]]
                dp[i][diff] += count + 1
                
        return total_slices