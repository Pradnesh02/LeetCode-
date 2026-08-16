class Solution(object):
    def maxNonOverlapping(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        seen = {0}
        curr_sum = 0
        ans = 0
        
        for num in nums:
            curr_sum += num
            
            # Check if there exists a previous prefix sum such that curr_sum - prev_sum == target
            if curr_sum - target in seen:
                ans += 1
                # Reset seen set to start finding the next non-overlapping subarray
                seen = {curr_sum}
            else:
                seen.add(curr_sum)
                
        return ans