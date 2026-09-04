class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n = len(nums)
        
        # Precompute suffix minimums: suffix_min[i] = min(nums[i..n-1])
        suffix_min = [0] * n
        suffix_min[-1] = nums[-1]
        for i in range(n - 2, -1, -1):
            suffix_min[i] = min(nums[i], suffix_min[i + 1])
        
        # Track running prefix maximum: pref_max = max(nums[0..i])
        pref_max = nums[0]
        for i in range(n):
            pref_max = max(pref_max, nums[i])
            if pref_max - suffix_min[i] <= k:
                return i
                
        return -1