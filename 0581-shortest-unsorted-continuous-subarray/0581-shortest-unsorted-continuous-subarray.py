class Solution(object):
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        left = -1
        right = -1
        
        max_val = nums[0]
        for i in range(1, n):
            if nums[i] < max_val:
                right = i
            else:
                max_val = nums[i]
                
        min_val = nums[-1]
        for i in range(n - 2, -1, -1):
            if nums[i] > min_val:
                left = i
            else:
                min_val = nums[i]
                
        return 0 if right == -1 else right - left + 1