class Solution(object):
    def findMissingElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        num_set = set(nums)
        min_val = min(nums)
        max_val = max(nums)
        
        # Iterate sequentially through the range; this automatically returns a sorted result
        return [x for x in range(min_val, max_val + 1) if x not in num_set]