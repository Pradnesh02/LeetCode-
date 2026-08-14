class Solution(object):
    def sortEvenOdd(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        even = sorted(nums[0::2])
        odd = sorted(nums[1::2], reverse=True)
        
        nums[0::2] = even
        nums[1::2] = odd
        
        return nums