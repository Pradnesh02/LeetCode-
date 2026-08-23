class Solution(object):
    def isZeroArray(self, nums, queries):
        """
        :type nums: List[int]
        :type queries: List[List[int]]
        :rtype: bool
        """
        n = len(nums)
        diff = [0] * (n + 1)
        
        # Apply difference array updates for each range [l, r]
        for l, r in queries:
            diff[l] += 1
            diff[r + 1] -= 1
            
        # Compute prefix sums to get total coverage per index
        curr_coverage = 0
        for i in range(n):
            curr_coverage += diff[i]
            if curr_coverage < nums[i]:
                return False
                
        return True