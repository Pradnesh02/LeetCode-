class Solution(object):
    def minOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        collected = set()
        operations = 0
        
        # Iterate backwards from the last element
        for i in range(len(nums) - 1, -1, -1):
            operations += 1
            if nums[i] <= k:
                collected.add(nums[i])
                
            # Stop as soon as we have all numbers from 1 to k
            if len(collected) == k:
                return operations
                
        return operations