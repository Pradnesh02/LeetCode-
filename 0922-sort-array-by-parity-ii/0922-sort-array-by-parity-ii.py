class Solution(object):
    def sortArrayByParityII(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        i, j = 0, 1

        while i < n and j < n:
            # Advance i until an odd number is found at an even index
            while i < n and nums[i] % 2 == 0:
                i += 2
            
            # Advance j until an even number is found at an odd index
            while j < n and nums[j] % 2 == 1:
                j += 2

            # Swap the misplaced elements
            if i < n and j < n:
                nums[i], nums[j] = nums[j], nums[i]

        return nums