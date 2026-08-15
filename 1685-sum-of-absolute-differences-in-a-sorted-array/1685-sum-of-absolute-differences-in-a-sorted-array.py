class Solution(object):
    def getSumAbsoluteDifferences(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        total_sum = sum(nums)
        prefix_sum = 0
        n = len(nums)
        result = []
        
        for i in range(n):
            val = nums[i]
            # Left part contribution
            left_sum = i * val - prefix_sum
            # Right part contribution
            right_sum = (total_sum - prefix_sum - val) - (n - 1 - i) * val
            
            result.append(left_sum + right_sum)
            prefix_sum += val
            
        return result