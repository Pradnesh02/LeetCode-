class Solution(object):
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
            
        max_len = 1
        cur_len = 1
        
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                cur_len += 1
            else:
                cur_len = 1
            max_len = max(max_len, cur_len)
            
        return max_len