class Solution(object):
    def minimumDeletions(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n <= 2:
            return n
            
        idx1 = nums.index(min(nums))
        idx2 = nums.index(max(nums))
        
        # Ensure i is the smaller index and j is the larger index
        i, j = min(idx1, idx2), max(idx1, idx2)
        
        # Option 1: Delete both from the front
        option1 = j + 1
        
        # Option 2: Delete both from the back
        option2 = n - i
        
        # Option 3: Delete i from the front and j from the back
        option3 = (i + 1) + (n - j)
        
        return min(option1, option2, option3)