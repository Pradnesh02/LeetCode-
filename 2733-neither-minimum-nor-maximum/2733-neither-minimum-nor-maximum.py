class Solution(object):
    def findNonMinOrMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 3:
            return -1
        
        # Since all numbers are distinct, the middle element
        # among any 3 numbers is guaranteed to be neither the global min nor max
        sub = sorted(nums[:3])
        return sub[1]