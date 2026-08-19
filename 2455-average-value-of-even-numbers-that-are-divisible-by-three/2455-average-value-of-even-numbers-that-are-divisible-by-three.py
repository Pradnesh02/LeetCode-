class Solution(object):
    def averageValue(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        valid = [x for x in nums if x % 6 == 0]
        
        return sum(valid) // len(valid) if valid else 0