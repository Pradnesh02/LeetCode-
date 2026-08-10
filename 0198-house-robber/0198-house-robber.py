class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        prev1 = 0  # Max profit up to previous house (i-1)
        prev2 = 0  # Max profit up to house before previous (i-2)
        
        for num in nums:
            # Decide to either skip current house (prev1) or rob it (prev2 + num)
            temp = max(prev1, prev2 + num)
            prev2 = prev1
            prev1 = temp
            
        return prev1