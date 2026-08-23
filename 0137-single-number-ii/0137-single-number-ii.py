class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ones = 0
        twos = 0
        
        for num in nums:
            # Add to 'ones' if not already in 'twos'
            ones = (ones ^ num) & ~twos
            # Add to 'twos' if not in updated 'ones'
            twos = (twos ^ num) & ~ones
            
        return ones