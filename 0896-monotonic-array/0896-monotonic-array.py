class Solution(object):
    def isMonotonic(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        is_increasing = True
        is_decreasing = True
        
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                is_increasing = False
            if nums[i] < nums[i + 1]:
                is_decreasing = False
                
        return is_increasing or is_decreasing