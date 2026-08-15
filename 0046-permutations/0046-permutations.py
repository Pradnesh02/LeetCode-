class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        n = len(nums)
        
        def backtrack(first):
            if first == n:
                result.append(list(nums))
                return
            
            for i in range(first, n):
                # Place element nums[i] at the current position 'first'
                nums[first], nums[i] = nums[i], nums[first]
                # Recurse for the remaining positions
                backtrack(first + 1)
                # Backtrack to restore original array
                nums[first], nums[i] = nums[i], nums[first]
                
        backtrack(0)
        return result