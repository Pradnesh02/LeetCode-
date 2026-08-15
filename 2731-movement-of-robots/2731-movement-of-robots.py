class Solution(object):
    def sumDistance(self, nums, s, d):
        """
        :type nums: List[int]
        :type s: str
        :type d: int
        :rtype: int
        """
        MOD = 10**9 + 7
        n = len(nums)
        
        # Calculate final positions assuming robots pass through each other
        pos = [nums[i] + d if s[i] == 'R' else nums[i] - d for i in range(n)]
        pos.sort()
        
        total_dist = 0
        prefix_sum = 0
        
        for i in range(n):
            total_dist = (total_dist + (i * pos[i] - prefix_sum)) % MOD
            prefix_sum += pos[i]
            
        return total_dist