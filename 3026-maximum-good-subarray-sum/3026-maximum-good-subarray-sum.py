class Solution(object):
    def maximumSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        ans = float('-inf')
        min_prefix = {}
        curr_sum = 0
        
        for num in nums:
            # Check for valid starting elements: (num - k) and (num + k)
            for target in (num - k, num + k):
                if target in min_prefix:
                    ans = max(ans, curr_sum + num - min_prefix[target])
            
            # Store/update the minimum prefix sum prior to encountering 'num'
            if num not in min_prefix or curr_sum < min_prefix[num]:
                min_prefix[num] = curr_sum
                
            curr_sum += num
            
        return ans if ans != float('-inf') else 0