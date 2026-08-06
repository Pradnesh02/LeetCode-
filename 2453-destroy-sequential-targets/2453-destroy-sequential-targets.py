class Solution(object):
    def destroyTargets(self, nums, space):
        """
        :type nums: List[int]
        :type space: int
        :rtype: int
        """
        # Count frequency of each remainder group
        mod_counts = {}
        for x in nums:
            rem = x % space
            mod_counts[rem] = mod_counts.get(rem, 0) + 1
            
        # Find maximum number of targets any seed can destroy
        max_targets = max(mod_counts.values())
        
        # Find minimum nums[i] that belongs to a max_targets remainder group
        ans = float('inf')
        for x in nums:
            if mod_counts[x % space] == max_targets:
                if x < ans:
                    ans = x
                    
        return ans