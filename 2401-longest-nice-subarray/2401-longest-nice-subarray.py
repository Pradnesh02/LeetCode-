class Solution(object):
    def longestNiceSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left = 0
        used_bits = 0
        max_len = 0
        
        for right in range(len(nums)):
            # If the current element shares any set bits with elements in the window,
            # shrink the window from the left.
            while (used_bits & nums[right]) != 0:
                used_bits ^= nums[left]
                left += 1
            
            # Include nums[right] into the active window's bit representation
            used_bits |= nums[right]
            
            # Update max length
            max_len = max(max_len, right - left + 1)
            
        return max_len